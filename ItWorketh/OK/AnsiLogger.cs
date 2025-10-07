using System;

namespace LoggerExample
{
    public class AnsiLogger : PlainLogger
    {
        public string ColorCode { get; private set; }

        public AnsiLogger(string name, int level, string prefix, string colorCode)
            : base(name, level, prefix)
        {
            SetColor(colorCode);
        }

        public void SetColor(string code)
        {
            if (string.IsNullOrWhiteSpace(code))
                throw new ArgumentException("Код цвета не может быть пустым");
            ColorCode = code;
        }

        public override string Format(string message)
        {
            string baseMessage = base.Format(message);
            return $"{ColorCode}{baseMessage}\u001b[0m";
        }
    }
}
