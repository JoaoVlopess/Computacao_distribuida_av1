from pathlib import Path

import matplotlib.pyplot as plt


def garantir_pasta(pasta):
    """
    Cria a pasta caso ela ainda não exista.
    """

    Path(pasta).mkdir(
        parents=True,
        exist_ok=True
    )


def grafico_analitico_por_caso(
    df,
    caso,
    pasta_saida
):
    """
    Gera gráfico de:

    p x disponibilidade analítica

    para diferentes valores de n.
    """

    garantir_pasta(pasta_saida)

    dados = df[df["caso"] == caso]

    plt.figure(figsize=(10, 6))

    for n in sorted(dados["n"].unique()):

        subconjunto = dados[
            dados["n"] == n
        ]

        plt.plot(
            subconjunto["p"],
            subconjunto["disponibilidade_analitica"],
            marker="o",
            markersize=3,
            label=f"n = {n}"
        )

    plt.xlabel("Probabilidade de disponibilidade do servidor (p)")
    plt.ylabel("Disponibilidade do serviço")
    plt.title(
        f"Disponibilidade analítica - {caso}"
    )

    plt.ylim(0, 1.05)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    nome = (
        caso
        .replace(" ", "_")
        .replace("=", "")
        .replace("/", "_")
    )

    caminho = Path(pasta_saida) / f"analitico_{nome}.png"

    plt.savefig(
        caminho,
        dpi=300
    )

    plt.close()


def grafico_comparacao(
    df,
    caso,
    pasta_saida
):
    """
    Compara valores analíticos e experimentais.
    """

    garantir_pasta(pasta_saida)

    dados = df[df["caso"] == caso]

    plt.figure(figsize=(11, 7))

    for n in sorted(dados["n"].unique()):

        subconjunto = dados[
            dados["n"] == n
        ]

        # Valor analítico
        plt.plot(
            subconjunto["p"],
            subconjunto["disponibilidade_analitica"],
            label=f"Analítico - n={n}"
        )

        # Valor experimental
        plt.scatter(
            subconjunto["p"],
            subconjunto["disponibilidade_experimental"],
            s=15,
            label=f"Simulação - n={n}"
        )

    plt.xlabel("Probabilidade de disponibilidade do servidor (p)")
    plt.ylabel("Disponibilidade do serviço")

    plt.title(
        f"Analítico x Simulação - {caso}"
    )

    plt.ylim(0, 1.05)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    nome = (
        caso
        .replace(" ", "_")
        .replace("=", "")
        .replace("/", "_")
    )

    caminho = (
        Path(pasta_saida)
        / f"comparacao_{nome}.png"
    )

    plt.savefig(
        caminho,
        dpi=300
    )

    plt.close()


def grafico_erro(
    df,
    pasta_saida
):
    """
    Mostra o erro absoluto entre o resultado matemático
    e o resultado obtido pela simulação.
    """

    garantir_pasta(pasta_saida)

    erro_medio = (
        df.groupby("caso")["erro_absoluto"]
        .mean()
    )

    plt.figure(figsize=(8, 5))

    plt.bar(
        erro_medio.index,
        erro_medio.values
    )

    plt.xlabel("Caso")
    plt.ylabel("Erro absoluto médio")
    plt.title(
        "Erro médio entre solução analítica e simulação"
    )

    plt.grid(
        True,
        axis="y"
    )

    plt.tight_layout()

    caminho = (
        Path(pasta_saida)
        / "erro_medio_simulacao.png"
    )

    plt.savefig(
        caminho,
        dpi=300
    )

    plt.close()