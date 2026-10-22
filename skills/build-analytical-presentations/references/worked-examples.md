# Worked examples

These examples are fictional. The names, values, and situations are illustrative and provide no evidence for a real organisation. Use them to understand the reasoning and arrangement, then replace them with authorised task inputs.

## Example A: A bounded service trial

### Brief and evidence

An operations manager must choose whether to authorise a two-week trial. A five-day sample at one service desk recorded a median waiting time of 24 minutes. A process study attributes 14 minutes of that wait to verification. The sample describes a bottleneck but does not prove the proposed solution.

The proposed trial moves document checking earlier. Its success criteria are a median wait of 18 minutes or less and no increase from the baseline 6 repeat requests per 100 completed requests. The trial uses existing staff. Trial planning estimates a cost of 2,000 budget units, including measurement time. These are proposed conditions, not observed results.

### Slide sequence

| Slide | Purpose and headline | Arrangement | Evidence or qualification |
| --- | --- | --- | --- |
| 1 | Decide: "Approve a two-week verification trial" | Recommendation and bounded ask | One desk, existing staff, cost cap of 2,000 budget units |
| 2 | Establish the observed problem: "Median waiting time was 24 minutes" | Dominant measured-value view with a short scope note | Five-day sample; not an organisation-wide estimate |
| 3 | Explain the mechanism: "Verification is the main measured source of waiting" | Process diagram with the 14-minute step highlighted | Process-study attribution; avoid claiming proven causality |
| 4 | Compare choices: "Earlier checking targets the constraint without adding a role" | Status quo versus earlier checking | Benefits are hypotheses; no invented savings |
| 5 | Bound the experiment: "Measure waiting and repeat requests together" | Criteria table and two-week timeline | Target wait at most 18 minutes; repeat rate at most 6 per 100 |
| 6 | Resolve the ask: "Approve the trial, then review both outcomes before expansion" | Decision block with scope, owner role, and checkpoint | Expansion remains a later decision |

### Writing and layout choices

The recommendation comes first because the audience has a decision to make. The mechanism receives a diagram instead of a generic list of benefits. The comparison includes the status quo. The conclusion repeats the bounded action, rather than pretending that the trial's result is already known.

For live delivery, keep the measurement-window qualification visible and move detailed collection instructions into notes. For independent reading, add a short explanation of how each metric will be collected.

## Example B: A technical release review

### Brief and evidence

A release board must decide whether a fictional document-processing service can move from a controlled test to a limited pilot. Under a fixed replay test, the system processed 100 documents per minute with a 95th-percentile response time of 1.4 seconds and 2 failed requests per 1,000. At 150 documents per minute, the corresponding results were 2.8 seconds and 9 per 1,000.

The agreed criteria are a 95th-percentile response time of at most 2 seconds and at most 5 failed requests per 1,000. The replay test does not establish behaviour with all real document types, concurrent deployments, or long-running operation.

### Slide sequence

| Slide | Purpose and headline | Arrangement | Evidence or qualification |
| --- | --- | --- | --- |
| 1 | State the decision: "Limit the pilot to 100 documents per minute" | Recommendation plus conditions | A proposed operating limit, not a maximum capacity claim |
| 2 | Establish criteria: "Acceptance requires both response time and reliability" | Two-metric criteria table | Both criteria were agreed before evaluating results |
| 3 | Explain the system: "Requests share a validation stage before processing" | Simple architecture or process diagram | An illustrative architecture, not evidence of the cause of failures |
| 4 | Show results: "The 100-document test met both criteria; the 150-document test missed both" | Aligned charts or a compact results table | Fixed replay test; identify units and percentile |
| 5 | Expose limits: "Replay results leave three pilot conditions untested" | Risk-and-next-test table | Real document mix, deployment overlap, and duration |
| 6 | Resolve the decision: "Approve a monitored pilot with a stop rule" | Decision and monitoring block | Use agreed criteria as stop thresholds; no claim of production readiness |

### Adaptation choices

For a specialist audience, retain the percentile and failure-rate definitions and provide the replay method in backup material. For a non-specialist board, add one sentence explaining the percentile and place implementation detail in notes. Both versions must preserve the limited evidence boundary.

Apply a different approved company template without changing these facts. Reassess the recommendation if that organisation uses different acceptance criteria; brand replacement alone is not substantive adaptation.
