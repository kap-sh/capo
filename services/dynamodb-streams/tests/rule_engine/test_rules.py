import pytest
from capo_dynamodb_streams._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_dynamodb_streams._rule_engine._endpoint_runtime import EndpointError
import re
import zapros

def test_for_region_af_south_1_with_fips_disabled():
    """For region af-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='af-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.af-south-1.amazonaws.com'

def test_for_region_ap_east_1_with_fips_disabled_():
    """For region ap-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.ap-east-1.amazonaws.com'

def test_for_region_ap_northeast_1_with_fips_disa():
    """For region ap-northeast-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.ap-northeast-1.amazonaws.com'

def test_for_region_ap_northeast_2_with_fips_disa():
    """For region ap-northeast-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.ap-northeast-2.amazonaws.com'

def test_for_region_ap_northeast_3_with_fips_disa():
    """For region ap-northeast-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-3', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.ap-northeast-3.amazonaws.com'

def test_for_region_ap_south_1_with_fips_disabled():
    """For region ap-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.ap-south-1.amazonaws.com'

def test_for_region_ap_southeast_1_with_fips_disa():
    """For region ap-southeast-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.ap-southeast-1.amazonaws.com'

def test_for_region_ap_southeast_2_with_fips_disa():
    """For region ap-southeast-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.ap-southeast-2.amazonaws.com'

def test_for_region_ap_southeast_3_with_fips_disa():
    """For region ap-southeast-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-3', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.ap-southeast-3.amazonaws.com'

def test_for_region_ca_central_1_with_fips_disabl():
    """For region ca-central-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ca-central-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.ca-central-1.amazonaws.com'

def test_for_region_eu_central_1_with_fips_disabl():
    """For region eu-central-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-central-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.eu-central-1.amazonaws.com'

def test_for_region_eu_north_1_with_fips_disabled():
    """For region eu-north-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-north-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.eu-north-1.amazonaws.com'

def test_for_region_eu_south_1_with_fips_disabled():
    """For region eu-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.eu-south-1.amazonaws.com'

def test_for_region_eu_west_1_with_fips_disabled_():
    """For region eu-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.eu-west-1.amazonaws.com'

def test_for_region_eu_west_2_with_fips_disabled_():
    """For region eu-west-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.eu-west-2.amazonaws.com'

def test_for_region_eu_west_3_with_fips_disabled_():
    """For region eu-west-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-3', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.eu-west-3.amazonaws.com'

def test_for_region_me_south_1_with_fips_disabled():
    """For region me-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='me-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.me-south-1.amazonaws.com'

def test_for_region_sa_east_1_with_fips_disabled_():
    """For region sa-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='sa-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.sa-east-1.amazonaws.com'

def test_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-east-1.amazonaws.com'

def test_for_region_us_east_2_with_fips_disabled_():
    """For region us-east-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-east-2.amazonaws.com'

def test_for_region_us_west_1_with_fips_disabled_():
    """For region us-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-west-1.amazonaws.com'

def test_for_region_us_west_2_with_fips_disabled_():
    """For region us-west-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-west-2.amazonaws.com'

def test_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.us-east-1.api.aws'

def test_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.us-east-1.amazonaws.com'

def test_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.us-east-1.api.aws'

def test_for_region_cn_north_1_with_fips_disabled():
    """For region cn-north-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.cn-north-1.amazonaws.com.cn'

def test_for_region_cn_northwest_1_with_fips_disa():
    """For region cn-northwest-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.cn-northwest-1.amazonaws.com.cn'

def test_for_region_cn_north_1_with_fips_enabled_():
    """For region cn-north-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test_for_region_cn_north_1_with_fips_enabled_():
    """For region cn-north-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.cn-north-1.amazonaws.com.cn'

def test_for_region_cn_north_1_with_fips_disabled():
    """For region cn-north-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.cn-north-1.api.amazonwebservices.com.cn'

def test_for_region_us_gov_east_1_with_fips_disab():
    """For region us-gov-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-gov-east-1.amazonaws.com'

def test_for_region_us_gov_east_1_with_fips_enabl():
    """For region us-gov-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-gov-east-1.amazonaws.com'

def test_for_region_us_gov_west_1_with_fips_disab():
    """For region us-gov-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-gov-west-1.amazonaws.com'

def test_for_region_us_gov_west_1_with_fips_enabl():
    """For region us-gov-west-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-gov-west-1.amazonaws.com'

def test_for_region_us_gov_east_1_with_fips_enabl():
    """For region us-gov-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.us-gov-east-1.api.aws'

def test_for_region_us_gov_east_1_with_fips_disab():
    """For region us-gov-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.us-gov-east-1.api.aws'

def test_for_region_us_iso_east_1_with_fips_disab():
    """For region us-iso-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-iso-east-1.c2s.ic.gov'

def test_for_region_us_iso_east_1_with_fips_enabl():
    """For region us-iso-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.us-iso-east-1.c2s.ic.gov'

def test_for_region_us_isob_east_1_with_fips_disa():
    """For region us-isob-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-isob-east-1.sc2s.sgov.gov'

def test_for_region_us_isob_east_1_with_fips_enab():
    """For region us-isob-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.us-isob-east-1.sc2s.sgov.gov'

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

