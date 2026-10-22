import pytest
from capo_dynamodb._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_dynamodb._rule_engine._endpoint_runtime import EndpointError
import re
import zapros

def test_for_region_af_south_1_with_fips_disabled():
    """For region af-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='af-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.af-south-1.amazonaws.com'

def test_for_region_ap_east_1_with_fips_disabled_():
    """For region ap-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.ap-east-1.amazonaws.com'

def test_for_region_ap_northeast_1_with_fips_disa():
    """For region ap-northeast-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.ap-northeast-1.amazonaws.com'

def test_for_region_ap_northeast_2_with_fips_disa():
    """For region ap-northeast-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.ap-northeast-2.amazonaws.com'

def test_for_region_ap_northeast_3_with_fips_disa():
    """For region ap-northeast-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-3', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.ap-northeast-3.amazonaws.com'

def test_for_region_ap_south_1_with_fips_disabled():
    """For region ap-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.ap-south-1.amazonaws.com'

def test_for_region_ap_southeast_1_with_fips_disa():
    """For region ap-southeast-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.ap-southeast-1.amazonaws.com'

def test_for_region_ap_southeast_2_with_fips_disa():
    """For region ap-southeast-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.ap-southeast-2.amazonaws.com'

def test_for_region_ap_southeast_3_with_fips_disa():
    """For region ap-southeast-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-3', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.ap-southeast-3.amazonaws.com'

def test_for_region_ca_central_1_with_fips_disabl():
    """For region ca-central-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ca-central-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.ca-central-1.amazonaws.com'

def test_for_region_ca_central_1_with_fips_enable():
    """For region ca-central-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='ca-central-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.ca-central-1.amazonaws.com'

def test_for_region_eu_central_1_with_fips_disabl():
    """For region eu-central-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-central-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.eu-central-1.amazonaws.com'

def test_for_region_eu_north_1_with_fips_disabled():
    """For region eu-north-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-north-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.eu-north-1.amazonaws.com'

def test_for_region_eu_south_1_with_fips_disabled():
    """For region eu-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.eu-south-1.amazonaws.com'

def test_for_region_eu_west_1_with_fips_disabled_():
    """For region eu-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.eu-west-1.amazonaws.com'

def test_for_region_eu_west_2_with_fips_disabled_():
    """For region eu-west-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.eu-west-2.amazonaws.com'

def test_for_region_eu_west_3_with_fips_disabled_():
    """For region eu-west-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-3', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.eu-west-3.amazonaws.com'

def test_for_region_local_with_fips_disabled_and_():
    """For region local with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='local', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_for_region_me_south_1_with_fips_disabled():
    """For region me-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='me-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.me-south-1.amazonaws.com'

def test_for_region_sa_east_1_with_fips_disabled_():
    """For region sa-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='sa-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.sa-east-1.amazonaws.com'

def test_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.amazonaws.com'

def test_for_region_us_east_2_with_fips_disabled_():
    """For region us-east-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-2.amazonaws.com'

def test_for_region_us_east_2_with_fips_enabled_a():
    """For region us-east-2 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-2', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-2.amazonaws.com'

def test_for_region_us_west_1_with_fips_disabled_():
    """For region us-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-west-1.amazonaws.com'

def test_for_region_us_west_1_with_fips_enabled_a():
    """For region us-west-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-west-1.amazonaws.com'

def test_for_region_us_west_2_with_fips_disabled_():
    """For region us-west-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-west-2.amazonaws.com'

def test_for_region_us_west_2_with_fips_enabled_a():
    """For region us-west-2 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-2', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-west-2.amazonaws.com'

def test_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.api.aws'

def test_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.api.aws'

def test_for_region_cn_north_1_with_fips_disabled():
    """For region cn-north-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.amazonaws.com.cn'

def test_for_region_cn_northwest_1_with_fips_disa():
    """For region cn-northwest-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-northwest-1.amazonaws.com.cn'

def test_for_region_cn_north_1_with_fips_enabled_():
    """For region cn-north-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test_for_region_cn_north_1_with_fips_enabled_():
    """For region cn-north-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.cn-north-1.amazonaws.com.cn'

def test_for_region_cn_north_1_with_fips_disabled():
    """For region cn-north-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.api.amazonwebservices.com.cn'

def test_for_region_us_gov_east_1_with_fips_disab():
    """For region us-gov-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test_for_region_us_gov_east_1_with_fips_enabl():
    """For region us-gov-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test_for_region_us_gov_west_1_with_fips_disab():
    """For region us-gov-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-west-1.amazonaws.com'

def test_for_region_us_gov_west_1_with_fips_enabl():
    """For region us-gov-west-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-west-1.amazonaws.com'

def test_for_region_us_gov_east_1_with_fips_enabl():
    """For region us-gov-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-gov-east-1.api.aws'

def test_for_region_us_gov_east_1_with_fips_disab():
    """For region us-gov-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.api.aws'

def test_for_region_us_iso_east_1_with_fips_disab():
    """For region us-iso-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.c2s.ic.gov'

def test_for_region_us_iso_west_1_with_fips_disab():
    """For region us-iso-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-west-1.c2s.ic.gov'

def test_for_region_us_iso_east_1_with_fips_enabl():
    """For region us-iso-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-iso-east-1.c2s.ic.gov'

def test_for_region_us_isob_east_1_with_fips_disa():
    """For region us-isob-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-isob-east-1.sc2s.sgov.gov'

def test_for_region_us_isob_east_1_with_fips_enab():
    """For region us-isob-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-isob-east-1.sc2s.sgov.gov'

