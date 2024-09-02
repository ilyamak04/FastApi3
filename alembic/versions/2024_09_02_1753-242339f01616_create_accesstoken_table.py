"""create AccessToken table

Revision ID: 242339f01616
Revises: 0c1aa2ba12e0
Create Date: 2024-09-02 17:53:43.021199

"""

from typing import Sequence, Union

import fastapi_users_db_sqlalchemy
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "242339f01616"
down_revision: Union[str, None] = "0c1aa2ba12e0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "access_token",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("token", sa.String(length=43), nullable=False),
        sa.Column(
            "created_at",
            fastapi_users_db_sqlalchemy.generics.TIMESTAMPAware(timezone=True),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
            name=op.f("fk_access_token_user_id_user"),
            ondelete="cascade",
        ),
        sa.PrimaryKeyConstraint("id", "token", name=op.f("pk_access_token")),
    )
    op.create_index(
        op.f("ix_access_token_created_at"), "access_token", ["created_at"], unique=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_access_token_created_at"), table_name="access_token")
    op.drop_table("access_token")
    # ### end Alembic commands ###