import torch
import torch.nn as nn


class Softmax(nn.Module):
    """
    Softmax class inherit torch.nn.Module
    """

    def __init__(self):
        super(Softmax, self).__init__()

    def softmax(self, x):
        """
        softmax calculation.

        Parameter:
        x (torch.Tensor): Tensor 1D.

        Return:
        torch.Tensor: Tensor after calculating softmax.
        """
        # Trừ giá trị lớn nhất trong tensor x để tránh overflow
        exp_x = torch.exp(x)
        sum_exp_x = torch.sum(exp_x)
        return exp_x / sum_exp_x

    def forward(self, x):
        """
        Override forward() method

        Parameter:
        x (torch.Tensor): Tensor input.

        Trả về:
        torch.Tensor: Tensor after calculating softmax.
        """
        return self.softmax(x)
