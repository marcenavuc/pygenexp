class Pipeline:
    def __init__(self, background=None, normalization=None, summarization=None):
        self.normalization = normalization
        self.background = background
        self.summarization = summarization

    def run(self):
        return self.summarization(self.normalization(self.background()))
