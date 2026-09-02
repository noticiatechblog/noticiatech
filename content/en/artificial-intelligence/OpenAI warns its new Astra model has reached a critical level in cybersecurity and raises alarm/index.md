---
title: "OpenAI warns its new Astra model has reached a critical level in cybersecurity and raises alarm"
slug: "openai-astra-nivel-critico-ciberseguranca"
translationKey: "openai-astra-nivel-critico-ciberseguranca"
date: "2026-09-03T00:20:00-03:00"
draft: false
author: "By Aluisio Soares, founder of Notícia Tech"
description: "OpenAI says Astra has reached the critical level of cyber capability and discovered two zero-day vulnerabilities during internal evaluations, prompting the company to strengthen safeguards before launch."
categories:
  - "Artificial Intelligence"
cover:
  image: "capa.webp"
  alt: "OpenAI Astra facing cybersecurity alerts and digital vulnerabilities"
  caption: "Astra is the first OpenAI model classified by the company at the critical level of cyber capability."
faq:
  - pergunta: "What does Astra's critical cybersecurity level mean?"
    resposta_curta: "It means OpenAI considers the model capable of identifying unknown vulnerabilities and developing exploits against hardened systems without step-by-step human guidance."
    resposta_longa: "Under OpenAI's Preparedness Framework, the Critical level is reached when a model can identify and develop functional zero-day exploits in real, hardened critical systems without human intervention, or execute novel attack strategies against protected targets from a general objective."
  - pergunta: "Did Astra find zero-day vulnerabilities?"
    resposta_curta: "Yes. OpenAI says Astra discovered and used two zero-day vulnerabilities during an internal evaluation."
    resposta_longa: "During an internal benchmark involving 20 recently disclosed high-severity vulnerabilities, OpenAI reports that Astra discovered and used two zero-day vulnerabilities as part of an exploitation chain. The company says it is working to disclose them to the maintainers of the affected systems."
  - pergunta: "Is Astra already available to all users?"
    resposta_curta: "No. OpenAI plans a gradual rollout, with more restricted initial access to its advanced cybersecurity capabilities."
    resposta_longa: "OpenAI says it plans to make Astra available soon but will initially limit access to its advanced cybersecurity capabilities. Advanced security work will begin with a group of testers and later expand through Daybreak Blue."
  - pergunta: "Why did OpenAI strengthen Astra's safeguards?"
    resposta_curta: "Because greater cyber capability also increases the risk of misuse and unauthorized actions by the model itself."
    resposta_longa: "OpenAI says models with critical cyber capability require protection against two risk paths: malicious users attempting to exploit the system and the model itself carrying out unauthorized or misaligned actions. The company therefore expanded monitoring, access controls, isolation and containment mechanisms."

---

*Astra has moved from the possibility of critical cyber capability to a formal classification by OpenAI itself. The company says the model found previously unknown vulnerabilities, developed exploitation chains and even identified two zero-days during internal evaluations, raising the security requirements before its release.*

## OpenAI confirms Astra has reached a new capability level

**OpenAI** said that **Astra**, one of its upcoming models, has reached the **Critical cyber capability** level defined by the company's Preparedness Framework. It is the first OpenAI model to receive this classification.

The change matters because the critical level is not simply an improvement in programming or security testing. Under the framework's definition, it involves the ability to identify and develop functional exploits for previously unknown vulnerabilities in real, hardened systems without human intervention.

The key point is that Astra is not being presented simply as a more efficient model for coding tasks. The evaluation indicates a greater ability to turn security discoveries into **exploitation chains**, changing the balance between defensive utility and the risk of misuse.

### What changed compared with previous models

OpenAI itself says Astra represents a significant improvement over **GPT-5.6 Sol** in identifying vulnerabilities and developing exploits. The model also demonstrated greater token efficiency during evaluations.

This matters because capability and efficiency can combine in systems capable of performing more complex security tasks with less intervention. For the company, that progress made it necessary to raise the level of protection applied during development and before distribution.

## Astra found two zero-day vulnerabilities during evaluation

![Astra from OpenAI analyzing vulnerabilities in a cybersecurity environment](imagem-1.webp)

*Astra identified two zero-day vulnerabilities during an internal OpenAI evaluation.*

One of the most significant pieces of evidence presented by **OpenAI** came from an internal benchmark designed to reduce concerns about contamination of evaluation data. The set contains **20 high-severity vulnerabilities** that had been disclosed most recently.

During the test, Astra achieved higher rates of arbitrary code execution than GPT-5.6 Sol while using fewer tokens. More importantly, the company says the model discovered and used **two zero-day vulnerabilities** as part of an exploitation chain.

A zero-day is a vulnerability that is unknown or has not yet been fixed by the software maintainer. This type of flaw is particularly significant in cybersecurity because a patch may not be available when exploitation begins.

### The test went beyond known vulnerabilities

OpenAI also subjected Astra to expert-led evaluations against a hardened browser and operating system. In these evaluations, the model found vulnerabilities that had not previously been known and turned them into functional exploitation chains.

