from typing import Union


def get_second_most_likely_fault(user_query: str, label: str, features: dict[str, float]):
    """
    Obtém a segunda classe de falha mais provável de um sinal com base em todas as 8 features de entrada.
    Args:
        user_query (str): Pergunta do usuário para contextualizar a resposta final.
        label (str): Classe de falha original do sinal, fornecida para contexto.
        features (dict[str, float]): Dicionário com nomes das features como chaves e valores float.
            Chaves OBRIGATÓRIAS esperadas:
                - "a"
                - "b"
                - "real_rotation_hz"
                - "peak1x"
                - "peak2x"
                - "rms(freq-1,freq+1)"
                - "median(freq-1,freq+1)"
                - "median(3,5)"
    """
    pass


def predict_with_some_features(user_query: str, label: str, features: dict[str, float], omitted_features: list[str]):
    """
    Executa a classificação e identifica o tipo de falha mais provável de um sinal, permitindo realizar a análise com alguma feature intencionalmente desconsiderada.
    As features representam aspectos específicos do espectro do sinal:
    - 'median(3,5)': nível de ruído em torno de 3Hz e 5Hz;
    - 'a' e 'b': comportamento da curva entre 5Hz e 19Hz;\n
    - 'peak1x': amplitude do pico na primeira harmônica;\n
    - 'median(freq-1,freq+1)': ruído ao redor da primeira harmônica;\n
    - 'rms(freq-1,freq+1)': visibilidade do pico na primeira harmônica;\n
    - 'peak2x': amplitude do pico na segunda harmônica;\n
    - 'real_rotation_hz': rotação real do equipamento em Hz.\n\n

    Args:
        user_query (str): Pergunta original do usuário para contextualizar a resposta final.
        label (str): Classe de falha original do sinal, fornecida para contexto.
        features (dict[str, float]): Dicionário com nomes das features como chaves e valores float.
            Chaves OBRIGATÓRIAS esperadas:
                - "a"
                - "b"
                - "real_rotation_hz"
                - "peak1x"
                - "peak2x"
                - "rms(freq-1,freq+1)"
                - "median(freq-1,freq+1)"
                - "median(3,5)"
        omitted_features (list[str]): Lista com os nomes das features que devem ser omitidas na análise. Por exemplo: ['a', 'b'], para desconsiderar o comportamento da curva entre 5Hz e 19Hz no treinamento e análise.
    """
    pass


def find_similar_signals_tool(
    features: dict[str, float],
    num_examples: Union[int, None] = None,
    fault_class: Union[str, None] = None,
    subset_features: Union[list[str], None] = None,
):
    """
    Obtém os sinais mais semelhantes ao fornecido com base na distância euclidiana normalizada entre as features.
    Args:
        features (dict[str, float]): Dicionário com nomes das features como chaves e valores float.
            Chaves OBRIGATÓRIAS esperadas:
                - "a"
                - "b"
                - "real_rotation_hz"
                - "peak1x"
                - "peak2x"
                - "rms(freq-1,freq+1)"
                - "median(freq-1,freq+1)"
                - "median(3,5)"
        num_examples (int, optional): Número de sinais semelhantes a serem retornados.
        fault_class (str, optional): Classe de falha para filtrar os sinais. Se não for fornecida, sinais de todas as classes são incluídos na pesquisa.
               Valores válidos: 'Normal', 'Roçamento', 'Desalinhamento', 'Desbalanceamento', 'Falha de sensor'.
        subset_features (list[str], optional): Lista de features a serem consideradas para o cálculo de similaridade. Se não for fornecida, todas as features são usadas no cálculo de similaridade.
    """
    pass
