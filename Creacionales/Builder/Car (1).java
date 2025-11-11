class Car {
    private String color;
    private String model;
    private String power;
    private String brand;
    private Float engineCap;
    private String chasis;

    private Car(CarBuilder builder) {
        this.color = builder.color;
        this.model = builder.model;
        this.power = builder.power;
        this.brand = builder.brand;
        this.engineCap = builder.engineCap;
        this.chasis = builder.chasis;
    }

    private static class CarBuilder {
        private String color;
        private String model;
        private String power;
        private String brand;
        private Float engineCap;
        private String chasis;

        public CarBuilder color(String color) {
            this.color = color;
            return this;
        }

        public CarBuilder model(String model) {
            this.model = model;
            return this;
        }

        public CarBuilder power(String power) {
            this.power = power;
            return this;
        }

        public CarBuilder brand(String brand) {
            this.brand = brand;
            return this;
        }

        public CarBuilder engineCap(Float engineCap) {
            this.engineCap = engineCap;
            return this;
        }

        public CarBuilder chasis(String chasis) {
            this.chasis = chasis;
            return this;
        }

        public Car build() {
            return new Car(this);
        }

    }

    public static CarBuilder builder() {
        return new CarBuilder();
    }

    public String toString() {
        return "{ color: " + this.color + ", " +
                "model: " + this.model + ", " +
                "power: " + this.power + ", " +
                "brand: " + this.brand + ", " +
                "engineCap: " + this.engineCap + ", " +
                "chasis: " + this.chasis +
                "}";
    }

    public static void main(String[] args) {
        Car car = Car.builder().brand("Mazda").model("3").build();
        Car car2 = Car.builder().brand("Mercedes").model("AMG").chasis("Sedan").build();
        Car car3 = Car.builder().brand("BMW").model("SerieZ").color("Black").build();
        Car car4 = Car.builder().brand("Toyota").model("Corolla").engineCap(1.6F).build();
        Car car5 = Car.builder().brand("Nissan").model("Pathfinder").power("1000HP").build();
        System.out.println(car);
        System.out.println(car2);
        System.out.println(car3);
        System.out.println(car4);
        System.out.println(car5);
    }
}