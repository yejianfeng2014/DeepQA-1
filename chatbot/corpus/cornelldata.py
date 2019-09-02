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
import ast

"""
Load the cornell movie dialog corpus.

Available from here:
http://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html

"""

class CornellData:
    """

    """

    def __init__(self, dirName):
        """
        Args:
            dirName (string): directory where to load the corpus
        """
        self.lines = {}
        self.conversations = []

        MOVIE_LINES_FIELDS = ["lineID","characterID","movieID","character","text"]

        MOVIE_CONVERSATIONS_FIELDS = ["character1ID","character2ID","movieID","utteranceIDs"]

        #获取聊天内容
        self.lines = self.loadLines(os.path.join(dirName, "movie_lines.txt"), MOVIE_LINES_FIELDS)
        # 构建对话
        self.conversations = self.loadConversations(os.path.join(dirName, "movie_conversations.txt"), MOVIE_CONVERSATIONS_FIELDS)

        # TODO: Cleaner program (merge copy-paste) !!

    def loadLines(self, fileName, fields):
        """
        Args:
            fileName (str): file to load
            field (set<str>): fields to extract
        Return:
            dict<dict<str>>: the extracted fields for each line
        """

        # 抽取所有的行数据
        lines = {}

        with open(fileName, 'r', encoding='iso-8859-1') as f:  # TODO: Solve Iso encoding pb !
            for line in f:
                # 按照指定符号分割
                values = line.split(" +++$+++ ")

                # Extract fields
                lineObj = {}
                for i, field in enumerate(fields):
                    lineObj[field] = values[i]

                lines[lineObj['lineID']] = lineObj

        return lines

    def loadConversations(self, fileName, fields):
        """
        Args:
            fileName (str): file to load
            field (set<str>): fields to extract
        Return:
            dict<dict<str>>: the extracted fields for each line
        """

        # 构建对话并且返回对话
        conversations = []

        with open(fileName, 'r', encoding='iso-8859-1') as f:  # TODO: Solve Iso encoding pb !
            for line in f:
                values = line.split(" +++$+++ ")

                # Extract fields 抽取属性
                convObj = {}
                for i, field in enumerate(fields):
                    convObj[field] = values[i]

                # Convert string to list (convObj["utteranceIDs"] == "['L598485', 'L598486', ...]")
                # 转换字符串到list 对象
                lineIds = ast.literal_eval(convObj["utteranceIDs"])

                # Reassemble lines
                convObj["lines"] = []
                for lineId in lineIds:
                    convObj["lines"].append(self.lines[lineId])

                conversations.append(convObj)

        return conversations

    def getConversations(self):
        return self.conversations
