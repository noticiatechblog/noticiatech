---
title: "O novo ataque contra agentes de IA que pode acontecer sem você clicar em nada"
slug: "novo-ataque-agentes-ia-sem-clique"
translationKey: "novo-ataque-agentes-ia-sem-clique"
date: 2026-08-08T00:30:00-03:00
author: "Por Aluisio Soares, fundador do blog Notícia Tech"
description: "Um novo tipo de ataque explora agentes de IA sem exigir um clique do usuário. Entenda por que ChatGPT, Claude e empresas entram no radar."
categories:
  - "inteligencia-artificial"
cover:
  image: "capa.webp"
  alt: "Agente de inteligência artificial sendo manipulado por conteúdo malicioso sem interação do usuário"
  caption: "A autonomia dos agentes de IA cria uma nova fronteira de risco: o conteúdo que eles leem também pode se transformar em uma instrução para agir."
faq:
  - pergunta: "O que é um ataque sem clique contra um agente de IA?"
    resposta_curta: "É um ataque que pode manipular um agente de IA por meio de conteúdo que ele processa, sem exigir que o usuário clique em um link ou execute um comando."
    resposta_longa: "Em ataques sem clique, o invasor coloca instruções maliciosas dentro de conteúdos que o agente já está autorizado a ler, como páginas, mensagens, documentos ou convites. Quando o agente interpreta esse conteúdo como parte da tarefa, pode executar ações não pretendidas pelo usuário."
  - pergunta: "Por que agentes de IA são vulneráveis a esse tipo de ataque?"
    resposta_curta: "Porque agentes de IA precisam interpretar conteúdo externo e também têm capacidade de executar ações."
    resposta_longa: "Um chatbot tradicional normalmente responde a uma solicitação. Um agente de IA pode ir além: acessar serviços, consultar informações, navegar por páginas e executar tarefas em nome do usuário. Essa combinação cria um problema de confiança, porque o agente precisa distinguir dados legítimos de instruções maliciosas escondidas nos dados."
  - pergunta: "O ataque exige que a vítima clique em alguma coisa?"
    resposta_curta: "Não necessariamente."
    resposta_longa: "A característica central dessa classe de ataque é justamente eliminar a interação explícita do usuário. O agente pode encontrar e interpretar o conteúdo malicioso durante uma tarefa legítima, fazendo com que a ação indevida ocorra como consequência de um processo que o usuário iniciou normalmente."
  - pergunta: "O que muda para empresas que usam agentes de IA?"
    resposta_curta: "Empresas precisam tratar agentes autônomos como sistemas com acesso privilegiado, e não apenas como ferramentas de produtividade."
    resposta_longa: "Quando um agente possui acesso a e-mail, arquivos, sistemas corporativos ou contas autenticadas, uma manipulação pode ter consequências muito maiores do que uma resposta incorreta de um chatbot. A expansão dos agentes exige controles de acesso, limitação de permissões, supervisão de ações sensíveis e monitoramento específico do comportamento da IA."
  - pergunta: "ChatGPT e Claude estão relacionados a esse novo risco?"
    resposta_curta: "Sim. Pesquisas de segurança vêm examinando agentes e navegadores baseados em IA, incluindo sistemas ligados ao ChatGPT e ao Claude."
    resposta_longa: "A preocupação não está limitada a uma única empresa. Pesquisadores vêm demonstrando que a arquitetura dos agentes, especialmente quando eles podem operar em várias páginas e serviços autenticados, cria uma superfície de ataque diferente da encontrada em chatbots tradicionais. O problema acompanha a expansão da autonomia dos sistemas de IA."
  - pergunta: "Esse tipo de ataque pode aumentar nos próximos meses?"
    resposta_curta: "A tendência é de aumento à medida que agentes ganham mais autonomia e acesso a sistemas reais."
    resposta_longa: "Quanto mais agentes de IA forem autorizados a ler e-mails, documentos, páginas da internet, sistemas internos e serviços corporativos, maior será a quantidade de conteúdo não confiável que eles precisarão interpretar. Isso tende a transformar a segurança de agentes em uma preocupação central para empresas que adotam automação baseada em IA."