def test_for_custom_endpoint_with_region_set_and_():
    """For custom endpoint with region set and fips disabled and dualstack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_for_custom_endpoint_with_region_not_set_():
    """For custom endpoint with region not set and fips disabled and dualstack disabled"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_for_custom_endpoint_with_fips_enabled_an():
    """For custom endpoint with fips enabled and dualstack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_for_custom_endpoint_with_fips_disabled_a():
    """For custom endpoint with fips disabled and dualstack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test_missing_region():
    """Missing region"""
    params = EndpointParams()
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Missing Region')):
        resolve(params)

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false, Endpoint=https://example.com}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False, Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true, Endpoint=https://example.com}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True, Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false, Endpoint=https://example.com}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False, Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true, Endpoint=https://example.com}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True, Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false, Endpoint=https://example.com}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False, Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true, Endpoint=https://example.com}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True, Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false, Endpoint=https://example.com}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False, Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true, Endpoint=https://example.com}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True, Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false, Endpoint=https://example.com}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False, Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true, Endpoint=https://example.com}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True, Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false, Endpoint=https://example.com}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False, Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true, Endpoint=https://example.com}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True, Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test__endpoint_https___dynamodb_cn_north_1_ap():
    """{Endpoint=https://dynamodb.cn-north-1.api.amazonwebservices.com.cn, Region=cn-north-1, AccountIdEndpointMode=preferred}"""
    params = EndpointParams(Endpoint='https://dynamodb.cn-north-1.api.amazonwebservices.com.cn', Region='cn-north-1', AccountIdEndpointMode='preferred')
    with pytest.raises(EndpointError, match=re.escape('Endpoint override is not supported for dual-stack endpoints. Please enable dual-stack functionality by enabling the configuration. For more details, see: https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html')):
        resolve(params)

def test__endpoint_https___dynamodb_us_gov_east_1():
    """{Endpoint=https://dynamodb.us-gov-east-1.api.aws, Region=us-gov-east-1, AccountIdEndpointMode=preferred}"""
    params = EndpointParams(Endpoint='https://dynamodb.us-gov-east-1.api.aws', Region='us-gov-east-1', AccountIdEndpointMode='preferred')
    with pytest.raises(EndpointError, match=re.escape('Endpoint override is not supported for dual-stack endpoints. Please enable dual-stack functionality by enabling the configuration. For more details, see: https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html')):
        resolve(params)

def test__endpoint_https___dynamodb_us_east_1_api():
    """{Endpoint=https://dynamodb.us-east-1.api.aws, Region=us-east-1, AccountIdEndpointMode=preferred}"""
    params = EndpointParams(Endpoint='https://dynamodb.us-east-1.api.aws', Region='us-east-1', AccountIdEndpointMode='preferred')
    with pytest.raises(EndpointError, match=re.escape('Endpoint override is not supported for dual-stack endpoints. Please enable dual-stack functionality by enabling the configuration. For more details, see: https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html')):
        resolve(params)

