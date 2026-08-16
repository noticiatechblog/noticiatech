---
title: "AI API Flaw Exposed Hidden Reasoning in ChatGPT, Claude and Gemini"
slug: "researchers-reveal-hidden-reasoning-chatgpt-claude-gemini"
translationKey: "pesquisadores-revelam-raciocinio-oculto-chatgpt-claude-gemini"
date: "2026-08-17T00:20:00-03:00"
draft: false
author: "By Aluisio Soares, founder of Notícia Tech"
description: "An AI API flaw made it possible to recover parts of the hidden reasoning from ChatGPT, Claude and Gemini, revealing new security risks for businesses."
categories:
  - "Artificial Intelligence"

cover:
  image: "capa.webp"
  alt: "Representation of ChatGPT, Claude and Gemini with internal reasoning layers exposed by an AI API flaw"
  caption: "A security research finding showed that the way AI models process intermediate data can create an exposure surface beyond the final response."

faq:
  - pergunta: "What did researchers discover about ChatGPT, Claude and Gemini?"
    resposta_curta: "They found a way to recover parts of the hidden reasoning produced by AI models."
    resposta_longa: "The research identified an architectural vulnerability related to the use of APIs by models from OpenAI, Anthropic and Google. Under certain conditions, protected reasoning blocks could be reused to recover information that would normally not appear in the response delivered to the user."

  - pergunta: "Did the flaw allow researchers to access all of the models' reasoning?"
    resposta_curta: "No. The research demonstrated that parts of reasoning traces could be recovered under specific conditions."
    resposta_longa: "The finding does not mean that the full internal processing of ChatGPT, Claude or Gemini became freely accessible. The study demonstrated a technique capable of recovering certain reasoning blocks, without showing that all internal model content could be retrieved."

  - pergunta: "Was the vulnerability in the AI APIs?"
    resposta_curta: "The issue was related to how certain intermediate data moved through the APIs."
    resposta_longa: "The research points to an architectural vulnerability in the interaction between models and APIs. The risk did not simply involve breaking encryption, but rather reusing certain protected blocks within the providers' model ecosystems."

  - pergunta: "Were personal data and credentials found?"
    resposta_curta: "Yes. Researchers identified sensitive information in the analyzed traces."
    resposta_longa: "In an analysis of 315,320 reasoning blocks obtained from public logs, the researchers found 367 artifacts containing personally identifiable information and 182 credentials. The findings show that sensitive data can appear in intermediate layers of AI systems."

  - pergunta: "Are ChatGPT, Claude and Gemini still vulnerable?"
    resposta_curta: "The companies were notified and took mitigation measures."
    resposta_longa: "The discovery was handled through responsible disclosure. OpenAI, Anthropic and Google were informed about the behavior identified by the researchers and took measures to reduce the risk demonstrated by the study."

  - pergunta: "What does the discovery change for businesses using AI?"
    resposta_curta: "Businesses also need to protect logs, traces and intermediate data."
    resposta_longa: "AI application security should not focus only on prompts and final responses. Intermediate data, execution traces, credentials, permissions and information processed by agents also need to be covered by corporate security and governance policies."

  - pergunta: "Why is this discovery important for AI agents?"
    resposta_curta: "Agents execute more steps and increase the amount of data moving through an operation."
    resposta_longa: "AI agents can query systems, use tools and execute tasks in sequence. As autonomy increases, so can the amount of intermediate information produced, making controls over traces, logs, permissions and data used during execution increasingly important."
---

*Security researchers have uncovered a weakness in a layer that normally remains invisible to users: the intermediate data produced by large AI models. The case involves **OpenAI**, **Anthropic** and **Google** and shows why securing AI requires more than protecting the final answer.*

## What Researchers Discovered in AI APIs

Researchers found a technique capable of recovering parts of the hidden reasoning produced by **ChatGPT**, **Claude** and **Gemini** under certain conditions. The discovery involves the way intermediate information is processed and reused by APIs.

The so-called **chain-of-thought** represents intermediate steps that reasoning models use to solve certain tasks. Users normally see only the final result, while intermediate information remains outside the interface for security, intellectual property and privacy reasons.

The key point is that the study does not describe a direct intrusion into the servers of **OpenAI**, **Anthropic** or **Google**. The issue involved the communication architecture between models and applications, revealing a security surface that can remain invisible during normal use.

### What Hidden Reasoning Means

An **LLM** can perform analysis, planning and verification steps before producing an answer. Users normally see only the final result, while intermediate information remains outside the interface.

That separation creates another layer that also needs to be protected. If intermediate data moves between different components of an application, a failure in that communication can have consequences that are not visible in the final output.

### Why It Matters to Major AI Labs

For **OpenAI**, **Anthropic** and **Google**, reasoning traces have technical and strategic value. They can reveal information about how certain models solve problems and, in some cases, contain data introduced during a task.

The discovery shows that hiding reasoning at the interface level is not enough. Protection has to cover the entire path that data follows during execution.

## How the API Flaw Created an Exposure Surface

The vulnerability was related to the behavior of certain protected blocks returned by APIs. Under specific conditions, researchers were able to exploit the way those blocks could be reused within the same model ecosystem.

![Representation of protected reasoning blocks being processed by different AI models](imagem-1.webp)

*Intermediate reasoning blocks can move between components during an interaction with artificial intelligence APIs.*

An **AI API** allows applications to send requests directly to a model and receive results programmatically. Businesses use this mechanism to integrate artificial intelligence into internal systems, applications, agents and automated workflows.

The identified risk shows that the security of such an integration does not depend only on the individual model. When different models and components share data, the behavior of one element can affect the protection of another.

