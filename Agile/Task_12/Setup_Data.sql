DROP TABLE IF EXISTS claims_import_lines;
CREATE TABLE claims_import_lines (
  id serial PRIMARY KEY,
  source_file text NOT NULL,
  line_no int NOT NULL,
  raw_line text NOT NULL,
  received_at timestamptz default now(),
  note text
);

INSERT INTO claims_import_lines (source_file, line_no, raw_line, note) VALUES
-- Контакты пациентов: email в угловых скобках и простые варианты, телефоны
('clinic_A_2025_11.csv', 1, 'Claim#C1001; Patient: Ivan Petrov <ivan.petrov@example.com>; +7 (900) 123-45-67; Policy: POL-12345', 'claim row'),
('clinic_A_2025_11.csv', 2, 'Claim#C1002; Patient: Olga S; olga.s@mail.co; 8-900-1234567; Policy: POL67890', 'claim row'),
('clinic_A_2025_11.csv', 3, 'Claim#C1003; Patient: Oops <bad@-domain.com>; 09001234567; Policy: BAD@@POL', 'broken email/policy'),

-- Процедурные коды и суммы (с разделителями тысяч и валютой)
('billing_feed.csv', 10, 'proc: CPT-99213; amount: "1,200.00" USD; provider: Clinic A', 'billing row'),
('billing_feed.csv', 11, 'code: ICD10-A41.9; charge: "2 500,00" EUR; note: urgent', 'billing row'),

-- Теги/метки диагноза / категории
('diagnosis_tags.csv', 1, 'tags: urgent, inpatient, cardio', 'tags row'),
('diagnosis_tags.csv', 2, 'tags: outpatient, , followup', 'tags with empty'),

-- «Грязные» CSV-строки: фамилии с запятыми, адреса, суммы в кавычках
('patients_dirty.csv', 5, '"Ivanov, Ivan","123 Med St, Bldg 2","claim: C2001","1,500.00"', 'dirty csv'),
('patients_dirty.csv', 6, '"Brown, Sarah","Ward 7, Room 12","notes: needs translator","2 000,00"', 'dirty csv'),

-- Логи обработки: разного регистра, ошибки и предупреждения
('ingest_claims_log.txt', 400, 'INFO: started claims ingest', 'log'),
('ingest_claims_log.txt', 401, 'warning: missing policy for claim C1003', 'log'),
('ingest_claims_log.txt', 402, 'error: failed to parse patients_dirty.csv line 6', 'log'),
('ingest_claims_log.txt', 403, 'Error: amount format invalid for claim C1002', 'log'),

-- Ловушки / edge-cases для проверки наивных regex
('clinic_A_2025_11.csv', 20, 'Patient: bad@@example..com; phone: +7 900 ABC-45-67; Policy: POL-12-!!', 'trap-bad-email-phone-policy'),
('patients_dirty.csv', 7, '"O''Neil, Patrick","100 Main St, Suite 5","claim: C2002",""', 'dirty csv with apostrophe and empty amount');