public class PrintContext
    {
        public bool IsColor { get; set; }
        public bool IsDuplex { get; set; }
        public bool HasBulkDiscount { get; set; }

        public PrintContext(bool isColor = false, bool isDuplex = false, bool hasBulkDiscount = false)
        {
            IsColor = isColor;
            IsDuplex = isDuplex;
            HasBulkDiscount = hasBulkDiscount;
        }
    }