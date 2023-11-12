package hellocucumber;

import io.cucumber.core.internal.com.fasterxml.jackson.core.Version;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import io.cucumber.java.en.Then;
import static org.junit.jupiter.api.Assertions.*;

import java.lang.ProcessBuilder.Redirect;
import java.net.Authenticator;
import java.net.InetSocketAddress;
import java.net.ProxySelector;

import org.apiguardian.api.API;

public class StepDefinitions {
    String baseURI = "http://localhost:4567/";
    String URL = "";
    String requestType = "";
    String payloadType = "json";
    String data = "";

    @Given("I setup the GET todos API endpoint")
    public void setGetEndpoint() {
        requestType = "GET";
        String endpoint = "todos";
        URL = baseURI + endpoint;
        System.out.println("Add URL: " + URL);
    }

    @When("I send GET request")
    public void sendGETRequest() {
        HttpClient client = HttpClient.newBuilder()
        .version(Version.HTTP_1_1)
        .followRedirects(Redirect.NORMAL)
        .connectTimeout(Duration.ofSeconds(20))
        .proxy(ProxySelector.of(new InetSocketAddress("proxy.example.com", 80)))
        .authenticator(Authenticator.getDefault())
        .build();

        HttpResponse<String> response = client.send(requestType, BodyHandlers.ofString());
        request.addHeader("accept", "application/json");
        HttpResponse httpResponse = httpClient.execute(request);
    }

    @Then("I should receive valid HTTP response code 200")
    public void verifyGETRequest() {
        throw new io.cucumber.java.PendingException();
    }
}