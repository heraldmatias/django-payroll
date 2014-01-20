# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Asignacion(models.Model):
    fe_asignacion = models.DateTimeField(blank=True, null=True)
    fe_modifica_asig = models.DateTimeField(blank=True, null=True)
    co_asignado = models.ForeignKey('Usuarios', db_column='co_asignado')
    co_tomo = models.ForeignKey('Tomos', db_column='co_tomo')
    co_asignador = models.ForeignKey('Usuarios', db_column='co_asignador')
    co_modificador = models.ForeignKey('Usuarios', db_column='co_modificador', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'asignacion'

class AsignacionLog(models.Model):
    fe_asignacion = models.DateTimeField(blank=True, null=True)
    co_asignado = models.IntegerField(blank=True, null=True)
    co_tomo = models.IntegerField(blank=True, null=True)
    co_asignador = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'asignacion_log'

class Conceptos(models.Model):
    codi_conc_tco = models.CharField(primary_key=True, max_length=5)
    codi_oper_ope = models.CharField(max_length=13, blank=True)
    codi_cicl_cic = models.CharField(max_length=1, blank=True)
    desc_conc_tco = models.CharField(max_length=150)
    desc_cort_tco = models.CharField(max_length=25, blank=True)
    tipo_conc_tco = models.CharField(max_length=1, blank=True)
    tipo_calc_tco = models.CharField(max_length=1, blank=True)
    secu_calc_tco = models.CharField(max_length=2, blank=True)
    flag_asoc_tco = models.CharField(max_length=1, blank=True)
    flag_recu_tco = models.CharField(max_length=1, blank=True)
    rnta_qnta_tco = models.CharField(max_length=1, blank=True)
    cts_cts_tco = models.CharField(max_length=1, blank=True)
    codi_conc_onc = models.CharField(max_length=5, blank=True)
    codi_enti_ent = models.CharField(max_length=8, blank=True)
    cnta_debe_tco = models.CharField(max_length=15, blank=True)
    cnta_habe_tco = models.CharField(max_length=15, blank=True)
    clas_conc_tco = models.CharField(max_length=1, blank=True)
    flag_pago_tco = models.CharField(max_length=1, blank=True)
    sede_conc_tco = models.CharField(max_length=1, blank=True)
    fec_creac = models.DateTimeField(blank=True, null=True)
    fec_mod = models.DateTimeField(blank=True, null=True)
    usu_crea = models.ForeignKey('Usuarios', blank=True, null=True)
    usu_mod = models.ForeignKey('Usuarios', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'conceptos'

class ConceptosEliminar(models.Model):
    codi_conc_tco = models.CharField(max_length=5, blank=True)
    class Meta:
        managed = False
        db_table = 'conceptos_eliminar'

class ConceptosFolios(models.Model):
    id = models.IntegerField(primary_key=True)
    orden_conc_folio = models.IntegerField()
    codi_folio = models.ForeignKey('Folios', db_column='codi_folio', blank=True, null=True)
    codi_conc_tco = models.ForeignKey(Conceptos, db_column='codi_conc_tco', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'conceptos_folios'

class ConceptosUsados(models.Model):
    codi_conc_tco = models.CharField(max_length=5, blank=True)
    class Meta:
        managed = False
        db_table = 'conceptos_usados'

class ExcelTomo(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=90)
    description = models.TextField(blank=True)
    filename = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    tomo = models.IntegerField(blank=True, null=True)
    usu_crea = models.ForeignKey('Usuarios', blank=True, null=True)
    usu_mod = models.ForeignKey('Usuarios', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'excel_tomo'

class Folios(models.Model):
    codi_folio = models.IntegerField(primary_key=True)
    num_folio = models.IntegerField()
    per_folio = models.CharField(max_length=100, blank=True)
    reg_folio = models.IntegerField(blank=True, null=True)
    subt_plan_stp = models.CharField(max_length=2, blank=True)
    codi_tomo = models.ForeignKey('Tomos', db_column='codi_tomo', blank=True, null=True)
    tipo_plan_tpl = models.ForeignKey('Tplanilla', db_column='tipo_plan_tpl', blank=True, null=True)
    fec_creac = models.DateTimeField(blank=True, null=True)
    fec_mod = models.DateTimeField(blank=True, null=True)
    usu_crea = models.ForeignKey('Usuarios', blank=True, null=True)
    usu_mod = models.ForeignKey('Usuarios', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'folios'

class LvAcumuladosTomo(models.Model):
    tomo = models.IntegerField(blank=True, null=True)
    tregistros = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tdias = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'lv_acumulados_tomo'

class LvAsignacion(models.Model):
    fe_asignacion = models.DateTimeField(blank=True, null=True)
    fe_modifica_asig = models.DateTimeField(blank=True, null=True)
    tomo = models.IntegerField(blank=True, null=True)
    digitador = models.CharField(max_length=25, blank=True)
    co_asignado = models.IntegerField(blank=True, null=True)
    asignador = models.CharField(max_length=25, blank=True)
    asignadorcambio = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'lv_asignacion'

class LvDatosTomo(models.Model):
    tomo = models.IntegerField(blank=True, null=True)
    folios = models.IntegerField(blank=True, null=True)
    resumen = models.BigIntegerField(blank=True, null=True)
    digitables = models.BigIntegerField(blank=True, null=True)
    digitados = models.BigIntegerField(blank=True, null=True)
    por_digitar = models.BigIntegerField(blank=True, null=True)
    registros = models.BigIntegerField(blank=True, null=True)
    estado = models.TextField(blank=True)
    completo = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'lv_datos_tomo'

class LvPersonalCodigo(models.Model):
    valo_calc_phi = models.CharField(max_length=150, blank=True)
    codi_empl_per = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'lv_personal_codigo'

class LvPersonalPlanillas(models.Model):
    empleado = models.CharField(max_length=100, blank=True)
    codigo = models.CharField(max_length=8, blank=True)
    soundex = models.CharField(max_length=8, blank=True)
    class Meta:
        managed = False
        db_table = 'lv_personal_planillas'

class LvPersonalPorNombre(models.Model):
    codi_empl_per = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'lv_personal_por_nombre'

class LvTomoAsignacion(models.Model):
    tomo = models.IntegerField(blank=True, null=True)
    folios = models.IntegerField(blank=True, null=True)
    resumen = models.BigIntegerField(blank=True, null=True)
    digitables = models.BigIntegerField(blank=True, null=True)
    digitados = models.BigIntegerField(blank=True, null=True)
    por_digitar = models.BigIntegerField(blank=True, null=True)
    registros = models.BigIntegerField(blank=True, null=True)
    estado = models.TextField(blank=True)
    completo = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'lv_tomo_asignacion'

class MaestroPersonal(models.Model):
    codi_empl_per = models.CharField(primary_key=True, max_length=8)
    ape_pat_per = models.CharField(max_length=35)
    ape_mat_per = models.CharField(max_length=35, blank=True)
    nom_emp_per = models.CharField(max_length=35)
    nomb_cort_per = models.CharField(max_length=70, blank=True)
    dir_emp_per = models.CharField(max_length=150, blank=True)
    codi_depa_dpt = models.CharField(max_length=2, blank=True)
    codi_prov_tpr = models.CharField(max_length=2, blank=True)
    codi_dist_tdi = models.CharField(max_length=2, blank=True)
    num_tel_per = models.CharField(max_length=10, blank=True)
    fec_ing_per = models.DateField(blank=True, null=True)
    tipo_plan_tpl = models.CharField(max_length=2, blank=True)
    est_civ_per = models.CharField(max_length=1, blank=True)
    sex_emp_per = models.CharField(max_length=1, blank=True)
    gra_ins_per = models.CharField(max_length=1, blank=True)
    fec_nac_per = models.DateField(blank=True, null=True)
    pais_naci_tpa = models.CharField(max_length=4, blank=True)
    depa_naci_dpt = models.CharField(max_length=2, blank=True)
    prov_naci_tpr = models.CharField(max_length=2, blank=True)
    dist_naci_tdi = models.CharField(max_length=2, blank=True)
    codi_depe_tde = models.CharField(max_length=4, blank=True)
    ubic_fisi_tde = models.CharField(max_length=4, blank=True)
    codi_nive_tni = models.CharField(max_length=3, blank=True)
    nive_enc_tni = models.CharField(max_length=3, blank=True)
    esta_trab_per = models.CharField(max_length=1, blank=True)
    con_tra_per = models.CharField(max_length=1, blank=True)
    reg_lab_per = models.CharField(max_length=8, blank=True)
    reg_pen_per = models.CharField(max_length=8, blank=True)
    codi_carg_tca = models.CharField(max_length=8, blank=True)
    carg_enc_tca = models.CharField(max_length=8, blank=True)
    flag_afp_per = models.CharField(max_length=1, blank=True)
    codi_afp = models.CharField(max_length=2, blank=True)
    fech_afp_per = models.DateField(blank=True, null=True)
    codi_afp_per = models.CharField(max_length=15, blank=True)
    libr_elec_per = models.CharField(max_length=8, blank=True)
    libr_mili_per = models.CharField(max_length=10, blank=True)
    codi_ipss_per = models.CharField(max_length=16, blank=True)
    nume_brev_per = models.CharField(max_length=15, blank=True)
    gru_sang_per = models.CharField(max_length=4, blank=True)
    cod_mon_suel_per = models.CharField(max_length=2, blank=True)
    flag_suel_per = models.CharField(max_length=1, blank=True)
    banc_suel_tbc = models.CharField(max_length=2, blank=True)
    suel_cta_per = models.CharField(max_length=18, blank=True)
    banc_cts_tbc = models.CharField(max_length=2, blank=True)
    cts_cta_per = models.CharField(max_length=18, blank=True)
    cod_mon_cts_per = models.CharField(max_length=2, blank=True)
    nume_plaz_per = models.CharField(max_length=8, blank=True)
    fech_rnom_per = models.DateField(blank=True, null=True)
    nume_rnom_per = models.CharField(max_length=10, blank=True)
    sede_actu_per = models.CharField(max_length=3, blank=True)
    fing_adm_per = models.DateField(blank=True, null=True)
    fing_carrp_per = models.DateField(blank=True, null=True)
    otro_docu_per = models.CharField(max_length=15, blank=True)
    observa_per = models.CharField(max_length=100, blank=True)
    cargo_remu_per = models.CharField(max_length=8, blank=True)
    nivel_remu_per = models.CharField(max_length=3, blank=True)
    plaza_remu_per = models.CharField(max_length=8, blank=True)
    depe_remu_per = models.CharField(max_length=4, blank=True)
    obser_remu_per = models.CharField(max_length=100, blank=True)
    tipo_cuen_per = models.CharField(max_length=1, blank=True)
    segu_medi_per = models.CharField(max_length=1, blank=True)
    sede_remu_per = models.CharField(max_length=3, blank=True)
    apep_solt_per = models.CharField(max_length=20, blank=True)
    apem_solt_per = models.CharField(max_length=20, blank=True)
    nomb_solt_er = models.CharField(max_length=30, blank=True)
    cesa_sobr_per = models.CharField(max_length=1, blank=True)
    fec_cese_per = models.DateField(blank=True, null=True)
    nomb_titu_ces = models.CharField(max_length=70, blank=True)
    nomb_cobr_ces = models.CharField(max_length=70, blank=True)
    enca_plaz_per = models.CharField(max_length=8, blank=True)
    flag_propuesta = models.CharField(max_length=1, blank=True)
    meta_prop = models.CharField(max_length=4, blank=True)
    ftefto = models.CharField(max_length=4, blank=True)
    codi_proy_pin = models.CharField(max_length=4, blank=True)
    codrie = models.CharField(max_length=2, blank=True)
    flag_almacen = models.CharField(max_length=1, blank=True)
    fech_ini_recu = models.DateField(blank=True, null=True)
    flag_recurrente = models.CharField(max_length=1, blank=True)
    obs_recu = models.CharField(max_length=200, blank=True)
    flag_fotoc_per = models.CharField(max_length=1, blank=True)
    ind_valido = models.CharField(max_length=1, blank=True)
    bio_suserid = models.CharField(max_length=8, blank=True)
    tipo_via_per = models.CharField(max_length=2, blank=True)
    nomb_via_per = models.CharField(max_length=50, blank=True)
    nume_dire_per = models.CharField(max_length=6, blank=True)
    km_dire_per = models.CharField(max_length=6, blank=True)
    mz_dire_per = models.CharField(max_length=6, blank=True)
    inte_dire_per = models.CharField(max_length=6, blank=True)
    dpto_dire_per = models.CharField(max_length=6, blank=True)
    lote_dire_per = models.CharField(max_length=6, blank=True)
    piso_dire_per = models.CharField(max_length=6, blank=True)
    tipo_zona_per = models.CharField(max_length=2, blank=True)
    nomb_zona_per = models.CharField(max_length=50, blank=True)
    nomb_refdom_per = models.CharField(max_length=150, blank=True)
    num_ruc_per = models.CharField(max_length=12, blank=True)
    num_cel_per = models.CharField(max_length=15, blank=True)
    email_per = models.CharField(max_length=50, blank=True)
    email_insti = models.CharField(max_length=50, blank=True)
    codi_func_tca = models.CharField(max_length=8, blank=True)
    carg_enc_per = models.CharField(max_length=3, blank=True)
    marca = models.CharField(max_length=1, blank=True)
    flag_cuenta = models.CharField(max_length=1, blank=True)
    codi_ubic_ofic = models.CharField(max_length=3, blank=True)
    nomb_prim_per = models.CharField(max_length=25, blank=True)
    nomb_segu_per = models.CharField(max_length=25, blank=True)
    tipo_comision_afp = models.CharField(max_length=2, blank=True)
    class Meta:
        managed = False
        db_table = 'maestro_personal'

class Module(models.Model):
    name = models.CharField(primary_key=True, max_length=15)
    description = models.CharField(max_length=70)
    query_path = models.CharField(max_length=30, blank=True)
    add_path = models.CharField(max_length=30, blank=True)
    order = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'module'

class Permission(models.Model):
    role = models.ForeignKey('Roles')
    module = models.ForeignKey(Module)
    type = models.TextField()
    class Meta:
        managed = False
        db_table = 'permission'

class PersonalDigitado(models.Model):
    id = models.IntegerField(primary_key=True)
    codi_empl_per = models.CharField(max_length=8, blank=True)
    nomb_cort_per = models.CharField(max_length=150)
    nomb_soundex_per = models.CharField(max_length=8, blank=True)
    codi_empl_per_persona = models.ForeignKey('PersonalEncontrado', db_column='codi_empl_per_persona', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'personal_digitado'

class PersonalEncontrado(models.Model):
    codi_empl_per = models.CharField(primary_key=True, max_length=8)
    ape_pat_per = models.CharField(max_length=35)
    ape_mat_per = models.CharField(max_length=35)
    nom_emp_per = models.CharField(max_length=35)
    nomb_cort_per = models.CharField(max_length=150)
    libr_elec_per = models.CharField(max_length=8, blank=True)
    class Meta:
        managed = False
        db_table = 'personal_encontrado'

class Planilla(models.Model):
    id = models.IntegerField(primary_key=True)
    ano_peri_tpe = models.CharField(max_length=30)
    tipo_plan_tpl = models.CharField(max_length=5)
    subt_plan_stp = models.CharField(max_length=2, blank=True)
    usu_crea_id = models.IntegerField(blank=True, null=True)
    usu_mod_id = models.IntegerField(blank=True, null=True)
    fec_creac = models.DateTimeField(blank=True, null=True)
    fec_mod = models.DateTimeField(blank=True, null=True)
    cant_reg = models.IntegerField(blank=True, null=True)
    codi_folio = models.ForeignKey(Folios, db_column='codi_folio', blank=True, null=True)
    codi_tomo = models.ForeignKey('Tomos', db_column='codi_tomo', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'planilla'

class PlanillaHistoricas(models.Model):
    id = models.IntegerField(primary_key=True)
    ano_peri_tpe = models.CharField(max_length=30)
    nume_peri_tpe = models.CharField(max_length=2)
    valo_calc_phi = models.CharField(max_length=150)
    tipo_plan_tpl = models.CharField(max_length=5, blank=True)
    subt_plan_stp = models.CharField(max_length=2, blank=True)
    codi_empl_per = models.CharField(max_length=100)
    codi_conc_tco = models.CharField(max_length=5)
    codi_folio = models.IntegerField(blank=True, null=True)
    desc_plan_stp = models.TextField(blank=True)
    flag_folio = models.IntegerField(blank=True, null=True)
    usu_crea_id = models.IntegerField(blank=True, null=True)
    usu_mod_id = models.IntegerField(blank=True, null=True)
    fec_creac = models.DateTimeField(blank=True, null=True)
    fec_mod = models.DateTimeField(blank=True, null=True)
    num_reg = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'planilla_historicas'

class PlanillaHistoricasLog(models.Model):
    id = models.IntegerField(blank=True, null=True)
    ano_peri_tpe = models.CharField(max_length=30, blank=True)
    nume_peri_tpe = models.CharField(max_length=2, blank=True)
    valo_calc_phi = models.CharField(max_length=150, blank=True)
    tipo_plan_tpl = models.CharField(max_length=5, blank=True)
    subt_plan_stp = models.CharField(max_length=2, blank=True)
    codi_empl_per = models.CharField(max_length=100, blank=True)
    codi_conc_tco = models.CharField(max_length=5, blank=True)
    codi_folio = models.IntegerField(blank=True, null=True)
    desc_plan_stp = models.TextField(blank=True)
    flag_folio = models.IntegerField(blank=True, null=True)
    usu_crea_id = models.IntegerField(blank=True, null=True)
    usu_del_id = models.IntegerField(blank=True, null=True)
    fec_creac = models.DateTimeField(blank=True, null=True)
    fec_del = models.DateTimeField(blank=True, null=True)
    num_reg = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'planilla_historicas_log'

class PlanillaHistoricasSiga(models.Model):
    id = models.IntegerField(primary_key=True)
    ano_peri_tpe = models.CharField(max_length=30)
    nume_peri_tpe = models.CharField(max_length=2)
    valo_calc_phi = models.CharField(max_length=150)
    tipo_plan_tpl = models.CharField(max_length=5, blank=True)
    subt_plan_stp = models.CharField(max_length=2, blank=True)
    codi_empl_per = models.CharField(max_length=100)
    codi_conc_tco = models.ForeignKey(Conceptos, db_column='codi_conc_tco')
    codi_folio = models.ForeignKey(Folios, db_column='codi_folio', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'planilla_historicas_siga'

class Roles(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    role = models.CharField(unique=True, max_length=20)
    class Meta:
        managed = False
        db_table = 'roles'

class Subtplanilla(models.Model):
    subt_plan_stp = models.CharField(max_length=2)
    desc_subt_stp = models.CharField(max_length=40)
    titu_subt_stp = models.CharField(max_length=40, blank=True)
    observ = models.TextField(blank=True)
    tipo_plan_tpl = models.ForeignKey('Tplanilla', db_column='tipo_plan_tpl')
    fec_creac = models.DateTimeField(blank=True, null=True)
    fec_mod = models.DateTimeField(blank=True, null=True)
    usu_crea = models.ForeignKey('Usuarios', blank=True, null=True)
    usu_mod = models.ForeignKey('Usuarios', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'subtplanilla'

class TmpConceptosFolios(models.Model):
    id = models.IntegerField(blank=True, null=True)
    orden_conc_folio = models.IntegerField(blank=True, null=True)
    codi_folio = models.IntegerField(blank=True, null=True)
    codi_conc_tco = models.CharField(max_length=5, blank=True)
    class Meta:
        managed = False
        db_table = 'tmp_conceptos_folios'

class Tomos(models.Model):
    codi_tomo = models.IntegerField(primary_key=True)
    per_tomo = models.CharField(max_length=100)
    ano_tomo = models.CharField(max_length=30)
    folios_tomo = models.IntegerField()
    desc_tomo = models.TextField(blank=True)
    fec_creac = models.DateTimeField(blank=True, null=True)
    fec_mod = models.DateTimeField(blank=True, null=True)
    usu_crea = models.ForeignKey('Usuarios', blank=True, null=True)
    usu_mod = models.ForeignKey('Usuarios', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tomos'

class Tplanilla(models.Model):
    tipo_plan_tpl = models.CharField(primary_key=True, max_length=3)
    desc_tipo_tpl = models.CharField(max_length=100)
    tarj_inic_tpl = models.CharField(max_length=4, blank=True)
    tarj_fina_tpl = models.CharField(max_length=4, blank=True)
    cant_peri_tpl = models.CharField(max_length=3, blank=True)
    codi_oper_ope = models.CharField(max_length=9, blank=True)
    abrev_tipo_tpl = models.CharField(max_length=10, blank=True)
    fec_creac = models.DateTimeField(blank=True, null=True)
    fec_mod = models.DateTimeField(blank=True, null=True)
    usu_crea = models.ForeignKey('Usuarios', blank=True, null=True)
    usu_mod = models.ForeignKey('Usuarios', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tplanilla'

class Usuarios(models.Model):
    id = models.IntegerField(primary_key=True)
    nom_comp_usu = models.CharField(max_length=150)
    cod_usu = models.CharField(unique=True, max_length=25)
    salt_usu = models.CharField(max_length=32)
    pass_usu = models.CharField(max_length=128)
    email_usu = models.CharField(max_length=60, blank=True)
    is_active = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'usuarios'

class UsuariosRole(models.Model):
    usuarios = models.ForeignKey(Usuarios)
    role = models.ForeignKey(Roles)
    class Meta:
        managed = False
        db_table = 'usuarios_role'

