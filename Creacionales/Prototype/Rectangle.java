public class Rectangle extends Shape {
    private double width;

    public double getWidth() {
        return width;
    }

    public void setWidth(double width) {
        this.width = width;
    }

    private double height;

    public double getHeight() {
        return height;
    }

    public void setHeight(double height) {
        this.height = height;
    }

    public Rectangle(Rectangle rectangle) {
        super(rectangle);
        this.height = rectangle.getHeight();
        this.width = rectangle.getWidth();
    }

    @Override
    Shape cloneShape() {
        return new Rectangle(this);
    }

}
