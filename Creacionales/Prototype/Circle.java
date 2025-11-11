public class Circle extends Shape {
    private double radius;

    public Circle(Circle cirle) {
        super(cirle);
        this.radius = cirle.getRadius();
    }

    @Override
    Shape cloneShape() {
        return new Circle(this);
    }

    public double getRadius() {
        return this.radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

}
