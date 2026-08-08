---
title: "The New Attack on AI Agents That Can Happen Without You Clicking Anything"
slug: "novo-ataque-agentes-ia-sem-clique"
translationKey: "novo-ataque-agentes-ia-sem-clique"
date: 2026-08-08T00:30:00-03:00
author: "By Aluisio Soares, founder of Notícia Tech"
description: "A new type of attack can exploit AI agents without requiring a user click. Here is why ChatGPT, Claude and businesses are now in the crosshairs."
categories:
  - "Artificial Intelligence"
cover:
  image: "capa.webp"
  alt: "Artificial intelligence agent being manipulated by malicious content without user interaction"
  caption: "The autonomy of AI agents creates a new security frontier: the content they read can also become an instruction that influences what they do."
faq:
  - pergunta: "What is a zero-click attack against an AI agent?"
    resposta_curta: "It is an attack that can manipulate an AI agent through content it processes, without requiring the user to click a link or execute a command."
    resposta_longa: "In zero-click attacks, an attacker embeds malicious instructions in content that an agent is already authorized to read, such as web pages, messages, documents or calendar invitations. When the agent interprets that content as part of the task, it may perform actions the user never intended."
  - pergunta: "Why are AI agents vulnerable to this type of attack?"
    resposta_curta: "Because AI agents need to interpret external content while also having the ability to take actions."
    resposta_longa: "A traditional chatbot typically responds to a request. An AI agent can go further by accessing services, retrieving information, browsing websites and completing tasks on behalf of the user. This combination creates a trust problem because the agent must distinguish legitimate data from malicious instructions embedded within that data."
  - pergunta: "Does the attack require the victim to click on something?"
    resposta_curta: "Not necessarily."
    resposta_longa: "The defining characteristic of this class of attack is that it removes the need for explicit user interaction. An agent can encounter and interpret malicious content while performing a legitimate task, allowing an unintended action to occur as part of a process the user originally initiated."
  - pergunta: "What changes for businesses using AI agents?"
    resposta_curta: "Businesses need to treat autonomous agents as systems with privileged access, not simply as productivity tools."
    resposta_longa: "When an agent has access to email, files, corporate systems or authenticated accounts, manipulation can have consequences far beyond an incorrect chatbot response. As agents become more capable, businesses need stronger access controls, limited permissions, human oversight for sensitive actions and dedicated monitoring of AI behavior."
  - pergunta: "Are ChatGPT and Claude connected to this new risk?"
    resposta_curta: "Yes. Security researchers are examining AI agents and agentic browsers, including systems associated with ChatGPT and Claude."
    resposta_longa: "The concern is not limited to a single company. Researchers have shown that agent architectures, particularly when agents can operate across multiple websites and authenticated services, create a different attack surface from traditional chatbots. The risk grows as AI systems become more autonomous."
  - pergunta: "Could this type of attack become more common in the coming months?"
    resposta_curta: "The risk is likely to increase as agents gain more autonomy and access to real-world systems."
    resposta_longa: "As more AI agents are authorized to read emails, documents, websites, internal systems and corporate services, they will encounter more untrusted content that they must interpret. That is likely to make agent security a central concern for businesses adopting AI-powered automation."
---

*AI agents are moving beyond simply answering questions and are beginning to act on behalf of users. They can read web pages, analyze documents, access services and complete tasks. That evolution can increase productivity, but it also raises a difficult question: what happens when content an agent is supposed to read tries to tell it what to do?*

## The New Attack Exploits the Autonomy of AI Agents

A new type of attack against **AI agents** exploits the ability of these systems to interpret content and perform tasks without requiring explicit user interaction. Instead of relying on a click, an attacker can attempt to place malicious instructions inside information that the agent has already been authorized to process.

![AI agent analyzing seemingly legitimate content containing malicious instructions](imagem-1.webp)

*AI agents can turn information that was supposed to be read into instructions capable of influencing their next actions.*

This changes the traditional attack model. In a conventional phishing attempt, for example, a criminal usually needs to convince a person to open a link, provide a password or download a file. With an autonomous agent, part of that interpretation can happen inside the system itself.

The warning gained new relevance with security research presented at **Black Hat 2026**, including work by **Zenity** on PleaseFix, a class of vulnerabilities involving AI-powered browsers. The central issue is that seemingly normal content can influence systems that browse the web and perform tasks on behalf of the user.

### What a Zero-Click Attack Means

A **zero-click attack** is an attempt to manipulate a system without relying on an explicit action from the victim, such as clicking a link. In the context of AI agents, malicious content can be encountered while the agent is performing a task the user legitimately initiated.

The agent might be analyzing a web page, reading a document, processing a calendar invitation or consulting an external source. If that content contains instructions the system interprets as part of the task, those instructions can influence its behavior.

