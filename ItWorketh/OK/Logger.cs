using System;

namespace LoggerExample
{
    public class Logger
    {
        private string name;
        private int level;

        public string Name
        {
            get => name;
            private set
            {
                if (string.IsNullOrWhiteSpace(value))
                    throw new ArgumentException("Имя логгера не может быть пустым");
                name = value;
            }
        }

        public int Level
        {
            get => level;
            private set
            {
                if (value < 0)
                    throw new ArgumentException("Уровень логгера должен быть >= 0");
                level = value;
            }
        }

        public Logger(string name, int level)
        {
            Name = name;
            Level = level;
        }

        public void Log(string msg)
        {
            Console.WriteLine(Format(msg));
        }

        public void SetLevel(int lvl)
        {
            Level = lvl;
        }

        public virtual string Format(string message)
        {
            return $"[{Level}] {Name}: {message}";
        }
    }
}
