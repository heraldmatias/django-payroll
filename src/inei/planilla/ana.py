__author__ = 'holivares'

from django.db import connection


def update_planilla():
    cr = connection.cursor()
    sql = 'UPDATE planilla_historicas AS p SET codi_tomo = f.codi_tomo, num_folio = f.num_folio FROM folios f WHERE ' \
          'p.codi_folio = f.codi_folio AND f.codi_tomo=%d;'
    cr.execute(sql, (41, ))
    print 'Actualizado'


update_planilla()