# Applied Compute Case Studies - Model Extraction Analysis

## Summary

Applied Compute is a training platform (not a model provider), but their case studies describe specific trained models for clients. These could potentially be extracted as vertical-domain model entries.

## Case Study Assessment

### 1. Harvey Legal Agent (case-studies__harvey.md) - HIGH VALUE

- **Model**: AC GLM-5.1 (trained for Harvey)
- **Domain**: `legal`
- **Base model**: GLM-5.1
- **Status**: released (in production)
- **Training details**: Full-parameter RL, detailed reward design, grader alignment analysis
- **Benchmarks**: Harvey LAB benchmark - rubric pass rate 0.853 -> 0.913, outperforms Opus 4.8 Max and GPT-5.5 xhigh
- **Key info**: 1,250+ tasks across 24 legal practice areas, 75,000+ binary criteria
- **Extractable**: YES - rich technical detail about training, benchmarks, base model

### 2. Harvey Review Table (case-studies__harvey-review-table.md) - HIGH VALUE

- **Model**: AC-Harvey Review Table Model
- **Domain**: `legal`
- **Base model**: GLM 5.2
- **Status**: released (in production)
- **Training details**: RL with custom reward function (precision/recall for citations), detailed reward math
- **Benchmarks**: Answer Score 0.903 (vs 0.867 Fable 5, 0.857 GPT-5.6-Sol), citation precision 84.1%, recall 91.93%
- **Key info**: 54.8% cost reduction vs Claude Sonnet 5, optimized for document review at scale
- **Extractable**: YES - clear model with metrics and production deployment

### 3. DoorDash Menu Model (case-studies__doordash.md) - MEDIUM VALUE

- **Model**: DoorDash Menu Error Correction Model (trained by Applied Compute)
- **Domain**: `retail-ecommerce` (food delivery / merchant onboarding)
- **Status**: released (rolled out to all US menu traffic)
- **Training details**: RL with automated grader calibrated to human QA, A/B testing
- **Benchmarks**: ~30% reduction in low-quality menus (relative)
- **Key info**: No base model specified, no parameter count, limited technical details
- **Extractable**: PARTIALLY - has deployment info but lacks model architecture/parameter details

### 4. Cognition SWE-Check (case-studies__cognition.md) - HIGH VALUE

- **Model**: SWE-check
- **Domain**: Could be `manufacturing` (software development tooling) - no exact domain fit, closest might be a new category
- **Company**: Cognition (Devin/Windsurf)
- **Status**: released (in production powering Quick Review in Windsurf)
- **Training details**: Two-phase post-training (capability maximization + product alignment), RL with F-beta reward, reward linearization
- **Benchmarks**: 10x faster than frontier (Opus 4.6) while matching quality
- **Key info**: Detailed reward function design, trained in production Windsurf environment replica
- **Extractable**: YES - very detailed training methodology, but domain mapping is unclear (not a clean fit for existing domains)
- **Note**: Domain does not fit schema enum. Closest would be omitting or using a generic category.

### 5. Mercor APEX-Agents (case-studies__mercor.md) - MEDIUM-HIGH VALUE

- **Model**: Applied Compute: Small
- **Domain**: `human-resources` (talent/hiring) or `legal` (top in corporate law)
- **Base model**: GLM 4.6
- **Status**: released
- **Training details**: Long-horizon RL, 874 tasks, no SFT warmup
- **Benchmarks**: #1 on APEX-Agents Corporate Law (54.8%), #4 overall, beats Opus 4.5 and GPT 5.2
- **Key info**: Multi-domain (banking, consulting, law), training from 3.8% to 16.3% Pass@1 on law
- **Extractable**: YES - has benchmark scores, base model, training details

### 6. NVIDIA (case-studies__nvidia.md) - LOW VALUE

- **Model**: No specific model trained - this is a partnership description
- **Domain**: N/A (general platform collaboration)
- **Status**: N/A
- **Key info**: Describes collaboration on Nemotron post-training, inference benchmarks, production statistics sharing
- **Extractable**: NO - no specific model produced, this is a partnership overview

## Recommended Extractions

| Case Study | Model Name | Domain | Priority |
|---|---|---|---|
| Harvey | AC GLM-5.1 Legal Agent | legal | P1 |
| Harvey Review Table | AC-Harvey Review Table | legal | P1 |
| Cognition | SWE-check | (no clean fit) | P2 |
| Mercor | Applied Compute: Small | human-resources or legal | P2 |
| DoorDash | DoorDash Menu Model | retail-ecommerce | P3 |
| NVIDIA | (none) | - | Skip |

## Notes

- The `extract_yaml.py --dry-run` successfully generates prompts for all case studies
- The script detects domain from the file's parent directory, so files would need to be placed in the correct `domains/` subdirectory before running actual extraction
- The Harvey case studies have the richest technical data (base model, benchmarks, training methodology) making them the best candidates
- The Cognition SWE-check model is very well documented but has no clean domain mapping in the schema (it's a software engineering tool)
