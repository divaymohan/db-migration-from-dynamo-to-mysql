import boto3
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
import uuid

Base = declarative_base()

class ConfigEntity(Base):
    __tablename__ = 'config'

    id = Column(String(256), primary_key=True)
    body_type = Column(String(256), default=None)
    body_wrapper = Column(String(256), default=None)
    category = Column(String(256), default=None)
    credit_free = Column(String(256), default=None)
    method = Column(String(256), default=None)
    request_type = Column(String(256), default=None)
    url = Column(String(256), default=None)
    created_at = Column(DateTime, default=datetime.utcnow)
    modified_at = Column(DateTime, onupdate=datetime.utcnow)

    def __init__(self, id, bodyType, bodyWrapper, category, creditFree, method, type, url, crDt, modDt):
        self.id = id
        self.body_type = bodyType
        self.body_wrapper = bodyWrapper
        self.category = category
        self.credit_free = creditFree
        self.method = method
        self.request_type = type
        self.url = url
        self.created_at = crDt
        self.modified_at = modDt

class KeyValueEntity(Base):
    __tablename__ = 'keyValues'

    id = Column(String(256), primary_key=True)
    config_id = Column(String(256))
    doc_type = Column(String(256))
    name = Column(String(100))
    type = Column(String(255), default=None)
    value = Column(String(255), default=None)
    

    def __init__(self, id, config_id, doc_type, name, type, value):
        self.id = id
        self.config_id = config_id
        self.doc_type = doc_type
        self.name = name
        self.type = type
        self.value = value

class configDTO:
    def __init__(self, id, bodyType, bodyWrapper, formData, formUrlEncoded, headers, jsonBody, queryParams,
                 category, creditFree, method, type, url, crDt, modDt):
        self.id = id
        self.bodyType = bodyType
        self.bodyWrapper = bodyWrapper
        self.formData = formData
        self.formUrlEncoded = formUrlEncoded
        self.headers = headers
        self.jsonBody = jsonBody
        self.queryParams = queryParams
        self.category = category
        self.creditFree = creditFree
        self.method = method
        self.type = type
        self.url = url
        self.crDt = crDt
        self.modDt = modDt
        
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            bodyType=data.get('bodyType'),
            bodyWrapper=data.get('bodyWrapper'),
            formData=data.get('formData'),
            formUrlEncoded=data.get('formUrlEncoded'),
            headers=data.get('headers'),
            jsonBody=data.get('jsonBody'),
            queryParams=data.get('queryParams'),
            category=data.get('category'),
            creditFree=data.get('creditFree'),
            method=data.get('method'),
            type=data.get('type'),
            url=data.get('url'),
            crDt=data.get('crDt'),
            modDt=data.get('modDt')
        )
    
    def __str__(self):
        return f"RequestDTO(id={self.id}, body_type={self.bodyType}, body_wrapper={self.bodyWrapper}, " \
               f"form_data={self.formData}, form_url_encoded={self.formUrlEncoded}, headers={self.headers}, " \
               f"json_body={self.jsonBody}, query_params={self.queryParams}, category={self.category}, " \
               f"is_credit_free={self.creditFree}, method={self.method}, request_type={self.type}, " \
               f"url={self.url}, created_at={self.crDt}, updated_at={self.modDt})"




# DynamoDB
dynamodb = boto3.resource('dynamodb')
dynamodb_table_name = 'dynamo-db-table'
dynamodb_table = dynamodb.Table(dynamodb_table_name)
# RDS
rds_connection_string = 'mysql://username:passowrd@host:port/db_name'
engine = create_engine(rds_connection_string)
Base = declarative_base()
Session = sessionmaker(bind=engine)

def get_data_from_dynamodb():
    response = dynamodb_table.scan()
    return response['Items']

def convert_to_dtos(data):
    dto_ls = []
   
    for d in data:
        dto = configDTO.from_dict(data=d)
        dto_ls.append(dto)
        
    return dto_ls

def checkKey(dic, key):
     
    if key in dic:
        return dic[key]
    else:
        return None

def conver_to_config_list(data):
    config_entity_list = []
    key_value_list = []
    for d in data:
        print(d)
        config_entity_list.append(ConfigEntity(id=d.id, bodyType=d.bodyType, bodyWrapper=d.bodyWrapper, 
                                               category=d.category, creditFree=d.creditFree, method=d.method, 
                                               type=d.type, url=d.url, crDt=d.crDt, modDt=d.modDt))
        
        if d.formData is not None:
            for item in d.formData:
                
                key_value_list.append(KeyValueEntity(id=uuid.uuid4(),
                                                config_id=d.id,
                                                doc_type="formData",
                                                name=checkKey(item, 'name'),
                                                type=checkKey(item, 'type'),
                                                value=checkKey(item, 'value')
                                                ))
            
       
        if d.formUrlEncoded is not None:
            for item in d.formUrlEncoded:
                key_value_list.append(KeyValueEntity(id=uuid.uuid4(),
                                                    config_id=d.id,
                                                    doc_type="formUrlEncoded",
                                                    name=checkKey(item, 'name'),
                                                    type=checkKey(item, 'type'),
                                                    value=checkKey(item, 'value')
                                                    ))
        if d.jsonBody is not None:
            for item in d.jsonBody:
                key_value_list.append(KeyValueEntity(id=uuid.uuid4(),
                                                config_id=d.id,
                                                doc_type="jsonBody",
                                                name=checkKey(item, 'name'),
                                                type=checkKey(item, 'type'),
                                                value=checkKey(item, 'value')
                                                ))
        
        if d.headers is not None:
            for item in d.headers:
                key_value_list.append(KeyValueEntity(id=uuid.uuid4(),
                                                config_id=d.id,
                                                doc_type="headers",
                                                name=checkKey(item, 'name'),
                                                type=checkKey(item, 'type'),
                                                value=checkKey(item, 'value')
                                                ))
        if d.queryParams is not None:
            for item in d.queryParams:
                key_value_list.append(KeyValueEntity(id=uuid.uuid4(),
                                                config_id=d.id,
                                                doc_type="queryParams",
                                                name=checkKey(item, 'name'),
                                                type=checkKey(item, 'type'),
                                                value=checkKey(item, 'value')
                                                ))
    return config_entity_list, key_value_list



def put_data_into_rds(entities):
    session = Session()
    try:
        session.add_all(entities)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

if __name__ == "__main__":
    data_from_dynamodb = get_data_from_dynamodb()
    dto_list = convert_to_dtos(data_from_dynamodb)
    config_entity_list, key_value_entity_lists = conver_to_config_list(dto_list)
    put_data_into_rds(config_entity_list)
    put_data_into_rds(key_value_entity_lists)


