"""The application's model objects"""
import sqlalchemy as sa

from zookeepr.model.meta import Base

person_role_map = sa.Table('person_role_map', Base.metadata,
        sa.Column('person_id', sa.types.Integer, sa.ForeignKey('person.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False),
        sa.Column('role_id',   sa.types.Integer, sa.ForeignKey('role.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
)
