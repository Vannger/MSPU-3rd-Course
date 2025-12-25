from dataclasses import dataclass, field
import pwnedpasswords


ERR_LENGTH = "length"
ERR_LETTER = "requires_letter"
ERR_DIGIT = "requires_digit"
ERR_SPECIAL = "requires_special"
WARN_PWNED = "password_pwned"
LEN_MIN = 12


@dataclass
class PasswordValidationResult:
    is_valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def __bool__(self) -> bool:
        return self.is_valid


'''
Требуется проверить минимальную длину пароля (>= 12 символов) и
наличие в пароле хотя бы одной буквы, цифры и спецсимвола.
'''
def validate_password(password: str) -> PasswordValidationResult:
    error_list = []
    warn_list = []
    num_flag = False
    alpha_flag = False
    special_flag = False
    checks = pwnedpasswords.Password(password, True)
    if checks.check!=0:
        warn_list.append(WARN_PWNED)

    for i in password:
        if i.isalpha():
            alpha_flag = True
        if i.isnumeric():
            num_flag = True
        if not i.isalnum():
            special_flag = True
        if num_flag and alpha_flag and special_flag:
            break
    
    final_flag = num_flag and alpha_flag and special_flag
    if len(password)>=LEN_MIN:
        if final_flag:
            return PasswordValidationResult(is_valid=True, warnings=warn_list)
    else:
        error_list.append(ERR_LENGTH)
    
    if not alpha_flag:
        error_list.append(ERR_LETTER)
    if not num_flag:
        error_list.append(ERR_DIGIT)
    if not special_flag:
        error_list.append(ERR_SPECIAL)
    
    return PasswordValidationResult(
        is_valid=False, 
        errors=error_list, 
        warnings=warn_list)
