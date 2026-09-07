# Calculadora Python DevOps

Projeto acadêmico desenvolvido em Python para demonstrar práticas de Git, CI/CD, testes automatizados e Docker.

## Funcionalidades

- Adição
- Subtração
- Multiplicação
- Divisão
- Potenciação
- Porcentagem
- Tratamento de divisão por zero

## Executar localmente

```bash
python main.py
```

## Executar testes

```bash
pip install -r requirements.txt
pytest -q
```

## Executar com Docker

Construir a imagem:

```bash
docker build -t calculadora-python-devops .
```

Executar o container:

```bash
docker run -it --name calculadora-python-devops calculadora-python-devops
```

Verificar containers:

```bash
docker ps
```

## CI/CD

O projeto possui workflows do GitHub Actions para execução automatizada dos testes em pushes e Pull Requests e validação no branch `main`.

## Objetivo acadêmico

Este projeto foi desenvolvido para demonstrar práticas de versionamento,
integração contínua, entrega contínua e conteinerização com Docker.
