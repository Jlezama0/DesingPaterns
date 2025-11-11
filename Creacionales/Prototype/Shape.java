abstract class Shape {
    private int X;
    private int Y;
    private String color;

    public Shape() {
    }

    public Shape(Shape shape) {
        this.X = shape.getX();
        this.Y = shape.getY();
        this.color = shape.getColor();
    }

    public int getX() {
        return this.X;
    }

    public int getY() {
        return this.Y;
    }

    public String getColor() {
        return this.color;
    }

    public void setX(int X) {
        this.X = X;
    }

    public void setY(int Y) {
        this.Y = Y;
    }

    public void setColor(String color) {
        this.color = color;
    }

    abstract Shape cloneShape();
}