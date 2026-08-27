# SWE-bench technical report (Devin)

Source: https://cognition.ai/blog/swe-bench-technical-report
Fetched: 2026-08-27

To evaluate Devin, Cognition turned to SWE-bench, an automated benchmark for software engineering systems consisting of GitHub issues and pull requests. SWE-bench deterministically evaluates (via unit tests) a system's ability to solve issues in real world codebases, unlike benchmarks like HumanEval which are limited to standalone functions.

In SWE-bench, Devin successfully resolves 13.86% of issues, far exceeding the previous highest unassisted baseline of 1.96%. Even when given the exact files to edit ("assisted"), the best previous model only resolves 4.80% of issues.

Evaluation harness and Devin's code edits at https://github.com/CognitionAI/devin-swebench-results.

## Background
SWE-bench is a dataset of 2,294 issues and pull requests scraped from popular open source Python repositories on GitHub. Each instance consists of a GitHub issue and the pull request which resolved it, with a "fail to pass" unit test.

In SWE-bench, LLMs are either given the set of correct files ("assisted") or a retrieval system selects files ("unassisted"). As an agent, Devin navigates files on its own, comparable to "unassisted."

## Methodology
- Run the agent end to end using a standardized prompt that asks it to edit code given only the GitHub issue description.
- The repo is cloned in the agent's environment; only base commit and ancestors kept to prevent leakage; git remote removed.
- Python conda environment set up before test.
- Devin limited to 45 minutes of runtime; can terminate earlier.

## Results
Evaluated on a randomly chosen 25% of the SWE-bench test set (570 of 2,294). Devin resolved 79 of 570 issues → 13.86% success rate, significantly higher than previous best assisted system (Claude 2) at 4.80%.
