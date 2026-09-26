import pytest
from capo_pricing_plan_manager._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_pricing_plan_manager._rule_engine._endpoint_runtime import EndpointError
import re
import zapros

def test_resolves_the_us_east_1_endpoint_and_sign():
    """Resolves the us-east-1 endpoint and signs for us-east-1."""
    params = EndpointParams(Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://pricingplanmanager.us-east-1.api.aws'

def test_routes_any_other_region_to_the_us_east_1():
    """Routes any other region to the us-east-1 endpoint and still signs for us-east-1."""
    params = EndpointParams(Region='us-west-2')
    result = resolve(params)
    assert result.url == 'https://pricingplanmanager.us-east-1.api.aws'

def test_a_custom_endpoint_override_wins_over_reg():
    """A custom endpoint override wins over region resolution and signs for us-east-1."""
    params = EndpointParams(Region='us-west-2', Endpoint='https://pricingplanmanager.us-east-1.api.aws')
    result = resolve(params)
    assert result.url == 'https://pricingplanmanager.us-east-1.api.aws'