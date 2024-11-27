from transformers import pipeline

# Global context to remove any possible latency
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")


def classify_tags(post, tags):
    res = classifier(post, tags) # type: ignore
    s = res['labels'][:3]  # type: ignore
    # TODO: Also measure the difference between the scores and select based on distribution

    return s
