__author__ = 'shenoisz'


def get_object_list( args ):
    csv = open( str( args ) , 'r')
    lines = [ ]
    for divier in csv.readlines( ):
        fatias = divier.replace('\n', '').split('|')
        lines.append( fatias )
    csv.close( )
    return lines

def get_object_dict( args ):

    csv = open( str( args ) , 'r')
    lines = [ ]

    for divier in csv.readlines( ):

        fatias = divier.replace('\n', '').split('|')

        lines.append( {
            'embed': fatias[0].replace('608','100%').replace('338','550'),
            'url': fatias[1],
            'imagem': fatias[2],
            'flipboard': fatias[3],
            'titulo': fatias[4],
            'tags': fatias[5],
            'duracao': fatias[6],
            'views': fatias[7],
            'qtdavaliacoes': fatias[8],
            'totalavaliacoes': fatias[9],
            'avaliacao': fatias[10],
        } )
    csv.close( )
    return lines
    
