public class testOutput {
    public static void main(String[] args) {
        int day = 10, month = 7, year = 2023;
        System.out.printf("Date is %02d/%02d/%04d\n", day, month, year);

        String item = "milk";
        double price = 3.5;
        int count = 5;
        System.out.printf("The price of %s is %.2f per bottle. You have purchased %d bottles. The total price is %.2f\n",
                          item, price, count, price * count);
    }
}
