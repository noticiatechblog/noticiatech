---
title: "Researchers Reveal What ChatGPT, Claude and Gemini Were Hiding"
slug: "researchers-reveal-hidden-reasoning-chatgpt-claude-gemini"
translationKey: "pesquisadores-revelam-raciocinio-oculto-chatgpt-claude-gemini"
date: "2026-08-13T00:30:00-03:00"
draft: false
author: "By Aluisio Soares, founder of Notícia Tech"
description: "Researchers found a flaw that exposed hidden reasoning from ChatGPT, Claude and Gemini, along with sensitive data. Here's what the risk means."
categories:
  - "Artificial Intelligence"

cover:
  image: "capa.webp"
  alt: "Representation of ChatGPT, Claude and Gemini with exposed hidden reasoning layers"
  caption: "A study uncovered a vulnerability in how major AI models protect reasoning traces when accessed through APIs."

faq:
  - pergunta: "What did researchers discover about ChatGPT, Claude and Gemini?"
    resposta_curta: "They found a way to recover parts of the hidden reasoning sent through the APIs of major AI models."
    resposta_longa: "The research identified an architectural vulnerability in APIs serving models from OpenAI, Anthropic and Google. The researchers demonstrated that encrypted reasoning blocks could be reused under certain conditions to recover their contents in readable form."

  - pergunta: "Was the hidden reasoning of AI models actually exposed?"
    resposta_curta: "Parts of the reasoning traces could be recovered."
    resposta_longa: "The study demonstrated the recovery of reasoning blocks from tested models. This does not mean the researchers gained access to the companies' servers or encryption keys, nor does it mean that all internal processing performed by a model was exposed."

  - pergunta: "Are ChatGPT, Claude and Gemini still vulnerable?"
    resposta_curta: "The companies were notified and took mitigation measures."
    resposta_longa: "The research was disclosed through a responsible disclosure process. The companies involved implemented or began implementing measures to reduce the behaviors exploited in the study, although the researchers indicate that some architectural risks still deserve attention."

  - pergunta: "Could the flaw recover personal data and credentials?"
    resposta_curta: "The researchers found personal data and credentials in the analyzed traces."
    resposta_longa: "After analyzing 315,320 reasoning blocks obtained from public logs, the researchers identified 367 artifacts containing personally identifiable information and 182 credentials. The study shows that sensitive information can end up inside blocks that developers may assume are protected."

  - pergunta: "Why do AI companies hide model reasoning?"
    resposta_curta: "To protect intellectual property and reduce the risk of exposing sensitive information."
    resposta_longa: "Major AI providers avoid fully exposing chain-of-thought to protect proprietary information, make it harder to reproduce model capabilities, and reduce the exposure of data that may appear during processing."

  - pergunta: "What changes for companies using AI APIs?"
    resposta_curta: "Logs and intermediate data need to be treated as sensitive information."
    resposta_longa: "Companies using AI APIs need to consider not only prompts and final responses, but also intermediate data, reasoning traces, logs and credentials processed during interactions. This increases the importance of access controls, secure storage and AI governance policies."

  - pergunta: "What is an LLM?"
    resposta_curta: "It is a large-scale language model used to understand and generate text."
    resposta_longa: "LLM stands for Large Language Model. These models are trained on large amounts of data to recognize language patterns and generate responses, code, analysis and other content. ChatGPT, Claude and Gemini use models in this category."

  - pergunta: "What is an AI API?"
    resposta_curta: "It is an interface that allows software applications to integrate AI models."
    resposta_longa: "An API allows applications to send requests to an artificial intelligence model and receive responses automatically. Companies use APIs to integrate AI capabilities into internal systems, applications, agents and business processes."
---

*New security research has uncovered an unexpected weakness in a layer that major AI companies have worked to keep protected: the reasoning traces produced by advanced models. The study involves OpenAI, Anthropic and Google and shows why AI security does not end with the answer displayed on a screen.*

## Researchers found a way to recover hidden reasoning from major AI models

Researchers have discovered a vulnerability that made it possible to recover parts of the hidden reasoning produced by artificial intelligence models accessed through APIs. The study examined systems associated with OpenAI, Anthropic and Google and showed that certain protected blocks could be reused in ways the security mechanisms were not designed to allow.

The term **chain-of-thought**, or reasoning process, refers to intermediate steps a model may use to solve certain tasks. In advanced models, this information may be kept out of the response shown to users because it can contain technical value, proprietary information or data that should not be exposed.

The vulnerability identified by the researchers does not mean that someone broke into OpenAI, Anthropic or Google's servers. The discovery involved the way information moves between models and applications through their APIs.

### What is hidden AI reasoning?

An **LLM**, short for Large Language Model, is an AI system trained on large amounts of data to understand instructions and generate responses. Modern models can perform intermediate steps to solve complex problems before delivering a final result.

Those steps can involve analysis, planning, verification and breaking a task into smaller parts. Users, however, typically receive only the final answer or a controlled summary of that process.

The researchers' study shows that this separation between what a model processes and what a user can see can create an additional security surface.

### Why do AI companies hide this data?

