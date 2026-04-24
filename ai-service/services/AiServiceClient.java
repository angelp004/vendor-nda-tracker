package com.example.service;

import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.*;

import java.util.Map;

@Component
public class AiServiceClient {

    private final String AI_URL = "http://127.0.0.1:5000/recommend"; // your Flask API

    public String callRecommendAPI(String input) {
        try {
            RestTemplate restTemplate = new RestTemplate();

            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);

            String requestBody = "{\"input\": \"" + input + "\"}";

            HttpEntity<String> request = new HttpEntity<>(requestBody, headers);

            ResponseEntity<Map> response = restTemplate.postForEntity(
                    AI_URL,
                    request,
                    Map.class
            );

            if (response.getBody() != null) {
                Object recommendations = response.getBody().get("recommendations");
if (recommendations == null) return null;
return recommendations.toString();
            }

        } catch (Exception e) {
            System.out.println("AI call failed: " + e.getMessage());
        }

        return null; // important for null handling
    }
}