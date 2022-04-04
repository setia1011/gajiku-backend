"""empty message

Revision ID: eefb16ab98bb
Revises: 
Create Date: 2022-04-04 11:43:26.423587

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eefb16ab98bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ref_user_group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('group_name', sa.String(length=50), nullable=False),
    sa.Column('group_description', sa.String(length=225), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ref_user_group_group_name'), 'ref_user_group', ['group_name'], unique=True)
    op.create_index(op.f('ix_ref_user_group_id'), 'ref_user_group', ['id'], unique=False)
    op.create_table('ref_user_id_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_type', sa.String(length=50), nullable=False),
    sa.Column('id_description', sa.String(length=225), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ref_user_id_type_id'), 'ref_user_id_type', ['id'], unique=False)
    op.create_index(op.f('ix_ref_user_id_type_id_type'), 'ref_user_id_type', ['id_type'], unique=True)
    op.create_table('tbl_subscription_plan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('plan', sa.Enum('basic', 'standard', 'premium'), nullable=True),
    sa.Column('monthly_price', sa.Float(), nullable=False),
    sa.Column('status', sa.Enum('valid', 'expired'), nullable=True),
    sa.Column('creator', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('editor', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tbl_subscription_plan_created_at'), 'tbl_subscription_plan', ['created_at'], unique=False)
    op.create_index(op.f('ix_tbl_subscription_plan_creator'), 'tbl_subscription_plan', ['creator'], unique=False)
    op.create_index(op.f('ix_tbl_subscription_plan_editor'), 'tbl_subscription_plan', ['editor'], unique=False)
    op.create_index(op.f('ix_tbl_subscription_plan_id'), 'tbl_subscription_plan', ['id'], unique=False)
    op.create_index(op.f('ix_tbl_subscription_plan_monthly_price'), 'tbl_subscription_plan', ['monthly_price'], unique=False)
    op.create_index(op.f('ix_tbl_subscription_plan_plan'), 'tbl_subscription_plan', ['plan'], unique=False)
    op.create_index(op.f('ix_tbl_subscription_plan_updated_at'), 'tbl_subscription_plan', ['updated_at'], unique=False)
    op.create_table('tbl_subscription',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subs_plan', sa.Integer(), nullable=False),
    sa.Column('subs_price', sa.Float(), nullable=False),
    sa.Column('subs_start', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('subs_end', sa.DateTime(timezone=True), nullable=False),
    sa.Column('creator', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('editor', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['subs_plan'], ['tbl_subscription_plan.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tbl_subscription_created_at'), 'tbl_subscription', ['created_at'], unique=False)
    op.create_index(op.f('ix_tbl_subscription_creator'), 'tbl_subscription', ['creator'], unique=False)
    op.create_index(op.f('ix_tbl_subscription_editor'), 'tbl_subscription', ['editor'], unique=False)
    op.create_index(op.f('ix_tbl_subscription_id'), 'tbl_subscription', ['id'], unique=False)
    op.create_index(op.f('ix_tbl_subscription_subs_end'), 'tbl_subscription', ['subs_end'], unique=False)
    op.create_index(op.f('ix_tbl_subscription_subs_plan'), 'tbl_subscription', ['subs_plan'], unique=False)
    op.create_index(op.f('ix_tbl_subscription_subs_price'), 'tbl_subscription', ['subs_price'], unique=False)
    op.create_index(op.f('ix_tbl_subscription_subs_start'), 'tbl_subscription', ['subs_start'], unique=False)
    op.create_index(op.f('ix_tbl_subscription_updated_at'), 'tbl_subscription', ['updated_at'], unique=False)
    op.create_table('tbl_client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('address', sa.TEXT(), nullable=True),
    sa.Column('responsible', sa.String(length=50), nullable=False),
    sa.Column('responsible_id_type', sa.Integer(), nullable=False),
    sa.Column('responsible_id_number', sa.Integer(), nullable=False),
    sa.Column('subscription_id', sa.Integer(), nullable=False),
    sa.Column('creator', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('editor', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['responsible_id_type'], ['ref_user_id_type.id'], ),
    sa.ForeignKeyConstraint(['subscription_id'], ['tbl_subscription.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_index(op.f('ix_tbl_client_id'), 'tbl_client', ['id'], unique=False)
    op.create_index(op.f('ix_tbl_client_name'), 'tbl_client', ['name'], unique=False)
    op.create_index(op.f('ix_tbl_client_responsible_id_number'), 'tbl_client', ['responsible_id_number'], unique=False)
    op.create_index(op.f('ix_tbl_client_responsible_id_type'), 'tbl_client', ['responsible_id_type'], unique=False)
    op.create_table('set_gaji_bpjs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kode', sa.String(length=50), nullable=False),
    sa.Column('keterangan', sa.String(length=500), nullable=True),
    sa.Column('besaran', sa.Float(), nullable=True),
    sa.Column('jenis_besaran', sa.Enum('persentase', 'spesifik'), nullable=False),
    sa.Column('dasar_penetapan', sa.String(length=500), nullable=True),
    sa.Column('mulai_berlaku', sa.DateTime(timezone=True), nullable=True),
    sa.Column('selesai_berlaku', sa.DateTime(timezone=True), nullable=True),
    sa.Column('status', sa.Enum('berlaku', 'tidak berlaku'), server_default='berlaku', nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('creator', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('editor', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['tbl_client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_set_gaji_bpjs_besaran'), 'set_gaji_bpjs', ['besaran'], unique=False)
    op.create_index(op.f('ix_set_gaji_bpjs_client_id'), 'set_gaji_bpjs', ['client_id'], unique=False)
    op.create_index(op.f('ix_set_gaji_bpjs_id'), 'set_gaji_bpjs', ['id'], unique=False)
    op.create_index(op.f('ix_set_gaji_bpjs_jenis_besaran'), 'set_gaji_bpjs', ['jenis_besaran'], unique=False)
    op.create_index(op.f('ix_set_gaji_bpjs_keterangan'), 'set_gaji_bpjs', ['keterangan'], unique=False)
    op.create_index(op.f('ix_set_gaji_bpjs_kode'), 'set_gaji_bpjs', ['kode'], unique=False)
    op.create_index(op.f('ix_set_gaji_bpjs_status'), 'set_gaji_bpjs', ['status'], unique=False)
    op.create_table('set_gaji_golongan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kode', sa.String(length=50), nullable=False),
    sa.Column('keterangan', sa.String(length=500), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('creator', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('editor', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['tbl_client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_set_gaji_golongan_client_id'), 'set_gaji_golongan', ['client_id'], unique=False)
    op.create_index(op.f('ix_set_gaji_golongan_id'), 'set_gaji_golongan', ['id'], unique=False)
    op.create_index(op.f('ix_set_gaji_golongan_keterangan'), 'set_gaji_golongan', ['keterangan'], unique=False)
    op.create_index(op.f('ix_set_gaji_golongan_kode'), 'set_gaji_golongan', ['kode'], unique=False)
    op.create_table('set_gaji_grade',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kode', sa.String(length=50), nullable=False),
    sa.Column('keterangan', sa.String(length=500), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('creator', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('editor', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['tbl_client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_set_gaji_grade_client_id'), 'set_gaji_grade', ['client_id'], unique=False)
    op.create_index(op.f('ix_set_gaji_grade_id'), 'set_gaji_grade', ['id'], unique=False)
    op.create_index(op.f('ix_set_gaji_grade_keterangan'), 'set_gaji_grade', ['keterangan'], unique=False)
    op.create_index(op.f('ix_set_gaji_grade_kode'), 'set_gaji_grade', ['kode'], unique=False)
    op.create_table('set_gaji_jabatan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kode', sa.String(length=50), nullable=False),
    sa.Column('keterangan', sa.String(length=500), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('creator', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('editor', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['tbl_client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_set_gaji_jabatan_client_id'), 'set_gaji_jabatan', ['client_id'], unique=False)
    op.create_index(op.f('ix_set_gaji_jabatan_id'), 'set_gaji_jabatan', ['id'], unique=False)
    op.create_index(op.f('ix_set_gaji_jabatan_keterangan'), 'set_gaji_jabatan', ['keterangan'], unique=False)
    op.create_index(op.f('ix_set_gaji_jabatan_kode'), 'set_gaji_jabatan', ['kode'], unique=False)
    op.create_table('set_gaji_pangkat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kode', sa.String(length=50), nullable=False),
    sa.Column('keterangan', sa.String(length=500), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('creator', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('editor', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['tbl_client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_set_gaji_pangkat_client_id'), 'set_gaji_pangkat', ['client_id'], unique=False)
    op.create_index(op.f('ix_set_gaji_pangkat_id'), 'set_gaji_pangkat', ['id'], unique=False)
    op.create_index(op.f('ix_set_gaji_pangkat_keterangan'), 'set_gaji_pangkat', ['keterangan'], unique=False)
    op.create_index(op.f('ix_set_gaji_pangkat_kode'), 'set_gaji_pangkat', ['kode'], unique=False)
    op.create_table('set_gaji_penghasilan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('komponen', sa.String(length=200), nullable=False),
    sa.Column('besaran', sa.Float(), nullable=False),
    sa.Column('jenis_besaran', sa.Enum('persentase', 'spesifik'), nullable=False),
    sa.Column('dasar_penetapan', sa.String(length=500), nullable=True),
    sa.Column('mulai_berlaku', sa.DateTime(timezone=True), nullable=True),
    sa.Column('selesai_berlaku', sa.DateTime(timezone=True), nullable=True),
    sa.Column('status', sa.Enum('berlaku', 'tidak berlaku'), server_default='berlaku', nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('creator', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('editor', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['tbl_client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_set_gaji_penghasilan_besaran'), 'set_gaji_penghasilan', ['besaran'], unique=False)
    op.create_index(op.f('ix_set_gaji_penghasilan_client_id'), 'set_gaji_penghasilan', ['client_id'], unique=False)
    op.create_index(op.f('ix_set_gaji_penghasilan_id'), 'set_gaji_penghasilan', ['id'], unique=False)
    op.create_index(op.f('ix_set_gaji_penghasilan_jenis_besaran'), 'set_gaji_penghasilan', ['jenis_besaran'], unique=False)
    op.create_index(op.f('ix_set_gaji_penghasilan_komponen'), 'set_gaji_penghasilan', ['komponen'], unique=False)
    op.create_index(op.f('ix_set_gaji_penghasilan_status'), 'set_gaji_penghasilan', ['status'], unique=False)
    op.create_table('set_gaji_potongan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('potongan', sa.String(length=200), nullable=False),
    sa.Column('besaran', sa.Float(), nullable=False),
    sa.Column('jenis_besaran', sa.Enum('persentase', 'spesifik'), nullable=False),
    sa.Column('dasar_penetapan', sa.String(length=500), nullable=True),
    sa.Column('mulai_berlaku', sa.DateTime(timezone=True), nullable=True),
    sa.Column('selesai_berlaku', sa.DateTime(timezone=True), nullable=True),
    sa.Column('status', sa.Enum('berlaku', 'tidak berlaku'), server_default='berlaku', nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('creator', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('editor', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['tbl_client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_set_gaji_potongan_besaran'), 'set_gaji_potongan', ['besaran'], unique=False)
    op.create_index(op.f('ix_set_gaji_potongan_client_id'), 'set_gaji_potongan', ['client_id'], unique=False)
    op.create_index(op.f('ix_set_gaji_potongan_id'), 'set_gaji_potongan', ['id'], unique=False)
    op.create_index(op.f('ix_set_gaji_potongan_jenis_besaran'), 'set_gaji_potongan', ['jenis_besaran'], unique=False)
    op.create_index(op.f('ix_set_gaji_potongan_potongan'), 'set_gaji_potongan', ['potongan'], unique=False)
    op.create_index(op.f('ix_set_gaji_potongan_status'), 'set_gaji_potongan', ['status'], unique=False)
    op.create_table('set_gaji_status_kawin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kode', sa.String(length=50), nullable=False),
    sa.Column('keterangan', sa.String(length=500), nullable=True),
    sa.Column('besaran', sa.Float(), nullable=True),
    sa.Column('jenis_besaran', sa.Enum('persentase', 'spesifik'), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('dasar_penetapan', sa.String(length=500), nullable=True),
    sa.Column('mulai_berlaku', sa.DateTime(timezone=True), nullable=True),
    sa.Column('selesai_berlaku', sa.DateTime(timezone=True), nullable=True),
    sa.Column('status', sa.Enum('berlaku', 'tidak berlaku'), server_default='berlaku', nullable=False),
    sa.Column('creator', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('editor', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['tbl_client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_set_gaji_status_kawin_besaran'), 'set_gaji_status_kawin', ['besaran'], unique=False)
    op.create_index(op.f('ix_set_gaji_status_kawin_client_id'), 'set_gaji_status_kawin', ['client_id'], unique=False)
    op.create_index(op.f('ix_set_gaji_status_kawin_id'), 'set_gaji_status_kawin', ['id'], unique=False)
    op.create_index(op.f('ix_set_gaji_status_kawin_jenis_besaran'), 'set_gaji_status_kawin', ['jenis_besaran'], unique=False)
    op.create_index(op.f('ix_set_gaji_status_kawin_keterangan'), 'set_gaji_status_kawin', ['keterangan'], unique=False)
    op.create_index(op.f('ix_set_gaji_status_kawin_kode'), 'set_gaji_status_kawin', ['kode'], unique=False)
    op.create_index(op.f('ix_set_gaji_status_kawin_status'), 'set_gaji_status_kawin', ['status'], unique=False)
    op.create_table('tbl_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('group_id', sa.Integer(), server_default='4', nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('id_type', sa.Integer(), nullable=True),
    sa.Column('id_number', sa.String(length=50), nullable=True),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.Column('address', sa.TEXT(), nullable=True),
    sa.Column('status', sa.Enum('enabled', 'disabled'), server_default='disabled', nullable=False),
    sa.Column('creator', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('editor', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['tbl_client.id'], ),
    sa.ForeignKeyConstraint(['group_id'], ['ref_user_group.id'], ),
    sa.ForeignKeyConstraint(['id_type'], ['ref_user_id_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tbl_user_client_id'), 'tbl_user', ['client_id'], unique=False)
    op.create_index(op.f('ix_tbl_user_email'), 'tbl_user', ['email'], unique=True)
    op.create_index(op.f('ix_tbl_user_group_id'), 'tbl_user', ['group_id'], unique=False)
    op.create_index(op.f('ix_tbl_user_id'), 'tbl_user', ['id'], unique=False)
    op.create_index(op.f('ix_tbl_user_id_number'), 'tbl_user', ['id_number'], unique=False)
    op.create_index(op.f('ix_tbl_user_id_type'), 'tbl_user', ['id_type'], unique=False)
    op.create_index(op.f('ix_tbl_user_name'), 'tbl_user', ['name'], unique=False)
    op.create_index(op.f('ix_tbl_user_status'), 'tbl_user', ['status'], unique=False)
    op.create_index(op.f('ix_tbl_user_username'), 'tbl_user', ['username'], unique=True)
    op.create_table('tbl_activation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('acticode', sa.String(length=255), nullable=False),
    sa.Column('expired', sa.DateTime(timezone=True), nullable=True),
    sa.Column('activated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('status', sa.Enum('activated', 'inactivated'), server_default='inactivated', nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['tbl_user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('acticode')
    )
    op.create_index(op.f('ix_tbl_activation_id'), 'tbl_activation', ['id'], unique=False)
    op.create_index(op.f('ix_tbl_activation_user_id'), 'tbl_activation', ['user_id'], unique=False)
    op.create_table('tbl_gaji_employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('id_number', sa.String(length=50), nullable=False),
    sa.Column('id_type', sa.Integer(), nullable=False),
    sa.Column('jabatan_id', sa.Integer(), nullable=True),
    sa.Column('pangkat_id', sa.Integer(), nullable=True),
    sa.Column('golongan_id', sa.Integer(), nullable=True),
    sa.Column('grade_id', sa.Integer(), nullable=True),
    sa.Column('masa_kerja', sa.Integer(), nullable=True),
    sa.Column('bpjs_id', sa.Integer(), nullable=True),
    sa.Column('status_kawin', sa.Integer(), nullable=False),
    sa.Column('status_bekerja', sa.Enum('aktif', 'tidak aktif'), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('creator', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('editor', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['bpjs_id'], ['set_gaji_bpjs.id'], ),
    sa.ForeignKeyConstraint(['client_id'], ['tbl_client.id'], ),
    sa.ForeignKeyConstraint(['golongan_id'], ['set_gaji_golongan.id'], ),
    sa.ForeignKeyConstraint(['grade_id'], ['set_gaji_grade.id'], ),
    sa.ForeignKeyConstraint(['id_type'], ['ref_user_id_type.id'], ),
    sa.ForeignKeyConstraint(['jabatan_id'], ['set_gaji_jabatan.id'], ),
    sa.ForeignKeyConstraint(['pangkat_id'], ['set_gaji_pangkat.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tbl_gaji_employee_bpjs_id'), 'tbl_gaji_employee', ['bpjs_id'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_employee_client_id'), 'tbl_gaji_employee', ['client_id'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_employee_golongan_id'), 'tbl_gaji_employee', ['golongan_id'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_employee_grade_id'), 'tbl_gaji_employee', ['grade_id'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_employee_id'), 'tbl_gaji_employee', ['id'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_employee_id_number'), 'tbl_gaji_employee', ['id_number'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_employee_id_type'), 'tbl_gaji_employee', ['id_type'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_employee_jabatan_id'), 'tbl_gaji_employee', ['jabatan_id'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_employee_masa_kerja'), 'tbl_gaji_employee', ['masa_kerja'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_employee_name'), 'tbl_gaji_employee', ['name'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_employee_pangkat_id'), 'tbl_gaji_employee', ['pangkat_id'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_employee_status_bekerja'), 'tbl_gaji_employee', ['status_bekerja'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_employee_status_kawin'), 'tbl_gaji_employee', ['status_kawin'], unique=False)
    op.create_table('tbl_gaji_master_penghasilan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('penghasilan', sa.Integer(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('creator', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('editor', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['tbl_client.id'], ),
    sa.ForeignKeyConstraint(['employee_id'], ['tbl_gaji_employee.id'], ),
    sa.ForeignKeyConstraint(['penghasilan'], ['set_gaji_penghasilan.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tbl_gaji_master_penghasilan_client_id'), 'tbl_gaji_master_penghasilan', ['client_id'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_master_penghasilan_created_at'), 'tbl_gaji_master_penghasilan', ['created_at'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_master_penghasilan_creator'), 'tbl_gaji_master_penghasilan', ['creator'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_master_penghasilan_editor'), 'tbl_gaji_master_penghasilan', ['editor'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_master_penghasilan_employee_id'), 'tbl_gaji_master_penghasilan', ['employee_id'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_master_penghasilan_id'), 'tbl_gaji_master_penghasilan', ['id'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_master_penghasilan_penghasilan'), 'tbl_gaji_master_penghasilan', ['penghasilan'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_master_penghasilan_updated_at'), 'tbl_gaji_master_penghasilan', ['updated_at'], unique=False)
    op.create_table('tbl_gaji_master_potongan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('potongan', sa.Integer(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('creator', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('editor', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['tbl_client.id'], ),
    sa.ForeignKeyConstraint(['employee_id'], ['tbl_gaji_employee.id'], ),
    sa.ForeignKeyConstraint(['potongan'], ['set_gaji_potongan.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tbl_gaji_master_potongan_client_id'), 'tbl_gaji_master_potongan', ['client_id'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_master_potongan_created_at'), 'tbl_gaji_master_potongan', ['created_at'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_master_potongan_creator'), 'tbl_gaji_master_potongan', ['creator'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_master_potongan_editor'), 'tbl_gaji_master_potongan', ['editor'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_master_potongan_employee_id'), 'tbl_gaji_master_potongan', ['employee_id'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_master_potongan_id'), 'tbl_gaji_master_potongan', ['id'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_master_potongan_potongan'), 'tbl_gaji_master_potongan', ['potongan'], unique=False)
    op.create_index(op.f('ix_tbl_gaji_master_potongan_updated_at'), 'tbl_gaji_master_potongan', ['updated_at'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tbl_gaji_master_potongan_updated_at'), table_name='tbl_gaji_master_potongan')
    op.drop_index(op.f('ix_tbl_gaji_master_potongan_potongan'), table_name='tbl_gaji_master_potongan')
    op.drop_index(op.f('ix_tbl_gaji_master_potongan_id'), table_name='tbl_gaji_master_potongan')
    op.drop_index(op.f('ix_tbl_gaji_master_potongan_employee_id'), table_name='tbl_gaji_master_potongan')
    op.drop_index(op.f('ix_tbl_gaji_master_potongan_editor'), table_name='tbl_gaji_master_potongan')
    op.drop_index(op.f('ix_tbl_gaji_master_potongan_creator'), table_name='tbl_gaji_master_potongan')
    op.drop_index(op.f('ix_tbl_gaji_master_potongan_created_at'), table_name='tbl_gaji_master_potongan')
    op.drop_index(op.f('ix_tbl_gaji_master_potongan_client_id'), table_name='tbl_gaji_master_potongan')
    op.drop_table('tbl_gaji_master_potongan')
    op.drop_index(op.f('ix_tbl_gaji_master_penghasilan_updated_at'), table_name='tbl_gaji_master_penghasilan')
    op.drop_index(op.f('ix_tbl_gaji_master_penghasilan_penghasilan'), table_name='tbl_gaji_master_penghasilan')
    op.drop_index(op.f('ix_tbl_gaji_master_penghasilan_id'), table_name='tbl_gaji_master_penghasilan')
    op.drop_index(op.f('ix_tbl_gaji_master_penghasilan_employee_id'), table_name='tbl_gaji_master_penghasilan')
    op.drop_index(op.f('ix_tbl_gaji_master_penghasilan_editor'), table_name='tbl_gaji_master_penghasilan')
    op.drop_index(op.f('ix_tbl_gaji_master_penghasilan_creator'), table_name='tbl_gaji_master_penghasilan')
    op.drop_index(op.f('ix_tbl_gaji_master_penghasilan_created_at'), table_name='tbl_gaji_master_penghasilan')
    op.drop_index(op.f('ix_tbl_gaji_master_penghasilan_client_id'), table_name='tbl_gaji_master_penghasilan')
    op.drop_table('tbl_gaji_master_penghasilan')
    op.drop_index(op.f('ix_tbl_gaji_employee_status_kawin'), table_name='tbl_gaji_employee')
    op.drop_index(op.f('ix_tbl_gaji_employee_status_bekerja'), table_name='tbl_gaji_employee')
    op.drop_index(op.f('ix_tbl_gaji_employee_pangkat_id'), table_name='tbl_gaji_employee')
    op.drop_index(op.f('ix_tbl_gaji_employee_name'), table_name='tbl_gaji_employee')
    op.drop_index(op.f('ix_tbl_gaji_employee_masa_kerja'), table_name='tbl_gaji_employee')
    op.drop_index(op.f('ix_tbl_gaji_employee_jabatan_id'), table_name='tbl_gaji_employee')
    op.drop_index(op.f('ix_tbl_gaji_employee_id_type'), table_name='tbl_gaji_employee')
    op.drop_index(op.f('ix_tbl_gaji_employee_id_number'), table_name='tbl_gaji_employee')
    op.drop_index(op.f('ix_tbl_gaji_employee_id'), table_name='tbl_gaji_employee')
    op.drop_index(op.f('ix_tbl_gaji_employee_grade_id'), table_name='tbl_gaji_employee')
    op.drop_index(op.f('ix_tbl_gaji_employee_golongan_id'), table_name='tbl_gaji_employee')
    op.drop_index(op.f('ix_tbl_gaji_employee_client_id'), table_name='tbl_gaji_employee')
    op.drop_index(op.f('ix_tbl_gaji_employee_bpjs_id'), table_name='tbl_gaji_employee')
    op.drop_table('tbl_gaji_employee')
    op.drop_index(op.f('ix_tbl_activation_user_id'), table_name='tbl_activation')
    op.drop_index(op.f('ix_tbl_activation_id'), table_name='tbl_activation')
    op.drop_table('tbl_activation')
    op.drop_index(op.f('ix_tbl_user_username'), table_name='tbl_user')
    op.drop_index(op.f('ix_tbl_user_status'), table_name='tbl_user')
    op.drop_index(op.f('ix_tbl_user_name'), table_name='tbl_user')
    op.drop_index(op.f('ix_tbl_user_id_type'), table_name='tbl_user')
    op.drop_index(op.f('ix_tbl_user_id_number'), table_name='tbl_user')
    op.drop_index(op.f('ix_tbl_user_id'), table_name='tbl_user')
    op.drop_index(op.f('ix_tbl_user_group_id'), table_name='tbl_user')
    op.drop_index(op.f('ix_tbl_user_email'), table_name='tbl_user')
    op.drop_index(op.f('ix_tbl_user_client_id'), table_name='tbl_user')
    op.drop_table('tbl_user')
    op.drop_index(op.f('ix_set_gaji_status_kawin_status'), table_name='set_gaji_status_kawin')
    op.drop_index(op.f('ix_set_gaji_status_kawin_kode'), table_name='set_gaji_status_kawin')
    op.drop_index(op.f('ix_set_gaji_status_kawin_keterangan'), table_name='set_gaji_status_kawin')
    op.drop_index(op.f('ix_set_gaji_status_kawin_jenis_besaran'), table_name='set_gaji_status_kawin')
    op.drop_index(op.f('ix_set_gaji_status_kawin_id'), table_name='set_gaji_status_kawin')
    op.drop_index(op.f('ix_set_gaji_status_kawin_client_id'), table_name='set_gaji_status_kawin')
    op.drop_index(op.f('ix_set_gaji_status_kawin_besaran'), table_name='set_gaji_status_kawin')
    op.drop_table('set_gaji_status_kawin')
    op.drop_index(op.f('ix_set_gaji_potongan_status'), table_name='set_gaji_potongan')
    op.drop_index(op.f('ix_set_gaji_potongan_potongan'), table_name='set_gaji_potongan')
    op.drop_index(op.f('ix_set_gaji_potongan_jenis_besaran'), table_name='set_gaji_potongan')
    op.drop_index(op.f('ix_set_gaji_potongan_id'), table_name='set_gaji_potongan')
    op.drop_index(op.f('ix_set_gaji_potongan_client_id'), table_name='set_gaji_potongan')
    op.drop_index(op.f('ix_set_gaji_potongan_besaran'), table_name='set_gaji_potongan')
    op.drop_table('set_gaji_potongan')
    op.drop_index(op.f('ix_set_gaji_penghasilan_status'), table_name='set_gaji_penghasilan')
    op.drop_index(op.f('ix_set_gaji_penghasilan_komponen'), table_name='set_gaji_penghasilan')
    op.drop_index(op.f('ix_set_gaji_penghasilan_jenis_besaran'), table_name='set_gaji_penghasilan')
    op.drop_index(op.f('ix_set_gaji_penghasilan_id'), table_name='set_gaji_penghasilan')
    op.drop_index(op.f('ix_set_gaji_penghasilan_client_id'), table_name='set_gaji_penghasilan')
    op.drop_index(op.f('ix_set_gaji_penghasilan_besaran'), table_name='set_gaji_penghasilan')
    op.drop_table('set_gaji_penghasilan')
    op.drop_index(op.f('ix_set_gaji_pangkat_kode'), table_name='set_gaji_pangkat')
    op.drop_index(op.f('ix_set_gaji_pangkat_keterangan'), table_name='set_gaji_pangkat')
    op.drop_index(op.f('ix_set_gaji_pangkat_id'), table_name='set_gaji_pangkat')
    op.drop_index(op.f('ix_set_gaji_pangkat_client_id'), table_name='set_gaji_pangkat')
    op.drop_table('set_gaji_pangkat')
    op.drop_index(op.f('ix_set_gaji_jabatan_kode'), table_name='set_gaji_jabatan')
    op.drop_index(op.f('ix_set_gaji_jabatan_keterangan'), table_name='set_gaji_jabatan')
    op.drop_index(op.f('ix_set_gaji_jabatan_id'), table_name='set_gaji_jabatan')
    op.drop_index(op.f('ix_set_gaji_jabatan_client_id'), table_name='set_gaji_jabatan')
    op.drop_table('set_gaji_jabatan')
    op.drop_index(op.f('ix_set_gaji_grade_kode'), table_name='set_gaji_grade')
    op.drop_index(op.f('ix_set_gaji_grade_keterangan'), table_name='set_gaji_grade')
    op.drop_index(op.f('ix_set_gaji_grade_id'), table_name='set_gaji_grade')
    op.drop_index(op.f('ix_set_gaji_grade_client_id'), table_name='set_gaji_grade')
    op.drop_table('set_gaji_grade')
    op.drop_index(op.f('ix_set_gaji_golongan_kode'), table_name='set_gaji_golongan')
    op.drop_index(op.f('ix_set_gaji_golongan_keterangan'), table_name='set_gaji_golongan')
    op.drop_index(op.f('ix_set_gaji_golongan_id'), table_name='set_gaji_golongan')
    op.drop_index(op.f('ix_set_gaji_golongan_client_id'), table_name='set_gaji_golongan')
    op.drop_table('set_gaji_golongan')
    op.drop_index(op.f('ix_set_gaji_bpjs_status'), table_name='set_gaji_bpjs')
    op.drop_index(op.f('ix_set_gaji_bpjs_kode'), table_name='set_gaji_bpjs')
    op.drop_index(op.f('ix_set_gaji_bpjs_keterangan'), table_name='set_gaji_bpjs')
    op.drop_index(op.f('ix_set_gaji_bpjs_jenis_besaran'), table_name='set_gaji_bpjs')
    op.drop_index(op.f('ix_set_gaji_bpjs_id'), table_name='set_gaji_bpjs')
    op.drop_index(op.f('ix_set_gaji_bpjs_client_id'), table_name='set_gaji_bpjs')
    op.drop_index(op.f('ix_set_gaji_bpjs_besaran'), table_name='set_gaji_bpjs')
    op.drop_table('set_gaji_bpjs')
    op.drop_index(op.f('ix_tbl_client_responsible_id_type'), table_name='tbl_client')
    op.drop_index(op.f('ix_tbl_client_responsible_id_number'), table_name='tbl_client')
    op.drop_index(op.f('ix_tbl_client_name'), table_name='tbl_client')
    op.drop_index(op.f('ix_tbl_client_id'), table_name='tbl_client')
    op.drop_table('tbl_client')
    op.drop_index(op.f('ix_tbl_subscription_updated_at'), table_name='tbl_subscription')
    op.drop_index(op.f('ix_tbl_subscription_subs_start'), table_name='tbl_subscription')
    op.drop_index(op.f('ix_tbl_subscription_subs_price'), table_name='tbl_subscription')
    op.drop_index(op.f('ix_tbl_subscription_subs_plan'), table_name='tbl_subscription')
    op.drop_index(op.f('ix_tbl_subscription_subs_end'), table_name='tbl_subscription')
    op.drop_index(op.f('ix_tbl_subscription_id'), table_name='tbl_subscription')
    op.drop_index(op.f('ix_tbl_subscription_editor'), table_name='tbl_subscription')
    op.drop_index(op.f('ix_tbl_subscription_creator'), table_name='tbl_subscription')
    op.drop_index(op.f('ix_tbl_subscription_created_at'), table_name='tbl_subscription')
    op.drop_table('tbl_subscription')
    op.drop_index(op.f('ix_tbl_subscription_plan_updated_at'), table_name='tbl_subscription_plan')
    op.drop_index(op.f('ix_tbl_subscription_plan_plan'), table_name='tbl_subscription_plan')
    op.drop_index(op.f('ix_tbl_subscription_plan_monthly_price'), table_name='tbl_subscription_plan')
    op.drop_index(op.f('ix_tbl_subscription_plan_id'), table_name='tbl_subscription_plan')
    op.drop_index(op.f('ix_tbl_subscription_plan_editor'), table_name='tbl_subscription_plan')
    op.drop_index(op.f('ix_tbl_subscription_plan_creator'), table_name='tbl_subscription_plan')
    op.drop_index(op.f('ix_tbl_subscription_plan_created_at'), table_name='tbl_subscription_plan')
    op.drop_table('tbl_subscription_plan')
    op.drop_index(op.f('ix_ref_user_id_type_id_type'), table_name='ref_user_id_type')
    op.drop_index(op.f('ix_ref_user_id_type_id'), table_name='ref_user_id_type')
    op.drop_table('ref_user_id_type')
    op.drop_index(op.f('ix_ref_user_group_id'), table_name='ref_user_group')
    op.drop_index(op.f('ix_ref_user_group_group_name'), table_name='ref_user_group')
    op.drop_table('ref_user_group')
    # ### end Alembic commands ###
