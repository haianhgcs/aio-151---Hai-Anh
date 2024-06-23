import torch
import torch.nn as nn


class SoftmaxStable(nn.Module):
    """
    Softmax class inherit torch.nn.Module
    """

    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def softmax_stable(self, x):
        """
        Calculating Softmax stable.

        Parameter:
        x (torch.Tensor): Tensor 1D.

        Return:
        torch.Tensor: Tensor after calculating Softmax.
        """
        # Minute to the max value in tensor x to avoid overflow
        max_x = torch.max(x)
        exp_x = torch.exp(x - max_x)
        sum_exp_x = torch.sum(exp_x)
        return exp_x / sum_exp_x

    def forward(self, x):
        """
        Override forward().

        Parameter:
        x (torch.Tensor): Tensor input.

        Return:
        torch.Tensor: Tensor after calculating Softmax.
        """
        return self.softmax_stable(x)
