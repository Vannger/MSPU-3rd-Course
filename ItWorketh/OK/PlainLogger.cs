namespace LoggerExample
{
    public class PlainLogger : Logger
    {
        public string Prefix { get; private set; }

        public PlainLogger(string name, int level, string prefix = "")
            : base(name, level)
        {
            Prefix = prefix;
        }

        public void SetPrefix(string p)
        {
            Prefix = p ?? "";
        }
    }
}
