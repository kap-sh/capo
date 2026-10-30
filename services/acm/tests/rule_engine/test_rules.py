import pytest
from capo_acm._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_acm._rule_engine._endpoint_runtime import EndpointError
import re
import zapros

def test_for_region_af_south_1_with_fips_disabled():
    """For region af-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='af-south-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.af-south-1.amazonaws.com'

def test_for_region_ap_east_1_with_fips_disabled_():
    """For region ap-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-east-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.ap-east-1.amazonaws.com'

def test_for_region_ap_northeast_1_with_fips_disa():
    """For region ap-northeast-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.ap-northeast-1.amazonaws.com'

def test_for_region_ap_northeast_2_with_fips_disa():
    """For region ap-northeast-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-2', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.ap-northeast-2.amazonaws.com'

def test_for_region_ap_northeast_3_with_fips_disa():
    """For region ap-northeast-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-3', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.ap-northeast-3.amazonaws.com'

def test_for_region_ap_south_1_with_fips_disabled():
    """For region ap-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-south-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.ap-south-1.amazonaws.com'

def test_for_region_ap_southeast_1_with_fips_disa():
    """For region ap-southeast-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.ap-southeast-1.amazonaws.com'

def test_for_region_ap_southeast_2_with_fips_disa():
    """For region ap-southeast-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-2', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.ap-southeast-2.amazonaws.com'

def test_for_region_ap_southeast_3_with_fips_disa():
    """For region ap-southeast-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-3', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.ap-southeast-3.amazonaws.com'

def test_for_region_ca_central_1_with_fips_disabl():
    """For region ca-central-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ca-central-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.ca-central-1.amazonaws.com'

def test_for_region_eu_central_1_with_fips_disabl():
    """For region eu-central-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-central-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.eu-central-1.amazonaws.com'

def test_for_region_eu_north_1_with_fips_disabled():
    """For region eu-north-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-north-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.eu-north-1.amazonaws.com'

def test_for_region_eu_south_1_with_fips_disabled():
    """For region eu-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-south-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.eu-south-1.amazonaws.com'

def test_for_region_eu_west_1_with_fips_disabled_():
    """For region eu-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.eu-west-1.amazonaws.com'

def test_for_region_eu_west_2_with_fips_disabled_():
    """For region eu-west-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-2', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.eu-west-2.amazonaws.com'

def test_for_region_eu_west_3_with_fips_disabled_():
    """For region eu-west-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-3', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.eu-west-3.amazonaws.com'

def test_for_region_me_south_1_with_fips_disabled():
    """For region me-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='me-south-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.me-south-1.amazonaws.com'

def test_for_region_sa_east_1_with_fips_disabled_():
    """For region sa-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='sa-east-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.sa-east-1.amazonaws.com'

def test_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.us-east-1.amazonaws.com'

def test_for_region_us_east_2_with_fips_disabled_():
    """For region us-east-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-2', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.us-east-2.amazonaws.com'

def test_for_region_us_west_1_with_fips_disabled_():
    """For region us-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.us-west-1.amazonaws.com'

def test_for_region_us_west_2_with_fips_disabled_():
    """For region us-west-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.us-west-2.amazonaws.com'

def test_for_region_ca_central_1_with_fips_enable():
    """For region ca-central-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='ca-central-1', UseFIPS=True, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm-fips.ca-central-1.amazonaws.com'

def test_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm-fips.us-east-1.amazonaws.com'

def test_for_region_us_east_2_with_fips_enabled_a():
    """For region us-east-2 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-2', UseFIPS=True, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm-fips.us-east-2.amazonaws.com'

def test_for_region_us_west_1_with_fips_enabled_a():
    """For region us-west-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=True, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm-fips.us-west-1.amazonaws.com'

def test_for_region_us_west_2_with_fips_enabled_a():
    """For region us-west-2 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-2', UseFIPS=True, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm-fips.us-west-2.amazonaws.com'

def test_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm-fips.us-east-1.api.aws'

def test_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.us-east-1.api.aws'

def test_for_region_cn_north_1_with_fips_disabled():
    """For region cn-north-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.cn-north-1.amazonaws.com.cn'

