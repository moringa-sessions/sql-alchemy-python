
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3561c3e117a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("users",
        sa.Column("id", sa.Integer(), nullable= False),        
        sa.Column("username", sa.String(), nullable= False), 
        sa.Column("email", sa.String(), nullable= False), 
        sa.Column("phone", sa.Integer(), nullable= False),

        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint("username"),
        sa.UniqueConstraint("email"),
        )
    
    op.create_table("posts",
        sa.Column("id", sa.Integer(), nullable= False),        
        sa.Column("title", sa.String(), nullable= False), 
        sa.Column("description", sa.Text(), nullable= False), 
        sa.Column("is_active", sa.Boolean(), default= True),
        sa.Column("created_at", sa.DateTime(timezone=True), default= sa.func.now()), 

        sa.Column("user_id", sa.Integer(), nullable= False), 
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"])

        )


def downgrade() -> None:
    pass