---

*Os agentes de IA estão deixando de ser apenas ferramentas que respondem perguntas e começando a agir em nome dos usuários. Eles podem ler páginas, analisar documentos, acessar serviços e executar tarefas. Essa evolução aumenta a produtividade, mas também cria uma pergunta difícil: o que acontece quando o conteúdo que o agente deveria apenas ler tenta dizer a ele o que fazer?*

## O novo ataque explora justamente a autonomia dos agentes de IA

Um novo tipo de ataque contra **agentes de IA** explora justamente a capacidade desses sistemas de interpretar conteúdo e executar tarefas sem exigir uma interação explícita do usuário. Em vez de depender de um clique, o invasor tenta colocar instruções maliciosas dentro de informações que o próprio agente já foi autorizado a processar.

![Agente de inteligência artificial analisando conteúdo aparentemente legítimo que contém instruções maliciosas](imagem-1.webp)

*Agentes de IA podem transformar informações que deveriam apenas ser lidas em instruções capazes de influenciar suas próximas ações.*

Essa diferença muda o modelo tradicional de ataque. Em uma tentativa convencional de phishing, por exemplo, o criminoso normalmente precisa convencer uma pessoa a abrir um link, fornecer uma senha ou baixar um arquivo. Com um agente autônomo, parte dessa interpretação pode acontecer dentro do próprio sistema.

O alerta ganhou nova dimensão com pesquisas de segurança apresentadas no **Black Hat 2026**, incluindo o trabalho da **Zenity** sobre o PleaseFix, uma classe de vulnerabilidades relacionada a navegadores com agentes de IA. A questão central é que conteúdos aparentemente normais podem influenciar sistemas que navegam e executam tarefas em nome do usuário.

### O que significa um ataque sem clique

Um **ataque sem clique** é uma tentativa de manipular um sistema sem depender de uma interação explícita da vítima, como clicar em um link. No contexto dos agentes de IA, o conteúdo malicioso pode ser encontrado durante uma tarefa que o usuário iniciou normalmente.

O agente pode estar analisando uma página, lendo um documento, processando um convite ou consultando uma fonte externa. Se o conteúdo contiver instruções que o sistema interprete como parte da tarefa, essas instruções podem influenciar seu comportamento.

O ponto crítico está na diferença entre **informação e comando**. Para uma pessoa, uma frase dentro de um documento normalmente é apenas informação. Para um agente de IA, que foi projetado para interpretar linguagem natural e decidir os próximos passos, essa separação pode ser muito mais difícil.

### Por que isso é diferente de um chatbot comum

Um **chatbot tradicional** pode receber uma instrução maliciosa e produzir uma resposta inadequada. Um agente conectado a ferramentas pode fazer algo além de responder: ele pode consultar sistemas, navegar por páginas, acessar arquivos ou executar determinadas tarefas.

Isso significa que o risco não está somente no conteúdo produzido pela IA. Ele também está relacionado ao que acontece **depois que a IA interpreta uma informação**.

Essa mudança ajuda a explicar por que a expansão dos agentes está criando uma nova camada de preocupação para a segurança digital. A mesma autonomia que torna um agente útil para automatizar tarefas também pode aumentar o impacto de uma manipulação.

