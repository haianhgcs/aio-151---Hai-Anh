import sys
sys.path.append("..")

if __name__ == "__main__":
    from util import transformer_util as tuti

    # Test
    seq_length = 10
    embed_size = 16
    position_matrix = tuti.create_position_matrix(
        seq_length=seq_length, embed_size=embed_size)
    print(position_matrix)
