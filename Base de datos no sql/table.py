import boto3

# Crear cliente para DynamoDB
dynamodb_client = boto3.client('dynamodb', region_name='us-east-1')

# Crear la tabla
response = dynamodb_client.create_table(
    TableName='tabla-alvaro-restrepo-z',
    KeySchema=[{
        'AttributeName':'id',
        'KeyType':'HASH'
    }],
    AttributeDefinitions=[{
        'AttributeName': 'id',
        'AttributeType': 'S'
    }],
    BillingMode='PAY_PER_REQUEST'  # Capacidad bajo demanda
)

# Esperar hasta que la tabla exista
waiter = dynamodb_client.get_waiter('table_exists')
waiter.wait(TableName='tabla-alvaro-restrepo-z')

print(f'Tabla tabla-alvaro-restrepo-z creada exitosamente con capacidad bajo demanda.')


#para borrar la tabla
# response = dynamodb_client.delete_table(TableName='tabla-alvaro-restrepo-z')