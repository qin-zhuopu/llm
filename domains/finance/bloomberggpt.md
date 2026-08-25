# BloombergGPT

> 来源: [https://www.bloomberg.com](https://www.bloomberg.com)
> 抓取时间: 2026-08-25
> 公司: Bloomberg

---

BloombergGPT is a 50.6 billion parameter large language model purpose-built for the financial domain, developed by Bloomberg's AI Engineering team. Published in a research paper (arxiv.org/abs/2303.17564) in March 2023, it represents one of the most ambitious domain-specific language model projects in financial services, trained over 53 days consuming 1.3 million GPU hours.

## Training Data

### FinPile — Domain-Specific Dataset
BloombergGPT was trained on FinPile, a comprehensive 363 billion token dataset constructed from Bloomberg's extensive proprietary data sources, representing perhaps the largest domain-specific dataset assembled at the time. FinPile includes:
- **Financial news articles**: Decades of financial journalism and market reporting
- **Regulatory filings**: SEC filings, annual reports, and corporate disclosures
- **Press releases**: Company announcements and industry news
- **Web-scraped financial documents**: Financial analysis, commentary, and research
- **Social media**: Financial discussion and sentiment from social platforms

### General-Purpose Dataset
The financial data is augmented with 345 billion tokens from general-purpose datasets commonly used for LLM training, creating a total training corpus of approximately 708 billion tokens with roughly equal parts domain-specific and general-purpose text.

## Model Architecture & Training

- **Parameters**: 50.6 billion (50B)
- **Architecture**: Decoder-only transformer (BLOOM architecture variant)
- **Training tokens**: ~708 billion (363B financial + 345B general)
- **Training duration**: 53 days
- **GPU hours**: 1.3 million
- **Estimated training cost**: $2.67 million to $10 million

## Performance

BloombergGPT demonstrates significant advantages on financial NLP tasks while maintaining competitive performance on general benchmarks:

### Financial Tasks
The model outperforms existing models of similar size on financial-specific tasks by 8-10 percentage points, achieving 62.5% average accuracy on public financial benchmarks. Key financial capabilities include:
- **Sentiment analysis**: Classifying financial news and social media sentiment
- **Named Entity Recognition (NER)**: Identifying companies, people, financial instruments, and other entities in financial text
- **News classification**: Categorizing financial news by topic, sector, and relevance
- **Question answering**: Responding to financial queries with domain expertise
- **Headline generation**: Creating summaries of financial events

### General Capabilities
Despite its financial specialization, BloombergGPT maintains strong performance on general NLP benchmarks including reading comprehension, language understanding, and common sense reasoning, demonstrating that domain-specific training does not sacrifice general capabilities.

## Usage

BloombergGPT is designed for internal use within Bloomberg's products and services, enhancing capabilities across the Bloomberg Terminal ecosystem. It assists Bloomberg in improving existing financial NLP applications that serve hundreds of thousands of financial professionals worldwide.

## Significance

BloombergGPT represents a landmark in domain-specific LLM development, demonstrating that training on a carefully curated mix of domain and general data produces a model that excels at specialized tasks while retaining broad language capabilities. It established a template for how organizations with large proprietary datasets can build custom language models tailored to their industry.