Protecting reasoning traces has a strategic dimension. A model's internal process can reveal information that could help competitors study, reproduce or train other systems based on the behavior of a proprietary model.

There is also a privacy concern. A model can process information supplied by users or applications that never appears directly in the final response.

That is why OpenAI, Anthropic and Google have implemented mechanisms designed to keep certain reasoning traces protected. The research shows that hiding this information from the user interface is not enough if the underlying data can still move through other parts of the architecture.

## The vulnerability was tied to how reasoning traces were sent through APIs

The discovery began when researchers identified an unusual characteristic in encrypted reasoning blocks used by different models within the providers' ecosystems.

![Representation of encrypted reasoning blocks being processed by different AI models](imagem-1.webp)

*Protected reasoning blocks can move between applications during interactions with AI APIs.*

An **AI API** is an interface that allows software to communicate with an AI model automatically. Instead of a person opening a chatbot, a company can send a request directly from its own system to a model and receive a response programmatically.

According to the research, certain encrypted blocks returned by the APIs could be reused across sessions, users and models within the same provider ecosystem. That compatibility created an opportunity the researchers were able to exploit.

### A weaker model could help reveal data from a more powerful model

The mechanism demonstrated by the researchers is particularly significant because it did not require directly attacking the most advanced model.

Under certain conditions, a reasoning block produced by a more capable model could be provided to another, less protected model within the same ecosystem.

That second model could then be prompted to transform the protected content into readable text.

In practice, the architecture created an indirect path. Instead of trying to persuade the more powerful model to reveal its own reasoning, the researchers exploited compatibility between different models from the same provider.

### The problem was not simply breaking encryption

This distinction is critical to understanding the story.

The researchers did not claim to have broken the encryption used by the providers or obtained their private cryptographic keys. The problem was related to how protected blocks could be reused and interpreted within the model ecosystem.

The study describes this as an architectural vulnerability. The risk emerged from interactions between components that could appear secure when considered individually.

This type of issue is particularly relevant to enterprise AI because modern systems rarely operate as a single isolated model. They combine APIs, different models, agents, tools, databases and internal systems.

## The impact became more serious when researchers examined real-world data

The second finding raised the stakes: the reasoning traces contained more than information about how models reached their conclusions.

When analyzing **315,320 reasoning blocks** obtained from public logs, the researchers found **367 artifacts containing personally identifiable information** and **182 credentials**.

That means information that appeared protected or invisible to someone examining a session could still exist in intermediate layers of the data.

### AI logs can contain information users never see

Logs are records generated by software to track operations, errors, requests and responses. In development environments, teams often share logs publicly to demonstrate projects, investigate problems or facilitate collaboration.

The problem is that an AI session can contain far more information than what appears on the screen.

A user may see a harmless question and answer while the underlying system records intermediate data used during processing.

The research shows why this difference needs to be considered when securing AI-powered applications.

### The warning for businesses is bigger than it first appears

For businesses, the issue is not limited to the possibility of someone observing how a model reached an answer.

If credentials, personally identifiable information or other sensitive data appear in reasoning traces or logs, the exposure can create operational and regulatory consequences.

