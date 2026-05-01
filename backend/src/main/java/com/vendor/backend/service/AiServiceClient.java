
package com.vendor.backend.service;

import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.*;

import java.util.HashMap;
import java.util.Map;

@Service
public class AiServiceClient {

    @Autowired
    private RestTemplate restTemplate;

    private final String BASE_URL = "http://127.0.0.1:5000";

    public String describe(String text) {
        try {
            String url = BASE_URL + "/describe";

            Map<String, String> requestBody = new HashMap<>();
            requestBody.put("text", text);

            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);

            HttpEntity<Map<String, String>> request =
                    new HttpEntity<>(requestBody, headers);

            ResponseEntity<Map> response = restTemplate.postForEntity(
                    url, request, Map.class);

            if (response.getStatusCode() == HttpStatus.OK) {
                Map body = response.getBody();
                return (String) body.get("description");
            }

        } catch (Exception e) {
            System.out.println("Error calling AI service: " + e.getMessage());
        }

        return null; // required
    }
}