import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv

class GnnModel(torch.nn.Module):
    def __init__(self, inChannels, hiddenChannels, outChannels):
        super(GnnModel, self).__init__()
        self.conv1 = GCNConv(inChannels, hiddenChannels)
        self.conv2 = GCNConv(hiddenChannels, outChannels)

    def forward(self, data):
        x, edgeIndex = data.x, data.edge_index
        x = self.conv1(x, edgeIndex)
        x = F.relu(x)
        x = self.conv2(x, edgeIndex)
        return F.log_softmax(x, dim=1)
        