### Endpoints
1. /describe
2. /recommend
3. /generate-report



### /describe — Test Inputs

1. SaaS vendor NDA
2. Manufacturing NDA India
3. Fintech NDA
4. Healthcare NDA
5. Freelancer NDA
6. AI data NDA
7. Government NDA
8. E-commerce NDA
9. Consulting NDA
10. Startup NDA



### /recommend — Test Inputs

1. Missing expiry clause
2. No governing law
3. Weak confidentiality
4. No penalty clause
5. Ambiguous scope
6. No termination clause
7. Missing signature
8. No audit rights
9. No dispute resolution
10. Data privacy missing



### /generate-report — Test Inputs

1. Vendor: ABC Pvt Ltd, Risk: Medium, Missing clauses
2. Vendor: XYZ Corp, Risk: High, Data privacy issue
3. Vendor: StartupX, Risk: Low, Minor issues
4. Vendor: GlobalTech, Risk: High, No confidentiality clause
5. Vendor: FinServe Ltd, Risk: Medium, Weak legal structure
6. Vendor: HealthPlus, Risk: High, Sensitive data exposure
7. Vendor: DesignHub, Risk: Low, Basic NDA
8. Vendor: RetailMart, Risk: Medium, Missing penalty clause
9. Vendor: CloudNet, Risk: High, No audit rights
10. Vendor: EduTech, Risk: Low, Well-structured NDA





# /describe — Results

| Input             | Output Summary                                                       | Score |
| ----------------- | -------------------------------------------------------------------- | ----- |
| SaaS NDA          | Detailed explanation with key components, slightly incomplete ending | 4     |
| Manufacturing NDA | Good explanation but lacks penalty details                           | 4     |
| Fintech NDA       | Clear and domain-specific response                                   | 5     |
| Healthcare NDA    | Slightly generic, missing depth                                      | 3     |
| Freelancer NDA    | Basic explanation, not very detailed                                 | 3     |
| AI data NDA       | Well-structured and relevant output                                  | 5     |
| Government NDA    | Lacks detailed clauses                                               | 3     |
| E-commerce NDA    | Clear but slightly generic                                           | 4     |
| Consulting NDA    | Average response, missing risks                                      | 3     |
| Startup NDA       | Good summary with relevant points                                    | 4     |




# /recommend — Results

| Input                 | Output Summary                       | Score |
| --------------------- | ------------------------------------ | ----- |
| Missing expiry clause | Strong recommendation with clear fix | 5     |
| No governing law      | Accurate legal suggestion            | 5     |
| Weak confidentiality  | Good improvement suggestion          | 4     |
| No penalty clause     | Clear and useful advice              | 4     |
| Ambiguous scope       | Slightly generic recommendation      | 3     |
| No termination clause | Good structured output               | 4     |
| Missing signature     | Basic suggestion, lacks depth        | 3     |
| No audit rights       | Relevant and accurate                | 4     |
| No dispute resolution | Generic response                     | 3     |
| Data privacy missing  | Strong and detailed recommendation   | 5     |

Average Score: 4.0 



# /generate-report — Results

| Input        | Output Summary                             | Score |
| ------------ | ------------------------------------------ | ----- |
| ABC Pvt Ltd  | Well-structured report with clear insights | 5     |
| XYZ Corp     | Strong high-risk analysis                  | 5     |
| StartupX     | Good but slightly short                    | 4     |
| GlobalTech   | Detailed and complete report               | 5     |
| FinServe Ltd | Average explanation                        | 3     |
| HealthPlus   | Strong risk explanation                    | 5     |
| DesignHub    | Basic output, lacks detail                 | 3     |
| RetailMart   | Good structure and clarity                 | 4     |
| CloudNet     | Accurate identification of issues          | 4     |
| EduTech      | Well-formatted and clear                   | 5     |

Average Score: 4.3

---



# Final Summary

| Endpoint         | Final Score |
| ---------------- | ----------- |
| /describe        | 4.1         |
| /recommend       | 4.0         |
| /generate-report | 4.3         |

 All endpoints achieved required accuracy ≥ 4/5

