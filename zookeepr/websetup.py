"""Setup the zookeepr application"""
import logging

from zookeepr.config.environment import load_environment
from zookeepr.model import meta
import pylons.test

import zookeepr.model

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    # Don't reload the app if it was loaded under the testing environment
    if not pylons.test.pylonsapp:
        load_environment(conf.global_conf, conf.local_conf)
    """Place any commands to setup zookeepr here"""

    # Create the tables if they don't already exist
    log.info("Creating tables...")
    meta.metadata.create_all(bind=meta.engine)

    log.info("Populating tables...")
    zookeepr.model.setup(meta)

    log.info("Successfully set up.")


