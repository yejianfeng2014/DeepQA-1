原始的的地址
https://github.com/Conchylicultor/DeepQA


https://colab.research.google.com/drive/1g3cf9T1zyXk53BjNy_UTy7dbfnnTtEoV#scrollTo=Cj8ClQMO_AyV
!python --version  这个来自google 最新使用的python 3.6.7

tensorflow 已经更新到1.13.1 print(tf.__version__)

https://blog.csdn.net/ppp8300885/article/details/74905828  这个博客仔细讲解了核心部分  添加了beamsearch 



## 安装

`pip3 install -r requirements.txt`):
 * python 3.5
 * tensorflow (tested with v1.0)
 * numpy
 * CUDA (for using GPU) 
 * nltk (natural language toolkit for tokenized the sentences)
 * tqdm (for the nice progression bars)



```
python3 -m nltk.downloader punkt   这个是必须的，在window 不运行就直接报错
```

## web 模块需要安装的内容

channels=1.1.6
django==1.10.7
asgi-redis==1.4.3

redis 需要单独安装然后启动




### Chatbot

main.py 训练模型
main.py --test 这个使用的预训练模型，

main.py --test interactive 采用的是实时对话的模式

python main.py -h 运行帮助模块

    --modelTag <name>: 指定模型名称进行运行
    --keepAll  训练完立刻进行测试
    

10个单词的上限 ，隐藏层256

### web 模块


复制 训练好的模型  到 `save/model-server/model.ckpt`.(如果没有model-sever 的路径进行创建)

使用这个web框架，第一次需要按照如下配置
```bash
export CHATBOT_SECRET_KEY="my-secret-key" 在window 环境换成 set  CHATBOT_SECRET_KEY="my-secret-key"
cd chatbot_website/
python manage.py makemigrations
python manage.py migrate
```

需要配置 

安装redis 
# 自己电脑安装的redise 的地址 

D:\Program Files\Redis



```bash
cd chatbot_website/
redis-server &  # Launch Redis in background
python manage.py runserver
```

http://localhost:8000/ 进行访问 



以下是测试过程的   

python main.py --test interactive 这个测试通过

python main.py --test interactive --modelTag opensubs 这个未通过

# 使用tensorflow 1.3版本测试

python main.py --test  --modelTag opensubs 这个通过了
python main.py --test  --modelTag ubuntu-tf1.3 这个通过
python main.py --test  --modelTag cornell-tf1.3 未通过




####  python main.py


TensorFlow detected: v1.10.0
configName D:\python_workspace\DeepQA\save\model\params.ini   # 配置文件地址

Warning: Restoring parameters:
globStep: 25519
watsonMode: False
autoEncode: False
corpus: cornell    语料
datasetTag:
maxLength: 10
filterVocab: 1
skipLines: False
vocabularySize: 40000  字典大小40000
hiddenSize: 512
numLayers: 2
softmaxSamples: 0
initEmbeddings: False
embeddingSize: 64
embeddingSource: GoogleNews-vectors-negative300.bin  

Loading dataset from D:\python_workspace\DeepQA\data\samples\dataset-cornell-length10-filter1-vocabSize40000.pkl
Loaded cornell: 24635 words, 159661 QA
Model creation...
2019-03-15 16:45:13.220056: W tensorflow/python/util/util.cc:159] Sets are not currently considered sequences, but this may change in the future, so consider avoiding u
sing them.
2019-03-15 16:45:20.851581: I tensorflow/core/common_runtime/process_util.cc:69] Creating new thread pool with default inter op setting: 4. Tune using inter_op_parallel
ism_threads for best performance.
Initialize variables...
WARNING: Restoring previous model from D:\python_workspace\DeepQA\save\model\model.ckpt
Start training (press Ctrl+C to save and exit)...





kaggle competitions download -c quora-insincere-questions-classification

#由于本地的电脑系统太烂，tensorflow 根本跑不起来，所以在google 平台上跑代码。


2019-9-2 把数据格式转成 电影对话的数据格式，然后直接跑起来看看。






