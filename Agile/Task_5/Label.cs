public class Label : IDrawable
{
    public string Color { get; init; }
    public bool IsVisible { get; init; }

    public Label(string color, bool isVisible)
    {
        Color = color;
        IsVisible = isVisible;
    }
    
    public string Draw()
    {
        if (IsVisible == false)
            return "hidden";
        else
            return "drawn";
    }
}