This reinforces a concern that Notícia Tech has already explored when explaining **[why AI security has become a priority for businesses](https://noticiatech.com.br/en/artificial-intelligence/what-is-ai-security-business-priority-coming-years/)**.

The difference now is that this research provides a concrete example of how an intermediate layer of an AI architecture can become an exposure vector.

## The vulnerability exposes a new challenge for AI security

The discovery matters because protecting only a model's final response is no longer enough.

In enterprise systems, artificial intelligence often works as a chain of components. An application sends a request to an API, the model processes the information, other models may participate in the task, and the results can be recorded by monitoring systems.

Each stage can generate data.

When that intermediate data contains sensitive information, a security weakness anywhere in the chain can create an exposure that the end user may never notice.

### The risk for companies using AI

The potential impact is greater for organizations that use AI for activities involving internal data.

Finance departments may send documents and business information to models. Technology teams may use AI to analyze source code. Sales teams can work with customer information. AI agents may receive permissions to access internal systems and execute tasks.

That makes protecting intermediate data just as important as securing the final response.

A company may have strict controls over who can access its database and still create a new exposure surface by sending that information to an AI application without fully understanding how the data is processed, stored and logged.

## OpenAI, Anthropic and Google were affected by the discovery

The research involved models from several major AI laboratories, including systems developed by OpenAI, Anthropic and Google.

![Representation of OpenAI, Anthropic and Google facing a security vulnerability in artificial intelligence models](imagem-2.webp)

*OpenAI, Anthropic and Google were involved in the research that revealed a new attack surface in AI APIs.*

The researchers followed a responsible disclosure process before making the study public. The companies were informed about the vulnerability and took steps to mitigate the behavior demonstrated by the researchers.

That distinction matters because publishing the research should not be interpreted as evidence that anyone can simply access the hidden reasoning of users across these services.

The study demonstrates an exploitation technique under specific conditions.

### The discovery does not mean that every conversation is exposed

There is an important difference between demonstrating a vulnerability and claiming that millions of conversations have been stolen.

The research shows that certain reasoning traces could be recovered using the technique described. It does not demonstrate that all content processed by ChatGPT, Claude or Gemini is publicly accessible.

It also does not mean that the researchers gained unrestricted access to the companies' infrastructure.

The warning is different: **an architecture considered secure can behave unexpectedly when different models and components interact with one another.**

That distinction is essential to avoid exaggerated interpretations of the story.

### Why fixing the problem is more complicated than it seems

Fixing a vulnerability like this does not necessarily mean simply turning off a feature.

Major AI models are used by millions of applications. APIs need to remain compatible with existing software while providers balance security, performance, costs and model capabilities.

At the same time, reasoning models are becoming an increasingly important part of AI products.

The more these architectures are used by agents capable of performing tasks, the more intermediate data can be generated during execution.

That means the discovery could influence not only immediate security patches but also the design of the next generation of AI APIs.

## What changes for users and AI professionals

For ordinary users, the discovery does not mean they need to stop using ChatGPT, Claude or Gemini.

The main lesson is to avoid entering highly sensitive information into any AI service without understanding how that service handles the data.

That is particularly important for passwords, API keys, confidential documents, financial information and personal data.

![User interacting with an AI system while sensitive information is protected across multiple security layers](imagem-3.webp)

*The growth of AI agents increases the importance of protecting not only prompts and responses, but the entire flow of data.*

For professionals building AI applications, the warning is even more direct.

Teams need to evaluate which data reaches the model, what information appears in logs, who can access those records and how long the information remains stored.

### AI security must keep pace with the rise of AI agents

AI agents are changing how companies use language models.

Instead of simply answering questions, an agent can query systems, retrieve information, execute commands and chain multiple steps together to achieve a goal.

That increases productivity, but it also expands the attack surface.

A system that simply answers a question produces fewer intermediate operations than an agent capable of querying a CRM, accessing documents, executing code and automatically sending a response.

The consequence is clear: **the more autonomous an AI system becomes, the greater the need to control the data flowing through its execution.**

This shift is also connected to the evolution of enterprise AI architecture, which increasingly combines models, APIs, agents, RAG and other technologies to integrate artificial intelligence into business processes.

## The discovery could change the AI race in the coming months

The research arrives as major AI laboratories accelerate the development of models capable of increasingly complex reasoning and task execution.

That makes the protection of reasoning traces a strategic issue.

If proprietary model reasoning can be recovered through indirect techniques, competitors could gain valuable information about how these systems behave.

That does not mean an entire AI model can simply be copied from its reasoning traces. Models depend on enormous parameter sets, training data and computational infrastructure.

But reasoning traces can reveal useful patterns about how certain systems approach complex problems.

### Security could become a competitive advantage

So far, the AI race has been dominated largely by performance.

Companies compete over which model delivers the strongest capabilities, the most advanced reasoning, the lowest inference cost and the fastest responses.

**Inference** is the process in which an already-trained model uses its parameters to generate an output from a request.

The discovery adds another dimension to that competition: the ability to protect what happens during inference.

This could encourage providers to develop architectures in which intermediate data is never exposed to client applications in the same way.

It could also increase the use of isolation mechanisms, stricter access controls and dedicated policies for reasoning traces and logs.

## What companies should watch from now on

The most immediate consequence of the research is a change in mindset.

Companies adopting AI should not evaluate only whether a selected model produces accurate answers. They also need to understand how data enters the system, where it goes and where it may remain recorded.

That includes five key areas:

1. **Data sent to models:** what information is allowed to reach the AI system.
2. **Processing:** which models and tools participate in the execution.
3. **Traces and logs:** what intermediate information is stored.
4. **Permissions:** which systems and agents can access that information.
5. **Retention:** how long the data remains available.

This assessment will become even more important as enterprise systems move from chatbots toward autonomous AI agents.

### The market may demand greater transparency

The evolution of AI is also likely to increase pressure for stronger governance mechanisms.

AI governance means establishing rules and controls for how artificial intelligence systems are developed, deployed, monitored and supervised.

In an enterprise environment, this includes security, privacy, access control, auditing and accountability.

A vulnerability such as the one described by the researchers reinforces the idea that governance cannot be limited to the visible behavior of a model.

It also needs to cover the infrastructure that makes the model work.

## The real warning behind the vulnerability

The researchers' discovery does not reveal only a specific weakness in the APIs of major AI models.

It points to a deeper change in artificial intelligence security.

The most advanced AI systems are no longer isolated tools. They are becoming platforms that combine models, data, tools, APIs and agents.

That creates new opportunities for businesses, but it also creates new paths for attacks.

Users may see only a question and an answer. Behind them, however, there can be dozens of intermediate operations.

That invisible layer is where the security of the next generation of AI will have to evolve.

For OpenAI, Anthropic, Google and other AI laboratories, the priority will be protecting not only the models themselves but also the data generated during their execution.

For businesses, the message is equally important: **adopting AI means taking responsibility for the entire flow of information, not just the content displayed on the screen.**

Over the coming months, security around reasoning traces, protection of intermediate data and isolation between models are likely to become increasingly important in AI API development.

The AI race is entering a phase in which performance and security will need to advance together.

---