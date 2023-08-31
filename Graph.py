'''''
---Informacion General---
Inteligencia Artificial Proyecto 2ndo Parcial
Universidad Panamericana
Inteligencia Artificial
Equipo: Alex Romero Mitiaeva, Angel Esqueda Ochoa, Leonardo Kenji Minemura Suazo
Fecha de entrega: 26/04/23
Ver 2

Este codigo contiene el Grafo de mexico 

-Pasos a Seguir para Ejecutar el Codigo-
importar el archivo cuando se requiera
'''''

mexDirectedGraph = {
    'Cancun':{'Valladolid':90,'Felipe Carrillo Puerto':100},
    'Valladolid':{'Felipe Carrillo Puerto':90},
    'Felipe Carrillo Puerto':{'Campeche':60},
    'Campeche':{'Ciudad del Carmen':90, 'Merida':90, 'Chetumal':100},
    'Merida':{},
    'Chetumal':{'Francisco Escarcega':110},
    'Francisco Escarcega':{},
    'Ciudad del Carmen':{'Villa Hermosa':90, 'Tuxtla':90},
    'Villa Hermosa':{'Acayucan':90},
    'Tuxtla':{'Acayucan':90},
    'Acayucan':{'Alvarado':110,'Tehuantepec':80},
    'Tehuantepec':{},
    'Alvarado':{'Oaxaca':100},
    'Oaxaca':{'Puerto Angel':90,'Tehuacan':80,'Izucar de Matamoros':90},
    'Tehuacan':{},
    'Puerto Angel':{'Pinotepa Nacional':100},
    'Pinotepa Nacional':{'Acapulco':100},
    'Acapulco':{'Chilpancingo':140},
    'Chilpancingo':{'Iguala':90},
    'Izucar de Matamoros':{'Puebla':90,'Cuernavaca':100},
    'Puebla':{'Cordoba':80,'Ciudad de Mexico':90},
    'Cordoba':{'Veracruz':90,},
    'Veracruz':{},  
    'Iguala':{'Cuernavaca':100,'Ciudad Altamirano':110},
    'Ciudad Altamirano':{'Zihuatanejo':90,'Toluca de Lerdo':100, 'Cuernavaca': 100},
    'Cuernavaca':{'Ciudad de Mexico':100},
    'Toluca de Lerdo':{'Ciudad de Mexico':110},
    'Ciudad de Mexico':{'Tlaxcala':100,'Pachuca de Soto':100,'Queretaro':90},    
    'Pachuca de Soto':{'Tuxpan de Rodriguez Cano':110},
    'Tuxpan de Rodriguez Cano':{'Tampico':80},
    'Tlaxcala':{},
    'Queretaro':{'San Luis Potosi':90,'Atlacomulco':90,'Salamanca':90},
    'Atlacomulco':{},
    'Salamanca':{'Guanajuato':90,'Guadalajara':90},
    'Guanajuato':{'Aguascalientes':80},
    'Morelia':{'Colima':90,'Salamanca':90},
    'Colima':{'Guadalajara':50},   
    'Zihuatanejo':{'Playa Azul':100},
    'Playa Azul':{'Manzanillo':100,'Morelia':100,'Colima':100},
    'Manzanillo':{'Colima':100,'Guadalajara':80},
    'Guadalajara':{'Tepic':110,'Aguascalientes':70},
    'Aguascalientes':{'San Luis Potosi':100},
    'San Luis Potosi':{'Zacatecas':90,'Durango':70},
    'Zacatecas':{},
    'Durango':{'Hidalgo del Parral':90},
    'Tepic':{'Mazatlan':110},
    'Mazatlan':{'Durango':90,'Culiacan':90},
    'Tampico':{'Ciudad Victoria':80},
    'Ciudad Victoria':{'Durango':80,'Soto la Marina':80,'Matamoros':80,'Monterrey':80},
    'Soto la Marina':{},
    'Matamoros':{'Reynosa':90},
    'Monterrey':{'Monclova':70,'Nuevo Laredo':110},
    'Reynosa':{'Nuevo Laredo':100},
    'Nuevo Laredo':{'Piedras Negras':100},
    'Piedras Negras':{'Monclova':100},
    'Monclova':{'Torreon':110,'Ojinaga':140},
    'Torreon':{'Durango':110},
    'Culiacan':{'Topolobampo':110,},
    'Hidalgo del Parral':{'Topolobampo':110,'Culiacan':80,'Chihuahua':130},
    'Chihuahua':{'Janos':90,'Ciudad Juarez':90},
    'Ojinaga':{'Chihuahua':90},
    'Ciudad Juarez':{},
    'Janos':{'Agua Prieta':110},
    'Agua Prieta':{'Santa Ana':60},
    'Santa Ana':{'Mexicalli':150},
    'Hermosillo':{'Santa Ana':60},
    'Guaymas':{'Hermosillo':80},
    'Ciudad Obregon':{'Guaymas':80},
    'Topolobampo':{'Ciudad Obregon':90},
    'Mexicalli':{'Tijuana':110,'San Felipe':70},
    'San Felipe':{'Ensenada':50},
    'Tijuana':{'Ensenada':50},
    'Ensenada':{'San Quintin':60},
    'San Quintin':{'Santa Rosalia':60},
    'Santa Rosalia':{'Santo Domingo':60},
    'Santo Domingo':{'La Paz':70},
    'La Paz':{'Cabo San Lucas':70},
    'Cabo San Lucas':{}
}