from os import mkdir
from os.path import exists, dirname, join
import jinja2
from certificate_test import get_certificate_mm


def main(debug=False):

    this_folder = dirname(__file__)
    certificate_mm = get_certificate_mm(debug)
    certificado_model = certificate_mm.model_from_file(
        join(this_folder, 'varios.cer'))

    def is_entity(n):
        """
        Test to prove if some type is an entity
        """
        if n.type in certificado_model.certificado:
            return True
        else:
            return False

    # Create output folder
    srcgen_folder = join(this_folder, 'srcgen')
    if not exists(srcgen_folder):
        mkdir(srcgen_folder)

    # Initialize template engine.
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    jinja_env.tests['entity'] = is_entity
    template = jinja_env.get_template('html.template')
    for certificate in certificado_model.certificado:
        # For each entity generate html file
        with open(join(srcgen_folder,
            "agregar%s.html" % certificate.name.capitalize()), 'w') as f:
            f.write(template.render(certificado=certificate))


if __name__ == "__main__":
    main()
