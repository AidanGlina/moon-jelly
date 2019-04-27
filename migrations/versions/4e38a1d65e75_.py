"""empty message

Revision ID: 4e38a1d65e75
Revises: 0daa0acd5042
Create Date: 2019-04-26 18:50:16.954000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4e38a1d65e75'
down_revision = '0daa0acd5042'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_index('auth_user_user_permissions_permission_id_1fbb5f2c', table_name='auth_user_user_permissions')
    # op.drop_index('auth_user_user_permissions_user_id_a95ead1b', table_name='auth_user_user_permissions')
    # op.drop_table('auth_user_user_permissions')
    # op.drop_index('auth_group_name_a6ea08ec_like', table_name='auth_group')
    # op.drop_table('auth_group')
    # op.drop_table('django_content_type')
    # op.drop_index('django_session_expire_date_a5c62663', table_name='django_session')
    # op.drop_index('django_session_session_key_c0390e0f_like', table_name='django_session')
    # op.drop_table('django_session')
    # op.drop_table('hello_greeting')
    # op.drop_index('auth_user_groups_group_id_97559544', table_name='auth_user_groups')
    # op.drop_index('auth_user_groups_user_id_6a12ed8b', table_name='auth_user_groups')
    # op.drop_table('auth_user_groups')
    # op.drop_table('django_migrations')
    # op.drop_index('auth_user_username_6821ab7c_like', table_name='auth_user')
    # op.drop_table('auth_user')
    # op.drop_index('auth_permission_content_type_id_2f476e4b', table_name='auth_permission')
    # op.drop_table('auth_permission')
    # op.drop_index('django_admin_log_content_type_id_c4bce8eb', table_name='django_admin_log')
    # op.drop_index('django_admin_log_user_id_c564eba6', table_name='django_admin_log')
    # op.drop_table('django_admin_log')
    # op.drop_index('auth_group_permissions_group_id_b120cbf9', table_name='auth_group_permissions')
    # op.drop_index('auth_group_permissions_permission_id_84c5c92e', table_name='auth_group_permissions')
    # op.drop_table('auth_group_permissions')
    op.add_column('users', sa.Column('first_name', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('last_name', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('specialty', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'specialty')
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    # op.create_table('auth_group_permissions',
    # sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    # sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.Column('permission_id', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.ForeignKeyConstraint(['group_id'], [u'auth_group.id'], name=u'auth_group_permissions_group_id_b120cbf9_fk_auth_group_id', initially=u'DEFERRED', deferrable=True),
    # sa.ForeignKeyConstraint(['permission_id'], [u'auth_permission.id'], name=u'auth_group_permissio_permission_id_84c5c92e_fk_auth_perm', initially=u'DEFERRED', deferrable=True),
    # sa.PrimaryKeyConstraint('id', name=u'auth_group_permissions_pkey'),
    # sa.UniqueConstraint('group_id', 'permission_id', name=u'auth_group_permissions_group_id_permission_id_0cd325b0_uniq')
    # )
    # op.create_index('auth_group_permissions_permission_id_84c5c92e', 'auth_group_permissions', ['permission_id'], unique=False)
    # op.create_index('auth_group_permissions_group_id_b120cbf9', 'auth_group_permissions', ['group_id'], unique=False)
    # op.create_table('django_admin_log',
    # sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    # sa.Column('action_time', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    # sa.Column('object_id', sa.TEXT(), autoincrement=False, nullable=True),
    # sa.Column('object_repr', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    # sa.Column('action_flag', sa.SMALLINT(), autoincrement=False, nullable=False),
    # sa.Column('change_message', sa.TEXT(), autoincrement=False, nullable=False),
    # sa.Column('content_type_id', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.CheckConstraint(u'action_flag >= 0', name=u'django_admin_log_action_flag_check'),
    # sa.ForeignKeyConstraint(['content_type_id'], [u'django_content_type.id'], name=u'django_admin_log_content_type_id_c4bce8eb_fk_django_co', initially=u'DEFERRED', deferrable=True),
    # sa.ForeignKeyConstraint(['user_id'], [u'auth_user.id'], name=u'django_admin_log_user_id_c564eba6_fk_auth_user_id', initially=u'DEFERRED', deferrable=True),
    # sa.PrimaryKeyConstraint('id', name=u'django_admin_log_pkey')
    # )
    # op.create_index('django_admin_log_user_id_c564eba6', 'django_admin_log', ['user_id'], unique=False)
    # op.create_index('django_admin_log_content_type_id_c4bce8eb', 'django_admin_log', ['content_type_id'], unique=False)
    # op.create_table('auth_permission',
    # sa.Column('id', sa.INTEGER(), server_default=sa.text(u"nextval('auth_permission_id_seq'::regclass)"), autoincrement=True, nullable=False),
    # sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    # sa.Column('content_type_id', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.Column('codename', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    # sa.ForeignKeyConstraint(['content_type_id'], [u'django_content_type.id'], name=u'auth_permission_content_type_id_2f476e4b_fk_django_co', initially=u'DEFERRED', deferrable=True),
    # sa.PrimaryKeyConstraint('id', name=u'auth_permission_pkey'),
    # sa.UniqueConstraint('content_type_id', 'codename', name=u'auth_permission_content_type_id_codename_01ab375a_uniq'),
    # postgresql_ignore_search_path=False
    # )
    # op.create_index('auth_permission_content_type_id_2f476e4b', 'auth_permission', ['content_type_id'], unique=False)
    # op.create_table('auth_user',
    # sa.Column('id', sa.INTEGER(), server_default=sa.text(u"nextval('auth_user_id_seq'::regclass)"), autoincrement=True, nullable=False),
    # sa.Column('password', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    # sa.Column('last_login', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    # sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=False),
    # sa.Column('username', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    # sa.Column('first_name', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    # sa.Column('last_name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    # sa.Column('email', sa.VARCHAR(length=254), autoincrement=False, nullable=False),
    # sa.Column('is_staff', sa.BOOLEAN(), autoincrement=False, nullable=False),
    # sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    # sa.Column('date_joined', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    # sa.PrimaryKeyConstraint('id', name=u'auth_user_pkey'),
    # sa.UniqueConstraint('username', name=u'auth_user_username_key'),
    # postgresql_ignore_search_path=False
    # )
    # op.create_index('auth_user_username_6821ab7c_like', 'auth_user', ['username'], unique=False)
    # op.create_table('django_migrations',
    # sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    # sa.Column('app', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    # sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    # sa.Column('applied', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    # sa.PrimaryKeyConstraint('id', name=u'django_migrations_pkey')
    # )
    # op.create_table('auth_user_groups',
    # sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    # sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.ForeignKeyConstraint(['group_id'], [u'auth_group.id'], name=u'auth_user_groups_group_id_97559544_fk_auth_group_id', initially=u'DEFERRED', deferrable=True),
    # sa.ForeignKeyConstraint(['user_id'], [u'auth_user.id'], name=u'auth_user_groups_user_id_6a12ed8b_fk_auth_user_id', initially=u'DEFERRED', deferrable=True),
    # sa.PrimaryKeyConstraint('id', name=u'auth_user_groups_pkey'),
    # sa.UniqueConstraint('user_id', 'group_id', name=u'auth_user_groups_user_id_group_id_94350c0c_uniq')
    # )
    # op.create_index('auth_user_groups_user_id_6a12ed8b', 'auth_user_groups', ['user_id'], unique=False)
    # op.create_index('auth_user_groups_group_id_97559544', 'auth_user_groups', ['group_id'], unique=False)
    # op.create_table('hello_greeting',
    # sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    # sa.Column('when', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    # sa.PrimaryKeyConstraint('id', name=u'hello_greeting_pkey')
    # )
    # op.create_table('django_session',
    # sa.Column('session_key', sa.VARCHAR(length=40), autoincrement=False, nullable=False),
    # sa.Column('session_data', sa.TEXT(), autoincrement=False, nullable=False),
    # sa.Column('expire_date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    # sa.PrimaryKeyConstraint('session_key', name=u'django_session_pkey')
    # )
    # op.create_index('django_session_session_key_c0390e0f_like', 'django_session', ['session_key'], unique=False)
    # op.create_index('django_session_expire_date_a5c62663', 'django_session', ['expire_date'], unique=False)
    # op.create_table('django_content_type',
    # sa.Column('id', sa.INTEGER(), server_default=sa.text(u"nextval('django_content_type_id_seq'::regclass)"), autoincrement=True, nullable=False),
    # sa.Column('app_label', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    # sa.Column('model', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    # sa.PrimaryKeyConstraint('id', name=u'django_content_type_pkey'),
    # sa.UniqueConstraint('app_label', 'model', name=u'django_content_type_app_label_model_76bd3d3b_uniq'),
    # postgresql_ignore_search_path=False
    # )
    # op.create_table('auth_group',
    # sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    # sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    # sa.PrimaryKeyConstraint('id', name=u'auth_group_pkey'),
    # sa.UniqueConstraint('name', name=u'auth_group_name_key')
    # )
    # op.create_index('auth_group_name_a6ea08ec_like', 'auth_group', ['name'], unique=False)
    # op.create_table('auth_user_user_permissions',
    # sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    # sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.Column('permission_id', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.ForeignKeyConstraint(['permission_id'], [u'auth_permission.id'], name=u'auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm', initially=u'DEFERRED', deferrable=True),
    # sa.ForeignKeyConstraint(['user_id'], [u'auth_user.id'], name=u'auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id', initially=u'DEFERRED', deferrable=True),
    # sa.PrimaryKeyConstraint('id', name=u'auth_user_user_permissions_pkey'),
    # sa.UniqueConstraint('user_id', 'permission_id', name=u'auth_user_user_permissions_user_id_permission_id_14a6b632_uniq')
    # )
    # op.create_index('auth_user_user_permissions_user_id_a95ead1b', 'auth_user_user_permissions', ['user_id'], unique=False)
    # op.create_index('auth_user_user_permissions_permission_id_1fbb5f2c', 'auth_user_user_permissions', ['permission_id'], unique=False)
    # ### end Alembic commands ###
