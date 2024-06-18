import boto3

# AWS servis ismi (Amazon Alexa için "alexaforbusiness" kullanılır)
service_name = 'alexaforbusiness'

# AWS API client'ını oluşturma
client = boto3.client(service_name,
                      region_name='us-east-1',  # AWS bölge kodu
                      aws_access_key_id='your_access_key_id',
                      aws_secret_access_key='your_secret_access_key')

# API çağrıları burada yapılır, örnek olarak list_devices çağrısı:
response = client.list_devices()

# Yanıtı yazdırma
print(response)
