public interface IDrawable
{
    string Color { get; }
    bool IsVisible { get; }
    string Draw()
    {
        if (IsVisible == false)
            return "hidden";
        else
            return "drawn";
    }
}
