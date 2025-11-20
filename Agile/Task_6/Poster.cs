public class Poster : Document
    {
        public Poster() : base(8) { }

        public override int GetPrintCost(PrintContext context)
        {
            int cost = BaseCost;
            if (context.IsColor) cost += 2;
            if (context.IsDuplex)
            {
                cost = (int)Math.Floor(cost * 0.9);
                if (cost < 1) cost = 1;
            }
            if (context.HasBulkDiscount)
            {
                cost -= 1;
                if (cost < 1) cost = 1;
            }
            return cost;
        }
    }