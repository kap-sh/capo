import pytest
from capo_agent_registry_control._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_agent_registry_control._rule_engine._endpoint_runtime import EndpointError
import re
import zapros

def test_region_us_west_2____region_based_prod_ho():
    """Region us-west-2 -> region-based prod host."""
    params = EndpointParams(Region='us-west-2')
    result = resolve(params)
    assert result.url == 'https://agent-registry-control.us-west-2.api.aws'

def test_region_us_east_1____region_based_prod_ho():
    """Region us-east-1 -> region-based prod host."""
    params = EndpointParams(Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://agent-registry-control.us-east-1.api.aws'

def test_endpoint_override_wins_over_region_():
    """Endpoint override wins over region."""
    params = EndpointParams(Region='us-west-2', Endpoint='https://custom.example.aws.dev')
    result = resolve(params)
    assert result.url == 'https://custom.example.aws.dev'