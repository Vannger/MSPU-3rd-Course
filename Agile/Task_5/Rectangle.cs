public class Rectangle : IDrawable, IScalable
{
    public string Color { get; init; }
    public bool IsVisible { get; init; }
    public double Scale { get;  set; }
    public double Width { get; init; }
    public double Height { get; init; }
    public double MinVisibleArea { get; init; }

    public Rectangle(string color, bool isVisible, double scale, double width, double height, double minVisibleArea)
    {
        Color = color;
        IsVisible = isVisible;
        Scale = scale;
        if (Scale < 0)
        {
            Scale = 0;
        }
        Width = width;
        Height = height;
        MinVisibleArea = minVisibleArea;


    }
    public void Resize(double factor)
    {
        Scale *= factor;
        if (Scale < 0)
        {
            Scale = 0;
        }
    }
    public string Draw()
    {
        double effectiveWidth = Width * Scale;
        double effectiveHeight = Height * Scale;
        if (effectiveHeight*effectiveWidth < MinVisibleArea)
        {
            return "donn donn papa gone don";
        }
        if (IsVisible == false)
        {
            return "hidden";
        }
        return "Rekt W=" + effectiveWidth + " H=" + effectiveHeight + " color=" + Color;
    }
}