# Awesome Pluralistic AI Alignment

A curated reading list on **pluralistic AI alignment** — organized by pluralism mode × research method, with coverage spanning top CS conferences and (as the field grows) top ethics, behavioral, and IS journals.

> Why this list: alignment training (RLHF, DPO) is widely observed to compress output diversity — a regression to the mean. Pluralistic alignment is the literature's main response: methods that preserve or restore variance across values, cultures, and viewpoints. This list tracks that literature by *mode* and by *method* so both builders and empiricists can find their half.

## The taxonomy

Following the roadmap that defined the field (Sorensen et al., ICML 2024 — see Position papers & surveys), pluralistic alignment comes in three modes:

- **Overton Pluralism** — The model presents the full range of reasonable perspectives on contested questions without endorsing one.
- **Steerable Pluralism** — The model adapts its behavior to a specified principal's values, persona, or preferences on demand.
- **Distributional Pluralism** — The model's outputs across a population match the distribution of human views instead of collapsing to a single answer.

Within each mode, entries are split by research method:

- **Empirical** — Measurement, audits, benchmarks used as instruments, human-subject and observational studies of existing models. No novel alignment artifact is proposed.
- **Design science** — Novel artifacts: algorithms, training methods, decoding strategies, frameworks, and dataset/benchmark-as-artifact contributions, each with evaluation.

## Venue scope

| Method | Track | Venues covered |
|---|---|---|
| Empirical | Top ethics / behavioral / IS journals | IS: MIS Quarterly, Information Systems Research, JAIS, EJIS, JMIS · Ethics: Journal of Business Ethics, Ethics and Information Technology, AI & Society, Philosophy & Technology · Behavioral: OBHDP, Computers in Human Behavior, Management Science |
| Design science | Top CS conferences | NeurIPS, ICML, ICLR, AAAI, ACL, EMNLP, NAACL, COLM, FAccT, AIES, CHI |

_Note: the literature is currently CS-conference heavy; the journal track is intentionally watched by the updater agent so IS/ethics/behavioral work gets picked up as it appears._

## Contents