def test_for_region_cn_northwest_1_with_fips_disa():
    """For region cn-northwest-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.cn-northwest-1.amazonaws.com.cn'

def test_for_region_cn_north_1_with_fips_enabled_():
    """For region cn-north-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=True, UseDualStack=True, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm-fips.cn-north-1.api.amazonwebservices.com.cn'

def test_for_region_cn_north_1_with_fips_enabled_():
    """For region cn-north-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=True, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm-fips.cn-north-1.amazonaws.com.cn'

def test_for_region_cn_north_1_with_fips_disabled():
    """For region cn-north-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=False, UseDualStack=True, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.cn-north-1.api.amazonwebservices.com.cn'

def test_for_region_us_gov_east_1_with_fips_disab():
    """For region us-gov-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.us-gov-east-1.amazonaws.com'

def test_for_region_us_gov_west_1_with_fips_disab():
    """For region us-gov-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.us-gov-west-1.amazonaws.com'

def test_for_region_us_gov_east_1_with_fips_enabl():
    """For region us-gov-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=True, UseDualStack=True, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm-fips.us-gov-east-1.api.aws'

def test_for_region_us_gov_east_1_with_fips_enabl():
    """For region us-gov-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=True, UseDualStack=False, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.us-gov-east-1.amazonaws.com'

def test_for_region_us_gov_east_1_with_fips_disab():
    """For region us-gov-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=False, UseDualStack=True, ServiceType='ACM')
    result = resolve(params)
    assert result.url == 'https://acm.us-gov-east-1.api.aws'

def test_for_custom_endpoint_with_region_set_and_():
    """For custom endpoint with region set and fips disabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_for_custom_endpoint_with_fips_enabled_an():
    """For custom endpoint with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, ServiceType='ACM', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_for_custom_endpoint_with_fips_disabled_a():
    """For custom endpoint with FIPS disabled and dualstack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, ServiceType='ACM', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_acm_acme_standard_endpoint_for_us_east_1():
    """ACM-ACME standard endpoint for us-east-1"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM-ACME')
    result = resolve(params)
    assert result.url == 'https://acm-acme.us-east-1.api.aws'

def test_acm_acme_fips_returns_error():
    """ACM-ACME FIPS returns error"""
    params = EndpointParams(Region='us-west-2', UseFIPS=True, UseDualStack=False, ServiceType='ACM-ACME')
    with pytest.raises(EndpointError, match=re.escape('FIPS endpoints are not available for ACME operations')):
        resolve(params)

def test_acm_acme_custom_endpoint():
    """ACM-ACME custom endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM-ACME', Endpoint='https://custom.example.com')
    result = resolve(params)
    assert result.url == 'https://custom.example.com'

def test_acm_acme_standard_endpoint_for_us_gov_we():
    """ACM-ACME standard endpoint for us-gov-west-1"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM-ACME')
    result = resolve(params)
    assert result.url == 'https://acm-acme.us-gov-west-1.api.aws'

def test_acm_acme_standard_endpoint_for_us_gov_ea():
    """ACM-ACME standard endpoint for us-gov-east-1"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM-ACME')
    result = resolve(params)
    assert result.url == 'https://acm-acme.us-gov-east-1.api.aws'

def test_acm_acme_in_cn_north_1_returns_partition():
    """ACM-ACME in cn-north-1 returns partition error"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM-ACME')
    with pytest.raises(EndpointError, match=re.escape('ACME operations are only available in the aws and aws-us-gov partitions')):
        resolve(params)

def test_acm_acme_in_cn_northwest_1_returns_parti():
    """ACM-ACME in cn-northwest-1 returns partition error"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=False, UseDualStack=False, ServiceType='ACM-ACME')
    with pytest.raises(EndpointError, match=re.escape('ACME operations are only available in the aws and aws-us-gov partitions')):
        resolve(params)

def test_acm_acme_with_dualstack_enabled_for_us_g():
    """ACM-ACME with DualStack enabled for us-gov-west-1"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=True, ServiceType='ACM-ACME')
    result = resolve(params)
    assert result.url == 'https://acm-acme.us-gov-west-1.api.aws'

def test_acm_acme_fips_in_us_gov_west_1_returns_e():
    """ACM-ACME FIPS in us-gov-west-1 returns error"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=True, UseDualStack=False, ServiceType='ACM-ACME')
    with pytest.raises(EndpointError, match=re.escape('FIPS endpoints are not available for ACME operations')):
        resolve(params)