from charms.layer import status
from charms.reactive import when, when_not, set_flag
from charmhelpers.core import host


@when_not('java.ready')
def no_java():
    """
    Wait on the Java relation.
    """
    status.blocked('Missing JRE.')

@when('java.ready')
@when_not('apt.installed.elasticsearch')
def install_elasticsearch():
    """
    Apt layer will take care of this.
    """
    status.maintenance('Preparing to install.')

@when('java.ready')
@when('apt.installed.elasticsearch')
def start_elasticsearch():
    """
    Make sure the service is running.
    """
    if not host.service_running('elasticsearch'):
        host.service_start('elasticsearch')
        status.ready('Ready.')