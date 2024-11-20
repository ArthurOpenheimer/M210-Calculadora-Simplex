### README.md

# Calculadora Simplex

## Descrição
A **Calculadora Simplex** é uma aplicação desenvolvida em Python utilizando a biblioteca **Streamlit**. O objetivo principal do projeto é resolver problemas de programação linear por meio do método Simplex. A aplicação permite configurar a função objetivo, restrições, e realizar ajustes interativos para visualizar os impactos no resultado.

## Funcionalidades
- Entrada de dados para a **função objetivo** e **restrições**.
- Propor alterações nas restrições com verificação de viabilidade.
- Exibição de:
  - Solução ótima (valores das variáveis de decisão).
  - Lucro ótimo (Z).
  - Preços sombra das restrições.
- Suporte a valores numéricos com até 4 casas decimais.


## Estrutura do Projeto
```plaintext
Calculadora-Simplex/
├── main.py                 # Código principal da aplicação Streamlit
├── programacao_linear.py   # Lógica para resolver o problema Simplex
├── README.md               # Documentação do projeto
├── .gitignore              # Arquivos e pastas ignorados no versionamento
```

## Tecnologias Utilizadas
- **Python 3.8+**
- **Streamlit**: Framework para criar interfaces web interativas.
- **Pulp**: Biblioteca para modelagem e resolução de problemas de programação linear.

## Pré-requisitos
Certifique-se de ter os seguintes softwares instalados:
- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)

Instale as dependências do projeto executando:
> ```bash
> pip install streamlit pulp
> ```

## Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/calculadora-simplex.git
   cd calculadora-simplex
   ```

2. Execute a aplicação:
   ```bash
   streamlit run main.py
   ```

3. Acesse a aplicação no navegador:
   ```
   http://localhost:8501
   ```

## Como Usar
1. **Entrada de Dados**:
   - Insira o número de variáveis e restrições na barra lateral.
   - Preencha os coeficientes da função objetivo e das restrições.
   - Clique em **Calcular Solução** para visualizar os resultados.

2. **Propor Alterações**:
   - Utilize o menu "Propor Alterações" para ajustar os limites das restrições.
   - Verifique a viabilidade das alterações clicando em **Verificar Viabilidade**.
   - Se as alterações forem viáveis, visualize o novo lucro ótimo (Z).


## Autor
Desenvolvido por **[Arthur](https://github.com/ArthurOpenheimer)**, **[Virginia](https://github.com/VLAfonso)** e **[Lucas](https://github.com/LucasLimaGadbem)**.

---
