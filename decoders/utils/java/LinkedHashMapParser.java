import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.ObjectInputStream;
import java.util.LinkedHashMap;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.lang.ClassNotFoundException;
import java.util.Map;
import java.util.ArrayList;

public class LinkedHashMapParser {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("usage: LinkedHashMapParser <path to hashmap>");
            return;
        }
        try {
            parseHashMap(args[0]);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void parseHashMap(String path) throws FileNotFoundException, IOException, ClassNotFoundException {
        FileInputStream fis = new FileInputStream(path);
        ObjectInputStream ois = new ObjectInputStream(fis);
        LinkedHashMap<String, Object[]> lhm = (LinkedHashMap<String, Object[]>) ois.readObject();

        for (Map.Entry<String, Object[]> entry : lhm.entrySet()) {
            String key = entry.getKey();
            Object[] objectList = entry.getValue();

            Entry e = new Entry();
            e.mapkey = key;

            for (Object o : objectList) {
                if (o instanceof java.lang.String) {
                    //System.out.println("Got string: " + (String) o);
                    e.addKey((String) o);
                }

                if (o instanceof java.lang.String[]) {
                    //System.out.println("String array:");
                    String[] s = (String[]) o;
                    for (String str : s) {
                        //System.out.println("  " + str);
                        e.add(str);
                    }
                }
            }

            e.print();
        }

        // cleanup
        ois.close();
        fis.close();
    }
}
