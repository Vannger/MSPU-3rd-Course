public class InternalMemo : Document
    {
        public InternalMemo() : base(1) { }

        public override int GetPrintCost(PrintContext context)
        {
            // модификаторы не применяются
            return BaseCost;
        }
    }