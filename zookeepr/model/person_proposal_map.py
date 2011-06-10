"""The application's model objects"""
import sqlalchemy as sa

from zookeepr.model.meta import Base

# for doing n-n mappings of people and proposals
person_proposal_map = sa.Table('person_proposal_map', Base.metadata,
        sa.Column('person_id', sa.types.Integer, sa.ForeignKey('person.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False),
        sa.Column('proposal_id',   sa.types.Integer, sa.ForeignKey('proposal.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
)
