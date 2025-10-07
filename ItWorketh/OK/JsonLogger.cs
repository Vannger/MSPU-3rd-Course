using System.Text.Json;

namespace LoggerExample
{
    public class JsonLogger : Logger
    {
        public bool Pretty { get; private set; }

        public JsonLogger(string name, int level, bool pretty = false)
            : base(name, level)
        {
            Pretty = pretty;
        }

        public void TogglePretty()
        {
            Pretty = !Pretty;
        }

        public override string Format(string message)
        {
            var obj = new
            {
                Level,
                Name,
                Message = message
            };

            var options = new JsonSerializerOptions
            {
                WriteIndented = Pretty
            };

            return JsonSerializer.Serialize(obj, options);
        }
    }
}
