import boto3
from datetime import datetime
#Valores globales
PORCENTAJE = 97

def leer_informacion(archivo="info.txt"):
    info = open(archivo)
    lineas = []
    for linea in info:
        linea = linea.strip().split("=")
        lineas.append(linea)
    bucket = lineas[0][1].replace(" ","")
    img_control = lineas[1][1].replace(" ","")
    pruebas = lineas[2][1].split(",")
    p_clean = []
    for i in pruebas:
        p_clean.append(i.replace(" ",""))

    info.close()
    return bucket, img_control, p_clean
    
def detectar_texto(photo, bucket):
    client=boto3.client('rekognition')
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
    textDetections=response['TextDetections']

    detectadas = set()
    for text in textDetections:
        confidence = text['Confidence']
        if(confidence >= PORCENTAJE and text['Type']== 'WORD'):
            detectadas.add(text['DetectedText'].upper())
    return detectadas

def main():
    bucket, img_control, pruebas = leer_informacion()
    #bucket='pruebasdesoftware1'
    #photo='51-ok.png'
    log = open("log.txt","w")
    log.write("Imagen de control: "+ img_control +  "\n\n")
 
    palabras_control=detectar_texto(img_control,bucket)
    for p in pruebas:
        comparacion = ''
        palabras_p = detectar_texto(p,bucket)
        incercepcion = palabras_control & palabras_p
        if(len(incercepcion)== len(palabras_control)):
            comparacion = 'True'
        else:
            comparacion = 'False'
        time = datetime.now()
        log.write(str(time)+ " | "+ str(p)+ " -- "+ "Resultado: "+comparacion + "\n")
        print(p, palabras_p)
    
    log.close()
    #print(palabras_control)
    #print("Text detected: " + str(text_count))


if __name__ == "__main__":
    main()