### A Less Capable Model Could Participate in the Exploit

The technique attracted attention because it did not necessarily require convincing the most advanced model to reveal its own reasoning. Instead, the researchers exploited compatibility between different components in the ecosystem.

Under certain conditions, a block produced by one model could be presented to another model capable of transforming protected information into readable content.

### It Was Not a Conventional Encryption Break

This distinction is important. The researchers did not demonstrate that private keys belonging to the companies had been obtained or that all encryption used by the providers had been broken.

The issue involved the architecture and reuse of information between components. It is an example of how complex systems can develop security risks through interactions between parts that appear protected when considered individually.

## The Risk Increases When Real Data Enters Reasoning Traces

The seriousness of the discovery became clearer when the researchers analyzed real-world data. In **315,320 reasoning blocks** obtained from public logs, they identified **367 artifacts containing personally identifiable information** and **182 credentials**.

![Representation of OpenAI, Anthropic and Google facing an artificial intelligence API vulnerability](imagem-2.webp)

*The case involving OpenAI, Anthropic and Google shows that intermediate data also needs to be part of an AI security strategy.*

These figures do not mean that all user conversations are exposed. They show, however, that information considered intermediate can contain sensitive data and deserves the same level of protection applied to other corporate records.

For businesses, this changes how an AI application needs to be evaluated. The information visible in the final response represents only one part of the data flow processed by the system.

### Logs Can Contain More Information Than the Final Response

Logs record operations, requests, errors and responses to support monitoring and development. In AI applications, they can also record information produced during intermediate processing steps.

A seemingly simple session can therefore generate a much larger amount of data behind the scenes. That material needs to be handled according to its sensitivity.

### The Problem Reaches the Enterprise Environment

A business may use AI to analyze documents, source code, financial information or customer data. If that information reaches traces or logs, a failure in an intermediate layer could create an exposure that the end user never notices.

The discovery therefore reinforces the importance of treating **AI intermediate data** as part of the security surface. The issue connects directly to **[why AI security has become a priority for businesses](https://noticiatech.com.br/en/artificial-intelligence/what-is-ai-security-business-priority-coming-years/)**.

## What the Discovery Changes for Businesses Adopting AI

Businesses using artificial intelligence need to evaluate not only the quality of model responses, but also the path data takes during execution. That includes models, APIs, tools, logs and permissions.

The risk becomes even greater when AI stops functioning as a chatbot and starts performing tasks. A system may query a CRM, access documents, call APIs and execute actions without the user following every step.

The discovery therefore reinforces an important shift: AI security needs to consider the **full information flow**, not just the interface.

### Five Areas Now Deserve Greater Attention

Businesses need to know what data reaches the model, which components participate in processing and what information is stored during execution.

They also need to control who can access logs and traces, how long those records remain available, and which credentials or permissions can appear during an operation.

### Agents Expand the Risk Surface

An AI agent can execute multiple steps to achieve a goal. As autonomy increases, so does the potential amount of intermediate data and the number of systems involved.

This makes identity, permissions and accountability even more important. The growth of AI agents is already creating new challenges for businesses, particularly as autonomous systems begin performing actions on behalf of organizations.

## Why the Discovery Could Influence the Next Generation of APIs

The research comes as **OpenAI**, **Anthropic**, **Google** and other AI labs expand the use of models capable of reasoning and executing complex tasks. That increases the value of the data produced during inference.

Providers must balance security, compatibility, performance and cost. A change in an AI API's architecture can affect millions of applications that depend on it.

The case could therefore encourage stricter isolation mechanisms and more specific controls for reasoning traces and logs.

![User interacting with AI while intermediate data is protected by multiple security layers](imagem-3.webp)

*As AI systems become more autonomous, protecting the full information flow generated during execution becomes increasingly important.*

### Security Could Become a Competitive Differentiator

The AI race is usually measured by performance, speed, cost and reasoning capabilities. Protecting internal processing adds another dimension to that competition.

Providers that can offer advanced models without unnecessarily increasing data exposure could gain an advantage among enterprise customers.

### The Impact Goes Beyond ChatGPT, Claude and Gemini

The discovery should not be interpreted solely as a problem involving three platforms. It exposes a structural challenge for systems that combine models, APIs, agents, tools and enterprise data.

As this architecture becomes more common, security and governance will need to follow every stage of execution. The market is likely to demand greater transparency around how intermediate information is handled.

## AI Security Will Have to Protect What Happens Behind the Scenes

The main lesson from the research is that the response displayed to a user represents only part of how an AI system works. Behind it may be different models, APIs, traces, logs, tools and multiple processing stages.

For businesses, that means expanding risk assessments. It is not enough to choose a trusted model. Organizations also need to understand how data enters, moves through, is recorded by and leaves the system.

That concern will become even more important as autonomous agents expand. The discussion around **[business responsibility for AI agent actions](https://noticiatech.com.br/en/artificial-intelligence/ai-agents-new-problem-businesses-responsibility-autonomous-actions/)** shows how autonomy is creating an additional layer of governance.

### The Next Challenge Will Be Controlling Data Flows

The trend is likely to put greater emphasis on reasoning-trace security, model isolation, log controls and permission management within enterprise AI architectures.

The case also shows that vulnerabilities can emerge not only inside a model, but in the way different components work together.

### What This Discovery Actually Changes

The research does not indicate that users should abandon **ChatGPT**, **Claude** or **Gemini**. The main warning is that businesses need to treat the entire data flow as part of AI security.

The next phase of enterprise artificial intelligence will be defined not only by the ability to reason and act, but by the ability to do so while keeping sensitive information protected throughout execution.

---