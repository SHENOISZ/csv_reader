__author__ = 'shenoisz'

from csv_reader.funcs import get_object_list, get_object_dict
import os

PATH = os.path.dirname(os.path.dirname(__file__))
file_ = os.path.join(PATH, 'CSV/test.csv')

# lines = get_object_list( file_ )
#
# for video in lines[:1]:
#         for x in range( 0, 11 ):
#                 print video[x]
#                 print ''

lines = get_object_dict( file_ )

for video in lines[:1]:
        print video['embed']
        print video['url']
        print video['imagem']
        print video['flipboard']
        print video['titulo']
        print video['tags']
        print video['duracao']
        print video['views']
        print video['qtdavaliacoes']
        print video['totalavaliacoes']
        print video['avaliacao']

# print( lines[1] )
print( 'splits', len( lines[1] ) )
print( 'total lines', len( lines ) )