def test__endpoint_https___111111111111_ddb_us_ea():
    """{Endpoint=https://111111111111.ddb.us-east-1.api.aws, Region=us-east-1, AccountIdEndpointMode=preferred}"""
    params = EndpointParams(Endpoint='https://111111111111.ddb.us-east-1.api.aws', Region='us-east-1', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-east-1.api.aws'

def test__endpoint_https___vpce_1a2b3c4d_5e6f_dyn():
    """{Endpoint=https://vpce-1a2b3c4d-5e6f.dynamodb.us-east-1.vpce.api.aws, Region=us-east-1, AccountIdEndpointMode=preferred}"""
    params = EndpointParams(Endpoint='https://vpce-1a2b3c4d-5e6f.dynamodb.us-east-1.vpce.api.aws', Region='us-east-1', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://vpce-1a2b3c4d-5e6f.dynamodb.us-east-1.vpce.api.aws'

def test__endpoint_https___dynamodb_eu_west_1_api():
    """{Endpoint=https://dynamodb.eu-west-1.api.aws, Region=eu-west-1, AccountIdEndpointMode=preferred}"""
    params = EndpointParams(Endpoint='https://dynamodb.eu-west-1.api.aws', Region='eu-west-1', AccountIdEndpointMode='preferred')
    with pytest.raises(EndpointError, match=re.escape('Endpoint override is not supported for dual-stack endpoints. Please enable dual-stack functionality by enabling the configuration. For more details, see: https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html')):
        resolve(params)

def test__endpoint_https___dynamodb_us_west_2_api():
    """{Endpoint=https://dynamodb.us-west-2.api.aws, Region=us-west-2, AccountIdEndpointMode=preferred}"""
    params = EndpointParams(Endpoint='https://dynamodb.us-west-2.api.aws', Region='us-west-2', AccountIdEndpointMode='preferred')
    with pytest.raises(EndpointError, match=re.escape('Endpoint override is not supported for dual-stack endpoints. Please enable dual-stack functionality by enabling the configuration. For more details, see: https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html')):
        resolve(params)

def test__endpoint_https___dynamodb_us_east_1_api():
    """{Endpoint=https://dynamodb.us-east-1.api.aws/, Region=us-east-1, AccountIdEndpointMode=preferred}"""
    params = EndpointParams(Endpoint='https://dynamodb.us-east-1.api.aws/', Region='us-east-1', AccountIdEndpointMode='preferred')
    with pytest.raises(EndpointError, match=re.escape('Endpoint override is not supported for dual-stack endpoints. Please enable dual-stack functionality by enabling the configuration. For more details, see: https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html')):
        resolve(params)

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and local endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and local endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and local endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test__usefips_false__usedualstack_false_():
    """{UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Missing Region')):
        resolve(params)

def test__region_us_east_1__accountidendpointmode():
    """{Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:not_an_account:table/table_name}"""
    params = EndpointParams(Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:not_an_account:table/table_name')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__region_us_east_1__accountidendpointmode():
    """{Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-east-1.amazonaws.com'

def test__accountid___region_us_east_1__accountid():
    """{AccountId=, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Credentials-sourced account ID parameter is invalid')):
        resolve(params)

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.us-east-1.amazonaws.com'

def test__resourcearn___region_us_east_1__account():
    """{ResourceArn=, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__resourcearnlist_____region_us_east_1__a():
    """{ResourceArnList=[], Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=[], Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__resourcearn_arn_aws_dynamodb_af_south_1():
    """{ResourceArn=arn:aws:dynamodb:af-south-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:af-south-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__resourcearn_arn_aws_s3_us_east_1_222222():
    """{ResourceArn=arn:aws:s3:us-east-1:222222222222:stream/testStream, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws:s3:us-east-1:222222222222:stream/testStream', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__resourcearnlist__arn_aws_dynamodb_us_ea():
    """{ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-east-1.amazonaws.com'

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__resourcearnlist():
    """{AccountId=111111111111, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__resourcearn_arn():
    """{AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__resourcearn_arn():
    """{AccountId=111111111111, ResourceArn=arn:aws:dynamodb:af-south-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArn='arn:aws:dynamodb:af-south-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__resourcearn_arn():
    """{AccountId=111111111111, ResourceArn=arn:aws:s3:us-east-1:222222222222:stream/testStream, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArn='arn:aws:s3:us-east-1:222222222222:stream/testStream', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__resourcearn_arn():
    """{AccountId=111111111111, ResourceArn=arn:aws:s3:af-south-1:222222222222:stream/testStream, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArn='arn:aws:s3:af-south-1:222222222222:stream/testStream', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__resourcearn_arn():
    """{AccountId=111111111111, ResourceArn=arn:aws:s3:af-south-1:222222222222:stream/testStream, ResourceArnList=[arn:aws:s3:us-east-1:333333333333:stream/testStream], Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArn='arn:aws:s3:af-south-1:222222222222:stream/testStream', ResourceArnList=['arn:aws:s3:us-east-1:333333333333:stream/testStream'], Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-east-1.amazonaws.com'

def test__resourcearn_arn_aws_s3_af_south_1_22222():
    """{ResourceArn=arn:aws:s3:af-south-1:222222222222:stream/testStream, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws:s3:af-south-1:222222222222:stream/testStream', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__resourcearn_arn():
    """{AccountId=111111111111, ResourceArn=arn:aws:dynamodb:af-south-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:af-south-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArn='arn:aws:dynamodb:af-south-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:af-south-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__resourcearn_arn():
    """{AccountId=111111111111, ResourceArn=arn:aws:s3:us-east-1:222222222222:stream/testStream, ResourceArnList=[arn:aws:s3:us-east-1:333333333333:stream/testStream], Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArn='arn:aws:s3:us-east-1:222222222222:stream/testStream', ResourceArnList=['arn:aws:s3:us-east-1:333333333333:stream/testStream'], Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-east-1.api.aws'

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.us-east-1.api.aws'

def test__resourcearnlist__arn_aws_dynamodb_us_ea():
    """{ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-east-1.api.aws'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.amazonaws.com'

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.amazonaws.com'

def test__resourcearnlist__arn_aws_dynamodb_us_ea():
    """{ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.api.aws'

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.api.aws'

def test__resourcearnlist__arn_aws_dynamodb_us_ea():
    """{ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.api.aws'

def test__region_us_east_1__accountidendpointmode():
    """{Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__accountid___region_us_east_1__accountid():
    """{AccountId=, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__resourcearn___region_us_east_1__account():
    """{ResourceArn=, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__resourcearnlist_____region_us_east_1__a():
    """{ResourceArnList=[], Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=[], Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__resourcearn_arn_aws_dynamodb_af_south_1():
    """{ResourceArn=arn:aws:dynamodb:af-south-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:af-south-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__resourcearn_arn_aws_s3_us_east_1_222222():
    """{ResourceArn=arn:aws:s3:us-east-1:222222222222:stream/testStream, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws:s3:us-east-1:222222222222:stream/testStream', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__resourcearnlist__arn_aws_dynamodb_us_ea():
    """{ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__resourcearnlist():
    """{AccountId=111111111111, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__resourcearn_arn():
    """{AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__resourcearn_arn():
    """{AccountId=111111111111, ResourceArn=arn:aws:dynamodb:af-south-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArn='arn:aws:dynamodb:af-south-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__resourcearn_arn():
    """{AccountId=111111111111, ResourceArn=arn:aws:s3:us-east-1:222222222222:stream/testStream, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArn='arn:aws:s3:us-east-1:222222222222:stream/testStream', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__resourcearn_arn():
    """{AccountId=111111111111, ResourceArn=arn:aws:s3:af-south-1:222222222222:stream/testStream, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArn='arn:aws:s3:af-south-1:222222222222:stream/testStream', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__resourcearn_arn():
    """{AccountId=111111111111, ResourceArn=arn:aws:s3:af-south-1:222222222222:stream/testStream, ResourceArnList=[arn:aws:s3:us-east-1:333333333333:stream/testStream], Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArn='arn:aws:s3:af-south-1:222222222222:stream/testStream', ResourceArnList=['arn:aws:s3:us-east-1:333333333333:stream/testStream'], Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__resourcearn_arn_aws_s3_af_south_1_22222():
    """{ResourceArn=arn:aws:s3:af-south-1:222222222222:stream/testStream, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws:s3:af-south-1:222222222222:stream/testStream', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__resourcearn_arn():
    """{AccountId=111111111111, ResourceArn=arn:aws:dynamodb:af-south-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:af-south-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArn='arn:aws:dynamodb:af-south-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:af-south-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__resourcearn_arn():
    """{AccountId=111111111111, ResourceArn=arn:aws:s3:us-east-1:222222222222:stream/testStream, ResourceArnList=[arn:aws:s3:us-east-1:333333333333:stream/testStream], Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArn='arn:aws:s3:us-east-1:222222222222:stream/testStream', ResourceArnList=['arn:aws:s3:us-east-1:333333333333:stream/testStream'], Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.api.aws'

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.api.aws'

def test__resourcearnlist__arn_aws_dynamodb_us_ea():
    """{ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.api.aws'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.amazonaws.com'

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.amazonaws.com'

def test__resourcearnlist__arn_aws_dynamodb_us_ea():
    """{ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.api.aws'

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.api.aws'

def test__resourcearnlist__arn_aws_dynamodb_us_ea():
    """{ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.api.aws'

def test__region_us_east_1__accountidendpointmode():
    """{Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-east-1.amazonaws.com'

def test__accountid___region_us_east_1__accountid():
    """{AccountId=, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Credentials-sourced account ID parameter is invalid')):
        resolve(params)

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.us-east-1.amazonaws.com'

def test__resourcearn___region_us_east_1__account():
    """{ResourceArn=, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test__resourcearnlist_____region_us_east_1__a():
    """{ResourceArnList=[], Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=[], Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test__resourcearn_arn_aws_dynamodb_af_south_1():
    """{ResourceArn=arn:aws:dynamodb:af-south-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:af-south-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test__resourcearn_arn_aws_s3_us_east_1_222222():
    """{ResourceArn=arn:aws:s3:us-east-1:222222222222:stream/testStream, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws:s3:us-east-1:222222222222:stream/testStream', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test__resourcearnlist__arn_aws_dynamodb_us_ea():
    """{ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-east-1.amazonaws.com'

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__resourcearnlist():
    """{AccountId=111111111111, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__resourcearn_arn():
    """{AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__resourcearn_arn():
    """{AccountId=111111111111, ResourceArn=arn:aws:dynamodb:af-south-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArn='arn:aws:dynamodb:af-south-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__resourcearn_arn():
    """{AccountId=111111111111, ResourceArn=arn:aws:s3:us-east-1:222222222222:stream/testStream, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArn='arn:aws:s3:us-east-1:222222222222:stream/testStream', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__resourcearn_arn():
    """{AccountId=111111111111, ResourceArn=arn:aws:s3:af-south-1:222222222222:stream/testStream, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArn='arn:aws:s3:af-south-1:222222222222:stream/testStream', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__resourcearn_arn():
    """{AccountId=111111111111, ResourceArn=arn:aws:s3:af-south-1:222222222222:stream/testStream, ResourceArnList=[arn:aws:s3:us-east-1:333333333333:stream/testStream], Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArn='arn:aws:s3:af-south-1:222222222222:stream/testStream', ResourceArnList=['arn:aws:s3:us-east-1:333333333333:stream/testStream'], Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-east-1.amazonaws.com'

def test__resourcearn_arn_aws_s3_af_south_1_22222():
    """{ResourceArn=arn:aws:s3:af-south-1:222222222222:stream/testStream, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws:s3:af-south-1:222222222222:stream/testStream', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test__accountid_111111111111__resourcearn_arn():
    """{AccountId=111111111111, ResourceArn=arn:aws:dynamodb:af-south-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:af-south-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArn='arn:aws:dynamodb:af-south-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:af-south-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__resourcearn_arn():
    """{AccountId=111111111111, ResourceArn=arn:aws:s3:us-east-1:222222222222:stream/testStream, ResourceArnList=[arn:aws:s3:us-east-1:333333333333:stream/testStream], Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ResourceArn='arn:aws:s3:us-east-1:222222222222:stream/testStream', ResourceArnList=['arn:aws:s3:us-east-1:333333333333:stream/testStream'], Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-east-1.api.aws'

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.us-east-1.api.aws'

def test__resourcearnlist__arn_aws_dynamodb_us_ea():
    """{ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-east-1.api.aws'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearnlist__arn_aws_dynamodb_us_ea():
    """{ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearnlist__arn_aws_dynamodb_us_ea():
    """{ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__region_us_new_1__accountidendpointmode_():
    """{Region=us-new-1, AccountIdEndpointMode=preferred, AccountId=111111111111, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(Region='us-new-1', AccountIdEndpointMode='preferred', AccountId='111111111111', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-new-1.amazonaws.com'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.cn-north-1.amazonaws.com.cn'

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.cn-north-1.amazonaws.com.cn'

def test__resourcearnlist__arn_aws_cn_dynamodb_cn():
    """{ResourceArnList=[arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name], Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name'], Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.cn-north-1.amazonaws.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.cn-north-1.api.amazonwebservices.com.cn'

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.cn-north-1.api.amazonwebservices.com.cn'

def test__resourcearnlist__arn_aws_cn_dynamodb_cn():
    """{ResourceArnList=[arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name], Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name'], Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.cn-north-1.api.amazonwebservices.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.cn-north-1.amazonaws.com.cn'

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.cn-north-1.amazonaws.com.cn'

def test__resourcearnlist__arn_aws_cn_dynamodb_cn():
    """{ResourceArnList=[arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name], Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name'], Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.cn-north-1.amazonaws.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test__resourcearnlist__arn_aws_cn_dynamodb_cn():
    """{ResourceArnList=[arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name], Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name'], Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.amazonaws.com.cn'

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.amazonaws.com.cn'

def test__resourcearnlist__arn_aws_cn_dynamodb_cn():
    """{ResourceArnList=[arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name], Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name'], Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.amazonaws.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.api.amazonwebservices.com.cn'

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.api.amazonwebservices.com.cn'

def test__resourcearnlist__arn_aws_cn_dynamodb_cn():
    """{ResourceArnList=[arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name], Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name'], Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.api.amazonwebservices.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.cn-north-1.amazonaws.com.cn'

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.cn-north-1.amazonaws.com.cn'

def test__resourcearnlist__arn_aws_cn_dynamodb_cn():
    """{ResourceArnList=[arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name], Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name'], Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.cn-north-1.amazonaws.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test__resourcearnlist__arn_aws_cn_dynamodb_cn():
    """{ResourceArnList=[arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name], Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name'], Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.cn-north-1.amazonaws.com.cn'

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.cn-north-1.amazonaws.com.cn'

def test__resourcearnlist__arn_aws_cn_dynamodb_cn():
    """{ResourceArnList=[arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name], Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name'], Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.cn-north-1.amazonaws.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.cn-north-1.api.amazonwebservices.com.cn'

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.cn-north-1.api.amazonwebservices.com.cn'

def test__resourcearnlist__arn_aws_cn_dynamodb_cn():
    """{ResourceArnList=[arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name], Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name'], Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.cn-north-1.api.amazonwebservices.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearnlist__arn_aws_cn_dynamodb_cn():
    """{ResourceArnList=[arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name], Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name'], Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearnlist__arn_aws_cn_dynamodb_cn():
    """{ResourceArnList=[arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name], Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws-cn:dynamodb:cn-north-1:333333333333:table/table_name'], Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__region_cn_new_1__accountidendpointmode_():
    """{Region=cn-new-1, AccountIdEndpointMode=preferred, AccountId=111111111111, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(Region='cn-new-1', AccountIdEndpointMode='preferred', AccountId='111111111111', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-new-1.amazonaws.com.cn'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-gov-east-1.amazonaws.com'

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.us-gov-east-1.amazonaws.com'

def test__resourcearnlist__arn_aws_us_gov_dynamod():
    """{ResourceArnList=[arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name], Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name'], Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-gov-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-gov-east-1.api.aws'

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.us-gov-east-1.api.aws'

def test__resourcearnlist__arn_aws_us_gov_dynamod():
    """{ResourceArnList=[arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name], Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name'], Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-gov-east-1.api.aws'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test__resourcearnlist__arn_aws_us_gov_dynamod():
    """{ResourceArnList=[arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name], Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name'], Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-gov-east-1.api.aws'

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-gov-east-1.api.aws'

def test__resourcearnlist__arn_aws_us_gov_dynamod():
    """{ResourceArnList=[arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name], Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name'], Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-gov-east-1.api.aws'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test__resourcearnlist__arn_aws_us_gov_dynamod():
    """{ResourceArnList=[arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name], Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name'], Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.api.aws'

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.api.aws'

def test__resourcearnlist__arn_aws_us_gov_dynamod():
    """{ResourceArnList=[arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name], Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name'], Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.api.aws'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test__resourcearnlist__arn_aws_us_gov_dynamod():
    """{ResourceArnList=[arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name], Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name'], Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-gov-east-1.api.aws'

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-gov-east-1.api.aws'

def test__resourcearnlist__arn_aws_us_gov_dynamod():
    """{ResourceArnList=[arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name], Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name'], Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-gov-east-1.api.aws'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-gov-east-1.amazonaws.com'

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.us-gov-east-1.amazonaws.com'

def test__resourcearnlist__arn_aws_us_gov_dynamod():
    """{ResourceArnList=[arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name], Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name'], Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-gov-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-gov-east-1.api.aws'

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.us-gov-east-1.api.aws'

def test__resourcearnlist__arn_aws_us_gov_dynamod():
    """{ResourceArnList=[arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name], Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name'], Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-gov-east-1.api.aws'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearnlist__arn_aws_us_gov_dynamod():
    """{ResourceArnList=[arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name], Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name'], Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearnlist__arn_aws_us_gov_dynamod():
    """{ResourceArnList=[arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name], Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/table_name'], Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__region_us_gov_new_1__accountidendpointm():
    """{Region=us-gov-new-1, AccountIdEndpointMode=preferred, AccountId=111111111111, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(Region='us-gov-new-1', AccountIdEndpointMode='preferred', AccountId='111111111111', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-new-1.amazonaws.com'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.c2s.ic.gov'

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.c2s.ic.gov'

def test__resourcearnlist__arn_aws_iso_dynamodb_u():
    """{ResourceArnList=[arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name], Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name'], Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.c2s.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.api.aws.ic.gov'

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.api.aws.ic.gov'

def test__resourcearnlist__arn_aws_iso_dynamodb_u():
    """{ResourceArnList=[arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name], Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name'], Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.api.aws.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-iso-east-1.c2s.ic.gov'

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-iso-east-1.c2s.ic.gov'

def test__resourcearnlist__arn_aws_iso_dynamodb_u():
    """{ResourceArnList=[arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name], Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name'], Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-iso-east-1.c2s.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-iso-east-1.api.aws.ic.gov'

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-iso-east-1.api.aws.ic.gov'

def test__resourcearnlist__arn_aws_iso_dynamodb_u():
    """{ResourceArnList=[arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name], Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name'], Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-iso-east-1.api.aws.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.c2s.ic.gov'

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.c2s.ic.gov'

def test__resourcearnlist__arn_aws_iso_dynamodb_u():
    """{ResourceArnList=[arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name], Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name'], Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.c2s.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.api.aws.ic.gov'

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.api.aws.ic.gov'

def test__resourcearnlist__arn_aws_iso_dynamodb_u():
    """{ResourceArnList=[arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name], Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name'], Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.api.aws.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-iso-east-1.c2s.ic.gov'

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-iso-east-1.c2s.ic.gov'

def test__resourcearnlist__arn_aws_iso_dynamodb_u():
    """{ResourceArnList=[arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name], Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name'], Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-iso-east-1.c2s.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-iso-east-1.api.aws.ic.gov'

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-iso-east-1.api.aws.ic.gov'

def test__resourcearnlist__arn_aws_iso_dynamodb_u():
    """{ResourceArnList=[arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name], Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name'], Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-iso-east-1.api.aws.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__resourcearnlist__arn_aws_iso_dynamodb_u():
    """{ResourceArnList=[arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name], Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name'], Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__resourcearnlist__arn_aws_iso_dynamodb_u():
    """{ResourceArnList=[arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name], Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name'], Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearnlist__arn_aws_iso_dynamodb_u():
    """{ResourceArnList=[arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name], Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ResourceArnList=['arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name'], Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearnlist__arn_aws_iso_dynamodb_u():
    """{ResourceArnList=[arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name], Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ResourceArnList=['arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/table_name'], Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__region_us_iso_new_1__accountidendpointm():
    """{Region=us-iso-new-1, AccountIdEndpointMode=preferred, AccountId=111111111111, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(Region='us-iso-new-1', AccountIdEndpointMode='preferred', AccountId='111111111111', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-new-1.c2s.ic.gov'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false, Endpoint=https://example.com, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False, Endpoint='https://example.com', IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://example.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true, Endpoint=https://example.com, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True, Endpoint='https://example.com', IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false, Endpoint=https://example.com, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False, Endpoint='https://example.com', IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true, Endpoint=https://example.com, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True, Endpoint='https://example.com', IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false, Endpoint=https://example.com, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False, Endpoint='https://example.com', IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://example.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true, Endpoint=https://example.com, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True, Endpoint='https://example.com', IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false, Endpoint=https://example.com, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False, Endpoint='https://example.com', IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true, Endpoint=https://example.com, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True, Endpoint='https://example.com', IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false, Endpoint=https://example.com, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False, Endpoint='https://example.com', IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://example.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true, Endpoint=https://example.com, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True, Endpoint='https://example.com', IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false, Endpoint=https://example.com, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False, Endpoint='https://example.com', IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true, Endpoint=https://example.com, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True, Endpoint='https://example.com', IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test__endpoint_https___dynamodb_cn_north_1_ap():
    """{Endpoint=https://dynamodb.cn-north-1.api.amazonwebservices.com.cn, Region=cn-north-1, AccountIdEndpointMode=preferred, IsSearchOperation=true}"""
    params = EndpointParams(Endpoint='https://dynamodb.cn-north-1.api.amazonwebservices.com.cn', Region='cn-north-1', AccountIdEndpointMode='preferred', IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Endpoint override is not supported for dual-stack endpoints. Please enable dual-stack functionality by enabling the configuration. For more details, see: https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html')):
        resolve(params)

def test__endpoint_https___dynamodb_us_gov_east_1():
    """{Endpoint=https://dynamodb.us-gov-east-1.api.aws, Region=us-gov-east-1, AccountIdEndpointMode=preferred, IsSearchOperation=true}"""
    params = EndpointParams(Endpoint='https://dynamodb.us-gov-east-1.api.aws', Region='us-gov-east-1', AccountIdEndpointMode='preferred', IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Endpoint override is not supported for dual-stack endpoints. Please enable dual-stack functionality by enabling the configuration. For more details, see: https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html')):
        resolve(params)

def test__endpoint_https___dynamodb_us_east_1_api():
    """{Endpoint=https://dynamodb.us-east-1.api.aws, Region=us-east-1, AccountIdEndpointMode=preferred, IsSearchOperation=true}"""
    params = EndpointParams(Endpoint='https://dynamodb.us-east-1.api.aws', Region='us-east-1', AccountIdEndpointMode='preferred', IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Endpoint override is not supported for dual-stack endpoints. Please enable dual-stack functionality by enabling the configuration. For more details, see: https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html')):
        resolve(params)

def test__endpoint_https___111111111111_ddb_us_ea():
    """{Endpoint=https://111111111111.ddb.us-east-1.api.aws, Region=us-east-1, AccountIdEndpointMode=preferred, IsSearchOperation=true}"""
    params = EndpointParams(Endpoint='https://111111111111.ddb.us-east-1.api.aws', Region='us-east-1', AccountIdEndpointMode='preferred', IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-east-1.api.aws'

def test__endpoint_https___vpce_1a2b3c4d_5e6f_dyn():
    """{Endpoint=https://vpce-1a2b3c4d-5e6f.dynamodb.us-east-1.vpce.api.aws, Region=us-east-1, AccountIdEndpointMode=preferred, IsSearchOperation=true}"""
    params = EndpointParams(Endpoint='https://vpce-1a2b3c4d-5e6f.dynamodb.us-east-1.vpce.api.aws', Region='us-east-1', AccountIdEndpointMode='preferred', IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://vpce-1a2b3c4d-5e6f.dynamodb.us-east-1.vpce.api.aws'

def test__endpoint_https___dynamodb_eu_west_1_api():
    """{Endpoint=https://dynamodb.eu-west-1.api.aws, Region=eu-west-1, AccountIdEndpointMode=preferred, IsSearchOperation=true}"""
    params = EndpointParams(Endpoint='https://dynamodb.eu-west-1.api.aws', Region='eu-west-1', AccountIdEndpointMode='preferred', IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Endpoint override is not supported for dual-stack endpoints. Please enable dual-stack functionality by enabling the configuration. For more details, see: https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html')):
        resolve(params)

def test__endpoint_https___dynamodb_us_west_2_api():
    """{Endpoint=https://dynamodb.us-west-2.api.aws, Region=us-west-2, AccountIdEndpointMode=preferred, IsSearchOperation=true}"""
    params = EndpointParams(Endpoint='https://dynamodb.us-west-2.api.aws', Region='us-west-2', AccountIdEndpointMode='preferred', IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Endpoint override is not supported for dual-stack endpoints. Please enable dual-stack functionality by enabling the configuration. For more details, see: https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html')):
        resolve(params)

def test__endpoint_https___dynamodb_us_east_1_api():
    """{Endpoint=https://dynamodb.us-east-1.api.aws/, Region=us-east-1, AccountIdEndpointMode=preferred, IsSearchOperation=true}"""
    params = EndpointParams(Endpoint='https://dynamodb.us-east-1.api.aws/', Region='us-east-1', AccountIdEndpointMode='preferred', IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Endpoint override is not supported for dual-stack endpoints. Please enable dual-stack functionality by enabling the configuration. For more details, see: https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html')):
        resolve(params)

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and local endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and local endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and local endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test__accountid_111111111111__region_local__a():
    """{AccountId=111111111111, Region=local, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='local', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test__usefips_false__usedualstack_false__isse():
    """{UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Missing Region')):
        resolve(params)

def test__region_us_east_1__accountidendpointmode():
    """{Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:not_an_account:table/table_name, IsSearchOperation=true}"""
    params = EndpointParams(Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:not_an_account:table/table_name', IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-east-1.amazonaws.com'

def test__region_us_east_1__accountidendpointmode():
    """{Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.search-ddb.us-east-1.amazonaws.com'

def test__accountid___region_us_east_1__accountid():
    """{AccountId=, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Credentials-sourced account ID parameter is invalid')):
        resolve(params)

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.search-ddb.us-east-1.amazonaws.com'

def test__resourcearn___region_us_east_1__account():
    """{ResourceArn=, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-east-1.amazonaws.com'

def test__resourcearn_arn_aws_dynamodb_af_south_1():
    """{ResourceArn=arn:aws:dynamodb:af-south-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:af-south-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-east-1.amazonaws.com'

def test__resourcearn_arn_aws_s3_us_east_1_222222():
    """{ResourceArn=arn:aws:s3:us-east-1:222222222222:stream/testStream, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws:s3:us-east-1:222222222222:stream/testStream', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-east-1.amazonaws.com'

def test__resourcearn_arn_aws_s3_af_south_1_22222():
    """{ResourceArn=arn:aws:s3:af-south-1:222222222222:stream/testStream, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws:s3:af-south-1:222222222222:stream/testStream', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.search-ddb.us-east-1.api.aws'

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.search-ddb.us-east-1.api.aws'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.us-east-1.amazonaws.com'

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.us-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.us-east-1.api.aws'

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.us-east-1.api.aws'

def test__region_us_east_1__accountidendpointmode():
    """{Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-east-1.amazonaws.com'

def test__accountid___region_us_east_1__accountid():
    """{AccountId=, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-east-1.amazonaws.com'

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-east-1.amazonaws.com'

def test__resourcearn___region_us_east_1__account():
    """{ResourceArn=, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-east-1.amazonaws.com'

def test__resourcearn_arn_aws_dynamodb_af_south_1():
    """{ResourceArn=arn:aws:dynamodb:af-south-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:af-south-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-east-1.amazonaws.com'

def test__resourcearn_arn_aws_s3_us_east_1_222222():
    """{ResourceArn=arn:aws:s3:us-east-1:222222222222:stream/testStream, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws:s3:us-east-1:222222222222:stream/testStream', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-east-1.amazonaws.com'

def test__resourcearn_arn_aws_s3_af_south_1_22222():
    """{ResourceArn=arn:aws:s3:af-south-1:222222222222:stream/testStream, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws:s3:af-south-1:222222222222:stream/testStream', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-east-1.api.aws'

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-east-1.api.aws'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.us-east-1.amazonaws.com'

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.us-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.us-east-1.api.aws'

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.us-east-1.api.aws'

def test__region_us_east_1__accountidendpointmode():
    """{Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.search-ddb.us-east-1.amazonaws.com'

def test__accountid___region_us_east_1__accountid():
    """{AccountId=, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Credentials-sourced account ID parameter is invalid')):
        resolve(params)

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.search-ddb.us-east-1.amazonaws.com'

def test__resourcearn___region_us_east_1__account():
    """{ResourceArn=, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test__resourcearn_arn_aws_dynamodb_af_south_1():
    """{ResourceArn=arn:aws:dynamodb:af-south-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:af-south-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test__resourcearn_arn_aws_s3_us_east_1_222222():
    """{ResourceArn=arn:aws:s3:us-east-1:222222222222:stream/testStream, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws:s3:us-east-1:222222222222:stream/testStream', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test__resourcearn_arn_aws_s3_af_south_1_22222():
    """{ResourceArn=arn:aws:s3:af-south-1:222222222222:stream/testStream, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws:s3:af-south-1:222222222222:stream/testStream', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.search-ddb.us-east-1.api.aws'

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.search-ddb.us-east-1.api.aws'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearn_arn_aws_dynamodb_us_east_1_():
    """{ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__region_us_new_1__accountidendpointmode_():
    """{Region=us-new-1, AccountIdEndpointMode=preferred, AccountId=111111111111, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(Region='us-new-1', AccountIdEndpointMode='preferred', AccountId='111111111111', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.search-ddb.us-new-1.amazonaws.com'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.search-ddb.cn-north-1.amazonaws.com.cn'

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.search-ddb.cn-north-1.amazonaws.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.search-ddb.cn-north-1.api.amazonwebservices.com.cn'

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.search-ddb.cn-north-1.api.amazonwebservices.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.cn-north-1.amazonaws.com.cn'

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.cn-north-1.amazonaws.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.cn-north-1.amazonaws.com.cn'

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.cn-north-1.amazonaws.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.cn-north-1.api.amazonwebservices.com.cn'

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.cn-north-1.api.amazonwebservices.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.cn-north-1.amazonaws.com.cn'

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.cn-north-1.amazonaws.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.search-ddb.cn-north-1.amazonaws.com.cn'

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.search-ddb.cn-north-1.amazonaws.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.search-ddb.cn-north-1.api.amazonwebservices.com.cn'

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.search-ddb.cn-north-1.api.amazonwebservices.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearn_arn_aws_cn_dynamodb_cn_nort():
    """{ResourceArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/table_name', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__region_cn_new_1__accountidendpointmode_():
    """{Region=cn-new-1, AccountIdEndpointMode=preferred, AccountId=111111111111, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(Region='cn-new-1', AccountIdEndpointMode='preferred', AccountId='111111111111', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.cn-new-1.amazonaws.com.cn'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.search-ddb.us-gov-east-1.amazonaws.com'

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.search-ddb.us-gov-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.search-ddb.us-gov-east-1.api.aws'

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.search-ddb.us-gov-east-1.api.aws'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-gov-east-1.amazonaws.com'

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-gov-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.us-gov-east-1.api.aws'

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.us-gov-east-1.api.aws'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-gov-east-1.amazonaws.com'

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-gov-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-gov-east-1.api.aws'

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-gov-east-1.api.aws'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-gov-east-1.amazonaws.com'

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-gov-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.us-gov-east-1.api.aws'

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.us-gov-east-1.api.aws'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.search-ddb.us-gov-east-1.amazonaws.com'

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.search-ddb.us-gov-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.search-ddb.us-gov-east-1.api.aws'

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.search-ddb.us-gov-east-1.api.aws'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearn_arn_aws_us_gov_dynamodb_us_():
    """{ResourceArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/table_name', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__region_us_gov_new_1__accountidendpointm():
    """{Region=us-gov-new-1, AccountIdEndpointMode=preferred, AccountId=111111111111, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(Region='us-gov-new-1', AccountIdEndpointMode='preferred', AccountId='111111111111', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-gov-new-1.amazonaws.com'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-iso-east-1.c2s.ic.gov'

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-iso-east-1.c2s.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-iso-east-1.api.aws.ic.gov'

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-iso-east-1.api.aws.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.us-iso-east-1.c2s.ic.gov'

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.us-iso-east-1.c2s.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.us-iso-east-1.api.aws.ic.gov'

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.us-iso-east-1.api.aws.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-iso-east-1.c2s.ic.gov'

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-iso-east-1.c2s.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-iso-east-1.api.aws.ic.gov'

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-iso-east-1.api.aws.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.us-iso-east-1.c2s.ic.gov'

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.us-iso-east-1.c2s.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.us-iso-east-1.api.aws.ic.gov'

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb-fips.us-iso-east-1.api.aws.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__resourcearn_arn_aws_iso_dynamodb_us_iso():
    """{ResourceArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true, IsSearchOperation=true}"""
    params = EndpointParams(ResourceArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/table_name', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True, IsSearchOperation=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test__region_us_iso_new_1__accountidendpointm():
    """{Region=us-iso-new-1, AccountIdEndpointMode=preferred, AccountId=111111111111, UseFIPS=false, UseDualStack=false, IsSearchOperation=true}"""
    params = EndpointParams(Region='us-iso-new-1', AccountIdEndpointMode='preferred', AccountId='111111111111', UseFIPS=False, UseDualStack=False, IsSearchOperation=True)
    result = resolve(params)
    assert result.url == 'https://search-dynamodb.us-iso-new-1.c2s.ic.gov'