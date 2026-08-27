# LeMaterial: an open source initiative to accelerate materials discovery and research (Hugging Face blog)

LeMaterial is an open-source collaborative project led by Entalpic and Hugging Face. LeMaterial aims to simplify and accelerate materials research, making it easier to train ML models, identify novel materials and explore chemical spaces.

## LeMat-Bulk dataset
The first release, LeMat-Bulk, unifies, cleans and standardizes the most prominent material datasets, including Materials Project, Alexandria and OQMD — giving rise to a single harmonized data format with 6.7M entries and 7 materials properties. Built on Optimade, Materials Project, Alexandria and OQMD. License CC-BY-4.0.

Challenges addressed: dataset integration issues (inconsistent formats), biases in dataset composition (e.g. Materials Project focus on oxides/batteries), limited scope, lack of connections between similar materials.

## Material fingerprint (hashing function)
A key contribution of LeMaterial: a definition of a material fingerprint through a hashing function that assigns a unique identifier to each material. Uses a bonding algorithm (e.g. EconNN) on the crystal structure to extract a graph, then computes the Weisfeiler-Lehman algorithm to get a hash, combined with composition and space group information. Much faster than Pymatgen's StructureMatcher (Carbon-24: 100 seconds vs 17 hours; MPTS-52: 330 seconds vs 4.9 hours).

## ML models
LeMaterial trains machine learning interatomic potentials like EquiformerV2 and FAENet on LeMat-Bulk. Future releases include r2SCAN data, OC20 & OC22 surface datasets, MPTrj and OMat24 trajectories.

Applications: exploring extended phase diagrams, comparing material properties across databases/functionals, determining if a material is novel, training predictive ML models (MLIP).

Thanks to Zachary Ulissi and Luis Barroso-Luque (Meta) and Matt McDermott (Newfound Materials).

Source: https://huggingface.co/blog/lematerial (fetched 2026-08-27)
