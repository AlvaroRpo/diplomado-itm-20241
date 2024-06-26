import boto3

#crear cliente para dynamodb
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

tabla = dynamodb.Table('tabla-alvaro-restrepo')

#leer un elemento de la tabla
response = tabla.get_item(Key={'id': '2'})

print(response['Item'])

#leer todos los elementos de la tabla
response = tabla.scan()

#print(response['Items'])

nuevo_item = {
    'id': '3',
    'nombre': 'Alvaro Restrepo',
    'edad': 30,
    'ciudad': 'Bogotá'
}

response = tabla.put_item(Item=nuevo_item)

#print(f'El ítem fue agregado exitosamente: {response}')

response = tabla.update_item(
        Key={
            'id': '3'
        },
        UpdateExpression='SET edad = :val1',
        ExpressionAttributeValues={
            ':val1': 31
        }
    )