# GPT-2 From Scratch

Building GPT-2 from scratch, following Andrej Karpathy's video lectures and Stanford CS224N.

## Repo Structure

```
src/                  # My implementation
  model.py            # GPT-2 architecture

karpathy/             # Working code following Karpathy's videos
  bigram-gpt.ipynb    # "Let's build GPT" (2hr video) - bigram to transformer
  gpt2.py             # "Let's reproduce GPT-2" (4hr video) - architecture + weight loading
```

## Learning Path

1. Transformer fundamentals - attention, MLP, residual connections, layer norm
2. GPT-2 architecture - implement and validate against HuggingFace pretrained weights
3. Closed book re-implementation under `src/`
4. LoRA fine-tuning on downstream tasks
5. GPT-2 training from scratch (upcoming)

## References

- [Karpathy - Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY)
- [Karpathy - Let's reproduce GPT-2](https://www.youtube.com/watch?v=l8pRSuU81PU)
- [Stanford CS224N](https://web.stanford.edu/class/cs224n/)
- [CS224N GPT-2 Project Repo](https://github.com/cfifty/public_cs224n_gpt)
- [Attention Is All You Need (2017)](https://arxiv.org/abs/1706.03762)
- [Language Models are Unsupervised Multitask Learners (GPT-2)](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
- [Language Models are Few-Shot Learners (GPT-3)](https://arxiv.org/abs/2005.14165)
