public class Database {
    private static Database instance;

    private Database() {
        // Lógica de inicialización
    }

    public static Database getInstance() {
        if (Database.instance == null) {
            Database.instance = new Database();
        }
        return Database.instance;
    }

    // ...
}
