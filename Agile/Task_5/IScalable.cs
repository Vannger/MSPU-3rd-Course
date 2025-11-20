public interface IScalable
{
    double Scale { get; set; }
    void Resize(double factor)
    {
        Scale *= factor;
        if (Scale < 0)
            Scale = 0;
    }
}
