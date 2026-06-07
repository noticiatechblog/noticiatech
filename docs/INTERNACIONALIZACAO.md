# Internacionalização do Notícia Tech

## 1. Como adicionar um artigo em português
- Crie a página em `content/` seguindo a mesma estrutura já usada no blog.
- Use o mesmo front matter do artigo atual e mantenha imagens no mesmo caminho.

## 2. Como adicionar um artigo em inglês
- Crie a página em `content/en/` com o mesmo slug em inglês.
- Repita o front matter e, quando necessário, use as mesmas imagens do artigo em português.

## 3. Como vincular traduções
- Mantenha a mesma estrutura de slug e nome do arquivo entre PT e EN.
- O seletor de idiomas usará as páginas traduzidas da home e os links alternativos do Hugo.

## 4. Como compartilhar imagens entre idiomas
- Aponte ambos os artigos para a mesma pasta de imagens em `static/images/`.
- Não é necessário criar versões duplicadas das imagens.

## 5. Como criar links internos multilíngues
- Use `absLangURL` ou caminhos relativos dentro do conteúdo.
- Para links entre idiomas, prefira o caminho correspondente em `/en/` quando existir tradução.
