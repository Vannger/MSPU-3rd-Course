public static class PrintCostCalculatorEnum
    {
        public static int GetPrintCost(DocumentType type, PrintContext context)
        {
            int cost = type switch
            {
                DocumentType.Text => 1,
                DocumentType.Report => 2,
                DocumentType.Photo => 5,
                DocumentType.Poster => 8,
                DocumentType.InternalMemo => 1,
                _ => 1
            };

            // InternalMemo не подвержен модификаторам
            if (type == DocumentType.InternalMemo)
                return cost;

            // Применяем модификаторы
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