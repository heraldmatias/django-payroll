__author__ = 'holivares'

from django.db import connection


def update_planilla():
    cr = connection.cursor()
    sql = 'UPDATE planilla_historicas AS p SET codi_tomo = f.codi_tomo, num_folio = f.num_folio FROM folios f WHERE ' \
          'p.codi_folio = f.codi_folio AND f.codi_tomo=%s AND p.codi_tomo IS NULL;'
    for tomo in range(42, 420):
        cr.execute(sql, (tomo, ))
        print 'Actualizado %s' % tomo


update_planilla()