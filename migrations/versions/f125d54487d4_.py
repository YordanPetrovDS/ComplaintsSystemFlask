"""empty message

Revision ID: f125d54487d4
Revises: 
Create Date: 2021-12-05 20:08:55.624733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f125d54487d4"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "administrators",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(length=255), nullable=False),
        sa.Column("last_name", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("phone", sa.String(length=13), nullable=False),
        sa.Column("password", sa.String(length=255), nullable=False),
        sa.Column(
            "role",
            sa.Enum("complainer", "approver", "admin", name="roletype"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_table(
        "approvers",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(length=255), nullable=False),
        sa.Column("last_name", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("phone", sa.String(length=13), nullable=False),
        sa.Column("password", sa.String(length=255), nullable=False),
        sa.Column("certificate", sa.String(length=255), nullable=False),
        sa.Column(
            "role",
            sa.Enum("complainer", "approver", "admin", name="roletype"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_table(
        "complainers",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(length=255), nullable=False),
        sa.Column("last_name", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("phone", sa.String(length=13), nullable=False),
        sa.Column("password", sa.String(length=255), nullable=False),
        sa.Column("iban", sa.String(length=22), nullable=True),
        sa.Column(
            "role",
            sa.Enum("complainer", "approver", "admin", name="roletype"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("complainers")
    op.drop_table("approvers")
    op.drop_table("administrators")
    # ### end Alembic commands ###
