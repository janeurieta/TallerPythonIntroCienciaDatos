import os

import nbformat
from nbformat.v4.nbbase import new_markdown_cell

from generate_contents import iter_notebooks, NOTEBOOK_DIR


BOOK_COMMENT = "<!--BOOK_INFORMATION-->"


BOOK_INFO = BOOK_COMMENT + """
<img align="left" style="padding-right:10px;" src="figures/header.png">

*Esta libreta contiene material del Taller de Python que se lleva a cabo como parte del 
evento [Data Challenge Industrial 4.0](www.lania.mx/dci). El material ha sido adaptado 
por HTM y GED a partir del libro [Python Data Science Handbook](http://shop.oreilly.com/product/0636920034919.do) 
de Jake VanderPlas y se mantiene la licencia sobre el texto, 
[CC-BY-NC-ND license](https://creativecommons.org/licenses/by-nc-nd/3.0/us/legalcode), 
y sobre el codigo [MIT license](https://opensource.org/licenses/MIT).*"""


def add_book_info():
    for nb_name in iter_notebooks():
        nb_file = os.path.join(NOTEBOOK_DIR, nb_name)
        nb = nbformat.read(nb_file, as_version=4)

        is_comment = lambda cell: cell.source.startswith(BOOK_COMMENT)

        if is_comment(nb.cells[0]):
            print('- amending comment for {0}'.format(nb_name))
            nb.cells[0].source = BOOK_INFO
        else:
            print('- inserting comment for {0}'.format(nb_name))
            nb.cells.insert(0, new_markdown_cell(BOOK_INFO))
        nbformat.write(nb, nb_file)


if __name__ == '__main__':
    add_book_info()
