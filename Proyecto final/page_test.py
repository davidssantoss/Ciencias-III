from __future__ import unicode_literals
import os
from os.path import dirname, join
from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export

this_folder = dirname(__file__)
def get_entity_mm(debug = False):
    entity_mm = metamodel_from_file(join(this_folder, 'entity.tx'))
    return entity_mm