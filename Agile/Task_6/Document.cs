public abstract class Document
    {
        private readonly int _baseCost;
        public int BaseCost => _baseCost;

        protected Document(int baseCost)
        {
            _baseCost = baseCost < 1 ? 1 : baseCost;
        }

        public virtual int GetPrintCost(PrintContext context)
        {
            return _baseCost;
        }
    }