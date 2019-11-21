import java.util.ArrayList;

public class Entry {
    public String mapkey;
    public ArrayList<String> enckey = new ArrayList<String>();
    public ArrayList<String> files = new ArrayList<String>();

    public void print() {
        String s = "";
        if (enckey.size() > 1) {
            s = mapkey + "||" + enckey.get(0) + "," + enckey.get(1) + "||";
        } else {
            s = mapkey + "||" + enckey.get(0) + "||";
        }

        for (int i = 0; i < files.size(); i++) {
            s += files.get(i);
            if (i < files.size() - 1) {
                s += ",";
            }
        }
        System.out.println(s);
    }

    public void addKey(String s) {
        enckey.add(s);
    }

    public void add(String s) {
        if (s.equals(".compressed") || s.equals(".encrypted") || s.equals(".splitted")) {
            return;
        }
        files.add(s);
    }
}