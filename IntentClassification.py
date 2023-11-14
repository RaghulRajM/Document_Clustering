import pandas as pd
import numpy as np
import spacy
from scipy import spatial
from sentence_transformers import SentenceTransformer

class IntentClassification():
    
    def __init__(self, intent_dict,threshold):
        self.intent_dict=intent_dict
        self.threshold=threshold

        
    def intent_mining(self, df,text_column,variable_dict):
        
        data=df.copy(deep=True)
        data[text_column].fillna('nan',inplace=True)
        data[text_column]=[i.lower() if(i!='nan') else 'nan' for i in data[text_column] ]
        model = SentenceTransformer('bert-base-nli-mean-tokens')
        sentence_embeddings = model.encode(data[text_column])
        intent_embeddings=dict.fromkeys(self.intent_dict.keys(),0)
        for key in self.intent_dict.keys():
            intent_embeddings[key]=model.encode(self.intent_dict[key])
        intent_score=dict.fromkeys(self.intent_dict.keys(),0)
        
        
        intent_emb=[]
        for text in range(len(data)):
            flag=0
            for i in variable_dict['user_columns']['kpi']:
                if(i in data.loc[text,text_column]):
                    intent_emb.append('kpi')
                    flag=1
            
            if(flag==0):
                for i in variable_dict['user_columns']['hierarchy']:
                    if(i in data.loc[text,text_column]):
                        intent_emb.append('hierarchy')
                        flag=1
                    
            if(flag==0):
                if('root cause' in data.loc[text,text_column]):
                    intent_emb.append('rc')
                else:
                    intent_score=dict.fromkeys(self.intent_dict.keys(),0)
                    for key in self.intent_dict.keys():
                        for emb in range(len(intent_embeddings[key])):
                            temp_score=1-spatial.distance.cosine(sentence_embeddings[text],intent_embeddings[key][emb])
                            if(temp_score>intent_score[key]):
                                intent_score[key]=temp_score
                    if(max(intent_score.values())>self.threshold):
                        intent_emb.append(max(intent_score, key=intent_score.get))
                    else:
                        intent_emb.append('other')
                
        data['intent_emb']=intent_emb
        return data