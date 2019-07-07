from __future__ import unicode_literals
import os
from os.path import dirname, join
from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export

this_folder = dirname(__file__)
def get_certificate_mm(debug = False):
    certificate_mm = metamodel_from_file(join(this_folder, 'certificate.tx'))
    return certificate_mm