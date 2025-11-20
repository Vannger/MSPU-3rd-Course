public class Program
{
    public static void Main()
    {
        Console.WriteLine("=== ЧАСТЬ A — enum + switch ===");

        var ctx1 = new PrintContext();
        Console.WriteLine($"Text без модификаторов: {PrintCostCalculatorEnum.GetPrintCost(DocumentType.Text, ctx1)}");

        var ctx2 = new PrintContext(isColor: true);
        Console.WriteLine($"Report с IsColor=true: {PrintCostCalculatorEnum.GetPrintCost(DocumentType.Report, ctx2)}");

        var ctx3 = new PrintContext(isDuplex: true);
        Console.WriteLine($"Photo с IsDuplex=true: {PrintCostCalculatorEnum.GetPrintCost(DocumentType.Photo, ctx3)}");

        var ctx4 = new PrintContext(hasBulkDiscount: true);
        Console.WriteLine($"Poster с HasBulkDiscount=true: {PrintCostCalculatorEnum.GetPrintCost(DocumentType.Poster, ctx4)}");

        var ctx5 = new PrintContext(isColor: true, isDuplex: true, hasBulkDiscount: true);
        Console.WriteLine($"InternalMemo (любой контекст): {PrintCostCalculatorEnum.GetPrintCost(DocumentType.InternalMemo, ctx5)}");

        Console.WriteLine("\n=== ЧАСТЬ B — Иерархия классов ===");

        Console.WriteLine($"Text: {PrintCostCalculatorOop.GetPrintCost(new Text(), new PrintContext())}");
        Console.WriteLine($"Report (IsColor=true): {PrintCostCalculatorOop.GetPrintCost(new Report(), new PrintContext(isColor: true))}");
        Console.WriteLine($"Photo (IsDuplex=true): {PrintCostCalculatorOop.GetPrintCost(new Photo(), new PrintContext(isDuplex: true))}");
        Console.WriteLine($"Poster (HasBulkDiscount=true): {PrintCostCalculatorOop.GetPrintCost(new Poster(), new PrintContext(hasBulkDiscount: true))}");
        Console.WriteLine($"InternalMemo (любой контекст): {PrintCostCalculatorOop.GetPrintCost(new InternalMemo(), new PrintContext(isColor: true, isDuplex: true))}");
    }
}