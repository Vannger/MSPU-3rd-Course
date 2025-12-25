from typing import Any, Tuple
from datetime import datetime, timezone
import crypto
import storage
import user
import crypto

def record_token(payload: dict[str, Any]) -> None:
    db = storage.load_tokens()
    entry = {
        "jti": payload["jti"],
        "sub": payload["sub"],
        "typ": payload["typ"],
        "exp": payload["exp"],
        "revoked": False,
    }
    db["tokens"].append(entry)
    storage.save_tokens(db)

def revoke_by_jti(jti: str) -> None:
    db = storage.load_tokens()
    for t in db["tokens"]:
        if t["jti"] == jti:
            t["revoked"] = True
    storage.save_tokens(db)

def is_revoked(jti: str) -> bool:
    db = storage.load_tokens()
    for t in db["tokens"]:
        if t["jti"] == jti:
            return bool(t.get("revoked", False))
    return False

def is_expired(exp: str) -> bool:
    return datetime.now(timezone.utc).timestamp() > float(exp)

def login(username: str, password: str) -> Tuple[str, str]:
    u = user.get_user(username)
    if not u or not user.verify_password(u, password):
        raise ValueError("invalid credentials")

    access_token, access_payload = crypto.issue_access(sub=username)
    refresh_token, refresh_payload = crypto.issue_refresh(sub=username)

    record_token(refresh_payload)
    record_token(access_payload)
    
    return access_token, refresh_token

def verify_access(access: str) -> dict[str, Any]:
    payload = crypto.decode(access)
    
    if payload.get("typ") != "access":
        raise ValueError("wrong token type")
    
    if is_revoked(payload["jti"]):
        raise ValueError("token revoked")
    
    if is_expired(payload["exp"]):
        raise ValueError("token expired")
        
    return payload

def refresh_pair(refresh_token: str) -> Tuple[str, str]:
    payload = crypto.decode(refresh_token)
    
    if payload.get("typ") != "refresh":
        raise ValueError("wrong token type")
    
    if is_revoked(payload["jti"]):
        raise ValueError("token revoked")
    
    if is_expired(payload["exp"]):
        raise ValueError("token expired")
    
    revoke_by_jti(payload["jti"])
    
    new_access, ap = crypto.issue_access(sub=payload["sub"])
    new_refresh, rp = crypto.issue_refresh(sub=payload["sub"])
    
    record_token(rp)
    record_token(ap)
    
    return new_access, new_refresh

def revoke(token: str) -> None:
    payload = crypto.decode(token)
    revoke_by_jti(payload["jti"])

def introspect(token: str) -> dict[str, Any]:
    try:
        payload = crypto.decode(token)
        active = (not is_revoked(payload["jti"])) and (not is_expired(payload["exp"]))
        return {
            "active": active,
            "sub": payload.get("sub"),
            "typ": payload.get("typ"),
            "exp": payload.get("exp"),
            "jti": payload.get("jti"),
        }
    except Exception:
        return {"active": False, "error": "invalid_token"}
