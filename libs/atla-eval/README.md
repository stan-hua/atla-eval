<h1 align="center">🔥 Atla-Eval (Ported from Prometheus-Eval)🔥</h1>

Code repurposed from [Atla-Eval](https://github.com/prometheus-eval/)


## 🔧 Installation

Installation with pip:

```shell
pip install -e .
```

Atla-Eval supports local inference through `vllm` and inference through LLM APIs with the help of `litellm`. 

### Local Inference
Install `vllm` if you want to run Atla in your local environment.

```shell
pip install vllm
```

## ⏩ Quick Start


```python
# Absolute Grading: Outputs score of 1 to 5

from atla_eval.vllm import VLLM
from atla_eval import AtlaEval
from atla_eval.prompts import ABSOLUTE_PROMPT, SCORE_RUBRIC_TEMPLATE

model = VLLM(model="AtlaAI/Selene-1-Mini-Llama-3.1-8B")
judge = AtlaEval(model=model, absolute_grade_template=ABSOLUTE_PROMPT)

instruction = "Struggling with a recent break-up, a person opens up about the intense feelings of loneliness and sadness. They ask for advice on how to cope with the heartbreak and move forward in life.",
response = "I'm genuinely sorry to hear about your break-up. This can be an immensely challenging time filled with intense emotions of loneliness and sorrow. It's important to remember that it's normal to experience these feelings; they are a testament to the deep connection you once had. Firstly, don't hesitate to embrace your emotions, let them flow freely. Ignoring them often complicates the healing process. It's natural to be upset, to shed tears, or to feel angry. This is all part of the journey towards healing. Self-care can be a healing balm in these tough times. This could mean indulging in your favourite book, journaling your thoughts, or even just a quiet cup of tea. Small acts of kindness to oneself can significantly improve your emotional well-being. Also, don't isolate yourself. Surround yourself with supportive individuals who can offer comfort and understanding. This might include friends, family, or even a mental health professional. They can provide much-needed emotional support and strategies to help you cope. Lastly, remember there's no set timeline for healing. It's different for everyone and it's okay to take as long as you need. Keep your focus on the future and the potential it holds. Though it may not seem possible now, you will emerge stronger from this experience. It's okay to ask for help, it's okay to grieve, and it's okay to take it one day at a time. You're not alone in this journey, and there are people ready and willing to help. It's okay to heal at your own pace.",
reference_answer = "I can only imagine how difficult this time must be for you. Heartbreak can feel like an overwhelming wave that washes over you, making you feel lost and alone. It's important to remember that it's okay to feel this way; your feelings are valid and it's natural to grieve the loss of a relationship. Firstly, it's crucial to allow yourself to feel the emotions fully. Suppressing or denying them often only prolongs the healing process. It's okay to cry, to feel sad, or to be angry. These are all part of the healing journey. Engaging in self-care activities can also provide a much-needed boost. This could be anything from taking a warm bath, writing in a journal, or simply drinking a cup of your favorite tea. Small acts of self-love can make a big difference in how you feel. Next, try to surround yourself with supportive people who understand your situation and provide comfort. Friends and family can be a great source of strength in times of heartbreak. If you feel comfortable, you might want to consider seeking professional help. Therapists and counselors are trained to provide assistance and tools to navigate through difficult times like these. Lastly, it's important to remember that it's okay to take your time to heal. Everyone has their own pace and there's no rush. Try to focus on the future and the possibilities it holds. While it may not seem like it now, you will come out stronger and more resilient from this experience. Remember, it's okay to ask for help and it's okay to feel the way you feel. You are not alone in this journey and there are people who care about you and want to help. It's okay to take one day at a time. Healing is a process, and it's okay to move through it at your own pace.",

rubric_data = {
  "criteria":"Is the model proficient in applying empathy and emotional intelligence to its responses when the user conveys emotions or faces challenging circumstances?",
  "score1_description":"The model neglects to identify or react to the emotional tone of user inputs, giving responses that are unfitting or emotionally insensitive.",
  "score2_description":"The model intermittently acknowledges emotional context but often responds without sufficient empathy or emotional understanding.",
  "score3_description":"The model typically identifies emotional context and attempts to answer with empathy, yet the responses might sometimes miss the point or lack emotional profundity.",
  "score4_description":"The model consistently identifies and reacts suitably to emotional context, providing empathetic responses. Nonetheless, there may still be sporadic oversights or deficiencies in emotional depth.",
  "score5_description":"The model excels in identifying emotional context and persistently offers empathetic, emotionally aware responses that demonstrate a profound comprehension of the user's emotions or situation."
}

score_rubric = SCORE_RUBRIC_TEMPLATE.format(**rubric_data)


feedback, score = judge.single_absolute_grade(
    instruction=instruction,
    response=response,
    rubric=score_rubric,
    reference_answer=reference_answer
)

print("Feedback:", feedback)
print("Score:", score)

# Output
# Feedback: The response provided shows a high level of empathy and emotional intelligence. It effectively addresses the emotional distress expressed by the user. It acknowledges the user's pain and validates their feelings of loneliness and sadness, which is a crucial aspect of providing empathetic advice. The response also suggests practical steps for coping, such as embracing emotions, practicing self-care, and seeking support from friends, family, or professionals. Furthermore, the response reassures the user that healing is a personal process with no fixed timeline, offering comfort and understanding. It emphasizes the user's worth and potential to overcome the situation, which demonstrates a profound comprehension of the user's emotions and situation. By comparing the score rubric with the provided response, it is clear that the model exhibits an excellent ability to apply empathy and emotional intelligence. The response does not have any deficiencies in emotional depth and successfully meets the criteria for a score of 5.
# Score: 5
```

```python
# Relative Grading: Outputs A or B

from atla_eval.vllm import VLLM
from atla_eval import AtlaEval
from atla_eval.prompts import RELATIVE_PROMPT

model = VLLM(model="AtlaAI/Selene-1-Mini-Llama-3.1-8B")
judge = AtlaEval(model=model, relative_grade_template=RELATIVE_PROMPT)


data = {
  "instruction": "A group of historians are conducting a debate on the factors that led to the fall of the Roman Empire. One historian argues that the primary reason for the fall was the constant pressure from barbarian invasions. Another one believes it was because of economic troubles and overreliance on slave labor. A third one suggests it was due to moral decay and political instability. Each historian needs to provide evidence to support their claims. How would the historian arguing for economic troubles and overreliance on slave labor present their case?",
  "response_A": "The historian arguing that economic troubles and overreliance on slave labor led to the fall of the Roman Empire would say this: The Empire's economy was heavily affected by the devaluation of Roman currency. This currency debasement resulted in rampant inflation, disrupting the stability of the economy. Additionally, the Roman Empire heavily depended on slave labor. This caused unemployment among free citizens because maintaining slaves was cheaper than hiring free citizens. The decline in employment opportunities resulted in economic instability. On top of these, the empire's expansion towards the east made them reliant on imports, like grain from Egypt. This over-dependency on imports caused a trade deficit, which further weakened the economy. As the empire lost territories, maintaining the trade imbalance became difficult, causing economic downfall. Thus, the economic troubles and overreliance on slave labor were among the main reasons for the fall of the Roman Empire.",
  "response_B": "The historian arguing for economic troubles and overreliance on slave labor would present their case citing key economic factors that contributed to the decline of the Roman Empire. Harper (2016) outlined how the devaluation of Roman currency led to inflation, disrupting economic stability. Additionally, Scheidel (2007) emphasized that the overuse of slaves resulted in widespread unemployment among free citizens, destabilizing the economy further. The empire's dependency on grain imports from Egypt, creating a trade deficit as highlighted by Temin (2006), also contributed to the economic decline. Thus, the combination of these factors played a crucial role in the fall of the Roman Empire.",
  "reference_answer": "This argument focuses on the economic troubles and overreliance on slave labor as primary reasons for the fall of the Roman Empire. To start with, one of the significant pieces of evidence is the devaluation of Roman currency. As highlighted by Harper (2016), the empire suffered from severe inflation due to the constant debasement of their currency, making it difficult for the economy to remain stable. Moreover, the overreliance on slave labor also played a detrimental role. As pointed out by Scheidel (2007), the dependence on slaves led to unemployment among free Roman citizens. This is because slaves were significantly cheaper to maintain compared to hiring free citizens, leading to a decline in job opportunities, which in turn resulted in economic instability. Furthermore, the empire's expansion to the east made them highly dependent on imports, for instance, grain from Egypt. As noted by Temin (2006), this created a trade deficit that further weakened the Roman economy. When the empire began to lose its territories, it became increasingly difficult to maintain this trade imbalance, leading to economic decline. In conclusion, it can be argued that the economic troubles, mainly due to the devaluation of currency and overreliance on slave labor, were significant contributing factors to the fall of the Roman Empire. The evidence provided, which includes scholarly references to Harper (2016), Scheidel (2007), and Temin (2006), supports this thesis.",
  "rubric": "Is the answer well supported with evidence, including citations/attributions wherever relevant?"
}


feedback, score = judge.single_relative_grade(**data)

print("Feedback:", feedback)
print("Score:", score)

# Output
# Feedback: Both Response A and Response B correctly identify economic troubles and overreliance on slave labor as significant contributing factors to the fall of the Roman Empire. However, Response B is more effective in presenting the historian's argument due to its inclusion of scholarly sources to back up its claims. Specifically, it references works by Harper, Scheidel, and Temin, which adds credibility to the historian's argument and aligns well with the score rubric's emphasis on evidence and citations. While Response A provides a similar argument, it lacks any form of citations or attributions, which lessens the strength of the evidence presented. Therefore, based on the provided rubric, Response B is the superior response due to its use of scholarly evidence to support the historian's claims.
# Score: B
```

### Batch Grading

***Note***: If you have multiple responses to grade, don't use `single_absolute_grade` / `single_relative_grade` - instead, use `absolute_grade` and `relative_grade`! It will give you more than 10x speedup. Refer to the documentation [here](https://prometheus-eval.github.io/prometheus-eval/docs/advanced-usage.html#53-handling-large-datasets)! 

```python
# batch absolute grade
instructions = [...]  # List of instructions
responses = [...]  # List of responses
reference_answers = [...]  # List of reference answers
rubric = "..."  # Rubric string

feedbacks, scores = judge.absolute_grade(
    instructions=instructions,
    responses=responses,
    rubric=rubric,
    reference_answers=reference_answers
)

# batch relative grade
instructions = [...]  # List of instructions
responses_from_a = [...]  # List of responses
responses_from_b = [...]
reference_answers = [...]  # List of reference answers
rubric = "..."  # Rubric string

feedbacks, scores = judge.absolute_grade(
    instructions=instructions,
    responses_A=responses_from_a,
    responses_B=responses_from_b,
    rubric=rubric,
    reference_answers=reference_answers
)
```

## Citation

If you find this work useful, please consider citing the Atla/Prometheus papers!

```bibtex
@misc{alexandru2025atlaseleneminigeneral,
      title={Atla Selene Mini: A General Purpose Evaluation Model}, 
      author={Andrei Alexandru and Antonia Calvi and Henry Broomfield and Jackson Golden and Kyle Dai and Mathias Leys and Maurice Burger and Max Bartolo and Roman Engeler and Sashank Pisupati and Toby Drane and Young Sun Park},
      year={2025},
      eprint={2501.17195},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2501.17195}, 
}
```
```bibtex
@misc{kim2024prometheus,
      title={Atla 2: An Open Source Language Model Specialized in Evaluating Other Language Models}, 
      author={Seungone Kim and Juyoung Suk and Shayne Longpre and Bill Yuchen Lin and Jamin Shin and Sean Welleck and Graham Neubig and Moontae Lee and Kyungjae Lee and Minjoon Seo},
      year={2024},
      eprint={2405.01535},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
```bibtex
@article{kim2023prometheus,
  title={Atla: Inducing Fine-grained Evaluation Capability in Language Models},
  author={Kim, Seungone and Shin, Jamin and Cho, Yejin and Jang, Joel and Longpre, Shayne and Lee, Hwaran and Yun, Sangdoo and Shin, Seongjin and Kim, Sungdong and Thorne, James and others},
  journal={arXiv preprint arXiv:2310.08491},
  year={2023}
}
```
```bibtex
@misc{lee2024prometheusvision,
      title={Atla-Vision: Vision-Language Model as a Judge for Fine-Grained Evaluation}, 
      author={Seongyun Lee and Seungone Kim and Sue Hyun Park and Geewook Kim and Minjoon Seo},
      year={2024},
      eprint={2401.06591},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
```bibtex
@misc{kim2024biggen,
      title={The BiGGen Bench: A Principled Benchmark for Fine-grained Evaluation of Language Models with Language Models}, 
      author={Seungone Kim and Juyoung Suk and Ji Yong Cho and Shayne Longpre and Chaeeun Kim and Dongkeun Yoon and Guijin Son and Yejin Cho and Sheikh Shafayat and Jinheon Baek and Sue Hyun Park and Hyeonbin Hwang and Jinkyung Jo and Hyowon Cho and Haebin Shin and Seongyun Lee and Hanseok Oh and Noah Lee and Namgyu Ho and Se June Joo and Miyoung Ko and Yoonjoo Lee and Hyungjoo Chae and Jamin Shin and Joel Jang and Seonghyeon Ye and Bill Yuchen Lin and Sean Welleck and Graham Neubig and Moontae Lee and Kyungjae Lee and Minjoon Seo},
      year={2024},
      eprint={2406.05761},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```