# config.py

class Config(object):
    embed_size = 100
    hidden_layers = 2
    hidden_size = 32
    bidirectional = True
    output_size = 2
    max_epochs = 10 #10
    lr = 0.25
    batch_size = 64
    max_sen_len = 20 # Sequence length for RNN
    dropout_keep = 0.8