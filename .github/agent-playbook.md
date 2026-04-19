# SDD Agent Playbook - Dashboard de Salários

Bem-vindo ao **Agent Playbook** focado em Spec-Driven Development (SDD). 
O SDD propõe que o fluxo de desenvolvimento seja direcionado primeiramente por uma especificação de negócio e técnica (Spec), minimizando assim alucinações das IAs e problemas arquiteturais durante a escrita do código.

## 🤖 Como funciona o fluxo SDD com Agentes

No ecossistema deste projeto, dividimos o desenvolvimento nos seguintes papéis simulados pelos modelos (agentes):

1. 🏗️ **Arquiteto** (`architect.md`)
2. 💻 **Dev Python** (`dev-python.md`)
3. 🕵️ **QA & Tester** (`qa-tester.md`)
4. ⚙️ **DevOps** (`devops.md`)

O ciclo de vida de uma nova funcionalidade (ou bug fix) é:

### Etapa 1: Planejamento (Arquiteto)

**Prompt sugerido para o seu Agente / Copilot:**
> "Atue como o Arquiteto lendo seu playbook em `.github/agents/architect.md`. O requisito de negócio é: [DESCREVER REQUISITO]. Crie a spec dentro de `.github/specs/`."

 O Arquiteto **NÃO VAI ESCREVER CÓDIGO FONTE**. Ele vai revisar o estado da arte e escrever um arquivo Markdown de especificação em `.github/specs/`.

### Etapa 2: Implementação (Dev Python)

**Prompt sugerido:**
> "Atue como o Desenvolvedor lendo `.github/agents/dev-python.md`. Crie o código-fonte estritamente embasado na especificação localizada em `.github/specs/nome-da-spec.md`."

O Dev vai se limitar exclusivamente ao que está na spec e usará Streamlit/Pandas/Plotly como definidos.

### Etapa 3: Revisão (QA)

**Prompt sugerido:**
> "Atue como o QA/Tester lendo `.github/agents/qa-tester.md`. Revise o código de `src/` comparando-o em relação à especificação definida em `.github/specs/nome-da-spec.md`. Corrija problemas (code smells) e, caso necessário, escreva testes unitários associados à spec."

### Etapa 4: Configuração (DevOps) - Se aplicável

**Prompt sugerido:**
> "Atue como DevOps lendo `.github/agents/devops.md`. Modifique a esteira CI/CD no GitHub Actions ou os mapeamentos de rede e pacotes no Dockerfile com as requisições oriundas de [REQUISITO/SPEC]."

---

## 📂 Organização da Pasta Specs

Toda spec gerada deverá ficar salva em: `.github/specs/`. 
As specs servem como fonte da verdade entre os Agentes para manter coerência. Caso uma alteração de código exija mudanças profundas, comece alterando a **Spec**, e não o código diretamente.