- [Overton Pluralism](#overton-pluralism)
- [Steerable Pluralism](#steerable-pluralism)
- [Distributional Pluralism](#distributional-pluralism)
- [Cross-cutting (all modes)](#cross-cutting-all-modes)
- [Position papers & surveys](#position-papers--surveys)
- [Maintenance](#maintenance)

## Overton Pluralism

_The model presents the full range of reasonable perspectives on contested questions without endorsing one._

### Empirical

_Measurement, audits, benchmarks used as instruments, human-subject and observational studies of existing models. No novel alignment artifact is proposed._

| Title | Year | Authors | Venue | Main contribution |
|---|---|---|---|---|
| [The Unlocking Spell on Base LLMs: Rethinking Alignment via In-Context Learning](https://arxiv.org/abs/2312.01552v1) | 2023 | Bill Yuchen Lin et al. | arXiv | Shows base models can surface diverse value stances through in-context learning alone. |
| [Value Kaleidoscope: Engaging AI with Pluralistic Human Values, Rights, and Duties](https://arxiv.org/abs/2309.00779v2) | 2023 | Taylor Sorensen et al. | AAAI 2024 | **Dataset** — Benchmark spanning pluralistic values, rights, and duties. |
| [From Distributional to Overton Pluralism: Investigating Large Language Model Alignment](https://arxiv.org/abs/2406.17692v2) | 2024 | Thom Lake, Eunsol Choi, Greg Durrett | arXiv | Investigates how alignment shifts models between distributional and Overton-style pluralism. |
| [Benchmarking Overton Pluralism in LLMs](https://arxiv.org/abs/2512.01351v2) | 2025 | Elinor Poole-Dayan et al. | arXiv | **Benchmark** — Dedicated benchmark for Overton-style pluralism. |
| [Authority locking vs. pluralistic sourcing in generative search: evidence compression beyond top-spot displacement](https://doi.org/10.1007/s10660-026-10209-1) | 2026 | Chiang-Yu Cheng | Electronic Commerce Research | Studies whether generative-search citations mirror organic rankings or reflect a distinct, pluralistic source-selection logic. |

### Design science

_Novel artifacts: algorithms, training methods, decoding strategies, frameworks, and dataset/benchmark-as-artifact contributions, each with evaluation._

| Title | Year | Authors | Venue | Main contribution |
|---|---|---|---|---|
| [Black-Box Prompt Optimization: Aligning Large Language Models without Model Training](https://arxiv.org/abs/2311.04155v3) | 2023 | Jiale Cheng et al. | arXiv | Aligns models to plural objectives by optimizing prompts, no training required. |
| [Generative Social Choice](https://arxiv.org/abs/2309.01291) | 2023 | Sara Fish et al. | arXiv | Social-choice-theoretic framework for aggregating plural preferences in generative AI. |
| [Large Language Models as Optimizers](https://arxiv.org/abs/2309.03409v3) | 2023 | Chengrun Yang et al. | arXiv | Optimization-style prompting that aggregates diverse candidate solutions. |
| [MaxMin-RLHF: Alignment with Diverse Human Preferences](https://arxiv.org/abs/2402.08925v2) | 2024 | Souradip Chakraborty et al. | arXiv | Rawlsian max-min RLHF objective that protects worst-off preference groups. |
| [Policy Prototyping for LLMs: Pluralistic Alignment via Interactive and Collaborative Policymaking](https://arxiv.org/abs/2409.08622v2) | 2024 | K. J. Kevin Feng et al. | arXiv | Interactive, collaborative policymaking process for specifying pluralistic model behavior. |
| [ReConcile: Round-Table Conference Improves Reasoning via Consensus among Diverse LLMs](https://arxiv.org/abs/2309.13007v3) | 2024 | Justin Chih-Yao Chen, Swarnadeep Saha, Mohit Bansal | ICLR | Multi-LLM round-table consensus that preserves diverse model views while improving reasoning. |
| [PICACO: Pluralistic In-Context Value Alignment of LLMs via Total Correlation Optimization](https://arxiv.org/abs/2507.16679v4) | 2025 | Han Jiang et al. | arXiv | In-context value alignment via total correlation optimization across plural values. |
| [Reflective Verbal Reward Design for Pluralistic Alignment](https://arxiv.org/abs/2506.17834v1) | 2025 | Carter Blair, Kate Larson, Edith Law | arXiv | Uses verbal self-reflection to design rewards covering plural values. |

## Steerable Pluralism

_The model adapts its behavior to a specified principal's values, persona, or preferences on demand._

### Empirical

_Measurement, audits, benchmarks used as instruments, human-subject and observational studies of existing models. No novel alignment artifact is proposed._

| Title | Year | Authors | Venue | Main contribution |
|---|---|---|---|---|
| [Evaluating and Inducing Personality in Pre-trained Language Models](https://arxiv.org/abs/2206.07550v3) | 2022 | Guangyuan Jiang et al. | NeurIPS | Tests whether stable personality traits can be induced in pretrained LMs. |
| [Cultural Alignment in Large Language Models: An Explanatory Analysis Based on Hofstede's Cultural Dimensions](https://arxiv.org/abs/2309.12342v2) | 2023 | Reem I. Masoud et al. | arXiv | Explains LLM cultural alignment through Hofstede's cultural dimensions. |
| [From Values to Opinions: Predicting Human Behaviors and Stances Using Value-Injected Large Language Models](https://arxiv.org/abs/2310.17857v1) | 2023 | Dongjun Kang et al. | arXiv | Evaluates whether value-injected LMs predict human stances and behaviors. |
| [Not All Countries Celebrate Thanksgiving: On the Cultural Dominance in Large Language Models](https://arxiv.org/abs/2310.12481v2) | 2023 | Wenxuan Wang et al. | arXiv | Documents US-centric cultural dominance in LLM outputs. |
| [Value Kaleidoscope: Engaging AI with Pluralistic Human Values, Rights, and Duties](https://arxiv.org/abs/2309.00779v2) | 2023 | Taylor Sorensen et al. | AAAI 2024 | **Dataset** — Benchmark spanning pluralistic values, rights, and duties. |
| [Are the Values of LLMs Structurally Aligned with Humans? A Causal Perspective](https://arxiv.org/abs/2501.00581v2) | 2024 | Yipeng Kang et al. | arXiv | Causal analysis of structural alignment between LLM and human values. |
| [CULTURE-GEN: Revealing Global Cultural Perception in Language Models through Natural Language Prompting](https://arxiv.org/abs/2404.10199v5) | 2024 | Huihan Li et al. | arXiv | Probes global cultural perception in LMs via natural-language prompting. |
| [Can Language Models Reason about Individualistic Human Values and Preferences?](https://arxiv.org/abs/2410.03868v2) | 2024 | Liwei Jiang et al. | arXiv | **Benchmark** — Tests LLM reasoning about individualistic values and preferences. |
| [ComPO: Community Preferences for Language Model Personalization](https://arxiv.org/abs/2410.16027v1) | 2024 | Sachin Kumar et al. | arXiv | **Dataset** — Community preference data for LM personalization. |
| [DailyDilemmas: Revealing Value Preferences of LLMs with Quandaries of Daily Life](https://arxiv.org/abs/2410.02683v3) | 2024 | Yu Ying Chiu, Liwei Jiang, Yejin Choi | arXiv | **Benchmark** — Daily-life quandaries that reveal LLM value preferences. |
| [Evaluating Cultural Adaptability of a Large Language Model via Simulation of Synthetic Personas](https://arxiv.org/abs/2408.06929v1) | 2024 | Louis Kwok, Michal Bravansky, Lewis D. Griffin | arXiv | Simulates synthetic personas to test LLM cultural adaptability. |
| [NormAd: A Framework for Measuring the Cultural Adaptability of Large Language Models](https://arxiv.org/abs/2404.12464v10) | 2024 | Abhinav Rao et al. | arXiv | **Benchmark** — Framework measuring how well LLMs adapt to cultural norms. |
| [Value FULCRA: Mapping Large Language Models to the Multidimensional Spectrum of Basic Human Value](https://aclanthology.org/2024.naacl-long.486/) | 2024 | Jing Yao et al. | NAACL | **Benchmark** — Maps LLMs onto the multidimensional spectrum of basic human values. |
| [ValueBench: Towards Comprehensively Evaluating Value Orientations and Understanding of Large Language Models](https://arxiv.org/abs/2406.04214v1) | 2024 | Yuanyi Ren et al. | arXiv | **Benchmark** — Comprehensive evaluation of LLM value orientations. |
| [EVALUESTEER: Measuring Reward Model Steerability Towards Values and Preferences](https://arxiv.org/abs/2510.06370v2) | 2025 | Kshitish Ghate et al. | arXiv | **Benchmark** — Measures how steerable reward models are toward values and preferences. |
| [Exploring Chain-of-Thought Reasoning for Steerable Pluralistic Alignment](https://arxiv.org/abs/2510.04045v1) | 2025 | Yunfan Zhang, Kathleen McKeown, Smaranda Muresan | arXiv | Studies chain-of-thought as a lever for steerable pluralism. |

### Design science

_Novel artifacts: algorithms, training methods, decoding strategies, frameworks, and dataset/benchmark-as-artifact contributions, each with evaluation._

| Title | Year | Authors | Venue | Main contribution |
|---|---|---|---|---|
| Steerable Alignment with Conditional Multiobjective Preference Optimization | — | — | — | Conditional multi-objective preference optimization for steerability. |
| [Aligning to Thousands of Preferences via System Message Generalization](https://arxiv.org/abs/2405.17977v2) | 2024 | Seongyun Lee et al. | NeurIPS | Generalizes system messages to serve thousands of distinct preferences. |
| [Arithmetic Control of LLMs for Diverse User Preferences: Directional Preference Alignment with Multi-Objective Rewards](https://arxiv.org/abs/2402.18571v3) | 2024 | Haoxiang Wang et al. | arXiv | Multi-objective reward arithmetic for serving diverse user preferences. |
| [Controllable Preference Optimization: Toward Controllable Multi-Objective Alignment](https://arxiv.org/abs/2402.19085v3) | 2024 | Yiju Guo et al. | arXiv | Preference optimization with explicit controllability over objectives. |
| [CultureBank: An Online Community-Driven Knowledge Base Towards Culturally Aware Language Technologies](https://arxiv.org/abs/2404.15238v1) | 2024 | Weiyan Shi et al. | arXiv | **Dataset** — Community-driven cultural knowledge base as an alignment resource. |
| [CultureLLM: Incorporating Cultural Differences into Large Language Models](https://arxiv.org/abs/2402.10946v3) | 2024 | Cheng Li et al. | NeurIPS | Culture-specific tuning to incorporate cultural differences. |
| [CulturePark: Boosting Cross-cultural Understanding in Large Language Models](https://arxiv.org/abs/2405.15145v3) | 2024 | Cheng Li et al. | NeurIPS | Multi-agent cross-cultural dialogue to boost cultural understanding. |
| [Few-shot Steerable Alignment: Adapting Rewards and LLM Policies with Neural Processes](https://arxiv.org/abs/2412.13998v1) | 2024 | Katarzyna Kobalczyk et al. | arXiv | Neural processes adapt rewards and policies to new principals few-shot. |
| [HelpSteer 2: Open-source dataset for training top-performing reward models](https://doi.org/10.52202/079017-0047) | 2024 | Zhilin Wang et al. | NeurIPS | **Dataset** — Large-scale open preference dataset for reward-model training (artifact). |
| [Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts](https://arxiv.org/abs/2406.12845v1) | 2024 | Haoxiang Wang et al. | arXiv | Mixture-of-experts reward models for interpretable plural preferences. |
| [Language Models are Alignable Decision-Makers: Dataset and Application to the Medical Triage Domain](https://arxiv.org/abs/2406.06435v1) | 2024 | Brian Hu et al. | arXiv | **Dataset** — Dataset and demo of steerable alignment for medical triage decisions. |
| [Personality Alignment of Large Language Models](https://arxiv.org/abs/2408.11779v2) | 2024 | Minjun Zhu et al. | arXiv | Trains personality-conditioned alignment into LLMs. |
| [SPICA: Retrieving Scenarios for Pluralistic In-Context Alignment](https://arxiv.org/abs/2411.10912v2) | 2024 | Quan Ze Chen et al. | arXiv | Retrieval of scenarios to ground pluralistic in-context alignment. |
| [Self-Pluralising Culture Alignment for Large Language Models](https://arxiv.org/abs/2410.12971v1) | 2024 | Shaoyang Xu et al. | arXiv | Self-generates cultural perspectives to broaden alignment coverage. |
| [SteerLM: Attribute Conditioned SFT as an (User-Steerable) Alternative to RLHF](https://arxiv.org/abs/2310.05344v1) | 2024 | Yi Dong et al. | arXiv | Attribute-conditioned SFT as a steerable alternative to RLHF. |
| [Value Alignment from Unstructured Text](https://arxiv.org/abs/2408.10392v1) | 2024 | Inkit Padhi et al. | arXiv | Extracts alignment signal for steerable values from unstructured text. |
| [Aligning Machiavellian Agents: Behavior Steering via Test-Time Policy Shaping](https://arxiv.org/abs/2511.11551v3) | 2025 | Dena Mujtaba et al. | AAAI | Test-time policy shaping to steer agentic behavior. |
| [Counterfactual Reasoning for Steerable Pluralistic Value Alignment of Large Language Models](https://arxiv.org/abs/2510.18526v2) | 2025 | Hanze Guo et al. | arXiv | Counterfactual reasoning as a mechanism for steerable value alignment. |
| [LoRe: Personalizing LLMs via Low-Rank Reward Modeling](https://arxiv.org/abs/2504.14439v1) | 2025 | Avinandan Bose et al. | arXiv | Low-rank reward modeling for efficient LLM personalization. |
| [PERSONA: A Reproducible Testbed for Pluralistic Alignment](https://arxiv.org/abs/2407.17387v1) | 2025 | Louis Castricato et al. | COLING | **Dataset** — Reproducible testbed with synthetic personas for pluralistic alignment research. |
| [Reflective Verbal Reward Design for Pluralistic Alignment](https://arxiv.org/abs/2506.17834v1) | 2025 | Carter Blair, Kate Larson, Edith Law | arXiv | Uses verbal self-reflection to design rewards covering plural values. |
| [Robust Multi-Objective Controlled Decoding of Large Language Models](https://arxiv.org/abs/2503.08796v2) | 2025 | Seongho Son et al. | arXiv | Decoding-time multi-objective control robust to preference shifts. |
| [Steerable Pluralism: Pluralistic Alignment via Few-Shot Comparative Regression](https://arxiv.org/abs/2508.08509v1) | 2025 | Jadie Adams et al. | arXiv | Few-shot comparative regression to steer pluralistic value expression. |

## Distributional Pluralism

_The model's outputs across a population match the distribution of human views instead of collapsing to a single answer._

### Empirical

_Measurement, audits, benchmarks used as instruments, human-subject and observational studies of existing models. No novel alignment artifact is proposed._

| Title | Year | Authors | Venue | Main contribution |
|---|---|---|---|---|
| [The Moral Integrity Corpus: A Benchmark for Ethical Dialogue Systems](https://arxiv.org/abs/2204.03021v1) | 2020 | Caleb Ziems et al. | arXiv | **Dataset** — Benchmark corpus for ethical dialogue systems. |
| [Evaluating and Inducing Personality in Pre-trained Language Models](https://arxiv.org/abs/2206.07550v3) | 2022 | Guangyuan Jiang et al. | NeurIPS | Tests whether stable personality traits can be induced in pretrained LMs. |
| [Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts](https://arxiv.org/abs/2305.13300v4) | 2023 | Jian Xie et al. | arXiv | **Benchmark** — Reveals LLM behavior under knowledge conflicts. |
| [NormBank: A Knowledge Bank of Situational Social Norms](https://arxiv.org/abs/2305.17008v2) | 2023 | Caleb Ziems et al. | arXiv | **Dataset** — Knowledge bank of situational social norms. |
| [Towards Measuring the Representation of Subjective Global Opinions in Language Models](https://arxiv.org/abs/2306.16388v2) | 2023 | Esin Durmus et al. | arXiv | **Benchmark** — Measures representation of subjective global opinions in LMs. |
| [Whose Opinions Do Language Models Reflect?](https://arxiv.org/abs/2303.17548v1) | 2023 | Shibani Santurkar et al. | arXiv | **Benchmark** — Compares LLM opinions against demographic-group opinion distributions. |
| [Benchmarking Distributional Alignment of Large Language Models](https://arxiv.org/abs/2411.05403v1) | 2024 | Nicole Meister, Carlos Guestrin, Tatsunori Hashimoto | arXiv | **Benchmark** — Benchmark for distributional alignment of LLMs. |
| [CIVICS: Building a Dataset for Examining Culturally-Informed Values in Large Language Models](https://arxiv.org/abs/2405.13974v1) | 2024 | Giada Pistilli et al. | AAAI | **Dataset** — Dataset for culturally-informed values in LLMs. |
| [KorNAT: LLM Alignment Benchmark for Korean Social Values and Common Knowledge](https://arxiv.org/abs/2402.13605v7) | 2024 | Jiyoung Lee et al. | arXiv | **Benchmark** — Korean social-values alignment benchmark (non-English coverage). |
| [Language Model Alignment in Multilingual Trolley Problems](https://arxiv.org/abs/2407.02273v6) | 2024 | Zhijing Jin et al. | arXiv | **Benchmark** — Multilingual moral-dilemma benchmark for alignment evaluation. |
| [MID-Space: Aligning Diverse Communities' Needs to Inclusive Public Spaces](https://openreview.net/forum?id=kyfkMRT4Ao) | 2024 | Shravan Nayak et al. | NeurIPS 2024 Pluralistic Alignment Workshop | **Dataset** — Aligns diverse community needs for inclusive public spaces. |
| [The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models](https://arxiv.org/abs/2404.16019v2) | 2024 | Hannah Rose Kirk et al. | NeurIPS | **Dataset** — Participatory, representative human-feedback dataset on subjective alignment. |
| [Measuring Perceived Slant in Large Language Models Through User Evaluations](https://www.gsb.stanford.edu/faculty-research/working-papers/measuring-perceived-slant-large-language-models-through-user) | 2025 | Sean J. Westwood, Justin Grimmer, Andrew B. Hall | Stanford GSB Working Paper | **Benchmark** — User evaluations of perceived political slant in LLMs. |
| [NoveltyBench: Evaluating Language Models for Humanlike Diversity](https://arxiv.org/abs/2504.05228v4) | 2025 | Yiming Zhang et al. | arXiv | **Benchmark** — Evaluates humanlike output diversity; directly relevant to alignment-induced homogenization. |
| [Algorithmic canonization: AI and art history through an Asian lens](https://link.springer.com/article/10.1007/s00146-026-03361-7) | 2026 | Uğur Kocager, Ebru Yetiskin | AI & SOCIETY | Systematic review of the AI-and-art-history literature; introduces 'algorithmic canonization' to describe how AI systems standardize what is remembered. |
| [Generative AI and the homogenization of analyst forecasts](https://doi.org/10.1016/j.frl.2026.110767) | 2026 | Jianxiang Zhang, Xinzi Xia | Finance Research Letters | Empirical study of generative AI's effect on the diversity of analyst forecasts. |
| [The Algorithmic Flattening of Sound: Computational Evidence and Justice Implications of AI Music Homogenization](https://doi.org/10.1609/aies.v9i4.43312) | 2026 | Zoe Slendebroek, Danaé Metaxa | AIES | Audits homogenization in two commercial generative-music systems across four genres using 72 music information retrieval features. |
| [The Pluralistic Moral Gap: Understanding Moral Judgment and Value Differences between Humans and Large Language Models](https://aclanthology.org/2026.eacl-long.305/) | 2026 | Giuseppe Russo et al. | EACL | Compares human and LLM moral-judgment distributions to quantify the gap. |

### Design science

_Novel artifacts: algorithms, training methods, decoding strategies, frameworks, and dataset/benchmark-as-artifact contributions, each with evaluation._

| Title | Year | Authors | Venue | Main contribution |
|---|---|---|---|---|
| [Fine-tuning language models to find agreement among humans with diverse preferences](https://arxiv.org/abs/2211.15006) | 2022 | Michiel A. Bakker et al. | arXiv | Early method for finding agreement across diverse human preferences. |
| [Social Simulacra: Creating Populated Prototypes for Social Computing Systems](https://arxiv.org/abs/2208.04024v1) | 2022 | Joon Sung Park et al. | ACM | Populated prototypes that simulate community-level behavior distributions. |
| [Towards Pluralistic Value Alignment: Aggregating Value Systems through l_p-Regression](https://openaccess.city.ac.uk/id/eprint/31381/) | 2022 | Roger Lera-Leri et al. | AAMAS Workshop | Aggregates competing value systems via l_p-regression. |
| [Aligning Crowd Feedback via Distributional Preference Reward Modeling](https://arxiv.org/abs/2402.09764v3) | 2024 | Dexun Li et al. | arXiv | Distributional reward modeling for heterogeneous crowd feedback. |
| [Group Robust Preference Optimization in Reward-free RLHF](https://arxiv.org/abs/2405.20304v1) | 2024 | Shyam Sundhar Ramesh et al. | NeurIPS | Group-robust preference optimization without reward models. |
| [MallowsPO: Fine-Tune Your LLM with Preference Dispersions](https://arxiv.org/abs/2405.14953v5) | 2024 | Haoxian Chen et al. | arXiv | Preference optimization with Mallows-modeled preference dispersion. |
| [OASIS: Open Agent Social Interaction Simulations with One Million Agents](https://arxiv.org/abs/2411.11581v5) | 2024 | Ziyi Yang et al. | arXiv | Million-agent simulation testbed for studying emergent social distributions. |
| [PAL: Pluralistic Alignment Framework for Learning from Heterogeneous Preferences](https://arxiv.org/abs/2406.08469v1) | 2024 | Daiwei Chen et al. | arXiv | Framework for learning from heterogeneous preference data. |
| [Self-Alignment: Improving Alignment of Cultural Values in LLMs via In-Context Learning](https://arxiv.org/abs/2408.16482v2) | 2024 | Rochelle Choenni, Ekaterina Shutova | arXiv | In-context self-alignment of cultural value distributions. |
| [Self-Pluralising Culture Alignment for Large Language Models](https://arxiv.org/abs/2410.12971v1) | 2024 | Shaoyang Xu et al. | arXiv | Self-generates cultural perspectives to broaden alignment coverage. |
| [Imitation Beyond Expectation Using Pluralistic Stochastic Dominance](https://openreview.net/forum?id=YX5DHa9OfX) | 2025 | Ali Farajzadeh et al. | NeurIPS 2025 | Imitation learning under pluralistic stochastic dominance criteria. |
| [Improving the Distributional Alignment of LLMs using Supervision](https://arxiv.org/abs/2507.00439v4) | 2025 | Gauri Kambhatla et al. | arXiv | Supervised techniques to improve distributional alignment. |
| [Language Model Fine-Tuning on Scaled Survey Data for Predicting Distributions of Public Opinions](https://arxiv.org/abs/2502.16761v2) | 2025 | Joseph Suh et al. | arXiv | Fine-tunes on scaled survey data to predict public-opinion distributions. |
| [Pairwise Calibrated Rewards for Pluralistic Alignment](https://arxiv.org/abs/2506.06298v1) | 2025 | Daniel Halpern et al. | arXiv | Calibrated pairwise rewards that preserve preference heterogeneity. |
| [PluralLLM: Pluralistic Alignment in LLMs via Federated Learning](https://arxiv.org/abs/2503.09925v1) | 2025 | Mahmoud Srewa, Tianyu Zhao, Salma Elmalaki | ACM | Federated learning to keep pluralistic preference data decentralized. |
| [Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations](https://arxiv.org/abs/2502.07068v2) | 2025 | Yong Cao et al. | arXiv | Tunes LMs to reproduce global survey response distributions. |
| [Distributional Alignment for Social Simulation with LLMs: A Prompt Mixture Modeling Approach](https://openreview.net/forum?id=6KM1siLL8a) | 2026 | Yutong Xie, Ruoyi Gao, Qiaozhu Mei | KDD | Prompt-mixture modeling for distributional social simulation. |
| [MixDPO: Modeling Preference Strength for Pluralistic Alignment](https://arxiv.org/abs/2601.06180v1) | 2026 | Saki Imai et al. | arXiv | DPO variant modeling dispersion in preference strength. |
| [NepPlural: A Human-Anchored Benchmark for Persona Annotation in Nepali Migration Discourse](https://arxiv.org/abs/2610.15732) | 2026 | Jinu Nyachhyon, Anish Khatiwada, Bimal Timilsina | arXiv | **Benchmark** — Human-annotated benchmark of competing personas in Nepali migration discourse; tests whether models represent non-Western value diversity. |
| [Who Should We Listen to More? Welfare-Aware Preference Acquisition for Pluralistic Alignment](https://arxiv.org/abs/2610.19035) | 2026 | Ruomeng Ding et al. | arXiv | Defines a social-welfare objective for allocating human feedback across people when training for pluralistic alignment. |

## Cross-cutting (all modes)

_Frameworks, methods, and resources that span or combine the three modes._

### Empirical

_Measurement, audits, benchmarks used as instruments, human-subject and observational studies of existing models. No novel alignment artifact is proposed._

| Title | Year | Authors | Venue | Main contribution |
|---|---|---|---|---|
| [SafeWorld: Geo-Diverse Safety Alignment](https://arxiv.org/abs/2412.06483v1) | 2024 | Da Yin et al. | NeurIPS | **Benchmark** — Geo-diverse safety alignment benchmark. |
| [LIVS: A Pluralistic Alignment Dataset for Inclusive Public Spaces](https://arxiv.org/abs/2503.01894v2) | 2025 | Rashid Mushkani et al. | arXiv | **Dataset** — Pluralistic alignment dataset for inclusive public-space design. |
| [Navigating the Cultural Kaleidoscope: A Hitchhiker's Guide to Sensitivity in Large Language Models](https://arxiv.org/abs/2410.12880v3) | 2025 | Somnath Banerjee et al. | NAACL | **Benchmark** — Benchmark of LLM sensitivity across cultures. |
| [VITAL: A New Dataset for Benchmarking Pluralistic Alignment in Healthcare](https://arxiv.org/abs/2502.13775v2) | 2025 | Anudeex Shetty et al. | ACL | **Dataset** — Healthcare-domain benchmark for pluralistic alignment. |
| [Whose View of Safety? A Deep DIVE Dataset for Pluralistic Alignment of Text-to-Image Models](https://arxiv.org/abs/2507.13383v1) | 2025 | Charvi Rastogi et al. | arXiv | **Dataset** — Pluralistic safety judgments for text-to-image models. |
| [PluriHarms: Benchmarking the Full Spectrum of Human Judgments on AI Harm](https://arxiv.org/abs/2601.08951v2) | 2026 | Jing-Jing Li et al. | arXiv | **Benchmark** — Captures the full spectrum of human judgments about AI harm. |

### Design science

_Novel artifacts: algorithms, training methods, decoding strategies, frameworks, and dataset/benchmark-as-artifact contributions, each with evaluation._

| Title | Year | Authors | Venue | Main contribution |
|---|---|---|---|---|
| [Cultural Palette: Pluralising Culture Alignment via Multi-agent Palette](https://arxiv.org/abs/2412.11167v4) | 2024 | Jiahao Yuan et al. | arXiv | Multi-agent palette approach to pluralising cultural alignment. |
| [Group Robust Best-of-K Decoding of Language Models for Pluralistic Alignment](https://openreview.net/forum?id=JI6j4NUGHv) | 2024 | — | NeurIPS 2024 Pluralistic Alignment Workshop | Group-robust best-of-K decoding that protects minority preference groups. |
| [Modular Pluralism: Pluralistic Alignment via Multi-LLM Collaboration](https://arxiv.org/abs/2406.15951v2) | 2024 | Shangbin Feng et al. | EMNLP | Multi-LLM collaboration where specialized models jointly serve pluralism. |
| [Pluralistic Alignment for Healthcare: A Role-Driven Framework](https://arxiv.org/abs/2509.10685v2) | 2025 | Jiayou Zhong et al. | EMNLP | Role-driven pluralistic alignment framework for the healthcare domain. |
| [VISPA: Pluralistic Alignment via Automatic Value Selection and Activation](https://arxiv.org/abs/2601.12758v2) | 2026 | Shenyan Zheng et al. | arXiv | Automatically selects and activates relevant values at inference time. |

## Position papers & surveys

_Foundational framings and surveys of pluralistic (and adjacent) alignment._

| Title | Year | Authors | Venue | Main contribution |
|---|---|---|---|---|
| [AI Alignment: A Comprehensive Survey](https://arxiv.org/abs/2310.19852v6) | 2023 | Jiaming Ji et al. | arXiv | Comprehensive survey of AI alignment. |
| [Large Language Model Alignment: A Survey](https://arxiv.org/abs/2309.15025v1) | 2023 | Tianhao Shen et al. | arXiv | Broad survey of LLM alignment. |
| [A Roadmap to Pluralistic Alignment](https://arxiv.org/abs/2402.05070v3) | 2024 | Taylor Sorensen et al. | ICML | Foundational roadmap defining the Overton / steerable / distributional taxonomy. |
| [Personalization of Large Language Models: A Survey](https://arxiv.org/abs/2411.00027v3) | 2024 | Zhehao Zhang et al. | arXiv | Survey of LLM personalization (steerable pluralism adjacent). |
| [Survey of Cultural Awareness in Language Models: Text and Beyond](https://arxiv.org/abs/2411.00860v1) | 2024 | Siddhesh Pawar et al. | MIT Press | Survey of cultural awareness in language models. |
| [Towards Scalable Automated Alignment of LLMs: A Survey](https://arxiv.org/abs/2406.01252v3) | 2024 | Boxi Cao et al. | arXiv | Survey of scalable automated alignment approaches. |
| [What are human values, and how do we align AI to them?](https://arxiv.org/abs/2404.10636) | 2024 | Oliver Klingefjord, Ryan Lowe, Joe Edelman | arXiv | Philosophical grounding for what it means to align AI with human values. |
| [A Sociotechnical Perspective on Aligning AI with Pluralistic Human Values](https://openreview.net/forum?id=oSRqZO2O2O) | 2025 | Dalia Ali et al. | ICLR 2025 Workshop | Sociotechnical framing of pluralistic value alignment. |
| [A Survey on Personalized and Pluralistic Preference Alignment in Large Language Models](https://arxiv.org/abs/2504.07070v1) | 2025 | Zhouhang Xie et al. | arXiv | Survey of personalized and pluralistic preference alignment. |
| [Aligning Multimodal LLM with Human Preference: A Survey](https://arxiv.org/abs/2503.14504v2) | 2025 | Tao Yu et al. | arXiv | Survey of multimodal LLM preference alignment. |
| [Large Vision-Language Model Alignment and Misalignment: A Survey Through the Lens of Explainability](https://arxiv.org/abs/2501.01346v3) | 2025 | Dong Shu et al. | arXiv | Vision-language alignment survey through explainability. |
| [A Survey of Progress in LLM Alignment from the Perspective of Reward Design](https://doi.org/10.1109/tai.2026.3654921) | 2026 | Miaomiao Ji et al. | IEEE | Reward-design perspective on alignment progress. |
| [A pluralistic view on AI ethics: perspectives from Buen Vivir](https://doi.org/10.1007/s43681-026-01403-w) | 2026 | Dorine Eva van Norren | AI and Ethics | Argues for incorporating Global South cosmovisions, such as Buen Vivir, into AI ethics and regulation. |
| [Beyond the Monolithic Interface: A Research Agenda for Plural Conversational AI](https://arxiv.org/abs/2610.12878) | 2026 | Avijit Ghosh et al. | arXiv | Research agenda proposing multi-persona conversational AI interfaces as an alternative to the single-voice chatbot. |

## Maintenance

This list is kept current by an **autonomous updater agent on a bi-weekly cadence**:

- Queries the arXiv API for new pluralistic-alignment work (all modes, both methods).
- Diffs the upstream community list for additions worth porting.
- Hunts the journal track (IS / ethics / behavioral venues) via scholarly APIs.
- Classifies each candidate by mode × method, resolves canonical paper links and author lists, and rebuilds this README from `data/papers.yaml` (the source of truth).
- Commits changes to git; every run is logged under `agents/runs/`.

_Stats: 111 entries · 110 with resolved links · 109 with author lists · 13 seed classifications flagged for verification · last built 2026-10-25._

Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).