def test__region_local__usefips_false__usedualsta():
    """{Region=local, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(Region='local', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.local.amazonaws.com'

def test__usefips_false__usedualstack_false_():
    """{UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Missing Region')):
        resolve(params)

def test__region_us_east_1__accountidendpointmode():
    """{Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false, StreamArn=arn:aws:dynamodb:us-east-1:not_an_account:table/T/stream/2024-01-01T00:00:00.000}"""
    params = EndpointParams(Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False, StreamArn='arn:aws:dynamodb:us-east-1:not_an_account:table/T/stream/2024-01-01T00:00:00.000')
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-east-1.amazonaws.com'

def test__region_us_east_1__accountidendpointmode():
    """{Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.us-east-1.amazonaws.com'

def test__accountid___region_us_east_1__accountid():
    """{AccountId=, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Credentials-sourced account ID parameter is invalid')):
        resolve(params)

def test__streamarn_arn_aws_dynamodb_us_east_1_22():
    """{StreamArn=arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.us-east-1.amazonaws.com'

def test__streamarn___region_us_east_1__accountid():
    """{StreamArn=, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-east-1.amazonaws.com'

def test__streamarn_arn_aws_dynamodb_af_south_1_2():
    """{StreamArn=arn:aws:dynamodb:af-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:af-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-east-1.amazonaws.com'

def test__streamarn_arn_aws_kinesis_us_east_1_222():
    """{StreamArn=arn:aws:kinesis:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:kinesis:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-east-1.amazonaws.com'

def test__sharditerator_arn_aws_dynamodb_us_east_():
    """{ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.us-east-1.amazonaws.com'

def test__sharditerator_arn_aws_dynamodb_af_south():
    """{ShardIterator=arn:aws:dynamodb:af-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:af-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-east-1.amazonaws.com'

def test__streamarn_arn_aws_dynamodb_us_east_1_22():
    """{StreamArn=arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__streamarn_arn_a():
    """{AccountId=111111111111, StreamArn=arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', StreamArn='arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__sharditerator_a():
    """{AccountId=111111111111, ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__streamarn_arn_a():
    """{AccountId=111111111111, StreamArn=arn:aws:dynamodb:af-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', StreamArn='arn:aws:dynamodb:af-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__streamarn_arn_a():
    """{AccountId=111111111111, StreamArn=arn:aws:kinesis:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', StreamArn='arn:aws:kinesis:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__streamarn_arn_a():
    """{AccountId=111111111111, StreamArn=arn:aws:dynamodb:af-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, ShardIterator=arn:aws:dynamodb:af-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', StreamArn='arn:aws:dynamodb:af-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', ShardIterator='arn:aws:dynamodb:af-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.us-east-1.api.aws'

def test__streamarn_arn_aws_dynamodb_us_east_1_22():
    """{StreamArn=arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.us-east-1.api.aws'

def test__sharditerator_arn_aws_dynamodb_us_east_():
    """{ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.us-east-1.api.aws'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.us-east-1.amazonaws.com'

def test__streamarn_arn_aws_dynamodb_us_east_1_22():
    """{StreamArn=arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.us-east-1.amazonaws.com'

def test__sharditerator_arn_aws_dynamodb_us_east_():
    """{ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.us-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.us-east-1.api.aws'

def test__streamarn_arn_aws_dynamodb_us_east_1_22():
    """{StreamArn=arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.us-east-1.api.aws'

def test__sharditerator_arn_aws_dynamodb_us_east_():
    """{ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.us-east-1.api.aws'

def test__region_us_east_1__accountidendpointmode():
    """{Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-east-1.amazonaws.com'

def test__accountid___region_us_east_1__accountid():
    """{AccountId=, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-east-1.amazonaws.com'

def test__streamarn_arn_aws_dynamodb_us_east_1_22():
    """{StreamArn=arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-east-1.amazonaws.com'

def test__streamarn___region_us_east_1__accountid():
    """{StreamArn=, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-east-1.amazonaws.com'

def test__streamarn_arn_aws_dynamodb_af_south_1_2():
    """{StreamArn=arn:aws:dynamodb:af-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:af-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-east-1.amazonaws.com'

def test__streamarn_arn_aws_kinesis_us_east_1_222():
    """{StreamArn=arn:aws:kinesis:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:kinesis:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-east-1.amazonaws.com'

def test__sharditerator_arn_aws_dynamodb_us_east_():
    """{ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-east-1.amazonaws.com'

def test__sharditerator_arn_aws_dynamodb_af_south():
    """{ShardIterator=arn:aws:dynamodb:af-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:af-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-east-1.amazonaws.com'

def test__streamarn_arn_aws_dynamodb_us_east_1_22():
    """{StreamArn=arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__streamarn_arn_a():
    """{AccountId=111111111111, StreamArn=arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', StreamArn='arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__sharditerator_a():
    """{AccountId=111111111111, ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__streamarn_arn_a():
    """{AccountId=111111111111, StreamArn=arn:aws:dynamodb:af-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', StreamArn='arn:aws:dynamodb:af-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__streamarn_arn_a():
    """{AccountId=111111111111, StreamArn=arn:aws:kinesis:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', StreamArn='arn:aws:kinesis:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__streamarn_arn_a():
    """{AccountId=111111111111, StreamArn=arn:aws:dynamodb:af-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, ShardIterator=arn:aws:dynamodb:af-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', StreamArn='arn:aws:dynamodb:af-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', ShardIterator='arn:aws:dynamodb:af-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.us-east-1.api.aws'

def test__streamarn_arn_aws_dynamodb_us_east_1_22():
    """{StreamArn=arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.us-east-1.api.aws'

def test__sharditerator_arn_aws_dynamodb_us_east_():
    """{ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.us-east-1.api.aws'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.us-east-1.amazonaws.com'

def test__streamarn_arn_aws_dynamodb_us_east_1_22():
    """{StreamArn=arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.us-east-1.amazonaws.com'

def test__sharditerator_arn_aws_dynamodb_us_east_():
    """{ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.us-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.us-east-1.api.aws'

def test__streamarn_arn_aws_dynamodb_us_east_1_22():
    """{StreamArn=arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.us-east-1.api.aws'

def test__sharditerator_arn_aws_dynamodb_us_east_():
    """{ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.us-east-1.api.aws'

def test__region_us_east_1__accountidendpointmode():
    """{Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.us-east-1.amazonaws.com'

def test__accountid___region_us_east_1__accountid():
    """{AccountId=, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Credentials-sourced account ID parameter is invalid')):
        resolve(params)

def test__streamarn_arn_aws_dynamodb_us_east_1_22():
    """{StreamArn=arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.us-east-1.amazonaws.com'

def test__streamarn___region_us_east_1__accountid():
    """{StreamArn=, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test__streamarn_arn_aws_dynamodb_af_south_1_2():
    """{StreamArn=arn:aws:dynamodb:af-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:af-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test__streamarn_arn_aws_kinesis_us_east_1_222():
    """{StreamArn=arn:aws:kinesis:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:kinesis:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test__sharditerator_arn_aws_dynamodb_us_east_():
    """{ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.us-east-1.amazonaws.com'

def test__sharditerator_arn_aws_dynamodb_af_south():
    """{ShardIterator=arn:aws:dynamodb:af-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:af-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test__streamarn_arn_aws_dynamodb_us_east_1_22():
    """{StreamArn=arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__streamarn_arn_a():
    """{AccountId=111111111111, StreamArn=arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', StreamArn='arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__sharditerator_a():
    """{AccountId=111111111111, ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__streamarn_arn_a():
    """{AccountId=111111111111, StreamArn=arn:aws:dynamodb:af-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', StreamArn='arn:aws:dynamodb:af-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__streamarn_arn_a():
    """{AccountId=111111111111, StreamArn=arn:aws:kinesis:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', StreamArn='arn:aws:kinesis:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__streamarn_arn_a():
    """{AccountId=111111111111, StreamArn=arn:aws:dynamodb:af-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, ShardIterator=arn:aws:dynamodb:af-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', StreamArn='arn:aws:dynamodb:af-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', ShardIterator='arn:aws:dynamodb:af-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.us-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.us-east-1.api.aws'

def test__streamarn_arn_aws_dynamodb_us_east_1_22():
    """{StreamArn=arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.us-east-1.api.aws'

def test__sharditerator_arn_aws_dynamodb_us_east_():
    """{ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.us-east-1.api.aws'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.us-east-1.amazonaws.com'

def test__streamarn_arn_aws_dynamodb_us_east_1_22():
    """{StreamArn=arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.us-east-1.amazonaws.com'

def test__sharditerator_arn_aws_dynamodb_us_east_():
    """{ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.us-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_east_():
    """{AccountId=111111111111, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.us-east-1.api.aws'

def test__streamarn_arn_aws_dynamodb_us_east_1_22():
    """{StreamArn=arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:us-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.us-east-1.api.aws'

def test__sharditerator_arn_aws_dynamodb_us_east_():
    """{ShardIterator=arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:us-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.us-east-1.api.aws'

def test__accountid_111111111111__region_eu_west_():
    """{AccountId=111111111111, Region=eu-west-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='eu-west-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.eu-west-1.amazonaws.com'

def test__streamarn_arn_aws_dynamodb_eu_west_1_22():
    """{StreamArn=arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=eu-west-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='eu-west-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.eu-west-1.amazonaws.com'

def test__sharditerator_arn_aws_dynamodb_eu_west_():
    """{ShardIterator=arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=eu-west-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='eu-west-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.eu-west-1.amazonaws.com'

def test__accountid_111111111111__region_eu_west_():
    """{AccountId=111111111111, Region=eu-west-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='eu-west-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.eu-west-1.api.aws'

def test__streamarn_arn_aws_dynamodb_eu_west_1_22():
    """{StreamArn=arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=eu-west-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='eu-west-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.eu-west-1.api.aws'

def test__sharditerator_arn_aws_dynamodb_eu_west_():
    """{ShardIterator=arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=eu-west-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='eu-west-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.eu-west-1.api.aws'

def test__accountid_111111111111__region_eu_west_():
    """{AccountId=111111111111, Region=eu-west-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='eu-west-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.eu-west-1.amazonaws.com'

def test__streamarn_arn_aws_dynamodb_eu_west_1_22():
    """{StreamArn=arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=eu-west-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='eu-west-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.eu-west-1.amazonaws.com'

def test__sharditerator_arn_aws_dynamodb_eu_west_():
    """{ShardIterator=arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=eu-west-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='eu-west-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.eu-west-1.amazonaws.com'

def test__accountid_111111111111__region_eu_west_():
    """{AccountId=111111111111, Region=eu-west-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='eu-west-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.eu-west-1.api.aws'

def test__streamarn_arn_aws_dynamodb_eu_west_1_22():
    """{StreamArn=arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=eu-west-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='eu-west-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.eu-west-1.api.aws'

def test__sharditerator_arn_aws_dynamodb_eu_west_():
    """{ShardIterator=arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=eu-west-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='eu-west-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.eu-west-1.api.aws'

def test__accountid_111111111111__region_eu_west_():
    """{AccountId=111111111111, Region=eu-west-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='eu-west-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.eu-west-1.amazonaws.com'

def test__streamarn_arn_aws_dynamodb_eu_west_1_22():
    """{StreamArn=arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=eu-west-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='eu-west-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.eu-west-1.amazonaws.com'

def test__sharditerator_arn_aws_dynamodb_eu_west_():
    """{ShardIterator=arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=eu-west-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='eu-west-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.eu-west-1.amazonaws.com'

def test__accountid_111111111111__region_eu_west_():
    """{AccountId=111111111111, Region=eu-west-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='eu-west-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.eu-west-1.api.aws'

def test__streamarn_arn_aws_dynamodb_eu_west_1_22():
    """{StreamArn=arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=eu-west-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='eu-west-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.eu-west-1.api.aws'

def test__sharditerator_arn_aws_dynamodb_eu_west_():
    """{ShardIterator=arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=eu-west-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='eu-west-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.eu-west-1.api.aws'

def test__accountid_111111111111__region_eu_west_():
    """{AccountId=111111111111, Region=eu-west-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='eu-west-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.eu-west-1.amazonaws.com'

def test__streamarn_arn_aws_dynamodb_eu_west_1_22():
    """{StreamArn=arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=eu-west-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='eu-west-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.eu-west-1.amazonaws.com'

def test__sharditerator_arn_aws_dynamodb_eu_west_():
    """{ShardIterator=arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=eu-west-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='eu-west-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.eu-west-1.amazonaws.com'

def test__accountid_111111111111__region_eu_west_():
    """{AccountId=111111111111, Region=eu-west-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='eu-west-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.eu-west-1.api.aws'

def test__streamarn_arn_aws_dynamodb_eu_west_1_22():
    """{StreamArn=arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=eu-west-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='eu-west-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.eu-west-1.api.aws'

def test__sharditerator_arn_aws_dynamodb_eu_west_():
    """{ShardIterator=arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=eu-west-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='eu-west-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.eu-west-1.api.aws'

def test__accountid_111111111111__region_eu_west_():
    """{AccountId=111111111111, Region=eu-west-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='eu-west-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.eu-west-1.amazonaws.com'

def test__streamarn_arn_aws_dynamodb_eu_west_1_22():
    """{StreamArn=arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=eu-west-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='eu-west-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.eu-west-1.amazonaws.com'

def test__sharditerator_arn_aws_dynamodb_eu_west_():
    """{ShardIterator=arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=eu-west-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='eu-west-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.eu-west-1.amazonaws.com'

def test__accountid_111111111111__region_eu_west_():
    """{AccountId=111111111111, Region=eu-west-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='eu-west-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.eu-west-1.api.aws'

def test__streamarn_arn_aws_dynamodb_eu_west_1_22():
    """{StreamArn=arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=eu-west-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='eu-west-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.eu-west-1.api.aws'

def test__sharditerator_arn_aws_dynamodb_eu_west_():
    """{ShardIterator=arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=eu-west-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='eu-west-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.eu-west-1.api.aws'

def test__accountid_111111111111__region_eu_west_():
    """{AccountId=111111111111, Region=eu-west-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='eu-west-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.eu-west-1.amazonaws.com'

def test__streamarn_arn_aws_dynamodb_eu_west_1_22():
    """{StreamArn=arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=eu-west-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='eu-west-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.eu-west-1.amazonaws.com'

def test__sharditerator_arn_aws_dynamodb_eu_west_():
    """{ShardIterator=arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=eu-west-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='eu-west-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.eu-west-1.amazonaws.com'

def test__accountid_111111111111__region_eu_west_():
    """{AccountId=111111111111, Region=eu-west-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='eu-west-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.eu-west-1.api.aws'

def test__streamarn_arn_aws_dynamodb_eu_west_1_22():
    """{StreamArn=arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=eu-west-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:eu-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='eu-west-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.eu-west-1.api.aws'

def test__sharditerator_arn_aws_dynamodb_eu_west_():
    """{ShardIterator=arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=eu-west-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:eu-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='eu-west-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.eu-west-1.api.aws'

def test__accountid_111111111111__region_me_centr():
    """{AccountId=111111111111, Region=me-central-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='me-central-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.me-central-1.amazonaws.com'

def test__streamarn_arn_aws_dynamodb_me_central_1():
    """{StreamArn=arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-central-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-central-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.me-central-1.amazonaws.com'

def test__sharditerator_arn_aws_dynamodb_me_centr():
    """{ShardIterator=arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-central-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-central-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.me-central-1.amazonaws.com'

def test__accountid_111111111111__region_me_centr():
    """{AccountId=111111111111, Region=me-central-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='me-central-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.me-central-1.api.aws'

def test__streamarn_arn_aws_dynamodb_me_central_1():
    """{StreamArn=arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-central-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-central-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.me-central-1.api.aws'

def test__sharditerator_arn_aws_dynamodb_me_centr():
    """{ShardIterator=arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-central-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-central-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.me-central-1.api.aws'

def test__accountid_111111111111__region_me_centr():
    """{AccountId=111111111111, Region=me-central-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='me-central-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.me-central-1.amazonaws.com'

def test__streamarn_arn_aws_dynamodb_me_central_1():
    """{StreamArn=arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-central-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-central-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.me-central-1.amazonaws.com'

def test__sharditerator_arn_aws_dynamodb_me_centr():
    """{ShardIterator=arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-central-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-central-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.me-central-1.amazonaws.com'

def test__accountid_111111111111__region_me_centr():
    """{AccountId=111111111111, Region=me-central-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='me-central-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.me-central-1.api.aws'

def test__streamarn_arn_aws_dynamodb_me_central_1():
    """{StreamArn=arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-central-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-central-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.me-central-1.api.aws'

def test__sharditerator_arn_aws_dynamodb_me_centr():
    """{ShardIterator=arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-central-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-central-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.me-central-1.api.aws'

def test__accountid_111111111111__region_me_centr():
    """{AccountId=111111111111, Region=me-central-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='me-central-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.me-central-1.amazonaws.com'

def test__streamarn_arn_aws_dynamodb_me_central_1():
    """{StreamArn=arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-central-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-central-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.me-central-1.amazonaws.com'

def test__sharditerator_arn_aws_dynamodb_me_centr():
    """{ShardIterator=arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-central-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-central-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.me-central-1.amazonaws.com'

def test__accountid_111111111111__region_me_centr():
    """{AccountId=111111111111, Region=me-central-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='me-central-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.me-central-1.api.aws'

def test__streamarn_arn_aws_dynamodb_me_central_1():
    """{StreamArn=arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-central-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-central-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.me-central-1.api.aws'

def test__sharditerator_arn_aws_dynamodb_me_centr():
    """{ShardIterator=arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-central-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-central-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.me-central-1.api.aws'

def test__accountid_111111111111__region_me_centr():
    """{AccountId=111111111111, Region=me-central-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='me-central-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.me-central-1.amazonaws.com'

def test__streamarn_arn_aws_dynamodb_me_central_1():
    """{StreamArn=arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-central-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-central-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.me-central-1.amazonaws.com'

def test__sharditerator_arn_aws_dynamodb_me_centr():
    """{ShardIterator=arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-central-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-central-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.me-central-1.amazonaws.com'

def test__accountid_111111111111__region_me_centr():
    """{AccountId=111111111111, Region=me-central-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='me-central-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.me-central-1.api.aws'

def test__streamarn_arn_aws_dynamodb_me_central_1():
    """{StreamArn=arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-central-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-central-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.me-central-1.api.aws'

def test__sharditerator_arn_aws_dynamodb_me_centr():
    """{ShardIterator=arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-central-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-central-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.me-central-1.api.aws'

def test__accountid_111111111111__region_me_centr():
    """{AccountId=111111111111, Region=me-central-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='me-central-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__streamarn_arn_aws_dynamodb_me_central_1():
    """{StreamArn=arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-central-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-central-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__sharditerator_arn_aws_dynamodb_me_centr():
    """{ShardIterator=arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-central-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-central-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__accountid_111111111111__region_me_centr():
    """{AccountId=111111111111, Region=me-central-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='me-central-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__streamarn_arn_aws_dynamodb_me_central_1():
    """{StreamArn=arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-central-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-central-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__sharditerator_arn_aws_dynamodb_me_centr():
    """{ShardIterator=arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-central-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-central-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__accountid_111111111111__region_me_centr():
    """{AccountId=111111111111, Region=me-central-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='me-central-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__streamarn_arn_aws_dynamodb_me_central_1():
    """{StreamArn=arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-central-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-central-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__sharditerator_arn_aws_dynamodb_me_centr():
    """{ShardIterator=arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-central-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-central-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__accountid_111111111111__region_me_centr():
    """{AccountId=111111111111, Region=me-central-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='me-central-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__streamarn_arn_aws_dynamodb_me_central_1():
    """{StreamArn=arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-central-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-central-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-central-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__sharditerator_arn_aws_dynamodb_me_centr():
    """{ShardIterator=arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-central-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-central-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-central-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__accountid_111111111111__region_me_south():
    """{AccountId=111111111111, Region=me-south-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='me-south-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.me-south-1.amazonaws.com'

def test__streamarn_arn_aws_dynamodb_me_south_1_2():
    """{StreamArn=arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-south-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-south-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.me-south-1.amazonaws.com'

def test__sharditerator_arn_aws_dynamodb_me_south():
    """{ShardIterator=arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-south-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-south-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.me-south-1.amazonaws.com'

def test__accountid_111111111111__region_me_south():
    """{AccountId=111111111111, Region=me-south-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='me-south-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.me-south-1.api.aws'

def test__streamarn_arn_aws_dynamodb_me_south_1_2():
    """{StreamArn=arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-south-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-south-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.me-south-1.api.aws'

def test__sharditerator_arn_aws_dynamodb_me_south():
    """{ShardIterator=arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-south-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-south-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.me-south-1.api.aws'

def test__accountid_111111111111__region_me_south():
    """{AccountId=111111111111, Region=me-south-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='me-south-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.me-south-1.amazonaws.com'

def test__streamarn_arn_aws_dynamodb_me_south_1_2():
    """{StreamArn=arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-south-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-south-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.me-south-1.amazonaws.com'

def test__sharditerator_arn_aws_dynamodb_me_south():
    """{ShardIterator=arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-south-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-south-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.me-south-1.amazonaws.com'

def test__accountid_111111111111__region_me_south():
    """{AccountId=111111111111, Region=me-south-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='me-south-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.me-south-1.api.aws'

def test__streamarn_arn_aws_dynamodb_me_south_1_2():
    """{StreamArn=arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-south-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-south-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.me-south-1.api.aws'

def test__sharditerator_arn_aws_dynamodb_me_south():
    """{ShardIterator=arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-south-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-south-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.me-south-1.api.aws'

def test__accountid_111111111111__region_me_south():
    """{AccountId=111111111111, Region=me-south-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='me-south-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.me-south-1.amazonaws.com'

def test__streamarn_arn_aws_dynamodb_me_south_1_2():
    """{StreamArn=arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-south-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-south-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.me-south-1.amazonaws.com'

def test__sharditerator_arn_aws_dynamodb_me_south():
    """{ShardIterator=arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-south-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-south-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.me-south-1.amazonaws.com'

def test__accountid_111111111111__region_me_south():
    """{AccountId=111111111111, Region=me-south-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='me-south-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.me-south-1.api.aws'

def test__streamarn_arn_aws_dynamodb_me_south_1_2():
    """{StreamArn=arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-south-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-south-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.me-south-1.api.aws'

def test__sharditerator_arn_aws_dynamodb_me_south():
    """{ShardIterator=arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-south-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-south-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.me-south-1.api.aws'

def test__accountid_111111111111__region_me_south():
    """{AccountId=111111111111, Region=me-south-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='me-south-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.me-south-1.amazonaws.com'

def test__streamarn_arn_aws_dynamodb_me_south_1_2():
    """{StreamArn=arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-south-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-south-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.me-south-1.amazonaws.com'

def test__sharditerator_arn_aws_dynamodb_me_south():
    """{ShardIterator=arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-south-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-south-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.me-south-1.amazonaws.com'

def test__accountid_111111111111__region_me_south():
    """{AccountId=111111111111, Region=me-south-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='me-south-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.me-south-1.api.aws'

def test__streamarn_arn_aws_dynamodb_me_south_1_2():
    """{StreamArn=arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-south-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-south-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.me-south-1.api.aws'

def test__sharditerator_arn_aws_dynamodb_me_south():
    """{ShardIterator=arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-south-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-south-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.me-south-1.api.aws'

def test__accountid_111111111111__region_me_south():
    """{AccountId=111111111111, Region=me-south-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='me-south-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__streamarn_arn_aws_dynamodb_me_south_1_2():
    """{StreamArn=arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-south-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-south-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__sharditerator_arn_aws_dynamodb_me_south():
    """{ShardIterator=arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-south-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-south-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__accountid_111111111111__region_me_south():
    """{AccountId=111111111111, Region=me-south-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='me-south-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__streamarn_arn_aws_dynamodb_me_south_1_2():
    """{StreamArn=arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-south-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-south-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__sharditerator_arn_aws_dynamodb_me_south():
    """{ShardIterator=arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-south-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-south-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__accountid_111111111111__region_me_south():
    """{AccountId=111111111111, Region=me-south-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='me-south-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__streamarn_arn_aws_dynamodb_me_south_1_2():
    """{StreamArn=arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-south-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-south-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__sharditerator_arn_aws_dynamodb_me_south():
    """{ShardIterator=arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-south-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-south-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__accountid_111111111111__region_me_south():
    """{AccountId=111111111111, Region=me-south-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='me-south-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__streamarn_arn_aws_dynamodb_me_south_1_2():
    """{StreamArn=arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=me-south-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws:dynamodb:me-south-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='me-south-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__sharditerator_arn_aws_dynamodb_me_south():
    """{ShardIterator=arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=me-south-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws:dynamodb:me-south-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='me-south-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.cn-north-1.amazonaws.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_north_():
    """{StreamArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.cn-north-1.amazonaws.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.cn-north-1.amazonaws.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.cn-north-1.api.amazonwebservices.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_north_():
    """{StreamArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.cn-north-1.api.amazonwebservices.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.cn-north-1.api.amazonwebservices.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.cn-north-1.amazonaws.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_north_():
    """{StreamArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.cn-north-1.amazonaws.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.cn-north-1.amazonaws.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_north_():
    """{StreamArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-north-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-north-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.cn-north-1.amazonaws.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_north_():
    """{StreamArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.cn-north-1.amazonaws.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.cn-north-1.amazonaws.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.cn-north-1.api.amazonwebservices.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_north_():
    """{StreamArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.cn-north-1.api.amazonwebservices.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.cn-north-1.api.amazonwebservices.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.cn-north-1.amazonaws.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_north_():
    """{StreamArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.cn-north-1.amazonaws.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.cn-north-1.amazonaws.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_north_():
    """{StreamArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-north-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-north-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.cn-north-1.amazonaws.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_north_():
    """{StreamArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.cn-north-1.amazonaws.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.cn-north-1.amazonaws.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.cn-north-1.api.amazonwebservices.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_north_():
    """{StreamArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.cn-north-1.api.amazonwebservices.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.cn-north-1.api.amazonwebservices.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.cn-north-1.amazonaws.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_north_():
    """{StreamArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.cn-north-1.amazonaws.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.cn-north-1.amazonaws.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_north_():
    """{StreamArn=arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-north-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-north-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-north-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-north-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-northwest-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-northwest-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.cn-northwest-1.amazonaws.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_northw():
    """{StreamArn=arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-northwest-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-northwest-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.cn-northwest-1.amazonaws.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-northwest-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-northwest-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.cn-northwest-1.amazonaws.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-northwest-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-northwest-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.cn-northwest-1.api.amazonwebservices.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_northw():
    """{StreamArn=arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-northwest-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-northwest-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.cn-northwest-1.api.amazonwebservices.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-northwest-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-northwest-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.cn-northwest-1.api.amazonwebservices.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-northwest-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-northwest-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.cn-northwest-1.amazonaws.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_northw():
    """{StreamArn=arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-northwest-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-northwest-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.cn-northwest-1.amazonaws.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-northwest-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-northwest-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.cn-northwest-1.amazonaws.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-northwest-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-northwest-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.cn-northwest-1.api.amazonwebservices.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_northw():
    """{StreamArn=arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-northwest-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-northwest-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.cn-northwest-1.api.amazonwebservices.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-northwest-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-northwest-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.cn-northwest-1.api.amazonwebservices.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-northwest-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-northwest-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.cn-northwest-1.amazonaws.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_northw():
    """{StreamArn=arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-northwest-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-northwest-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.cn-northwest-1.amazonaws.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-northwest-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-northwest-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.cn-northwest-1.amazonaws.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-northwest-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-northwest-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.cn-northwest-1.api.amazonwebservices.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_northw():
    """{StreamArn=arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-northwest-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-northwest-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.cn-northwest-1.api.amazonwebservices.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-northwest-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-northwest-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.cn-northwest-1.api.amazonwebservices.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-northwest-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-northwest-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.cn-northwest-1.amazonaws.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_northw():
    """{StreamArn=arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-northwest-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-northwest-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.cn-northwest-1.amazonaws.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-northwest-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-northwest-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.cn-northwest-1.amazonaws.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-northwest-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-northwest-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.cn-northwest-1.api.amazonwebservices.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_northw():
    """{StreamArn=arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-northwest-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-northwest-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.cn-northwest-1.api.amazonwebservices.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-northwest-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-northwest-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.cn-northwest-1.api.amazonwebservices.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-northwest-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-northwest-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.cn-northwest-1.amazonaws.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_northw():
    """{StreamArn=arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-northwest-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-northwest-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.cn-northwest-1.amazonaws.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-northwest-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-northwest-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.cn-northwest-1.amazonaws.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-northwest-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-northwest-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.cn-northwest-1.api.amazonwebservices.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_northw():
    """{StreamArn=arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-northwest-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-northwest-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.cn-northwest-1.api.amazonwebservices.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-northwest-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-northwest-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.cn-northwest-1.api.amazonwebservices.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-northwest-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-northwest-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.cn-northwest-1.amazonaws.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_northw():
    """{StreamArn=arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-northwest-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-northwest-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.cn-northwest-1.amazonaws.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-northwest-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-northwest-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.cn-northwest-1.amazonaws.com.cn'

def test__accountid_111111111111__region_cn_north():
    """{AccountId=111111111111, Region=cn-northwest-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='cn-northwest-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.cn-northwest-1.api.amazonwebservices.com.cn'

def test__streamarn_arn_aws_cn_dynamodb_cn_northw():
    """{StreamArn=arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=cn-northwest-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-cn:dynamodb:cn-northwest-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='cn-northwest-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.cn-northwest-1.api.amazonwebservices.com.cn'

def test__sharditerator_arn_aws_cn_dynamodb_cn_no():
    """{ShardIterator=arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=cn-northwest-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-cn:dynamodb:cn-northwest-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='cn-northwest-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.cn-northwest-1.api.amazonwebservices.com.cn'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.us-gov-east-1.amazonaws.com'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.us-gov-east-1.amazonaws.com'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.us-gov-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.us-gov-east-1.api.aws'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.us-gov-east-1.api.aws'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.us-gov-east-1.api.aws'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.us-gov-east-1.amazonaws.com'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.us-gov-east-1.amazonaws.com'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.us-gov-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.us-gov-east-1.api.aws'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.us-gov-east-1.api.aws'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.us-gov-east-1.api.aws'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-gov-east-1.amazonaws.com'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-gov-east-1.amazonaws.com'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-gov-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.us-gov-east-1.api.aws'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.us-gov-east-1.api.aws'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.us-gov-east-1.api.aws'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-gov-east-1.amazonaws.com'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-gov-east-1.amazonaws.com'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-gov-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.us-gov-east-1.api.aws'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.us-gov-east-1.api.aws'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.us-gov-east-1.api.aws'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.us-gov-east-1.amazonaws.com'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.us-gov-east-1.amazonaws.com'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.us-gov-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.us-gov-east-1.api.aws'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.us-gov-east-1.api.aws'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.us-gov-east-1.api.aws'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.us-gov-east-1.amazonaws.com'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.us-gov-east-1.amazonaws.com'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.us-gov-east-1.amazonaws.com'

def test__accountid_111111111111__region_us_gov_e():
    """{AccountId=111111111111, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.us-gov-east-1.api.aws'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.us-gov-east-1.api.aws'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.us-gov-east-1.api.aws'

def test__accountid_111111111111__region_us_gov_w():
    """{AccountId=111111111111, Region=us-gov-west-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-west-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.us-gov-west-1.amazonaws.com'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-west-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-west-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.us-gov-west-1.amazonaws.com'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-west-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-west-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.us-gov-west-1.amazonaws.com'

def test__accountid_111111111111__region_us_gov_w():
    """{AccountId=111111111111, Region=us-gov-west-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-west-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.us-gov-west-1.api.aws'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-west-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-west-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.us-gov-west-1.api.aws'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-west-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-west-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.us-gov-west-1.api.aws'

def test__accountid_111111111111__region_us_gov_w():
    """{AccountId=111111111111, Region=us-gov-west-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-west-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.us-gov-west-1.amazonaws.com'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-west-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-west-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.us-gov-west-1.amazonaws.com'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-west-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-west-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.us-gov-west-1.amazonaws.com'

def test__accountid_111111111111__region_us_gov_w():
    """{AccountId=111111111111, Region=us-gov-west-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-west-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.us-gov-west-1.api.aws'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-west-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-west-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.us-gov-west-1.api.aws'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-west-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-west-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.us-gov-west-1.api.aws'

def test__accountid_111111111111__region_us_gov_w():
    """{AccountId=111111111111, Region=us-gov-west-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-west-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-gov-west-1.amazonaws.com'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-west-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-west-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-gov-west-1.amazonaws.com'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-west-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-west-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-gov-west-1.amazonaws.com'

def test__accountid_111111111111__region_us_gov_w():
    """{AccountId=111111111111, Region=us-gov-west-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-west-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.us-gov-west-1.api.aws'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-west-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-west-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.us-gov-west-1.api.aws'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-west-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-west-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.us-gov-west-1.api.aws'

def test__accountid_111111111111__region_us_gov_w():
    """{AccountId=111111111111, Region=us-gov-west-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-west-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-gov-west-1.amazonaws.com'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-west-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-west-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-gov-west-1.amazonaws.com'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-west-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-west-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-gov-west-1.amazonaws.com'

def test__accountid_111111111111__region_us_gov_w():
    """{AccountId=111111111111, Region=us-gov-west-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-west-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.us-gov-west-1.api.aws'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-west-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-west-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.us-gov-west-1.api.aws'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-west-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-west-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.us-gov-west-1.api.aws'

def test__accountid_111111111111__region_us_gov_w():
    """{AccountId=111111111111, Region=us-gov-west-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-west-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.us-gov-west-1.amazonaws.com'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-west-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-west-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.us-gov-west-1.amazonaws.com'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-west-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-west-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.us-gov-west-1.amazonaws.com'

def test__accountid_111111111111__region_us_gov_w():
    """{AccountId=111111111111, Region=us-gov-west-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-west-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.us-gov-west-1.api.aws'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-west-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-west-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb.us-gov-west-1.api.aws'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-west-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-west-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb.us-gov-west-1.api.aws'

def test__accountid_111111111111__region_us_gov_w():
    """{AccountId=111111111111, Region=us-gov-west-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-west-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.us-gov-west-1.amazonaws.com'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-west-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-west-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.us-gov-west-1.amazonaws.com'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-west-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-west-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.us-gov-west-1.amazonaws.com'

def test__accountid_111111111111__region_us_gov_w():
    """{AccountId=111111111111, Region=us-gov-west-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-gov-west-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb-fips.us-gov-west-1.api.aws'

def test__streamarn_arn_aws_us_gov_dynamodb_us_go():
    """{StreamArn=arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-gov-west-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-us-gov:dynamodb:us-gov-west-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-gov-west-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://222222222222.streams-ddb-fips.us-gov-west-1.api.aws'

def test__sharditerator_arn_aws_us_gov_dynamodb_u():
    """{ShardIterator=arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-gov-west-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-us-gov:dynamodb:us-gov-west-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-gov-west-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://333333333333.streams-ddb-fips.us-gov-west-1.api.aws'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-iso-east-1.c2s.ic.gov'

def test__streamarn_arn_aws_iso_dynamodb_us_iso_e():
    """{StreamArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-iso-east-1.c2s.ic.gov'

def test__sharditerator_arn_aws_iso_dynamodb_us_i():
    """{ShardIterator=arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-iso-east-1.c2s.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.us-iso-east-1.api.aws.ic.gov'

def test__streamarn_arn_aws_iso_dynamodb_us_iso_e():
    """{StreamArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.us-iso-east-1.api.aws.ic.gov'

def test__sharditerator_arn_aws_iso_dynamodb_us_i():
    """{ShardIterator=arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.us-iso-east-1.api.aws.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.us-iso-east-1.c2s.ic.gov'

def test__streamarn_arn_aws_iso_dynamodb_us_iso_e():
    """{StreamArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.us-iso-east-1.c2s.ic.gov'

def test__sharditerator_arn_aws_iso_dynamodb_us_i():
    """{ShardIterator=arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.us-iso-east-1.c2s.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.us-iso-east-1.api.aws.ic.gov'

def test__streamarn_arn_aws_iso_dynamodb_us_iso_e():
    """{StreamArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.us-iso-east-1.api.aws.ic.gov'

def test__sharditerator_arn_aws_iso_dynamodb_us_i():
    """{ShardIterator=arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-iso-east-1, AccountIdEndpointMode=preferred, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-iso-east-1', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.us-iso-east-1.api.aws.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-iso-east-1.c2s.ic.gov'

def test__streamarn_arn_aws_iso_dynamodb_us_iso_e():
    """{StreamArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-iso-east-1.c2s.ic.gov'

def test__sharditerator_arn_aws_iso_dynamodb_us_i():
    """{ShardIterator=arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-iso-east-1.c2s.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.us-iso-east-1.api.aws.ic.gov'

def test__streamarn_arn_aws_iso_dynamodb_us_iso_e():
    """{StreamArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.us-iso-east-1.api.aws.ic.gov'

def test__sharditerator_arn_aws_iso_dynamodb_us_i():
    """{ShardIterator=arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb.us-iso-east-1.api.aws.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.us-iso-east-1.c2s.ic.gov'

def test__streamarn_arn_aws_iso_dynamodb_us_iso_e():
    """{StreamArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.us-iso-east-1.c2s.ic.gov'

def test__sharditerator_arn_aws_iso_dynamodb_us_i():
    """{ShardIterator=arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb-fips.us-iso-east-1.c2s.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.us-iso-east-1.api.aws.ic.gov'

def test__streamarn_arn_aws_iso_dynamodb_us_iso_e():
    """{StreamArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.us-iso-east-1.api.aws.ic.gov'

def test__sharditerator_arn_aws_iso_dynamodb_us_i():
    """{ShardIterator=arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-iso-east-1, AccountIdEndpointMode=disabled, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-iso-east-1', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://streams-dynamodb-fips.us-iso-east-1.api.aws.ic.gov'

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__streamarn_arn_aws_iso_dynamodb_us_iso_e():
    """{StreamArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__sharditerator_arn_aws_iso_dynamodb_us_i():
    """{ShardIterator=arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__streamarn_arn_aws_iso_dynamodb_us_iso_e():
    """{StreamArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__sharditerator_arn_aws_iso_dynamodb_us_i():
    """{ShardIterator=arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=false, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=False, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__streamarn_arn_aws_iso_dynamodb_us_iso_e():
    """{StreamArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(StreamArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__sharditerator_arn_aws_iso_dynamodb_us_i():
    """{ShardIterator=arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=false}"""
    params = EndpointParams(ShardIterator='arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__accountid_111111111111__region_us_iso_e():
    """{AccountId=111111111111, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(AccountId='111111111111', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__streamarn_arn_aws_iso_dynamodb_us_iso_e():
    """{StreamArn=arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(StreamArn='arn:aws-iso:dynamodb:us-iso-east-1:222222222222:table/T/stream/2024-01-01T00:00:00.000', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__sharditerator_arn_aws_iso_dynamodb_us_i():
    """{ShardIterator=arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz, Region=us-iso-east-1, AccountIdEndpointMode=required, UseFIPS=true, UseDualStack=true}"""
    params = EndpointParams(ShardIterator='arn:aws-iso:dynamodb:us-iso-east-1:333333333333:table/T/stream/2024-01-01T00:00:00.000|1|AAAAAAAAAAIxyz', Region='us-iso-east-1', AccountIdEndpointMode='required', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region')):
        resolve(params)

def test__region_us_new_1__accountidendpointmode_():
    """{Region=us-new-1, AccountIdEndpointMode=preferred, AccountId=111111111111, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(Region='us-new-1', AccountIdEndpointMode='preferred', AccountId='111111111111', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.us-new-1.amazonaws.com'

def test__region_cn_new_1__accountidendpointmode_():
    """{Region=cn-new-1, AccountIdEndpointMode=preferred, AccountId=111111111111, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(Region='cn-new-1', AccountIdEndpointMode='preferred', AccountId='111111111111', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.cn-new-1.amazonaws.com.cn'

def test__region_us_gov_new_1__accountidendpointm():
    """{Region=us-gov-new-1, AccountIdEndpointMode=preferred, AccountId=111111111111, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(Region='us-gov-new-1', AccountIdEndpointMode='preferred', AccountId='111111111111', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://111111111111.streams-ddb.us-gov-new-1.amazonaws.com'

def test__region_us_iso_new_1__accountidendpointm():
    """{Region=us-iso-new-1, AccountIdEndpointMode=preferred, AccountId=111111111111, UseFIPS=false, UseDualStack=false}"""
    params = EndpointParams(Region='us-iso-new-1', AccountIdEndpointMode='preferred', AccountId='111111111111', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://streams.dynamodb.us-iso-new-1.c2s.ic.gov'