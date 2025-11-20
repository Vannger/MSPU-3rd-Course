public class Program
{
    public static void Main()
    {
        Label label = new Label("Red", false);
        Console.WriteLine("Label " + label.Draw());
        Rectangle rectangle = new Rectangle("Red",true,4.0,4.0,4.0,1.0);
        Console.WriteLine(rectangle.Draw());
    }
}