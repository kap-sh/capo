import pytest
from capo_opensearchmemory._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_opensearchmemory._rule_engine._endpoint_runtime import EndpointError
import re
import zapros

def test_a_space_id_that_is_not_a_host_label_is_r():
    """A space ID that is not a host label is rejected rather than put in the host name."""
    params = EndpointParams(Region='us-east-1', SpaceId='evil.example/#')
    with pytest.raises(EndpointError, match=re.escape('Invalid SpaceId: must be a valid host label')):
        resolve(params)

def test_a_region_that_is_not_a_host_label_is_rej():
    """A Region that is not a host label is rejected."""
    params = EndpointParams(Region='us-east-1/#')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Region must be a valid host label')):
        resolve(params)

def test_a_space_id_containing_a_dot_is_rejected_():
    """A space ID containing a dot is rejected rather than split across host labels."""
    params = EndpointParams(Region='us-east-1', SpaceId='sp-abc.def123')
    with pytest.raises(EndpointError, match=re.escape('Invalid SpaceId: must be a valid host label')):
        resolve(params)

def test_getmemory_goes_to_the_endpoint_of_the_sp():
    """GetMemory goes to the endpoint of the space in its input."""
    params = EndpointParams(Region='us-east-1', SpaceId='sp-abc123def456')
    result = resolve(params)
    assert result.url == 'https://sp-abc123def456.osm.us-east-1.on.aws'

def test_listspaces_goes_to_the_regional_endpoint():
    """ListSpaces goes to the regional endpoint."""
    params = EndpointParams(Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://osm.us-east-1.api.aws'

def test_with_a_space_id__the_space_s_endpoint_():
    """With a space ID: the space's endpoint."""
    params = EndpointParams(Region='us-east-1', SpaceId='sp-abc123def456')
    result = resolve(params)
    assert result.url == 'https://sp-abc123def456.osm.us-east-1.on.aws'

def test_without_a_space_id__the_regional_endpoin():
    """Without a space ID: the regional endpoint."""
    params = EndpointParams(Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://osm.us-east-1.api.aws'

def test_endpoint_override_with_a_space_id__the_o():
    """Endpoint override with a space ID: the override URL."""
    params = EndpointParams(Region='us-east-1', SpaceId='sp-000000000000', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_endpoint_override_without_a_space_id__th():
    """Endpoint override without a space ID: the override URL."""
    params = EndpointParams(Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_fips_without_a_space_id_fails__the_servi():
    """FIPS without a space ID fails: the service has no FIPS endpoint."""
    params = EndpointParams(Region='us-east-1', UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS is not supported with OpenSearch Memory.')):
        resolve(params)

def test_fips_with_a_space_id_fails__the_service_():
    """FIPS with a space ID fails: the service has no FIPS endpoint."""
    params = EndpointParams(Region='us-east-1', SpaceId='sp-abc123def456', UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS is not supported with OpenSearch Memory.')):
        resolve(params)

def test_fips_with_an_endpoint_override_fails_():
    """FIPS with an endpoint override fails."""
    params = EndpointParams(Region='us-east-1', Endpoint='https://example.com', UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_getmemory_with_fips_on_fails_rather_than():
    """GetMemory with FIPS on fails rather than going to the space's endpoint."""
    params = EndpointParams(Region='us-east-1', SpaceId='sp-abc123def456', UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS is not supported with OpenSearch Memory.')):
        resolve(params)

def test_listspaces_with_fips_on_fails_rather_tha():
    """ListSpaces with FIPS on fails rather than going to the regional endpoint."""
    params = EndpointParams(Region='us-east-1', UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS is not supported with OpenSearch Memory.')):
        resolve(params)