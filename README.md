# An LLM-Powered Virtual Assistant for Software Navigation and Explainability in the Oil Industry
This is a repository which contains the supplementary material for the article.
Aside from this README.md, in this repository you'll find the [prompt templates](Prompts.md) used to construct the prompts sent to the generative models.

Additionally, a video demonstrating the virtual assistant's interface inside the software, showing the chat window and action suggestion feature, can be seen below:

https://github.com/user-attachments/assets/7f829737-d507-4154-b8e1-63ce576bd182

## Experimental Setup

Specifics:
 - Ubuntu 24.04.2 LTS
 - NVIDIA RTX A6000 GPU (48GB)
 - CUDA 12.4
 - Python 3.12.3

This work uses the SentenceTransformer class from the SentenceTransformers library [[1]](#1) for loading the chunk and query encoders and CrossEncoder for reranker models.
Database vector retrieval uses FAISS [[2]](#2), which quickly retrieves the $k$-closest items due to algorithms being executed on the GPU.
Lastly, the transformers library [[3]](#3) was used to load the models.

## References
<a id="1">[1]</a> 
[Reimers, Nils and Gurevych, Iryna (2019). 
"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks"
Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing, 11.](https://arxiv.org/abs/1908.10084)
  
<a id="2">[2]</a> 
[Johnson, Jeff and Douze, Matthijs and Jégou, Hervé (2021).
"Billion-Scale Similarity Search with GPUs"
IEEE Transactions on Big Data, 7(3). 535-547.](10.1109/TBDATA.2019.2921572)

<a id="3">[3]</a> 
[Thomas Wolf and Lysandre Debut and Victor Sanh and Julien Chaumond and Clement Delangue and Anthony Moi and Pierric Cistac and Tim Rault and Rémi Louf and Morgan Funtowicz and Joe Davison and Sam Shleifer and Patrick von Platen and Clara Ma and Yacine Jernite and Julien Plu and Canwen Xu and Teven Le Scao and Sylvain Gugger and Mariama Drame and Quentin Lhoest and Alexander M. Rush (2020),
"Transformers: State-of-the-Art Natural Language Processing"
Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations, 38-45](https://www.aclweb.org/anthology/2020.emnlp-demos.6)
