# S202 - Banco de Dados II

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-4.4+-green.svg)](https://www.mongodb.com/)
[![Neo4j](https://img.shields.io/badge/Neo4j-4.0+-red.svg)](https://neo4j.com/)

Repositório acadêmico contendo projetos e relatórios desenvolvidos durante a disciplina de **Banco de Dados II**.

Este repositório abrange implementações práticas com bancos de dados NoSQL, incluindo MongoDB e Neo4j, demonstrando conceitos de modelagem não-relacional, agregações, consultas complexas e desenvolvimento de aplicações.

## Estrutura do Repositório

### Projetos Principais

#### 📚 Project_SensorSimulation
Simulação de sensores IoT usando MongoDB com threading para monitoramento de temperatura em tempo real.

**Características:**
- Simulação de 3 sensores com diferentes intervalos de execução
- Detecção automática de alarmes (temperatura > 38°C)
- Persistência de dados em MongoDB
- Threading para execução paralela

**Tecnologias:** Python, PyMongo, Threading

--- 

#### 📚 ProjectSCM (Supply Chain Management)
Sistema de gerenciamento de cadeia de suprimentos utilizando Neo4j para modelagem de relacionamentos entre redes de supermercados e fornecedores.

**Funcionalidades:**
- CRUD completo para redes de supermercados
- CRUD completo para fornecedores
- Gerenciamento de parcerias e relacionamentos
- Interface CLI interativa

**Tecnologias:** Python, Neo4j, Cypher

--- 

### Relatórios e Exercícios

#### 📚 FamilyTime
Modelagem de árvore genealógica usando Neo4j para demonstrar relacionamentos familiares complexos.

**Relacionamentos implementados:**
- PAI_DE, ESPOSO_DE, AVO_DE
- IRMAO_DE, SOGRO_DE, PRIMO_DE, SOBRINHO_DE

---

#### 📚 exercicio_Neo4j
Rede social básica modelada em Neo4j com análises estatísticas.

**Funcionalidades:**
- Criação de usuários e postagens
- Sistema de amizades
- Consultas analíticas (idade média, usuários mais velhos, etc.)

---

#### 📚 exercicio_Zoologico
Sistema de gerenciamento de zoológico usando MongoDB com padrão DAO.

**Estrutura:**
- Modelo de dados hierárquico (Animal → Habitat → Cuidador)
- Interface CLI para operações CRUD
- Validação de dados

---

#### 📚 Relatórios Específicos

**relatorio03** - Análise de dados Pokémon
- Consultas por tipo, HP e características específicas
- Exportação de resultados em JSON

**relatorio04** - Sistema de análise de vendas
- Agregações complexas no MongoDB
- Análises de produtos e clientes

**relatorio05** - Sistema de biblioteca
- Modelo CRUD para livros
- Demonstração de operações básicas

**relatorio06 & relatorio07** - Neo4j avançado
- Consultas Cypher complexas
- Funções de agregação e manipulação de strings

**relatorio08** - Sistema de jogos
- Modelagem de jogadores e partidas
- Histórico de jogadores e relacionamentos

## Tecnologias Utilizadas

### Bancos de Dados
- **MongoDB** - Banco de dados NoSQL orientado a documentos
- **Neo4j** - Banco de dados de grafos

### Linguagens e Frameworks
- **Python 3.8+** - Linguagem principal
- **PyMongo** - Driver oficial do MongoDB para Python
- **Neo4j Python Driver** - Driver oficial do Neo4j para Python

### Bibliotecas Auxiliares
- `threading` - Para execução paralela
- `random` - Geração de dados aleatórios
- `bson` - Manipulação de ObjectId
- `pprint` - Pretty printing
- `json` - Manipulação de arquivos JSON

## Como Executar

### Pré-requisitos
```bash
# Instalar MongoDB
# Instalar Neo4j Desktop ou Neo4j Community Edition

# Instalar dependências Python
pip install pymongo neo4j bson
```

### Configuração dos Bancos

#### MongoDB
```bash
# Iniciar MongoDB (padrão: localhost:27017)
mongod

# Verificar conexão
mongo
```

#### Neo4j
```bash
# Configurar instância Neo4j
# URI padrão: bolt://localhost:7687
# Usuário: neo4j
# Senha: (configurar durante instalação)
```

### Execução dos Projetos

#### Simulação de Sensores
```bash
cd Project_SensorSimulation
python main.py
```

#### Sistema SCM
```bash
cd ProjectSCM
python main.py
```

#### Exercícios Específicos
```bash
cd exercicio_Zoologico
python main.py

cd FamilyTime
python main.py

# E assim por diante para outros exercícios
```