O mercado já está avançando nessa direção. O **Claude**, por exemplo, passou a operar computadores de maneira semelhante a um usuário, uma mudança que o Notícia Tech já analisou em detalhes ao explicar **[como o Claude passou a usar o computador como um humano](https://noticiatech.com.br/inteligencia-artificial/claude-usa-computador-como-humano-chatgpt/)**.

## O conteúdo que a IA lê pode virar uma instrução para agir

O principal mecanismo por trás desse risco é a **injeção indireta de instruções**. Nesse tipo de situação, o atacante não precisa necessariamente conversar diretamente com o modelo. A instrução maliciosa pode estar escondida em uma fonte externa que o agente recebeu autorização para consultar.

![Agente de IA conectando informações externas a sistemas corporativos enquanto processa uma instrução maliciosa](imagem-2.webp)

*Quando um agente pode interpretar conteúdo externo e agir sobre sistemas conectados, a fronteira entre dado e instrução se torna uma questão de segurança.*

Imagine uma empresa utilizando um agente para organizar compromissos. O usuário pede que a IA analise sua agenda e cuide de uma tarefa relacionada a uma reunião. Se o conteúdo de um convite contiver instruções manipuladas, o agente poderá interpretar parte daquele texto como uma orientação legítima.

O usuário não precisou clicar em nada porque a própria tarefa já autorizava o agente a ler aquele conteúdo. É justamente essa combinação entre **leitura automática e capacidade de ação** que cria uma superfície de ataque diferente.

### Quando dados deixam de ser apenas dados

Para uma pessoa, existe normalmente uma separação intuitiva entre uma informação que está sendo lida e uma ordem que deve ser obedecida. Um agente de IA precisa estabelecer essa diferença por meio de arquitetura, políticas e contexto.

Um agente pode receber informações de e-mails, páginas da internet, documentos, calendários ou sistemas corporativos. Nem tudo que aparece nesses ambientes foi produzido pelo usuário ou possui autoridade para orientar o sistema.

Esse problema se torna ainda mais sério quando o agente utiliza uma sessão autenticada do usuário. Nesse cenário, um conteúdo externo pode tentar influenciar uma IA que já possui acesso legítimo a determinados recursos.

A questão, portanto, não é apenas se o conteúdo é malicioso. É também **qual autoridade o agente possui quando encontra esse conteúdo**.

### O verdadeiro problema é o poder que vem depois da interpretação

Uma instrução maliciosa dentro de um chatbot pode resultar apenas em uma resposta indesejada. Em um agente conectado a sistemas corporativos, a consequência potencial é muito maior.

O agente pode ter autorização para consultar informações, preencher formulários, enviar mensagens, movimentar arquivos ou interagir com serviços externos. Quando essas permissões são combinadas com conteúdo não confiável, a autonomia do agente pode ser utilizada contra o próprio usuário.

Esse é o ponto que merece atenção das empresas: **o risco não cresce apenas porque os modelos estão mais inteligentes. Ele cresce porque os agentes estão recebendo mais capacidade de agir.**

Essa mudança também explica por que a identidade dos agentes começa a ganhar importância dentro da segurança corporativa. O Notícia Tech já abordou esse conceito ao explicar **[por que a identidade de um agente de IA precisa ser tratada como parte da infraestrutura empresarial](https://noticiatech.com.br/inteligencia-artificial/ai-agent-identity-identidade-agentes-ia-empresas/)**.

Quando a IA recebe permissões próprias para operar sistemas, a empresa precisa saber não apenas qual modelo está sendo utilizado, mas **qual agente está agindo, quais recursos ele pode acessar e quais ações pode executar**.

É essa combinação entre conteúdo externo, interpretação automática e privilégios de execução que transforma um simples problema de manipulação de texto em uma questão de segurança operacional.

## O problema vai além do navegador e começa a atingir a segurança corporativa

O risco dos ataques contra **agentes de IA** não está restrito aos navegadores. Qualquer agente que interprete conteúdo externo e tenha permissões para executar ações pode criar uma superfície semelhante de ataque, incluindo sistemas conectados a e-mails, documentos, CRMs, calendários, bancos de dados e ferramentas corporativas.

![Agente de inteligência artificial conectado a sistemas corporativos e processando conteúdo externo potencialmente malicioso](imagem-3.webp)

*Quanto mais sistemas corporativos um agente de IA consegue acessar, maior é a importância de controlar suas permissões e limitar suas ações.*

Pesquisas acadêmicas realizadas em 2026 reforçam essa preocupação. Um estudo sobre navegadores agentivos identificou uma taxonomia com **20 tipos de ataques**, reproduzindo 18 deles experimentalmente e mostrando que ameaças tradicionais da web podem reaparecer ou ser ampliadas quando um agente passa a interpretar o conteúdo das páginas e agir sobre elas.

O problema, portanto, não deve ser interpretado como uma falha isolada de um produto. Ele está relacionado ao próprio modelo de funcionamento dos **agentes de IA**: observar informações, interpretar o contexto, decidir o próximo passo e executar uma ação.

### O agente pode virar um "confused deputy"

Em segurança da informação, existe o conceito de *confused deputy*, quando um sistema que possui determinados privilégios é manipulado para utilizá-los em benefício de outra pessoa.

É uma boa maneira de entender o risco dos agentes. O sistema pode ter acesso legítimo a uma conta, arquivo ou aplicação, mas receber uma instrução maliciosa de uma fonte que não deveria ter autoridade para comandá-lo.

A diferença é que o agente não necessariamente percebe que está sendo manipulado. Para ele, a ação pode parecer apenas mais uma etapa necessária para concluir a tarefa solicitada pelo usuário.

Esse é um dos motivos pelos quais a segurança de agentes precisa separar **intenção do usuário, conteúdo externo e permissões de execução**. Misturar essas três camadas aumenta a possibilidade de que uma informação maliciosa seja transformada em uma ação legítima do ponto de vista técnico, mas completamente indevida do ponto de vista do usuário.

## O que esse ataque muda para empresas que adotam agentes de IA

Para as empresas, a principal mudança de mentalidade é tratar um **agente de IA como uma identidade operacional com privilégios**, e não simplesmente como um chatbot mais avançado.

Isso significa que uma organização precisa saber exatamente quais sistemas o agente pode acessar, quais ações pode executar sozinho e quais operações exigem aprovação humana.

Quanto maior a autonomia, maior também precisa ser a capacidade de limitar o impacto de uma eventual manipulação.

### Acesso amplo pode transformar um erro em incidente

Um agente autorizado a apenas consultar uma base interna apresenta um risco diferente de outro capaz de enviar e-mails, modificar registros, acessar documentos confidenciais ou operar contas autenticadas.

Essa diferença é fundamental porque o impacto de uma **injeção indireta de instruções** depende também das permissões disponíveis.

**O modelo pode ser manipulado, mas o estrago potencial é determinado pelo que o agente consegue fazer depois.**

A pesquisa da **Zenity** sobre o **PleaseFix** mostrou justamente esse problema em navegadores agentivos. Em um dos cenários analisados, conteúdo malicioso inserido em um convite de calendário conseguiu induzir o agente do **Perplexity Comet** a acessar arquivos locais e enviar informações para um servidor controlado pelo atacante. A empresa posteriormente corrigiu a falha explorada.

### A segurança precisa acontecer fora do modelo

Uma das conclusões mais importantes dessa nova geração de pesquisas é que não basta pedir ao próprio modelo para "não obedecer instruções maliciosas".

Filtros baseados exclusivamente em IA podem ser enganados pelo mesmo tipo de conteúdo que deveriam identificar. Por isso, pesquisadores defendem **barreiras determinísticas**, ou seja, controles técnicos que bloqueiem determinadas ações independentemente da decisão tomada pelo modelo.

Na prática, isso pode significar impedir que um agente acesse determinados recursos locais, restringir domínios, separar sessões, limitar credenciais e exigir confirmação humana para operações de alto impacto.

É uma mudança importante porque coloca a segurança no nível da arquitetura. O objetivo deixa de ser apenas construir um modelo que "entenda" o perigo e passa a ser construir um sistema no qual determinadas ações simplesmente não possam acontecer sem autorização adequada.

## A autonomia que torna a IA útil também aumenta o risco

A expansão dos **agentes de IA** está tornando esse problema mais relevante porque empresas estão transformando assistentes em sistemas capazes de executar tarefas durante períodos maiores, navegar por aplicações e operar ferramentas em nome do usuário.

O próprio **ChatGPT Work** mostra essa mudança ao aproximar a IA de um colaborador digital capaz de executar tarefas de trabalho.

Esse avanço aumenta o valor econômico dos agentes, mas também aumenta a importância de controlar suas permissões e seus caminhos de execução.

O problema é que segurança e autonomia entram em uma relação delicada.

**Quanto mais coisas um agente consegue fazer sozinho, maior é o impacto potencial de uma manipulação bem-sucedida.**

Essa transformação também torna a **governança de IA** mais importante. Empresas que adotam agentes precisarão estabelecer políticas não apenas sobre quais modelos podem ser utilizados, mas sobre quais ações podem ser delegadas, quais dados podem ser acessados e quando um humano precisa assumir o controle.

Essa discussão se conecta diretamente à arquitetura de sistemas corporativos de IA. O Notícia Tech já analisou como **RAG, MCP, APIs, agentes e workflows** estão formando uma nova arquitetura para sistemas empresariais de IA. Esse contexto ajuda a entender por que segurança não pode ser adicionada apenas no final de um projeto: ela precisa fazer parte da arquitetura desde o início.

## O próximo campo de disputa será controlar o que a IA pode fazer

A tendência para os próximos meses é clara: os ataques contra agentes devem se concentrar cada vez menos em simplesmente produzir respostas erradas e mais em **influenciar ações realizadas por sistemas que possuem acesso real a dados e serviços**.

Isso cria uma nova prioridade para fabricantes e empresas. O desafio não será apenas tornar os agentes mais inteligentes, mas garantir que inteligência, autonomia e segurança evoluam juntas.

### Empresas terão de reduzir o privilégio dos agentes

A primeira consequência prática tende a ser a adoção de modelos de **menor privilégio**.

Em vez de conceder acesso amplo a um agente, as empresas deverão limitar cada sistema ao conjunto mínimo de recursos necessário para realizar sua função.

Um agente responsável por organizar reuniões não precisa necessariamente acessar documentos financeiros.

Um agente de atendimento não deveria ter automaticamente permissão para alterar dados críticos de clientes.

Um agente de desenvolvimento não precisa receber acesso irrestrito a todos os sistemas de produção.

Essa lógica já é conhecida na segurança tradicional, mas ganha uma dimensão nova quando o usuário não controla manualmente cada ação realizada pelo software.

### A aprovação humana deve ficar nas ações certas

Isso não significa transformar todos os agentes em ferramentas que pedem autorização para cada passo. Se isso acontecer, parte do ganho de produtividade desaparece.

A tendência mais provável é uma arquitetura híbrida: tarefas de baixo risco serão executadas automaticamente, enquanto operações envolvendo dinheiro, credenciais, dados sensíveis, comunicação externa ou alterações irreversíveis exigirão confirmação.

O objetivo será encontrar o equilíbrio entre **autonomia suficiente para gerar produtividade e controle suficiente para limitar o impacto de uma manipulação**.

Esse cenário ajuda a explicar por que a segurança dos agentes deve evoluir junto com a adoção empresarial. Quanto mais empresas utilizarem IA para executar trabalho real, mais importante será definir não apenas o que o agente sabe, mas principalmente **o que ele está autorizado a fazer**.

O ataque sem clique representa uma mudança importante justamente por isso.

A ameaça não precisa mais convencer uma pessoa a apertar um botão. Basta encontrar um agente que já tenha acesso, inserir conteúdo no caminho que ele naturalmente percorre e esperar que a própria autonomia faça o restante.

Para as empresas, isso muda a lógica de segurança.

A próxima geração de proteção para sistemas de IA não dependerá apenas de senhas, antivírus ou filtros de conteúdo. Ela precisará controlar **identidade, permissões, contexto, ferramentas e ações executadas pelos agentes**.

A pergunta central passa a ser outra:

**Quando uma inteligência artificial recebe permissão para agir em nosso nome, quem controla aquilo que ela considera uma instrução?**

---