In one test, Astra built a chain capable of compromising a browser, escaping its sandbox and executing commands on the host system. In another, it combined flaws in a hardened operating system to create a privilege-escalation chain.

## Why the Critical classification is different

OpenAI's **Preparedness Framework** establishes the Critical level when a model can identify and develop functional zero-day exploits in many real, hardened critical systems without human intervention, or when it can create and execute novel attack strategies against protected targets starting from a general objective.

The classification therefore does not mean Astra is an "autonomous hacker" capable of breaking into any system. It describes a specific capability threshold observed in controlled evaluations under particular tools and access conditions.

This distinction matters because performance demonstrated in test environments should not be confused with unrestricted access to real-world systems. At the same time, the capability observed is sufficient for **OpenAI** to treat the model as a new category of risk within its own preparedness framework.

The development also highlights an important shift in the AI model race: as systems become better at operating tools and executing complex tasks, evaluating only the quality of their responses is no longer enough. Security, control and containment become part of the deployment architecture itself.

## OpenAI delays parts of development to strengthen protection

![Isolated development environment representing the new safeguards applied to Astra](imagem-2.webp)

*Astra's development has moved under stricter security controls as its capabilities have increased.*

**OpenAI** says it delayed parts of Astra's development and launch in recent weeks while strengthening and testing protections against misuse of cyber capabilities and unauthorized actions by the model.

The measures include more isolated testing environments, restrictions on network and tool access, stronger protection for model weights, additional monitoring and mechanisms capable of interrupting activities considered high risk.

The company is also treating two risk paths separately: abuse by malicious users and the possibility that the model itself could take actions that are misaligned or outside its authorized scope.

### The Hugging Face incident influenced the strategy

OpenAI says Astra was not involved in the incident involving **Hugging Face**, but the company incorporated lessons from that episode into the security measures for the new model.

This context helps explain why the launch is not being treated as a simple capability update. The company says it strengthened training to reject prohibited cyber requests, expanded monitoring mechanisms and added controls capable of interrupting certain activities.

The move reflects a broader concern across the industry. The Notícia Tech has already covered how **OpenAI, Anthropic and Microsoft** have warned about the growth of AI-powered attacks and the shrinking amount of time available for defense.

## The impact on businesses goes beyond fear of attacks

The arrival of a model with this profile creates a strategic issue for businesses that rely on software, cloud infrastructure and connected systems. The same capability used to find a vulnerability can, in principle, be directed toward defense when used in authorized environments.

The impact therefore should not be analyzed only through the risk of criminals using AI to accelerate attacks. There is also a race to identify flaws before they are exploited, automate security testing and reduce the time required to fix vulnerabilities.

This scenario makes **AI security** increasingly connected to corporate governance. Businesses adopting agents capable of taking actions inside internal systems need to consider not only what a model can answer, but also which tools it can access and which actions it can perform.

For organizations still building this layer, the discussion around **[why AI security is becoming a business priority](https://noticiatech.com.br/en/artificial-intelligence/what-is-ai-security-business-priority-coming-years/)** becomes more concrete as frontier models begin operating closer to this level of capability.

The development also fits into a broader industry movement around AI security, including efforts by major technology companies to coordinate defenses against increasingly capable AI-driven threats. The Notícia Tech has previously covered how **[NVIDIA brought together 37 technology companies around AI security](https://noticiatech.com.br/en/artificial-intelligence/nvidia-unites-37-tech-giants-openai-google-anthropic-stay-out-ai-security/)**.

## Astra will have a more controlled rollout

![Astra model represented within a controlled-access cybersecurity architecture](imagem-3.webp)

*Access to Astra's advanced cybersecurity capabilities will be expanded gradually by OpenAI.*

**OpenAI** says it plans to make Astra available soon, but does not intend to immediately release its most advanced cybersecurity capabilities broadly. Initial access will be given to a group of testers, followed by expansion through **Daybreak Blue** for defensive use cases.

This decision shows that the Critical classification does not necessarily mean the model will remain unavailable. The stated goal is to create mechanisms that allow legitimate security uses without providing the same level of capability for potentially abusive activities.

The company also says it plans to continue calibrating its safeguards to reduce disruption to legitimate tasks. This will be particularly important in security work, where overly aggressive restrictions could prevent authorized investigation and remediation activities.

### The next challenge will be controlling capability and access

The Astra case suggests that the AI security debate is entering a more operational phase. The challenge is no longer simply deciding whether a model is safe, but determining **how much power it should receive, in which environments and under what controls**.

This could influence how businesses evaluate AI models for programming, security and automation. A more capable system can deliver greater benefits, but it also requires controls proportional to the actions it can perform.

OpenAI itself says future models will require even stronger standards for alignment, monitoring and containment. For the market, the key question now is whether security mechanisms can evolve at the same pace as model capabilities.

Astra puts that question into concrete terms: the technology has reached a level that OpenAI itself classifies as critical for cybersecurity. The next competition will not be only about which company builds the most capable model, but **which one can put capabilities at this level into production while maintaining sufficient control over what the system can do**.

---