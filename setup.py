from setuptools import setup, find_packages

setup(
    name='meu_pacote_imagem',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
    description='Um pacote simples para processamento de imagens',
    author='Rodrigo de Oliveira Silva',
    author_email='rodrigoolive98@hotmail.com',
    url='https://github.com/panpan-del/meu_pacote_imagem.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
