using System;

namespace LoggerExample
{
    class Program
    {
        static void Main(string[] args)
        {
            Logger l1 = new Logger("Base", 1);
            l1.Log("Привет!");

            JsonLogger l2 = new JsonLogger("Json", 2, true);
            l2.Log("Сообщение в JSON");

            PlainLogger l3 = new PlainLogger("Plain", 3, "[INFO] ");
            l3.Log("Просто текст");

            AnsiLogger l4 = new AnsiLogger("Ansi", 4, "[WARN] ", "\u001b[31m");
            l4.Log("Сообщение с цветом");
        }
    }
}
