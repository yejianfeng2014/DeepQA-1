# Copyright 2015 Conchylicultor. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import os

"""
Load data from a dataset of simply-formatted data

from A to B
from B to A
from A to B
from B to A
from A to B
===
from C to D
from D to C
from C to D
from D to C
from C to D
from D to C
...

`===` lines just separate linear conversations between 2 people.

"""

"""
最终的数据格式是这样的  

每一行都是一个person的语句，下一行是下一个人的回复。实际只有内容没有from  to 也没有A B 等

"""


class LightweightData:
    """
    """

    def __init__(self, lightweightFile):
        """
        Args:
            lightweightFile (string): file containing our lightweight-formatted corpus
        """
        self.CONVERSATION_SEP = "==="
        self.conversations = []
        self.loadLines(lightweightFile + '.txt')

    def loadLines(self, fileName):
        """
        Args:
            fileName (str): file to load
        """

        linesBuffer = []
        with open(fileName, 'r') as f:
            for line in f:
                l = line.strip()
                if l == self.CONVERSATION_SEP:
                    self.conversations.append({"lines": linesBuffer})
                    linesBuffer = []
                else:
                    linesBuffer.append({"text": l})
            if len(linesBuffer):  # Eventually flush the last conversation
                self.conversations.append({"lines": linesBuffer})

    def getConversations(self):
        return self.conversations
# 临时注释掉，否则会直接运行这个文件。。。。。。
# myfile = 'D:/python_workspace/DeepQA-1/data/lightweight/mydata'
#
# mydata = LightweightData(myfile)
#
# conversations = mydata.getConversations()
#
#
# print(">>>>>")

# mydata.loadLines()

