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

- **[The Unlocking Spell on Base LLMs: Rethinking Alignment via In-Context Learning](https://arxiv.org/abs/2312.01552v1)** — 2023. Shows base models can surface diverse value stances through in-context learning alone.
- **[Value Kaleidoscope: Engaging AI with Pluralistic Human Values, Rights, and Duties](https://arxiv.org/abs/2309.00779v2)** — 2023, `dataset`. Benchmark spanning pluralistic values, rights, and duties.
- **[From Distributional to Overton Pluralism: Investigating Large Language Model Alignment](https://arxiv.org/abs/2406.17692v2)** — 2024. Investigates how alignment shifts models between distributional and Overton-style pluralism.
- **[Benchmarking Overton Pluralism in LLMs](https://arxiv.org/abs/2512.01351v2)** — 2025, `benchmark`. Dedicated benchmark for Overton-style pluralism.
- **[Authority locking vs. pluralistic sourcing in generative search: evidence compression beyond top-spot displacement](https://doi.org/10.1007/s10660-026-10209-1)** — Electronic Commerce Research, 2026, journal track. Studies whether generative-search citations mirror organic rankings or reflect a distinct, pluralistic source-selection logic.

### Design science

_Novel artifacts: algorithms, training methods, decoding strategies, frameworks, and dataset/benchmark-as-artifact contributions, each with evaluation._

- **[Black-Box Prompt Optimization: Aligning Large Language Models without Model Training](https://arxiv.org/abs/2311.04155v3)** — 2023. Aligns models to plural objectives by optimizing prompts, no training required.
- **[Generative Social Choice](https://arxiv.org/abs/2309.01291)** — 2023. Social-choice-theoretic framework for aggregating plural preferences in generative AI.
- **[Large Language Models as Optimizers](https://arxiv.org/abs/2309.03409v3)** — 2023. Optimization-style prompting that aggregates diverse candidate solutions.
- **[MaxMin-RLHF: Alignment with Diverse Human Preferences](https://arxiv.org/abs/2402.08925v2)** — 2024. Rawlsian max-min RLHF objective that protects worst-off preference groups.
- **[Policy Prototyping for LLMs: Pluralistic Alignment via Interactive and Collaborative Policymaking](https://arxiv.org/abs/2409.08622v2)** — 2024. Interactive, collaborative policymaking process for specifying pluralistic model behavior.
- **[ReConcile: Round-Table Conference Improves Reasoning via Consensus among Diverse LLMs](https://arxiv.org/abs/2309.13007v3)** — ICLR, 2024. Multi-LLM round-table consensus that preserves diverse model views while improving reasoning.
- **[PICACO: Pluralistic In-Context Value Alignment of LLMs via Total Correlation Optimization](https://arxiv.org/abs/2507.16679v4)** — 2025. In-context value alignment via total correlation optimization across plural values.
- **[Reflective Verbal Reward Design for Pluralistic Alignment](https://arxiv.org/abs/2506.17834v1)** — 2025. Uses verbal self-reflection to design rewards covering plural values.

## Steerable Pluralism

_The model adapts its behavior to a specified principal's values, persona, or preferences on demand._

### Empirical

_Measurement, audits, benchmarks used as instruments, human-subject and observational studies of existing models. No novel alignment artifact is proposed._

- **[Evaluating and Inducing Personality in Pre-trained Language Models](https://arxiv.org/abs/2206.07550v3)** — NeurIPS. Tests whether stable personality traits can be induced in pretrained LMs.
- **[Cultural Alignment in Large Language Models: An Explanatory Analysis Based on Hofstede's Cultural Dimensions](https://arxiv.org/abs/2309.12342v2)** — 2023. Explains LLM cultural alignment through Hofstede's cultural dimensions.
- **[From Values to Opinions: Predicting Human Behaviors and Stances Using Value-Injected Large Language Models](https://arxiv.org/abs/2310.17857v1)** — 2023. Evaluates whether value-injected LMs predict human stances and behaviors.
- **[Not All Countries Celebrate Thanksgiving: On the Cultural Dominance in Large Language Models](https://arxiv.org/abs/2310.12481v2)** — 2023. Documents US-centric cultural dominance in LLM outputs.
- **[Value Kaleidoscope: Engaging AI with Pluralistic Human Values, Rights, and Duties](https://arxiv.org/abs/2309.00779v2)** — 2023, `dataset`. Benchmark spanning pluralistic values, rights, and duties.
- **[Are the Values of LLMs Structurally Aligned with Humans? A Causal Perspective](https://arxiv.org/abs/2501.00581v2)** — 2024. Causal analysis of structural alignment between LLM and human values.
- **[CULTURE-GEN: Revealing Global Cultural Perception in Language Models through Natural Language Prompting](https://arxiv.org/abs/2404.10199v5)** — 2024. Probes global cultural perception in LMs via natural-language prompting.
- **[Can Language Models Reason about Individualistic Human Values and Preferences?](https://arxiv.org/abs/2410.03868v2)** — 2024, `benchmark`. Tests LLM reasoning about individualistic values and preferences.
- **[ComPO: Community Preferences for Language Model Personalization](https://arxiv.org/abs/2410.16027v1)** — 2024, `dataset`. Community preference data for LM personalization.
- **[DailyDilemmas: Revealing Value Preferences of LLMs with Quandaries of Daily Life](https://arxiv.org/abs/2410.02683v3)** — 2024, `benchmark`. Daily-life quandaries that reveal LLM value preferences.
- **[Evaluating Cultural Adaptability of a Large Language Model via Simulation of Synthetic Personas](https://arxiv.org/abs/2408.06929v1)** — 2024. Simulates synthetic personas to test LLM cultural adaptability.
- **[NormAd: A Framework for Measuring the Cultural Adaptability of Large Language Models](https://arxiv.org/abs/2404.12464v10)** — 2024, `benchmark`. Framework measuring how well LLMs adapt to cultural norms.
- **[Value FULCRA: Mapping Large Language Models to the Multidimensional Spectrum of Basic Human Value](https://aclanthology.org/2024.naacl-long.486/)** — NAACL, 2024, `benchmark`. Maps LLMs onto the multidimensional spectrum of basic human values.
- **[ValueBench: Towards Comprehensively Evaluating Value Orientations and Understanding of Large Language Models](https://arxiv.org/abs/2406.04214v1)** — 2024, `benchmark`. Comprehensive evaluation of LLM value orientations.
- **[EVALUESTEER: Measuring Reward Model Steerability Towards Values and Preferences](https://arxiv.org/abs/2510.06370v2)** — 2025, `benchmark`. Measures how steerable reward models are toward values and preferences.
- **[Exploring Chain-of-Thought Reasoning for Steerable Pluralistic Alignment](https://arxiv.org/abs/2510.04045v1)** — 2025. Studies chain-of-thought as a lever for steerable pluralism.

### Design science

_Novel artifacts: algorithms, training methods, decoding strategies, frameworks, and dataset/benchmark-as-artifact contributions, each with evaluation._

- **[Aligning Machiavellian Agents: Behavior Steering via Test-Time Policy Shaping](https://arxiv.org/abs/2511.11551v3)** — AAAI. Test-time policy shaping to steer agentic behavior.
- **[Aligning to Thousands of Preferences via System Message Generalization](https://arxiv.org/abs/2405.17977v2)** — NeurIPS. Generalizes system messages to serve thousands of distinct preferences.
- **[CultureLLM: Incorporating Cultural Differences into Large Language Models](https://arxiv.org/abs/2402.10946v3)** — NeurIPS. Culture-specific tuning to incorporate cultural differences.
- **[CulturePark: Boosting Cross-cultural Understanding in Large Language Models](https://arxiv.org/abs/2405.15145v3)** — NeurIPS. Multi-agent cross-cultural dialogue to boost cultural understanding.
- **[HelpSteer 2: Open-source dataset for training top-performing reward models](https://doi.org/10.52202/079017-0047)** — NeurIPS, `dataset`. Large-scale open preference dataset for reward-model training (artifact).
- **Steerable Alignment with Conditional Multiobjective Preference Optimization**. Conditional multi-objective preference optimization for steerability. *(link pending)*
- **[Arithmetic Control of LLMs for Diverse User Preferences: Directional Preference Alignment with Multi-Objective Rewards](https://arxiv.org/abs/2402.18571v3)** — 2024. Multi-objective reward arithmetic for serving diverse user preferences.
- **[Controllable Preference Optimization: Toward Controllable Multi-Objective Alignment](https://arxiv.org/abs/2402.19085v3)** — 2024. Preference optimization with explicit controllability over objectives.
- **[CultureBank: An Online Community-Driven Knowledge Base Towards Culturally Aware Language Technologies](https://arxiv.org/abs/2404.15238v1)** — 2024, `dataset`. Community-driven cultural knowledge base as an alignment resource.
- **[Few-shot Steerable Alignment: Adapting Rewards and LLM Policies with Neural Processes](https://arxiv.org/abs/2412.13998v1)** — 2024. Neural processes adapt rewards and policies to new principals few-shot.
- **[Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts](https://arxiv.org/abs/2406.12845v1)** — 2024. Mixture-of-experts reward models for interpretable plural preferences.
- **[Language Models are Alignable Decision-Makers: Dataset and Application to the Medical Triage Domain](https://arxiv.org/abs/2406.06435v1)** — 2024, `dataset`. Dataset and demo of steerable alignment for medical triage decisions.
- **[Personality Alignment of Large Language Models](https://arxiv.org/abs/2408.11779v2)** — 2024. Trains personality-conditioned alignment into LLMs.
- **[SPICA: Retrieving Scenarios for Pluralistic In-Context Alignment](https://arxiv.org/abs/2411.10912v2)** — 2024. Retrieval of scenarios to ground pluralistic in-context alignment.
- **[Self-Pluralising Culture Alignment for Large Language Models](https://arxiv.org/abs/2410.12971v1)** — 2024. Self-generates cultural perspectives to broaden alignment coverage.
- **[SteerLM: Attribute Conditioned SFT as an (User-Steerable) Alternative to RLHF](https://arxiv.org/abs/2310.05344v1)** — 2024. Attribute-conditioned SFT as a steerable alternative to RLHF.
- **[Value Alignment from Unstructured Text](https://arxiv.org/abs/2408.10392v1)** — 2024. Extracts alignment signal for steerable values from unstructured text.
- **[Counterfactual Reasoning for Steerable Pluralistic Value Alignment of Large Language Models](https://arxiv.org/abs/2510.18526v2)** — 2025. Counterfactual reasoning as a mechanism for steerable value alignment.
- **[LoRe: Personalizing LLMs via Low-Rank Reward Modeling](https://arxiv.org/abs/2504.14439v1)** — 2025. Low-rank reward modeling for efficient LLM personalization.
- **[PERSONA: A Reproducible Testbed for Pluralistic Alignment](https://arxiv.org/abs/2407.17387v1)** — COLING, 2025, `dataset`. Reproducible testbed with synthetic personas for pluralistic alignment research.
- **[Reflective Verbal Reward Design for Pluralistic Alignment](https://arxiv.org/abs/2506.17834v1)** — 2025. Uses verbal self-reflection to design rewards covering plural values.
- **[Robust Multi-Objective Controlled Decoding of Large Language Models](https://arxiv.org/abs/2503.08796v2)** — 2025. Decoding-time multi-objective control robust to preference shifts.
- **[Steerable Pluralism: Pluralistic Alignment via Few-Shot Comparative Regression](https://arxiv.org/abs/2508.08509v1)** — 2025. Few-shot comparative regression to steer pluralistic value expression.

## Distributional Pluralism

_The model's outputs across a population match the distribution of human views instead of collapsing to a single answer._

### Empirical

_Measurement, audits, benchmarks used as instruments, human-subject and observational studies of existing models. No novel alignment artifact is proposed._

- **[CIVICS: Building a Dataset for Examining Culturally-Informed Values in Large Language Models](https://arxiv.org/abs/2405.13974v1)** — AAAI, `dataset`. Dataset for culturally-informed values in LLMs.
- **[Evaluating and Inducing Personality in Pre-trained Language Models](https://arxiv.org/abs/2206.07550v3)** — NeurIPS. Tests whether stable personality traits can be induced in pretrained LMs.
- **[MID-Space: Aligning Diverse Communities' Needs to Inclusive Public Spaces](https://openreview.net/forum?id=kyfkMRT4Ao)** — `dataset`. Aligns diverse community needs for inclusive public spaces.
- **[The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models](https://arxiv.org/abs/2404.16019v2)** — NeurIPS, `dataset`. Participatory, representative human-feedback dataset on subjective alignment.
- **[The Moral Integrity Corpus: A Benchmark for Ethical Dialogue Systems](https://arxiv.org/abs/2204.03021v1)** — 2020, `dataset`. Benchmark corpus for ethical dialogue systems.
- **[Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts](https://arxiv.org/abs/2305.13300v4)** — 2023, `benchmark`. Reveals LLM behavior under knowledge conflicts.
- **[NormBank: A Knowledge Bank of Situational Social Norms](https://arxiv.org/abs/2305.17008v2)** — 2023, `dataset`. Knowledge bank of situational social norms.
- **[Towards Measuring the Representation of Subjective Global Opinions in Language Models](https://arxiv.org/abs/2306.16388v2)** — 2023, `benchmark`. Measures representation of subjective global opinions in LMs.
- **[Whose Opinions Do Language Models Reflect?](https://arxiv.org/abs/2303.17548v1)** — 2023, `benchmark`. Compares LLM opinions against demographic-group opinion distributions.
- **[Benchmarking Distributional Alignment of Large Language Models](https://arxiv.org/abs/2411.05403v1)** — 2024, `benchmark`. Benchmark for distributional alignment of LLMs.
- **[KorNAT: LLM Alignment Benchmark for Korean Social Values and Common Knowledge](https://arxiv.org/abs/2402.13605v7)** — 2024, `benchmark`. Korean social-values alignment benchmark (non-English coverage).
- **[Language Model Alignment in Multilingual Trolley Problems](https://arxiv.org/abs/2407.02273v6)** — 2024, `benchmark`. Multilingual moral-dilemma benchmark for alignment evaluation.
- **[Measuring Perceived Slant in Large Language Models Through User Evaluations](https://www.gsb.stanford.edu/faculty-research/working-papers/measuring-perceived-slant-large-language-models-through-user)** — 2025, `benchmark`. User evaluations of perceived political slant in LLMs.
- **[NoveltyBench: Evaluating Language Models for Humanlike Diversity](https://arxiv.org/abs/2504.05228v4)** — 2025, `benchmark`. Evaluates humanlike output diversity; directly relevant to alignment-induced homogenization.
- **[Algorithmic canonization: AI and art history through an Asian lens](https://link.springer.com/article/10.1007/s00146-026-03361-7)** — AI & SOCIETY, 2026, journal track. Systematic review of the AI-and-art-history literature; introduces 'algorithmic canonization' to describe how AI systems standardize what is remembered.
- **[Generative AI and the homogenization of analyst forecasts](https://doi.org/10.1016/j.frl.2026.110767)** — Finance Research Letters, 2026, journal track. Empirical study of generative AI's effect on the diversity of analyst forecasts.
- **[The Algorithmic Flattening of Sound: Computational Evidence and Justice Implications of AI Music Homogenization](https://doi.org/10.1609/aies.v9i4.43312)** — AIES, 2026. Audits homogenization in two commercial generative-music systems across four genres using 72 music information retrieval features.
- **[The Pluralistic Moral Gap: Understanding Moral Judgment and Value Differences between Humans and Large Language Models](https://aclanthology.org/2026.eacl-long.305/)** — EACL, 2026. Compares human and LLM moral-judgment distributions to quantify the gap.

### Design science

_Novel artifacts: algorithms, training methods, decoding strategies, frameworks, and dataset/benchmark-as-artifact contributions, each with evaluation._

- **[Distributional Alignment for Social Simulation with LLMs: A Prompt Mixture Modeling Approach](https://openreview.net/forum?id=6KM1siLL8a)**. Prompt-mixture modeling for distributional social simulation.
- **[Group Robust Preference Optimization in Reward-free RLHF](https://arxiv.org/abs/2405.20304v1)** — NeurIPS. Group-robust preference optimization without reward models.
- **[Imitation Beyond Expectation Using Pluralistic Stochastic Dominance](https://openreview.net/forum?id=YX5DHa9OfX)**. Imitation learning under pluralistic stochastic dominance criteria.
- **[PluralLLM: Pluralistic Alignment in LLMs via Federated Learning](https://arxiv.org/abs/2503.09925v1)** — ACM. Federated learning to keep pluralistic preference data decentralized.
- **[Fine-tuning language models to find agreement among humans with diverse preferences](https://arxiv.org/abs/2211.15006)** — 2022. Early method for finding agreement across diverse human preferences.
- **[Social Simulacra: Creating Populated Prototypes for Social Computing Systems](https://arxiv.org/abs/2208.04024v1)** — ACM, 2022. Populated prototypes that simulate community-level behavior distributions.
- **[Towards Pluralistic Value Alignment: Aggregating Value Systems through l_p-Regression](https://openaccess.city.ac.uk/id/eprint/31381/)** — AAMAS Workshop, 2022. Aggregates competing value systems via l_p-regression.
- **[Aligning Crowd Feedback via Distributional Preference Reward Modeling](https://arxiv.org/abs/2402.09764v3)** — 2024. Distributional reward modeling for heterogeneous crowd feedback.
- **[MallowsPO: Fine-Tune Your LLM with Preference Dispersions](https://arxiv.org/abs/2405.14953v5)** — 2024. Preference optimization with Mallows-modeled preference dispersion.
- **[OASIS: Open Agent Social Interaction Simulations with One Million Agents](https://arxiv.org/abs/2411.11581v5)** — 2024. Million-agent simulation testbed for studying emergent social distributions.
- **[PAL: Pluralistic Alignment Framework for Learning from Heterogeneous Preferences](https://arxiv.org/abs/2406.08469v1)** — 2024. Framework for learning from heterogeneous preference data.
- **[Self-Alignment: Improving Alignment of Cultural Values in LLMs via In-Context Learning](https://arxiv.org/abs/2408.16482v2)** — 2024. In-context self-alignment of cultural value distributions.
- **[Self-Pluralising Culture Alignment for Large Language Models](https://arxiv.org/abs/2410.12971v1)** — 2024. Self-generates cultural perspectives to broaden alignment coverage.
- **[Improving the Distributional Alignment of LLMs using Supervision](https://arxiv.org/abs/2507.00439v4)** — 2025. Supervised techniques to improve distributional alignment.
- **[Language Model Fine-Tuning on Scaled Survey Data for Predicting Distributions of Public Opinions](https://arxiv.org/abs/2502.16761v2)** — 2025. Fine-tunes on scaled survey data to predict public-opinion distributions.
- **[Pairwise Calibrated Rewards for Pluralistic Alignment](https://arxiv.org/abs/2506.06298v1)** — 2025. Calibrated pairwise rewards that preserve preference heterogeneity.
- **[Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations](https://arxiv.org/abs/2502.07068v2)** — 2025. Tunes LMs to reproduce global survey response distributions.
- **[MixDPO: Modeling Preference Strength for Pluralistic Alignment](https://arxiv.org/abs/2601.06180v1)** — 2026. DPO variant modeling dispersion in preference strength.
- **[NepPlural: A Human-Anchored Benchmark for Persona Annotation in Nepali Migration Discourse](https://arxiv.org/abs/2610.15732)** — 2026, `benchmark`. Human-annotated benchmark of competing personas in Nepali migration discourse; tests whether models represent non-Western value diversity.
- **[Who Should We Listen to More? Welfare-Aware Preference Acquisition for Pluralistic Alignment](https://arxiv.org/abs/2610.19035)** — 2026. Defines a social-welfare objective for allocating human feedback across people when training for pluralistic alignment.

## Cross-cutting (all modes)

_Frameworks, methods, and resources that span or combine the three modes._

### Empirical

_Measurement, audits, benchmarks used as instruments, human-subject and observational studies of existing models. No novel alignment artifact is proposed._

- **[SafeWorld: Geo-Diverse Safety Alignment](https://arxiv.org/abs/2412.06483v1)** — NeurIPS, `benchmark`. Geo-diverse safety alignment benchmark.
- **[LIVS: A Pluralistic Alignment Dataset for Inclusive Public Spaces](https://arxiv.org/abs/2503.01894v2)** — 2025, `dataset`. Pluralistic alignment dataset for inclusive public-space design.
- **[Navigating the Cultural Kaleidoscope: A Hitchhiker's Guide to Sensitivity in Large Language Models](https://arxiv.org/abs/2410.12880v3)** — NAACL, 2025, `benchmark`. Benchmark of LLM sensitivity across cultures.
- **[VITAL: A New Dataset for Benchmarking Pluralistic Alignment in Healthcare](https://arxiv.org/abs/2502.13775v2)** — ACL, 2025, `dataset`. Healthcare-domain benchmark for pluralistic alignment.
- **[Whose View of Safety? A Deep DIVE Dataset for Pluralistic Alignment of Text-to-Image Models](https://arxiv.org/abs/2507.13383v1)** — 2025, `dataset`. Pluralistic safety judgments for text-to-image models.
- **[PluriHarms: Benchmarking the Full Spectrum of Human Judgments on AI Harm](https://arxiv.org/abs/2601.08951v2)** — 2026, `benchmark`. Captures the full spectrum of human judgments about AI harm.

### Design science

_Novel artifacts: algorithms, training methods, decoding strategies, frameworks, and dataset/benchmark-as-artifact contributions, each with evaluation._

- **[Group Robust Best-of-K Decoding of Language Models for Pluralistic Alignment](https://openreview.net/forum?id=JI6j4NUGHv)**. Group-robust best-of-K decoding that protects minority preference groups.
- **[Cultural Palette: Pluralising Culture Alignment via Multi-agent Palette](https://arxiv.org/abs/2412.11167v4)** — 2024. Multi-agent palette approach to pluralising cultural alignment.
- **[Modular Pluralism: Pluralistic Alignment via Multi-LLM Collaboration](https://arxiv.org/abs/2406.15951v2)** — EMNLP, 2024. Multi-LLM collaboration where specialized models jointly serve pluralism.
- **[Pluralistic Alignment for Healthcare: A Role-Driven Framework](https://arxiv.org/abs/2509.10685v2)** — EMNLP, 2025. Role-driven pluralistic alignment framework for the healthcare domain.
- **[VISPA: Pluralistic Alignment via Automatic Value Selection and Activation](https://arxiv.org/abs/2601.12758v2)** — 2026. Automatically selects and activates relevant values at inference time.

## Position papers & surveys

_Foundational framings and surveys of pluralistic (and adjacent) alignment._

- **[A Sociotechnical Perspective on Aligning AI with Pluralistic Human Values](https://openreview.net/forum?id=oSRqZO2O2O)**. Sociotechnical framing of pluralistic value alignment.
- **[A Survey of Progress in LLM Alignment from the Perspective of Reward Design](https://doi.org/10.1109/tai.2026.3654921)** — IEEE. Reward-design perspective on alignment progress.
- **[Survey of Cultural Awareness in Language Models: Text and Beyond](https://arxiv.org/abs/2411.00860v1)** — MIT Press. Survey of cultural awareness in language models.
- **[AI Alignment: A Comprehensive Survey](https://arxiv.org/abs/2310.19852v6)** — 2023. Comprehensive survey of AI alignment.
- **[Large Language Model Alignment: A Survey](https://arxiv.org/abs/2309.15025v1)** — 2023. Broad survey of LLM alignment.
- **[A Roadmap to Pluralistic Alignment](https://arxiv.org/abs/2402.05070v3)** — ICML, 2024. Foundational roadmap defining the Overton / steerable / distributional taxonomy.
- **[Personalization of Large Language Models: A Survey](https://arxiv.org/abs/2411.00027v3)** — 2024. Survey of LLM personalization (steerable pluralism adjacent).
- **[Towards Scalable Automated Alignment of LLMs: A Survey](https://arxiv.org/abs/2406.01252v3)** — 2024. Survey of scalable automated alignment approaches.
- **[What are human values, and how do we align AI to them?](https://arxiv.org/abs/2404.10636)** — 2024. Philosophical grounding for what it means to align AI with human values.
- **[A Survey on Personalized and Pluralistic Preference Alignment in Large Language Models](https://arxiv.org/abs/2504.07070v1)** — 2025. Survey of personalized and pluralistic preference alignment.
- **[Aligning Multimodal LLM with Human Preference: A Survey](https://arxiv.org/abs/2503.14504v2)** — 2025. Survey of multimodal LLM preference alignment.
- **[Large Vision-Language Model Alignment and Misalignment: A Survey Through the Lens of Explainability](https://arxiv.org/abs/2501.01346v3)** — 2025. Vision-language alignment survey through explainability.
- **[A pluralistic view on AI ethics: perspectives from Buen Vivir](https://doi.org/10.1007/s43681-026-01403-w)** — AI and Ethics, 2026, journal track. Argues for incorporating Global South cosmovisions, such as Buen Vivir, into AI ethics and regulation.
- **[Beyond the Monolithic Interface: A Research Agenda for Plural Conversational AI](https://arxiv.org/abs/2610.12878)** — 2026. Research agenda proposing multi-persona conversational AI interfaces as an alternative to the single-voice chatbot.

## Maintenance

This list is kept current by an **autonomous updater agent on a bi-weekly cadence**:

- Queries the arXiv API for new pluralistic-alignment work (all modes, both methods).
- Diffs the upstream community list for additions worth porting.
- Hunts the journal track (IS / ethics / behavioral venues) via scholarly APIs.
- Classifies each candidate by mode × method, resolves canonical paper links, and rebuilds this README from `data/papers.yaml` (the source of truth).
- Commits changes to git; every run is logged under `agents/runs/`.

_Stats: 111 entries · 110 with resolved links · 13 seed classifications flagged for verification · last built 2026-10-15._

Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).
