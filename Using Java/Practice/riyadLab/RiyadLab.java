package riyadLab;

import java.net.URL;
import java.io.IOException;
import java.net.HttpURLConnection;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class RiyadLab {

    public static void main(String[] args) throws IOException {
        URL url = new URL("https://youtu.be/U2SVCCENLjE?si=_TA3u7LMQbfxQcVW");
        HttpURLConnection connect = (HttpURLConnection) url.openConnection();

        connect.setRequestMethod("GET");
        connect.setRequestProperty("User-Agent", "Chrome");

        int response = connect.getResponseCode();
        System.out.println("Response Code" + response);
        System.out.println("Response message" + connect.getResponseMessage());

        if (response == HttpURLConnection.HTTP_OK) {
            BufferedReader read = new BufferedReader(new InputStreamReader(connect.getInputStream()));
            StringBuffer str = new StringBuffer();
            String store = null;

            while ((store = read.readLine()) != null) {
                str.append(store);

            }

            read.close();
            System.out.println("Get Response" + str.toString());

        }
    }

}