The critical distinction is between **information and commands**. To a person, a sentence inside a document is normally just information. For an AI agent designed to understand natural language and determine its next steps, separating information from instructions can be much harder.

### Why This Is Different From a Traditional Chatbot

A **traditional chatbot** can receive a malicious instruction and produce an inappropriate response. An agent connected to tools can do more than answer: it can query systems, browse websites, access files or perform specific tasks.

That means the risk is not limited to what the AI generates. It is also tied to what happens **after the AI interprets information**.

This shift helps explain why the expansion of AI agents is creating a new layer of concern for cybersecurity. The same autonomy that makes an agent useful for automating tasks can also increase the potential impact of manipulation.

The market is already moving in this direction. **Claude**, for example, gained the ability to operate computers in a way that resembles how a human user interacts with them, a development that Notícia Tech has already analyzed in detail in its coverage of [how Claude gained the ability to use a computer like a human](https://noticiatech.com.br/en/artificial-intelligence/claude-gains-ability-use-computer-like-human-chatgpt/).

## The Content AI Reads Can Become an Instruction to Act

The main mechanism behind this risk is **indirect prompt injection**. In this type of attack, the attacker does not necessarily need to communicate directly with the model. The malicious instruction can be hidden inside an external source that the agent has been authorized to access.

![AI agent connecting external information to corporate systems while processing a malicious instruction](imagem-2.webp)

*When an agent can interpret external content and act on connected systems, the boundary between data and instructions becomes a security issue.*

Imagine a company using an agent to manage appointments. A user asks the AI to analyze their calendar and handle a task related to a meeting. If the content of a calendar invitation contains manipulated instructions, the agent could interpret part of that text as a legitimate instruction.

The user did not need to click anything because the task itself had already authorized the agent to read that content. That combination of **automated reading and the ability to take action** creates a different attack surface.

### When Data Stops Being Just Data

For a person, there is usually an intuitive distinction between information being read and an order that should be followed. An AI agent has to establish that distinction through architecture, policies and context.

An agent may receive information from emails, websites, documents, calendars or corporate systems. Not everything that appears in those environments was created by the user or has the authority to direct the system.

The problem becomes even more serious when the agent operates within an authenticated user session. In that scenario, external content can attempt to influence an AI that already has legitimate access to specific resources.

The question, therefore, is not only whether the content is malicious. It is also **what authority the agent has when it encounters that content**.

### The Real Problem Is What the Agent Can Do After Interpreting the Content

A malicious instruction inside a chatbot may result only in an unwanted response. In an agent connected to corporate systems, the potential consequences are much greater.

The agent may be authorized to retrieve information, fill out forms, send messages, move files or interact with external services. When those permissions are combined with untrusted content, the agent's autonomy can potentially be turned against the user.

That is the point businesses need to pay attention to: **the risk does not increase only because AI models are becoming smarter. It increases because agents are being given more ability to act.**

This shift also explains why agent identity is becoming increasingly important in enterprise security. Notícia Tech has already covered this concept in its analysis of [why AI agent identity needs to be treated as part of enterprise infrastructure](https://noticiatech.com.br/en/artificial-intelligence/what-is-ai-agent-identity-businesses/).

When AI receives its own permissions to operate systems, a company needs to know not only which model is being used, but **which agent is acting, which resources it can access and which actions it can perform**.

That combination of external content, automated interpretation and execution privileges transforms what might appear to be a simple text-manipulation problem into an operational security issue.

## The Problem Goes Beyond the Browser and Into Enterprise Security

The risk posed by attacks against **AI agents** is not limited to browsers. Any agent that interprets external content and has permissions to perform actions can create a similar attack surface, including systems connected to email, documents, CRMs, calendars, databases and enterprise software.

![AI agent connected to corporate systems and processing potentially malicious external content](imagem-3.webp)

*The more corporate systems an AI agent can access, the more important it becomes to control its permissions and limit what it can do.*

Academic research published in 2026 reinforces this concern. A study of agentic browsers identified a taxonomy containing **20 types of attacks**, experimentally reproducing 18 of them and showing that traditional web threats can reappear or be amplified when an agent begins interpreting web content and acting on it.

The problem, therefore, should not be viewed as an isolated flaw in a single product. It is connected to the way **AI agents** operate: observing information, interpreting context, deciding what to do next and executing an action.

### The Agent Can Become a "Confused Deputy"

In information security, the concept of a *confused deputy* describes a system that has legitimate privileges but is manipulated into using those privileges on behalf of someone else.

It is a useful way to understand the risk posed by AI agents. The system may have legitimate access to an account, file or application, but receive a malicious instruction from a source that should not have the authority to control it.

The difference is that the agent may not realize it is being manipulated. From its perspective, the action can appear to be simply another step required to complete the user's task.

This is one reason agent security needs to separate **user intent, external content and execution permissions**. Mixing these three layers increases the possibility that malicious information will be transformed into an action that is technically valid but completely unintended by the user.

## What This Attack Changes for Businesses Adopting AI Agents

For businesses, the main change is a shift in mindset: an **AI agent should be treated as an operational identity with privileges**, not simply as a more advanced chatbot.

That means an organization needs to know exactly which systems an agent can access, which actions it can perform autonomously and which operations require human approval.

The greater the autonomy, the greater the need to limit the potential impact of a successful manipulation.

### Broad Access Can Turn a Mistake Into a Security Incident

An agent authorized only to retrieve information from an internal database presents a different risk from one capable of sending emails, modifying records, accessing confidential documents or operating authenticated accounts.

That distinction matters because the impact of an **indirect prompt injection** also depends on the permissions available to the agent.

**The model can be manipulated, but the potential damage is determined by what the agent can do afterward.**

Zenity's research into **PleaseFix** demonstrated this problem in agentic browsers. In one scenario, malicious content inserted into a calendar invitation was able to induce the **Perplexity Comet** agent to access local files and send information to an attacker-controlled server. The company subsequently fixed the exploited vulnerability.

### Security Needs to Exist Outside the Model

One of the most important conclusions emerging from this new generation of research is that it is not enough to ask the model itself to "ignore malicious instructions."

AI-based filters can be fooled by the same type of content they are supposed to detect. Researchers therefore advocate for **deterministic safeguards**, meaning technical controls that block certain actions regardless of the decision made by the model.

In practice, this can mean preventing an agent from accessing specific local resources, restricting domains, isolating sessions, limiting credentials and requiring human confirmation for high-impact operations.

This is an important architectural shift. The goal is no longer simply to build a model that can "understand" danger. It is to build a system in which certain actions cannot happen without the appropriate authorization.

## The Autonomy That Makes AI Useful Also Increases the Risk

The expansion of **AI agents** is making this problem more relevant because businesses are turning assistants into systems capable of performing tasks for longer periods, navigating applications and operating tools on behalf of users.

**ChatGPT Work**, for example, illustrates this shift by bringing AI closer to the role of a digital coworker capable of carrying out work-related tasks.

This evolution increases the economic value of agents, but it also increases the importance of controlling their permissions and execution paths.

The problem is that security and autonomy are entering a delicate relationship.

**The more things an agent can do on its own, the greater the potential impact of a successful manipulation.**

This transformation also makes **AI governance** more important. Businesses adopting agents will need policies not only defining which models can be used, but also which actions can be delegated, which data can be accessed and when a human must take control.

This discussion is directly connected to the architecture of enterprise AI systems. Notícia Tech has already analyzed how **RAG, MCP, APIs, agents and workflows** are forming a new architecture for enterprise AI systems. That context helps explain why security cannot simply be added at the end of an AI project: it needs to be part of the architecture from the beginning.

## The Next Battleground Will Be Controlling What AI Can Do

The trend for the coming months is becoming clear: attacks against AI agents are likely to focus less on simply producing incorrect answers and more on **influencing actions performed by systems with real access to data and services**.

This creates a new priority for vendors and businesses. The challenge will not simply be making agents smarter, but ensuring that intelligence, autonomy and security evolve together.

### Businesses Will Have to Reduce Agent Privileges

The first practical consequence is likely to be wider adoption of **least-privilege models**.

Instead of giving an agent broad access, companies will need to limit each system to the minimum set of resources required to perform its role.

An agent responsible for scheduling meetings does not necessarily need access to financial documents.

A customer service agent should not automatically have permission to modify critical customer records.

A development agent does not need unrestricted access to every production system.

This logic is already well established in traditional cybersecurity, but it takes on a new dimension when users are no longer manually controlling every action performed by software.

### Human Approval Should Be Required for the Right Actions

This does not mean turning every agent into a tool that asks for permission at every step. If that happened, much of the productivity benefit would disappear.

The more likely direction is a hybrid architecture: low-risk tasks will be executed automatically, while operations involving money, credentials, sensitive data, external communication or irreversible changes will require confirmation.

The goal will be to find the balance between **enough autonomy to generate productivity and enough control to limit the impact of a successful attack**.

This scenario helps explain why agent security needs to evolve alongside enterprise adoption. As more companies use AI to perform real work, it will become increasingly important to define not only what an agent knows, but above all **what it is authorized to do**.

That is precisely why the zero-click attack represents such an important shift.

The threat no longer needs to convince a person to press a button. It only needs to find an agent that already has access, place malicious content somewhere along the path the agent naturally follows and wait for the agent's own autonomy to do the rest.

For businesses, this changes the security equation.

The next generation of protection for AI systems will not depend only on passwords, antivirus software or content filters. It will need to control **identity, permissions, context, tools and the actions performed by agents**.

The central question is becoming something else:

**When artificial intelligence is given permission to act on our behalf, who controls what it considers an instruction?**

---