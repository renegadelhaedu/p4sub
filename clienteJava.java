import com.google.gson.Gson;
import java.io.IOException;
import java.net.*;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;



public class Main {

    public void consumirSemCookies(){

        HttpClient httpClient = HttpClient.newHttpClient();

        HttpRequest httpRequest = HttpRequest.newBuilder()
                .header("Content-Type", "application/json")
                .uri(URI.create("http://127.0.0.1:5000/listarusuarios" ))
                .GET()
                .build();

        HttpResponse<String> httpResponse = null;
        try {
            httpResponse = httpClient.send(httpRequest, HttpResponse.BodyHandlers.ofString());
        } catch (IOException e) {
            throw new RuntimeException(e);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        if(httpResponse.statusCode() >= 200 && httpResponse.statusCode() <= 226){
            Gson gson = new Gson();
            Usuario[] pessoas = gson.fromJson(httpResponse.body(), Usuario[].class);

            for(Usuario p: pessoas){
                System.out.println(p.getNome() + " - " + p.getMatricula());
            }
        }else{
            System.out.println(httpResponse.body());
        }

    }
    public static void main(String[] args) throws IOException, InterruptedException, URISyntaxException {

        //new Main().consumirSemCookies();

        new Main().consumirSemCookies();
    }
}