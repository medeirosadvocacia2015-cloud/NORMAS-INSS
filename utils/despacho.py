def gerar_despacho(tipo, termo, artigo, resultados):
    fundamentacao = ""
    for resultado in resultados:
        for trecho in resultado["trechos"]:
            fundamentacao += f"- {trecho}\n"

    if tipo == "deferimento":
        texto = (
            "Despacho de Deferimento\n\n"
            f"Após análise do requerimento e considerando as disposições legais pertinentes, em especial:\n"
            f"{fundamentacao}\n"
            "DEFIRO o pedido, por estarem presentes os requisitos legais.\n"
            "Publique-se. Cumpra-se."
        )
    else:
        texto = (
            "Despacho de Indeferimento\n\n"
            f"Após análise do requerimento e considerando as disposições legais pertinentes, em especial:\n"
            f"{fundamentacao}\n"
            "INDEFIRO o pedido, por ausência dos requisitos legais.\n"
            "Publique-se. Cumpra-se."
        )
    return texto
