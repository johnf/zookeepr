"""The application's model objects"""
from zookeepr.model.meta import Session, Base

from sqlalchemy.exc import IntegrityError

import person
import role
import person_role_map
import password_reset_confirmation
import proposal
import person_proposal_map
import attachment
import review
import db_content
import volunteer
import voucher
import invoice
import invoice_item
import payment
import ceiling
import product
import product_ceiling_map
import rego_note
import social_network
import person_social_network_map
import funding
import funding_attachment
import funding_review
import special_offer
import special_registration
import url_hash
import schedule

from person import Person
from role import Role
from password_reset_confirmation import PasswordResetConfirmation

from social_network import SocialNetwork

from proposal import Proposal, ProposalStatus, ProposalType, TravelAssistanceType, AccommodationAssistanceType, TargetAudience
from attachment import Attachment
from review import Review, Stream
from funding import Funding, FundingType, FundingStatus
from funding_attachment import FundingAttachment
from funding_review import FundingReview

from product import Product, ProductInclude
from product_category import ProductCategory
from ceiling import Ceiling

from payment_allocation import PaymentAllocation
from invoice import Invoice
from invoice_item import InvoiceItem
from payment import Payment
from payment_received import PaymentReceived

from registration import Registration
from registration_product import RegistrationProduct

from location import Location
from event    import Event
from event_type import EventType
from time_slot import TimeSlot
from schedule import Schedule

from voucher import Voucher, VoucherProduct

from db_content import DbContentType, DbContent

from url_hash import URLHash

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)


def setup():
    """Setup any data in the tables"""
    try:
        role.setup()
        person.setup()

        social_network.setup()

        product_category.setup()
        ceiling.setup()
        product.setup()

        proposal.setup()

        db_content.setup()

        funding.setup()

        Session.commit()
    except IntegrityError, inst:
        print inst

## Non-reflected tables may be defined and mapped at module level
#foo_table = sa.Table("Foo", meta.metadata,
#    sa.Column("id", sa.types.Integer, primary_key=True),
#    sa.Column("bar", sa.types.String(255), nullable=False),
#    )
#
#class Foo(object):
#    pass
#
#orm.mapper(Foo, foo_table)


## Classes for reflected tables may be defined here, but the table and
## mapping itself must be done in the init_model function
#reflected_table = None
#
#class Reflected(object):
#    pass
