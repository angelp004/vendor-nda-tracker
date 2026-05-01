package com.vendor.backend.controller;

import com.vendor.backend.service.AiServiceClient;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/ai")
public class AiController {

    private final AiServiceClient aiServiceClient;

    public AiController(AiServiceClient aiServiceClient) {
        this.aiServiceClient = aiServiceClient;
    }

    @PostMapping("/describe")
    public String describe(@RequestBody Map<String, String> request) {
        String text = request.get("text");
        return aiServiceClient.describe(text);
    }

}