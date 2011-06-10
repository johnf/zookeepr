"""Setup the zookeepr application"""
import logging

import pylons.test

from zookeepr.config.environment import load_environment
from zookeepr.model.meta import Session, Base

import zookeepr.model

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup zookeepr here"""
    # Don't reload the app if it was loaded under the testing environment
    if not pylons.test.pylonsapp:
        load_environment(conf.global_conf, conf.local_conf)

    # Create the tables if they don't already exist
    log.info("Creating tables...")
    Base.metadata.create_all(bind=Session.bind)

    log.info("Populating tables...")
    zookeepr.model.setup()

    log.info("Successfully set up.")
