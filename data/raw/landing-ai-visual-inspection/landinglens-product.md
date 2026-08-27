# LandingLens Product Notes

Source: https://landing.ai/landinglens (fetched 2026-08-27)

LandingLens is LandingAI's computer-vision platform purpose-built for manufacturing visual inspection. It embodies Andrew Ng's data-centric AI thesis: for narrow industrial defect-detection tasks the training set is small (often tens to a few hundred images), so the leverage is in systematically improving data quality and label consistency rather than scaling the model.

## Workflow
1. Upload images from the production line.
2. Label defects (classification, object detection, segmentation, anomaly detection).
3. Train a deep-learning model in the cloud.
4. Deploy to the edge (LandingEdge) for real-time inline inspection.
5. Continuously improve by feeding misclassified cases back into the dataset.

## Technical
- Underlying models are CNN / vision-transformer based deep networks for image classification, object detection, and segmentation.
- Emphasis on consistent labeling, defect book / class ontology, and human-in-the-loop review.
- Runs on GPU in cloud training and CPU/GPU at the edge for inference.
- Integrates with factory cameras and PLCs for pass/fail signaling.

## Funding / traction
- LandingAI raised a $57M Series A led by McRock Capital and Insight Partners (2021).
- Andrew Ng is founder and CEO.
