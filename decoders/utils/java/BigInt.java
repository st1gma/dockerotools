import java.lang.String;

public class BigInt {
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("usage: BigInt <string> <radix>");
            return;
        }
        String s = new String(new java.math.BigInteger(args[0], Integer.parseInt(args[1])).toByteArray());
        System.out.println(s);
    }
}
