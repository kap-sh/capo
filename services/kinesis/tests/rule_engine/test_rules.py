import pytest
from capo_kinesis._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_kinesis._rule_engine._endpoint_runtime import EndpointError
import re
import zapros

def test_for_region_af_south_1_with_fips_disabled():
    """For region af-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='af-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.af-south-1.amazonaws.com'

def test_for_region_ap_east_1_with_fips_disabled_():
    """For region ap-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.ap-east-1.amazonaws.com'

def test_for_region_ap_northeast_1_with_fips_disa():
    """For region ap-northeast-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.ap-northeast-1.amazonaws.com'

def test_for_region_ap_northeast_2_with_fips_disa():
    """For region ap-northeast-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.ap-northeast-2.amazonaws.com'

def test_for_region_ap_northeast_3_with_fips_disa():
    """For region ap-northeast-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-3', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.ap-northeast-3.amazonaws.com'

def test_for_region_ap_south_1_with_fips_disabled():
    """For region ap-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.ap-south-1.amazonaws.com'

def test_for_region_ap_southeast_1_with_fips_disa():
    """For region ap-southeast-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.ap-southeast-1.amazonaws.com'

def test_for_region_ap_southeast_2_with_fips_disa():
    """For region ap-southeast-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.ap-southeast-2.amazonaws.com'

def test_for_region_ap_southeast_3_with_fips_disa():
    """For region ap-southeast-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-3', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.ap-southeast-3.amazonaws.com'

def test_for_region_ca_central_1_with_fips_disabl():
    """For region ca-central-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ca-central-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.ca-central-1.amazonaws.com'

def test_for_region_eu_central_1_with_fips_disabl():
    """For region eu-central-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-central-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.eu-central-1.amazonaws.com'

def test_for_region_eu_north_1_with_fips_disabled():
    """For region eu-north-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-north-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.eu-north-1.amazonaws.com'

def test_for_region_eu_south_1_with_fips_disabled():
    """For region eu-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.eu-south-1.amazonaws.com'

def test_for_region_eu_west_1_with_fips_disabled_():
    """For region eu-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.eu-west-1.amazonaws.com'

def test_for_region_eu_west_2_with_fips_disabled_():
    """For region eu-west-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.eu-west-2.amazonaws.com'

def test_for_region_eu_west_3_with_fips_disabled_():
    """For region eu-west-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-3', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.eu-west-3.amazonaws.com'

def test_for_region_me_south_1_with_fips_disabled():
    """For region me-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='me-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.me-south-1.amazonaws.com'

def test_for_region_sa_east_1_with_fips_disabled_():
    """For region sa-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='sa-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.sa-east-1.amazonaws.com'

def test_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-east-1.amazonaws.com'

def test_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-east-1.amazonaws.com'

def test_for_region_us_east_2_with_fips_disabled_():
    """For region us-east-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-east-2.amazonaws.com'

def test_for_region_us_east_2_with_fips_enabled_a():
    """For region us-east-2 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-2', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-east-2.amazonaws.com'

def test_for_region_us_west_1_with_fips_disabled_():
    """For region us-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-west-1.amazonaws.com'

def test_for_region_us_west_1_with_fips_enabled_a():
    """For region us-west-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-west-1.amazonaws.com'

def test_for_region_us_west_2_with_fips_disabled_():
    """For region us-west-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-west-2.amazonaws.com'

def test_for_region_us_west_2_with_fips_enabled_a():
    """For region us-west-2 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-2', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-west-2.amazonaws.com'

def test_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-east-1.api.aws'

def test_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-east-1.api.aws'

def test_for_region_cn_north_1_with_fips_disabled():
    """For region cn-north-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.cn-north-1.amazonaws.com.cn'

def test_for_region_cn_northwest_1_with_fips_disa():
    """For region cn-northwest-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.cn-northwest-1.amazonaws.com.cn'

def test_for_region_cn_north_1_with_fips_enabled_():
    """For region cn-north-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.cn-north-1.api.amazonwebservices.com.cn'

def test_for_region_cn_north_1_with_fips_enabled_():
    """For region cn-north-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.cn-north-1.amazonaws.com.cn'

def test_for_region_cn_north_1_with_fips_disabled():
    """For region cn-north-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://kinesis.cn-north-1.api.amazonwebservices.com.cn'

def test_for_region_us_gov_east_1_with_fips_disab():
    """For region us-gov-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-gov-east-1.amazonaws.com'

def test_for_region_us_gov_east_1_with_fips_enabl():
    """For region us-gov-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-gov-east-1.amazonaws.com'

def test_for_region_us_gov_west_1_with_fips_disab():
    """For region us-gov-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-gov-west-1.amazonaws.com'

def test_for_region_us_gov_west_1_with_fips_enabl():
    """For region us-gov-west-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-gov-west-1.amazonaws.com'

def test_for_region_us_gov_east_1_with_fips_enabl():
    """For region us-gov-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-gov-east-1.api.aws'

def test_for_region_us_gov_east_1_with_fips_disab():
    """For region us-gov-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-gov-east-1.api.aws'

def test_for_region_us_iso_east_1_with_fips_disab():
    """For region us-iso-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-east-1.c2s.ic.gov'

def test_for_region_us_iso_west_1_with_fips_disab():
    """For region us-iso-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-west-1.c2s.ic.gov'

def test_for_region_us_iso_east_1_with_fips_enabl():
    """For region us-iso-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-iso-east-1.c2s.ic.gov'

def test_for_region_us_isob_east_1_with_fips_disa():
    """For region us-isob-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-isob-east-1.sc2s.sgov.gov'

def test_for_region_us_isob_east_1_with_fips_enab():
    """For region us-isob-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-isob-east-1.sc2s.sgov.gov'

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

def test_invalid_arn__failed_to_parse_arn_():
    """Invalid ARN: Failed to parse ARN."""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, StreamARN='arn')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Failed to parse ARN.')):
        resolve(params)

def test_invalid_arn__partition_missing_from_arn_():
    """Invalid ARN: partition missing from ARN."""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, StreamARN='arn::kinesis:us-west-2:123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Failed to parse ARN.')):
        resolve(params)

def test_invalid_arn__partitions_mismatch_():
    """Invalid ARN: partitions mismatch."""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=False, StreamARN='arn:aws:kinesis:us-west-2:123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape("Partition: aws from ARN doesn't match with partition name: aws-us-gov.")):
        resolve(params)

def test_invalid_arn__not_kinesis():
    """Invalid ARN: Not Kinesis"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, StreamARN='arn:aws:s3:us-west-2:123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The ARN was not for the Kinesis service, found: s3.')):
        resolve(params)

def test_invalid_arn__region_is_missing_in_arn():
    """Invalid ARN: Region is missing in ARN"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, StreamARN='arn:aws:kinesis::123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid region.')):
        resolve(params)

def test_invalid_arn__region_is_empty_string_in_a():
    """Invalid ARN: Region is empty string in ARN"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, StreamARN='arn:aws:kinesis:  :123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid region.')):
        resolve(params)

def test_invalid_arn__invalid_account_id():
    """Invalid ARN: Invalid account id"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, StreamARN='arn:aws:kinesis:us-east-1::stream/testStream', OperationType='control')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid account id.')):
        resolve(params)

def test_invalid_arn__invalid_account_id():
    """Invalid ARN: Invalid account id"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, StreamARN='arn:aws:kinesis:us-east-1:   :stream/testStream', OperationType='control')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid account id.')):
        resolve(params)

def test_invalid_arn__kinesis_arns_only_support_s():
    """Invalid ARN: Kinesis ARNs only support stream arn types"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, StreamARN='arn:aws:kinesis:us-east-1:123:accesspoint/testStream')
    with pytest.raises(EndpointError, match=re.escape("Invalid ARN: Kinesis ARNs don't support `accesspoint` arn types.")):
        resolve(params)

def test_operationtype_not_set():
    """OperationType not set"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, StreamARN='arn:aws:kinesis:us-east-1:123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape('Operation Type is not set. Please contact service team for resolution.')):
        resolve(params)

def test_custom_endpoint_is_specified():
    """Custom Endpoint is specified"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_account_endpoint_targeting_control_opera():
    """Account endpoint targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-east-1.amazonaws.com'

def test_account_endpoint_targeting_data_operatio():
    """Account endpoint targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-east-1.amazonaws.com'

def test_account_endpoint_with_fips_targeting_dat():
    """Account endpoint with fips targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='data', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.us-east-1.amazonaws.com'

def test_account_endpoint_with_fips_targeting_con():
    """Account endpoint with fips targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis-fips.us-east-1.amazonaws.com'

def test_account_endpoint_with_dual_stack_and_fip():
    """Account endpoint with Dual Stack and FIPS enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis-fips.us-east-1.api.aws'

def test_account_endpoint_with_dual_stack_enabled():
    """Account endpoint with Dual Stack enabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=True, OperationType='data', StreamARN='arn:aws:kinesis:us-west-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-west-1.api.aws'

def test_account_endpoint_with_fips_and_dualstack():
    """Account endpoint with FIPS and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=False, OperationType='control', StreamARN='arn:aws:kinesis:us-west-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-west-1.amazonaws.com'

def test_regionmismatch__client_region_should_be_():
    """RegionMismatch: client region should be used for endpoint region"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', StreamARN='arn:aws:kinesis:us-west-1:123:stream/testStream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-east-1.amazonaws.com'

def test_account_endpoint_with_fips_enabled():
    """Account endpoint with FIPS enabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=True, UseDualStack=False, OperationType='data', StreamARN='arn:aws-cn:kinesis:cn-northwest-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.cn-northwest-1.amazonaws.com.cn'

def test_account_endpoint_with_fips_and_dualstack():
    """Account endpoint with FIPS and DualStack enabled for cn regions."""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=True, UseDualStack=True, OperationType='data', StreamARN='arn:aws-cn:kinesis:cn-northwest-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.cn-northwest-1.api.amazonwebservices.com.cn'

def test_account_endpoint_targeting_control_opera():
    """Account endpoint targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', StreamARN='arn:aws-iso:kinesis:us-iso-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-east-1.c2s.ic.gov'

def test_account_endpoint_targeting_control_opera():
    """Account endpoint targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-west-1', UseFIPS=False, UseDualStack=False, OperationType='control', StreamARN='arn:aws-iso:kinesis:us-iso-west-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-west-1.c2s.ic.gov'

def test_account_endpoint_targeting_data_operatio():
    """Account endpoint targeting data operation type in ADC regions"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', StreamARN='arn:aws-iso-b:kinesis:us-isob-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-isob-east-1.sc2s.sgov.gov'

def test_account_endpoint_with_fips_targeting_con():
    """Account endpoint with fips targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', StreamARN='arn:aws-iso:kinesis:us-iso-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-iso-east-1.c2s.ic.gov'

def test_account_endpoint_with_fips_targeting_dat():
    """Account endpoint with fips targeting data operation type in ADC regions"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=True, UseDualStack=False, OperationType='data', StreamARN='arn:aws-iso-b:kinesis:us-isob-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-isob-east-1.sc2s.sgov.gov'

def test_invalid_consumerarn__failed_to_parse_arn():
    """Invalid ConsumerARN: Failed to parse ARN."""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ConsumerARN='arn')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Failed to parse ARN.')):
        resolve(params)

def test_invalid_consumerarn__partition_missing_f():
    """Invalid ConsumerARN: partition missing from ARN."""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ConsumerARN='arn::kinesis:us-west-2:123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Failed to parse ARN.')):
        resolve(params)

def test_invalid_arn__partitions_mismatch_():
    """Invalid ARN: partitions mismatch."""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=False, ConsumerARN='arn:aws:kinesis:us-west-2:123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape("Partition: aws from ARN doesn't match with partition name: aws-us-gov.")):
        resolve(params)

def test_invalid_arn__not_kinesis():
    """Invalid ARN: Not Kinesis"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ConsumerARN='arn:aws:s3:us-west-2:123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The ARN was not for the Kinesis service, found: s3.')):
        resolve(params)

def test_invalid_arn__region_is_missing_in_arn():
    """Invalid ARN: Region is missing in ARN"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ConsumerARN='arn:aws:kinesis::123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid region.')):
        resolve(params)

def test_invalid_arn__region_is_empty_string_in_a():
    """Invalid ARN: Region is empty string in ARN"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ConsumerARN='arn:aws:kinesis:  :123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid region.')):
        resolve(params)

def test_invalid_arn__invalid_account_id():
    """Invalid ARN: Invalid account id"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ConsumerARN='arn:aws:kinesis:us-east-1::stream/testStream/consumer/test-consumer:1525898737', OperationType='control')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid account id.')):
        resolve(params)

def test_invalid_arn__invalid_account_id():
    """Invalid ARN: Invalid account id"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ConsumerARN='arn:aws:kinesis:us-east-1:   :stream/testStream/consumer/test-consumer:1525898737', OperationType='control')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid account id.')):
        resolve(params)

def test_invalid_arn__kinesis_arns_only_support_s():
    """Invalid ARN: Kinesis ARNs only support stream arn/consumer arn types"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ConsumerARN='arn:aws:kinesis:us-east-1:123:accesspoint/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape("Invalid ARN: Kinesis ARNs don't support `accesspoint` arn types.")):
        resolve(params)

def test_operationtype_not_set():
    """OperationType not set"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ConsumerARN='arn:aws:kinesis:us-east-1:123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape('Operation Type is not set. Please contact service team for resolution.')):
        resolve(params)

def test_custom_endpoint_is_specified():
    """Custom Endpoint is specified"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ConsumerARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_account_endpoint_targeting_control_opera():
    """Account endpoint targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ConsumerARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-east-1.amazonaws.com'

def test_account_endpoint_targeting_data_operatio():
    """Account endpoint targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ConsumerARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-east-1.amazonaws.com'

def test_account_endpoint_with_fips_targeting_dat():
    """Account endpoint with fips targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='data', ConsumerARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.us-east-1.amazonaws.com'

def test_account_endpoint_with_fips_targeting_con():
    """Account endpoint with fips targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', ConsumerARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis-fips.us-east-1.amazonaws.com'

def test_account_endpoint_with_dual_stack_and_fip():
    """Account endpoint with Dual Stack and FIPS enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', ConsumerARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis-fips.us-east-1.api.aws'

def test_account_endpoint_with_dual_stack_enabled():
    """Account endpoint with Dual Stack enabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=True, OperationType='data', ConsumerARN='arn:aws:kinesis:us-west-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-west-1.api.aws'

def test_account_endpoint_with_fips_and_dualstack():
    """Account endpoint with FIPS and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=False, OperationType='control', ConsumerARN='arn:aws:kinesis:us-west-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-west-1.amazonaws.com'

def test_regionmismatch__client_region_should_be_():
    """RegionMismatch: client region should be used for endpoint region"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ConsumerARN='arn:aws:kinesis:us-west-1:123:stream/testStream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-east-1.amazonaws.com'

def test_account_endpoint_with_fips_enabled():
    """Account endpoint with FIPS enabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=True, UseDualStack=False, OperationType='data', ConsumerARN='arn:aws-cn:kinesis:cn-northwest-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.cn-northwest-1.amazonaws.com.cn'

def test_account_endpoint_with_fips_and_dualstack():
    """Account endpoint with FIPS and DualStack enabled for cn regions."""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=True, UseDualStack=True, OperationType='data', ConsumerARN='arn:aws-cn:kinesis:cn-northwest-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.cn-northwest-1.api.amazonwebservices.com.cn'

def test_account_endpoint_targeting_control_opera():
    """Account endpoint targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ConsumerARN='arn:aws-iso:kinesis:us-iso-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-east-1.c2s.ic.gov'

def test_account_endpoint_targeting_control_opera():
    """Account endpoint targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-west-1', UseFIPS=False, UseDualStack=False, OperationType='control', ConsumerARN='arn:aws-iso:kinesis:us-iso-west-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-west-1.c2s.ic.gov'

def test_account_endpoint_targeting_data_operatio():
    """Account endpoint targeting data operation type in ADC regions"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ConsumerARN='arn:aws-iso-b:kinesis:us-isob-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-isob-east-1.sc2s.sgov.gov'

def test_account_endpoint_with_fips_targeting_con():
    """Account endpoint with fips targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', ConsumerARN='arn:aws-iso:kinesis:us-iso-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-iso-east-1.c2s.ic.gov'

def test_account_endpoint_with_fips_targeting_dat():
    """Account endpoint with fips targeting data operation type in ADC regions"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=True, UseDualStack=False, OperationType='data', ConsumerARN='arn:aws-iso-b:kinesis:us-isob-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-isob-east-1.sc2s.sgov.gov'

def test_consumerarn_targeting_us_east_1():
    """ConsumerARN targeting US-EAST-1"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ConsumerARN='arn:aws:kinesis:us-east-1:123456789123:stream/foobar/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123456789123.data-kinesis.us-east-1.amazonaws.com'

def test_both_streamarn_and_consumerarn_specified():
    """Both StreamARN and ConsumerARN specified. StreamARN should take precedence"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', StreamARN='arn:aws:kinesis:us-east-1:123:stream/foobar', ConsumerARN='arn:aws:kinesis:us-east-1:123456789123:stream/foobar/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-east-1.amazonaws.com'

def test_resourcearn_test__invalid_arn__failed_to():
    """ResourceARN test: Invalid ARN: Failed to parse ARN."""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Failed to parse ARN.')):
        resolve(params)

def test_resourcearn_as_streamarn_test__invalid_a():
    """ResourceARN as StreamARN test: Invalid ARN: partition missing from ARN."""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn::kinesis:us-west-2:123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Failed to parse ARN.')):
        resolve(params)

def test_resourcearn_as_streamarn_test__invalid_a():
    """ResourceARN as StreamARN test: Invalid ARN: partitions mismatch."""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:us-west-2:123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape("Partition: aws from ARN doesn't match with partition name: aws-us-gov.")):
        resolve(params)

def test_resourcearn_as_streamarn_test__invalid_a():
    """ResourceARN as StreamARN test: Invalid ARN: Not Kinesis"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:s3:us-west-2:123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The ARN was not for the Kinesis service, found: s3.')):
        resolve(params)

def test_resourcearn_as_streamarn_test__invalid_a():
    """ResourceARN as StreamARN test: Invalid ARN: Region is missing in ARN"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis::123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid region.')):
        resolve(params)

def test_resourcearn_as_streamarn_test__invalid_a():
    """ResourceARN as StreamARN test: Invalid ARN: Region is empty string in ARN"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:  :123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid region.')):
        resolve(params)

def test_resourcearn_as_streamarn_test__invalid_a():
    """ResourceARN as StreamARN test: Invalid ARN: Invalid account id"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:us-east-1::stream/testStream', OperationType='control')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid account id.')):
        resolve(params)

def test_resourcearn_as_streamarn_test__invalid_a():
    """ResourceARN as StreamARN test: Invalid ARN: Invalid account id"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:us-east-1:   :stream/testStream', OperationType='control')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid account id.')):
        resolve(params)

def test_resourcearn_as_streamarn_test__invalid_a():
    """ResourceARN as StreamARN test: Invalid ARN: Kinesis ARNs only support stream arn types"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:us-east-1:123:accesspoint/testStream')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Unsupported resource type `accesspoint`. Expected: stream, channel, or queue.')):
        resolve(params)

def test_resourcearn_as_streamarn_test__operation():
    """ResourceARN as StreamARN test: OperationType not set"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:us-east-1:123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape('Operation Type is not set. Please contact service team for resolution.')):
        resolve(params)

def test_resourcearn_as_streamarn_test__custom_en():
    """ResourceARN as StreamARN test: Custom Endpoint is specified"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-east-1.amazonaws.com'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-east-1.amazonaws.com'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint with fips targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='data', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.us-east-1.amazonaws.com'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint with fips targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis-fips.us-east-1.amazonaws.com'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint with Dual Stack and FIPS enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis-fips.us-east-1.api.aws'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint with Dual Stack enabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=True, OperationType='data', ResourceARN='arn:aws:kinesis:us-west-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-west-1.api.aws'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint with FIPS and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-west-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-west-1.amazonaws.com'

def test_resourcearn_as_streamarn_test__regionmis():
    """ResourceARN as StreamARN test: RegionMismatch: client region should be used for endpoint region"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ResourceARN='arn:aws:kinesis:us-west-1:123:stream/testStream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-east-1.amazonaws.com'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint with FIPS enabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=True, UseDualStack=False, OperationType='data', ResourceARN='arn:aws-cn:kinesis:cn-northwest-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.cn-northwest-1.amazonaws.com.cn'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint with FIPS and DualStack enabled for cn regions."""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=True, UseDualStack=True, OperationType='data', ResourceARN='arn:aws-cn:kinesis:cn-northwest-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.cn-northwest-1.api.amazonwebservices.com.cn'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-iso:kinesis:us-iso-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-east-1.c2s.ic.gov'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-west-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-iso:kinesis:us-iso-west-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-west-1.c2s.ic.gov'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint targeting data operation type in ADC regions"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ResourceARN='arn:aws-iso-b:kinesis:us-isob-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-isob-east-1.sc2s.sgov.gov'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint with fips targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-iso:kinesis:us-iso-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-iso-east-1.c2s.ic.gov'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint with fips targeting data operation type in ADC regions"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=True, UseDualStack=False, OperationType='data', ResourceARN='arn:aws-iso-b:kinesis:us-isob-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-isob-east-1.sc2s.sgov.gov'

def test_resourcearn_as_consumerarn_test__invalid():
    """ResourceARN as ConsumerARN test: Invalid ARN: partition missing from ARN."""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn::kinesis:us-west-2:123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Failed to parse ARN.')):
        resolve(params)

def test_resourcearn_as_consumerarn_test__invalid():
    """ResourceARN as ConsumerARN test: Invalid ARN: partitions mismatch."""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:us-west-2:123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape("Partition: aws from ARN doesn't match with partition name: aws-us-gov.")):
        resolve(params)

def test_resourcearn_as_consumerarn_test__invalid():
    """ResourceARN as ConsumerARN test: Invalid ARN: Not Kinesis"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:s3:us-west-2:123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The ARN was not for the Kinesis service, found: s3.')):
        resolve(params)

def test_resourcearn_as_consumerarn_test__invalid():
    """ResourceARN as ConsumerARN test: Invalid ARN: Region is missing in ARN"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis::123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid region.')):
        resolve(params)

def test_resourcearn_as_consumerarn_test__invalid():
    """ResourceARN as ConsumerARN test: Invalid ARN: Region is empty string in ARN"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:  :123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid region.')):
        resolve(params)

def test_resourcearn_as_consumerarn_test__invalid():
    """ResourceARN as ConsumerARN test: Invalid ARN: Invalid account id"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:us-east-1::stream/testStream/consumer/test-consumer:1525898737', OperationType='control')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid account id.')):
        resolve(params)

def test_resourcearn_as_consumerarn_test__invalid():
    """ResourceARN as ConsumerARN test: Invalid ARN: Invalid account id"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:us-east-1:   :stream/testStream/consumer/test-consumer:1525898737', OperationType='control')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid account id.')):
        resolve(params)

def test_resourcearn_as_consumerarn_test__invalid():
    """ResourceARN as ConsumerARN test: Invalid ARN: Kinesis ARNs only support stream arn/consumer arn types"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:us-east-1:123:accesspoint/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Unsupported resource type `accesspoint`. Expected: stream, channel, or queue.')):
        resolve(params)

def test_resourcearn_as_consumerarn_test__operati():
    """ResourceARN as ConsumerARN test: OperationType not set"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:us-east-1:123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape('Operation Type is not set. Please contact service team for resolution.')):
        resolve(params)

def test_resourcearn_as_consumerarn_test__custom_():
    """ResourceARN as ConsumerARN test: Custom Endpoint is specified"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-east-1.amazonaws.com'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-east-1.amazonaws.com'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint with fips targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='data', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.us-east-1.amazonaws.com'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint with fips targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis-fips.us-east-1.amazonaws.com'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint with Dual Stack and FIPS enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis-fips.us-east-1.api.aws'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint with Dual Stack enabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=True, OperationType='data', ResourceARN='arn:aws:kinesis:us-west-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-west-1.api.aws'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint with FIPS and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-west-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-west-1.amazonaws.com'

def test_resourcearn_as_consumerarn_test__regionm():
    """ResourceARN as ConsumerARN test: RegionMismatch: client region should be used for endpoint region"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ResourceARN='arn:aws:kinesis:us-west-1:123:stream/testStream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-east-1.amazonaws.com'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint with FIPS enabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=True, UseDualStack=False, OperationType='data', ResourceARN='arn:aws-cn:kinesis:cn-northwest-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.cn-northwest-1.amazonaws.com.cn'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint with FIPS and DualStack enabled for cn regions."""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=True, UseDualStack=True, OperationType='data', ResourceARN='arn:aws-cn:kinesis:cn-northwest-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.cn-northwest-1.api.amazonwebservices.com.cn'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-iso:kinesis:us-iso-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-east-1.c2s.ic.gov'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-west-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-iso:kinesis:us-iso-west-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-west-1.c2s.ic.gov'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint targeting data operation type in ADC regions"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ResourceARN='arn:aws-iso-b:kinesis:us-isob-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-isob-east-1.sc2s.sgov.gov'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint with fips targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-iso:kinesis:us-iso-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-iso-east-1.c2s.ic.gov'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint with fips targeting data operation type in ADC regions"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=True, UseDualStack=False, OperationType='data', ResourceARN='arn:aws-iso-b:kinesis:us-isob-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-isob-east-1.sc2s.sgov.gov'

def test_resourcearn_as_channelarn_test__invalid_():
    """ResourceARN as ChannelARN test: Invalid ARN: unsupported resource type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:298091445058:accesspoint/apu0zt8ge6utbndxe')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Unsupported resource type `accesspoint`. Expected: stream, channel, or queue.')):
        resolve(params)

def test_resourcearn_as_channelarn_test__invalid_():
    """ResourceARN as ChannelARN test: Invalid ARN: Not Kinesis"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:s3:us-east-1:298091445058:channel/apu0zt8ge6utbndxe')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The ARN was not for the Kinesis service, found: s3.')):
        resolve(params)

def test_resourcearn_as_channelarn_test__invalid_():
    """ResourceARN as ChannelARN test: Invalid ARN: partitions mismatch"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-west-2:298091445058:channel/apu0zt8ge6utbndxe')
    with pytest.raises(EndpointError, match=re.escape("Partition: aws from ARN doesn't match with partition name: aws-us-gov.")):
        resolve(params)

def test_resourcearn_as_channelarn_test__operatio():
    """ResourceARN as ChannelARN test: OperationType not set"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:us-east-1:298091445058:channel/apu0zt8ge6utbndxe')
    with pytest.raises(EndpointError, match=re.escape('Operation Type is not set. Please contact service team for resolution.')):
        resolve(params)

def test_resourcearn_as_channelarn_test__missing_():
    """ResourceARN as ChannelARN test: Missing channel id"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:298091445058:channel')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Missing channel id.')):
        resolve(params)

def test_resourcearn_as_channelarn_test__invalid_():
    """ResourceARN as ChannelARN test: Invalid channel id (subdomains not allowed)"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:298091445058:channel/apu0zt8.ge6utbndxe')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid channel id.')):
        resolve(params)

def test_resourcearn_as_channelarn_test__custom_e():
    """ResourceARN as ChannelARN test: Custom Endpoint is specified"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:298091445058:channel/apu0zt8ge6utbndxe', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_resourcearn_as_channelarn_test__endpoint():
    """ResourceARN as ChannelARN test: endpoint targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:298091445058:channel/apu0zt8ge6utbndxe')
    result = resolve(params)
    assert result.url == 'https://apu0zt8ge6utbndxe.control-kinesis.us-east-1.amazonaws.com'

def test_resourcearn_as_channelarn_test__endpoint():
    """ResourceARN as ChannelARN test: endpoint with fips targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:298091445058:channel/apu0zt8ge6utbndxe')
    result = resolve(params)
    assert result.url == 'https://apu0zt8ge6utbndxe.control-kinesis-fips.us-east-1.amazonaws.com'

def test_resourcearn_as_channelarn_test__endpoint():
    """ResourceARN as ChannelARN test: endpoint with Dual Stack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:298091445058:channel/apu0zt8ge6utbndxe')
    result = resolve(params)
    assert result.url == 'https://apu0zt8ge6utbndxe.control-kinesis.us-east-1.api.aws'

def test_resourcearn_as_channelarn_test__endpoint():
    """ResourceARN as ChannelARN test: endpoint with Dual Stack and FIPS enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:298091445058:channel/apu0zt8ge6utbndxe')
    result = resolve(params)
    assert result.url == 'https://apu0zt8ge6utbndxe.control-kinesis-fips.us-east-1.api.aws'

def test_resourcearn_as_channelarn_test__regionmi():
    """ResourceARN as ChannelARN test: RegionMismatch: client region should be used for endpoint region"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-west-1:298091445058:channel/apu0zt8ge6utbndxe')
    result = resolve(params)
    assert result.url == 'https://apu0zt8ge6utbndxe.control-kinesis.us-east-1.amazonaws.com'

def test_resourcearn_as_channelarn_test__account_():
    """ResourceARN as ChannelARN test: Account endpoint with FIPS enabled for cn regions"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=True, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-cn:kinesis:cn-northwest-1:298091445058:channel/apu0zt8ge6utbndxe')
    result = resolve(params)
    assert result.url == 'https://apu0zt8ge6utbndxe.control-kinesis-fips.cn-northwest-1.amazonaws.com.cn'

def test_resourcearn_as_channelarn_test__account_():
    """ResourceARN as ChannelARN test: Account endpoint with FIPS and DualStack enabled for cn regions"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=True, UseDualStack=True, OperationType='control', ResourceARN='arn:aws-cn:kinesis:cn-northwest-1:298091445058:channel/apu0zt8ge6utbndxe')
    result = resolve(params)
    assert result.url == 'https://apu0zt8ge6utbndxe.control-kinesis-fips.cn-northwest-1.api.amazonwebservices.com.cn'

def test_resourcearn_as_channelarn_test__account_():
    """ResourceARN as ChannelARN test: Account endpoint targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-iso:kinesis:us-iso-east-1:298091445058:channel/apu0zt8ge6utbndxe')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-east-1.c2s.ic.gov'

def test_resourcearn_as_channelarn_test__account_():
    """ResourceARN as ChannelARN test: Account endpoint with fips targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-iso:kinesis:us-iso-east-1:298091445058:channel/apu0zt8ge6utbndxe')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-iso-east-1.c2s.ic.gov'

def test_streamid_test__operationtype_not_set_wit():
    """StreamId test: OperationType not set with StreamId"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, StreamId='af4lwng4k01746835071-xyz')
    with pytest.raises(EndpointError, match=re.escape('Operation Type is not set. Please contact service team for resolution.')):
        resolve(params)

def test_streamid_test__stream_endpoint_targeting():
    """StreamId test: Stream endpoint targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071-xyz', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis.us-east-1.amazonaws.com'

def test_streamid_test__stream_endpoint_targeting():
    """StreamId test: Stream endpoint targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', StreamId='af4lwng4k01746835071-xyz', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis.us-east-1.amazonaws.com'

def test_streamid_test__stream_endpoint_with_fips():
    """StreamId test: Stream endpoint with fips targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='data', StreamId='af4lwng4k01746835071-xyz', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis-fips.us-east-1.amazonaws.com'

def test_streamid_test__stream_endpoint_with_fips():
    """StreamId test: Stream endpoint with fips targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071-xyz', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis-fips.us-east-1.amazonaws.com'

def test_streamid_test__stream_endpoint_with_dual():
    """StreamId test: Stream endpoint with Dual Stack and FIPS enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', StreamId='af4lwng4k01746835071-xyz', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis-fips.us-east-1.api.aws'

def test_streamid_test__stream_endpoint_with_dual():
    """StreamId test: Stream endpoint with Dual Stack enabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=True, OperationType='data', StreamId='af4lwng4k01746835071-xyz', StreamARN='arn:aws:kinesis:us-west-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis.us-west-1.api.aws'

def test_streamid_test__stream_endpoint_with_fips():
    """StreamId test: Stream endpoint with FIPS and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071-xyz', StreamARN='arn:aws:kinesis:us-west-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis.us-west-1.amazonaws.com'

def test_streamid_test__stream_endpoint_fips_and_():
    """StreamId test: Stream endpoint FIPS and DualStack disabled with endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071-xyz', Endpoint='kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis-pod1.us-east-1.amazonaws.com'

def test_streamid_test__stream_endpoint_targeting():
    """StreamId test: Stream endpoint targeting data operation type with endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', StreamId='af4lwng4k01746835071-xyz', Endpoint='kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis-pod1.us-east-1.amazonaws.com'

def test_streamid_test__stream_endpoint_with_fips():
    """StreamId test: Stream endpoint with fips targeting data operation type with endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='data', StreamId='af4lwng4k01746835071-xyz', Endpoint='kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis-pod1-fips.us-east-1.amazonaws.com'

def test_streamid_test__stream_endpoint_with_fips():
    """StreamId test: Stream endpoint with fips targeting control operation type with endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071-xyz', Endpoint='kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis-pod1-fips.us-east-1.amazonaws.com'

def test_streamid_test__stream_endpoint_with_dual():
    """StreamId test: Stream endpoint with Dual Stack and FIPS enabled with endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', StreamId='af4lwng4k01746835071-xyz', Endpoint='kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis-pod1-fips.us-east-1.api.aws'

def test_streamid_test__stream_endpoint_with_dual():
    """StreamId test: Stream endpoint with Dual Stack enabled with endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, OperationType='data', StreamId='af4lwng4k01746835071-xyz', Endpoint='kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis-pod1.us-east-1.api.aws'

def test_streamid_test__stream_endpoint_targeting():
    """StreamId test: Stream endpoint targeting data operation type with https endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', StreamId='af4lwng4k01746835071-xyz', Endpoint='https://kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis-pod1.us-east-1.amazonaws.com'

def test_streamid_test__https_endpoint_with_fips_():
    """StreamId test: HTTPS endpoint with FIPS enabled targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071-xyz', Endpoint='https://kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis-pod1-fips.us-east-1.amazonaws.com'

def test_streamid_test__https_endpoint_with_fips_():
    """StreamId test: HTTPS endpoint with FIPS enabled targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='data', StreamId='af4lwng4k01746835071-xyz', Endpoint='https://kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis-pod1-fips.us-east-1.amazonaws.com'

def test_streamid_test__https_endpoint_with_duals():
    """StreamId test: HTTPS endpoint with DualStack enabled targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, OperationType='control', StreamId='af4lwng4k01746835071-xyz', Endpoint='https://kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis-pod1.us-east-1.api.aws'

def test_streamid_test__https_endpoint_with_duals():
    """StreamId test: HTTPS endpoint with DualStack enabled targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, OperationType='data', StreamId='af4lwng4k01746835071-xyz', Endpoint='https://kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis-pod1.us-east-1.api.aws'

def test_streamid_test__https_endpoint_with_fips_():
    """StreamId test: HTTPS endpoint with FIPS and DualStack enabled targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', StreamId='af4lwng4k01746835071-xyz', Endpoint='https://kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis-pod1-fips.us-east-1.api.aws'

def test_streamid_test__https_endpoint_with_fips_():
    """StreamId test: HTTPS endpoint with FIPS and DualStack enabled targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='data', StreamId='af4lwng4k01746835071-xyz', Endpoint='https://kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis-pod1-fips.us-east-1.api.aws'

def test_streamid_test__https_endpoint_with_fips_():
    """StreamId test: HTTPS endpoint with FIPS enabled in different region"""
    params = EndpointParams(Region='us-west-2', UseFIPS=True, UseDualStack=False, OperationType='data', StreamId='af4lwng4k01746835071-xyz', Endpoint='https://kinesis-pod2.us-west-2.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis-pod2-fips.us-west-2.amazonaws.com'

def test_streamid_test__https_endpoint_with_duals():
    """StreamId test: HTTPS endpoint with DualStack enabled in different region"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=True, OperationType='control', StreamId='af4lwng4k01746835071-xyz', Endpoint='https://kinesis-pod2.us-west-2.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis-pod2.us-west-2.api.aws'

def test_streamid_test__stream_endpoint_with_cons():
    """StreamId test: Stream endpoint with ConsumerARN targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071-xyz', ConsumerARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis.us-east-1.amazonaws.com'

def test_streamid_test__stream_endpoint_with_cons():
    """StreamId test: Stream endpoint with ConsumerARN targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', StreamId='af4lwng4k01746835071-xyz', ConsumerARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis.us-east-1.amazonaws.com'

def test_streamid_test__stream_endpoint_with_reso():
    """StreamId test: Stream endpoint with ResourceARN targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071-xyz', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis.us-east-1.amazonaws.com'

def test_streamid_test__stream_endpoint_with_reso():
    """StreamId test: Stream endpoint with ResourceARN targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', StreamId='af4lwng4k01746835071-xyz', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis.us-east-1.amazonaws.com'

def test_streamid_test__invalid_streamid_with_arn():
    """StreamId test: Invalid StreamId with ARN"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', StreamId='af4lwng4k01746835071=xyz', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-east-1.amazonaws.com'

def test_streamid_test__invalid_streamid_with_cus():
    """StreamId test: Invalid streamId with custom endpoint"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071=xyz', Endpoint='https://kinesis-pod2.us-west-2.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://kinesis-pod2.us-west-2.amazonaws.com'

def test_streamid_test__invalid_streamid():
    """StreamId test: Invalid streamId"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071=xyz')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-west-2.amazonaws.com'

def test_streamid_test__invalid_streamid_with_cus():
    """StreamId test: Invalid streamId with custom endpoint and ARN"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071=xyz', Endpoint='https://kinesis-pod2.us-west-2.amazonaws.com', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis-pod2.us-west-2.amazonaws.com'

def test_streamid_test__invalid_streamid_with_lon():
    """StreamId test: Invalid streamId with longer prefix"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k0174683507123-xyz', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-west-2.amazonaws.com'

def test_streamid_test__invalid_streamid_with_sho():
    """StreamId test: Invalid streamId with shorter prefix"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835-xyz', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-west-2.amazonaws.com'

def test_streamid_test__invalid_streamid_with_lon():
    """StreamId test: Invalid streamId with longer suffix"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071-wxyz', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-west-2.amazonaws.com'

def test_streamid_test__invalid_streamid_with_sho():
    """StreamId test: Invalid streamId with shorter suffix"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071-yz', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-west-2.amazonaws.com'

def test_channelarn__endpoint_targeting_control_o():
    """ChannelARN: endpoint targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ChannelARN='arn:aws:kinesis:us-east-1:298091445058:channel/apu0zt8ge6utbndxe')
    result = resolve(params)
    assert result.url == 'https://apu0zt8ge6utbndxe.control-kinesis.us-east-1.amazonaws.com'

def test_channelarn__endpoint_with_fips_targeting():
    """ChannelARN: endpoint with FIPS targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', ChannelARN='arn:aws:kinesis:us-east-1:298091445058:channel/apu0zt8ge6utbndxe')
    result = resolve(params)
    assert result.url == 'https://apu0zt8ge6utbndxe.control-kinesis-fips.us-east-1.amazonaws.com'

def test_channelarn__endpoint_with_dualstack_targ():
    """ChannelARN: endpoint with DualStack targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, OperationType='control', ChannelARN='arn:aws:kinesis:us-east-1:298091445058:channel/apu0zt8ge6utbndxe')
    result = resolve(params)
    assert result.url == 'https://apu0zt8ge6utbndxe.control-kinesis.us-east-1.api.aws'

def test_channelarn__endpoint_with_fips_and_duals():
    """ChannelARN: endpoint with FIPS and DualStack targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', ChannelARN='arn:aws:kinesis:us-east-1:298091445058:channel/apu0zt8ge6utbndxe')
    result = resolve(params)
    assert result.url == 'https://apu0zt8ge6utbndxe.control-kinesis-fips.us-east-1.api.aws'

def test_invalid_channelarn__channelarn_only_supp():
    """Invalid ChannelARN: ChannelARN only supports channel arn types"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ChannelARN='arn:aws:kinesis:us-east-1:298091445058:stream/test-stream')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: ChannelARN only supports `channel` arn types, found: `stream`.')):
        resolve(params)

def test_invalid_channelarn__arn_was_not_for_the_():
    """Invalid ChannelARN: ARN was not for the Kinesis service"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ChannelARN='arn:aws:s3:us-east-1:298091445058:channel/apu0zt8ge6utbndxe')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The ARN was not for the Kinesis service, found: s3.')):
        resolve(params)

def test_invalid_channelarn__operationtype_not_se():
    """Invalid ChannelARN: OperationType not set"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ChannelARN='arn:aws:kinesis:us-east-1:298091445058:channel/apu0zt8ge6utbndxe')
    with pytest.raises(EndpointError, match=re.escape('Operation Type is not set. Please contact service team for resolution.')):
        resolve(params)

def test_invalid_channelarn__partitions_mismatch():
    """Invalid ChannelARN: partitions mismatch"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=False, OperationType='data', ChannelARN='arn:aws:kinesis:us-west-2:298091445058:channel/apu0zt8ge6utbndxe')
    with pytest.raises(EndpointError, match=re.escape("Partition: aws from ARN doesn't match with partition name: aws-us-gov.")):
        resolve(params)

def test_invalid_channelarn__missing_channel_id():
    """Invalid ChannelARN: missing channel id"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ChannelARN='arn:aws:kinesis:us-east-1:298091445058:channel')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Missing channel id.')):
        resolve(params)

def test_invalid_channelarn__channel_id_contains_():
    """Invalid ChannelARN: channel id contains a period (subdomains not allowed)"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ChannelARN='arn:aws:kinesis:us-east-1:298091445058:channel/apu0zt8.ge6utbndxe')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid channel id.')):
        resolve(params)

def test_invalid_channelarn__channel_id_exceeds_6():
    """Invalid ChannelARN: channel id exceeds 63 character host label limit"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ChannelARN='arn:aws:kinesis:us-east-1:298091445058:channel/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid channel id.')):
        resolve(params)

def test_invalid_channelarn__channel_id_starts_wi():
    """Invalid ChannelARN: channel id starts with a hyphen"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ChannelARN='arn:aws:kinesis:us-east-1:298091445058:channel/-pu0zt8ge6utbndxe')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid channel id.')):
        resolve(params)

def test_invalid_channelarn__channel_id_contains_():
    """Invalid ChannelARN: channel id contains an invalid character"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ChannelARN='arn:aws:kinesis:us-east-1:298091445058:channel/apu0zt8_ge6utbndxe')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid channel id.')):
        resolve(params)

def test_invalid_channelarn__data_operation_type_():
    """Invalid ChannelARN: data operation type is not supported for channel"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ChannelARN='arn:aws:kinesis:us-east-1:298091445058:channel/apu0zt8ge6utbndxe')
    with pytest.raises(EndpointError, match=re.escape('ChannelARN does not support the `data` operation type.')):
        resolve(params)

def test_accountid_test__account_id_present():
    """AccountId test: Account Id present"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='data', AccountId='012345678901', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://012345678901.data-kinesis.us-west-2.amazonaws.com'

def test_accountid_test__account_id_present_with_():
    """AccountId test: Account Id present with fips"""
    params = EndpointParams(Region='us-west-2', UseFIPS=True, UseDualStack=False, OperationType='control', AccountId='123', AccountIdEndpointMode='required')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis-fips.us-west-2.amazonaws.com'

def test_accountid_test__account_id_present_with_():
    """AccountId test: Account Id present with dual stack"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=True, OperationType='control', AccountId='123', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-west-2.api.aws'

def test_accountid_test__account_id_present_with_():
    """AccountId test: Account Id present with fips and dual stack"""
    params = EndpointParams(Region='us-west-2', UseFIPS=True, UseDualStack=True, OperationType='control', AccountId='123', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis-fips.us-west-2.api.aws'

def test_account_id_present_with_streamid():
    """Account Id present with streamId"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071-xyz', AccountId='123', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis.us-west-2.amazonaws.com'

def test_account_id_present_with_stream_arn():
    """Account Id present with stream ARN"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream', AccountId='123', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-west-2.amazonaws.com'

def test_account_id_present_with_consumer_arn():
    """Account Id present with consumer ARN"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', ConsumerARN='arn:aws:kinesis:us-west-2:123:stream/testStream/consumer/test-consumer:1525898737', AccountId='123', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-west-2.amazonaws.com'

def test_account_id_present_with_resource_arn():
    """Account Id present with resource ARN"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-west-2:123:stream/testStream/consumer/test-consumer:1525898737', AccountId='123', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-west-2.amazonaws.com'

def test_account_id_present_and_stream_arn_with_d():
    """Account Id present and stream ARN with different accountId"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-west-2:456:stream/testStream', AccountId='123', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://456.control-kinesis.us-west-2.amazonaws.com'

def test_account_id_present_and_consumer_arn_with():
    """Account Id present and consumer ARN with different accountId"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-west-2:456:stream/testStream/consumer/test-consumer:1525898737', AccountId='123', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://456.control-kinesis.us-west-2.amazonaws.com'

def test_account_id__streamid_and_resource_arn_wi():
    """Account Id, streamId and resource ARN with different accountId"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071-xyz', ResourceARN='arn:aws:kinesis:us-west-2:456:stream/testStream/consumer/test-consumer:1525898737', AccountId='123', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis.us-west-2.amazonaws.com'

def test_resourcearn_with_queue_type__basic_contr():
    """ResourceARN with queue type: basic control endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:123456789012:queue/myQueueId')
    result = resolve(params)
    assert result.url == 'https://myQueueId.control-kinesis-queues.us-east-1.amazonaws.com'

def test_resourcearn_with_queue_type__fips():
    """ResourceARN with queue type: FIPS"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:123456789012:queue/myQueueId')
    result = resolve(params)
    assert result.url == 'https://myQueueId.control-kinesis-queues-fips.us-east-1.amazonaws.com'

def test_resourcearn_with_queue_type__dualstack():
    """ResourceARN with queue type: DualStack"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=True, OperationType='control', ResourceARN='arn:aws:kinesis:us-west-2:123456789012:queue/myQueueId')
    result = resolve(params)
    assert result.url == 'https://myQueueId.control-kinesis-queues.us-west-2.api.aws'

def test_resourcearn_with_channel_type__basic_con():
    """ResourceARN with channel type: basic control endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:298091445058:channel/apu0zt8ge6utbndxe')
    result = resolve(params)
    assert result.url == 'https://apu0zt8ge6utbndxe.control-kinesis.us-east-1.amazonaws.com'

def test_account_id_with_account_id_endpoint_mode():
    """Account Id with account id endpoint mode disabled"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', AccountId='123', AccountIdEndpointMode='disabled')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-west-2.amazonaws.com'

def test_account_id_and_streamarn_with_account_id():
    """Account Id and StreamArn with account id endpoint mode disabled"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', StreamARN='arn:aws:kinesis:us-west-2:456:stream/testStream', AccountId='123', AccountIdEndpointMode='disabled')
    result = resolve(params)
    assert result.url == 'https://456.control-kinesis.us-west-2.amazonaws.com'

def test_account_id_missing_with_account_id_endpo():
    """Account Id missing with account id endpoint mode required"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', AccountIdEndpointMode='required')
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test_account_id_missing_with_account_id_endpo():
    """Account Id missing with account id endpoint mode required, fips and dual stack enabled"""
    params = EndpointParams(Region='us-west-2', UseFIPS=True, UseDualStack=True, OperationType='control', AccountIdEndpointMode='required')
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test_account_id_missing_with_account_id_endpo():
    """Account Id missing with account id endpoint mode required in ADC region"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', AccountIdEndpointMode='required')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this partition')):
        resolve(params)

def test_account_id_present_with_account_id_endpo():
    """Account Id present with account id endpoint mode required in ADC region"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='required')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this partition')):
        resolve(params)

def test_account_id_present_with_account_id_endpo():
    """Account Id present with account id endpoint mode preferred in ADC region"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-east-1.c2s.ic.gov'

def test_account_id_missing_with_account_id_endpo():
    """Account Id missing with account id endpoint mode required and endpoint override"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', Endpoint='https://kinesis-pod1.us-west-2.amazonaws.com', AccountIdEndpointMode='required')
    result = resolve(params)
    assert result.url == 'https://kinesis-pod1.us-west-2.amazonaws.com'

def test_account_id_missing_with_streamarn_and_ac():
    """Account Id missing with StreamArn and account id endpoint mode required"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', StreamARN='arn:aws:kinesis:us-west-2:456:stream/testStream', AccountIdEndpointMode='required')
    result = resolve(params)
    assert result.url == 'https://456.control-kinesis.us-west-2.amazonaws.com'

def test_account_id_missing_with_streamid_and_acc():
    """Account Id missing with StreamId and account id endpoint mode required"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071-xyz', AccountIdEndpointMode='required')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis.us-west-2.amazonaws.com'

def test_account_id_missing_with_account_id_endpo():
    """Account Id missing with account id endpoint mode preferred"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-west-2.amazonaws.com'

def test_account_id_missing_with_account_id_endpo():
    """Account Id missing with account id endpoint mode disabled"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', AccountIdEndpointMode='disabled')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-west-2.amazonaws.com'

def test_createstream__control_operation_type_wit():
    """CreateStream: control operation type with AccountId"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.control-kinesis.us-east-1.amazonaws.com'

def test_createstream__control_operation_type_wit():
    """CreateStream: control operation type with FIPS and AccountId"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.control-kinesis-fips.us-east-1.amazonaws.com'

def test_liststreams__control_operation_type_with():
    """ListStreams: control operation type with AccountId"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.control-kinesis.us-west-2.amazonaws.com'

def test_liststreams__control_operation_type_with():
    """ListStreams: control operation type with FIPS and DualStack"""
    params = EndpointParams(Region='us-west-2', UseFIPS=True, UseDualStack=True, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.control-kinesis-fips.us-west-2.api.aws'

def test_describelimits__control_operation_type_w():
    """DescribeLimits: control operation type with AccountId"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.control-kinesis.us-east-1.amazonaws.com'

def test_describelimits__control_operation_type_w():
    """DescribeLimits: control operation type with FIPS"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.control-kinesis-fips.us-east-1.amazonaws.com'

def test_describeaccountsettings__control_operati():
    """DescribeAccountSettings: control operation type with AccountId"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.control-kinesis.us-west-2.amazonaws.com'

def test_describeaccountsettings__control_operati():
    """DescribeAccountSettings: control operation type with FIPS and DualStack"""
    params = EndpointParams(Region='us-west-2', UseFIPS=True, UseDualStack=True, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.control-kinesis-fips.us-west-2.api.aws'

def test_updateaccountsettings__control_operation():
    """UpdateAccountSettings: control operation type with AccountId"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.control-kinesis.us-east-1.amazonaws.com'

def test_updateaccountsettings__control_operation():
    """UpdateAccountSettings: control operation type with FIPS"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.control-kinesis-fips.us-east-1.amazonaws.com'

def test_createstream__account_id_endpoint_mode_d():
    """CreateStream: account id endpoint mode disabled falls back to regional endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='disabled')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-east-1.amazonaws.com'

def test_liststreams__account_id_endpoint_mode_di():
    """ListStreams: account id endpoint mode disabled falls back to regional endpoint"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='disabled')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-west-2.amazonaws.com'

def test_describelimits__account_id_endpoint_mode():
    """DescribeLimits: account id endpoint mode disabled falls back to regional endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='disabled')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-east-1.amazonaws.com'

def test_describeaccountsettings__account_id_endp():
    """DescribeAccountSettings: account id endpoint mode disabled falls back to regional endpoint"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='disabled')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-west-2.amazonaws.com'

def test_updateaccountsettings__account_id_endpoi():
    """UpdateAccountSettings: account id endpoint mode disabled falls back to regional endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='disabled')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-east-1.amazonaws.com'

def test_createstream__account_id_endpoint_mode_d():
    """CreateStream: account id endpoint mode disabled with FIPS falls back to regional FIPS endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='disabled')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-east-1.amazonaws.com'

def test_createstream__account_id_endpoint_mode_d():
    """CreateStream: account id endpoint mode disabled with DualStack falls back to regional DualStack endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='disabled')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-east-1.api.aws'

def test_createstream__account_id_endpoint_mode_d():
    """CreateStream: account id endpoint mode disabled with FIPS and DualStack falls back to regional FIPS DualStack endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='disabled')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-east-1.api.aws'

def test_createchannel__control_operation_type_wi():
    """CreateChannel: control operation type with AccountId"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.control-kinesis.us-east-1.amazonaws.com'

def test_createchannel__control_operation_type_wi():
    """CreateChannel: control operation type with FIPS and AccountId"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.control-kinesis-fips.us-east-1.amazonaws.com'

def test_createchannel__control_operation_type_wi():
    """CreateChannel: control operation type with DualStack and AccountId"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.control-kinesis.us-east-1.api.aws'

def test_createchannel__control_operation_type_wi():
    """CreateChannel: control operation type with FIPS and DualStack and AccountId"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.control-kinesis-fips.us-east-1.api.aws'

def test_createchannel__account_id_endpoint_mode_():
    """CreateChannel: account id endpoint mode disabled falls back to regional endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='disabled')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-east-1.amazonaws.com'

def test_createchannel__account_id_endpoint_mode_():
    """CreateChannel: account id endpoint mode disabled with FIPS falls back to regional FIPS endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='disabled')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-east-1.amazonaws.com'

def test_createchannel__account_id_endpoint_mode_():
    """CreateChannel: account id endpoint mode disabled with DualStack falls back to regional DualStack endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='disabled')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-east-1.api.aws'

def test_createchannel__account_id_endpoint_mode_():
    """CreateChannel: account id endpoint mode disabled with FIPS and DualStack falls back to regional FIPS DualStack endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='disabled')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-east-1.api.aws'

def test_listchannels__control_operation_type_wit():
    """ListChannels: control operation type with AccountId"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.control-kinesis.us-west-2.amazonaws.com'

def test_listchannels__control_operation_type_wit():
    """ListChannels: control operation type with FIPS and DualStack"""
    params = EndpointParams(Region='us-west-2', UseFIPS=True, UseDualStack=True, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.control-kinesis-fips.us-west-2.api.aws'

def test_listchannels__account_id_endpoint_mode_d():
    """ListChannels: account id endpoint mode disabled falls back to regional endpoint"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='disabled')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-west-2.amazonaws.com'

def test_queuearn__basic_endpoint_resolution_with():
    """QueueARN: basic endpoint resolution with control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceType='queue', QueueARN='arn:aws:kinesis:us-east-1:123456789012:queue/myQueueId')
    result = resolve(params)
    assert result.url == 'https://myQueueId.control-kinesis-queues.us-east-1.amazonaws.com'

def test_queuearn__endpoint_with_fips():
    """QueueARN: endpoint with FIPS"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', ResourceType='queue', QueueARN='arn:aws:kinesis:us-east-1:123456789012:queue/myQueueId')
    result = resolve(params)
    assert result.url == 'https://myQueueId.control-kinesis-queues-fips.us-east-1.amazonaws.com'

def test_queuearn__endpoint_with_dualstack():
    """QueueARN: endpoint with DualStack"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, OperationType='control', ResourceType='queue', QueueARN='arn:aws:kinesis:us-east-1:123456789012:queue/myQueueId')
    result = resolve(params)
    assert result.url == 'https://myQueueId.control-kinesis-queues.us-east-1.api.aws'

def test_queuearn__endpoint_with_fips_and_dualsta():
    """QueueARN: endpoint with FIPS and DualStack"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', ResourceType='queue', QueueARN='arn:aws:kinesis:us-east-1:123456789012:queue/myQueueId')
    result = resolve(params)
    assert result.url == 'https://myQueueId.control-kinesis-queues-fips.us-east-1.api.aws'

def test_queuearn__data_operation_type():
    """QueueARN: data operation type"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='data', ResourceType='queue', QueueARN='arn:aws:kinesis:us-west-2:123456789012:queue/abc123def456')
    result = resolve(params)
    assert result.url == 'https://abc123def456.data-kinesis-queues.us-west-2.amazonaws.com'

def test_queuearn__data_operation_type_with_fips():
    """QueueARN: data operation type with FIPS"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='data', ResourceType='queue', QueueARN='arn:aws:kinesis:us-east-1:123456789012:queue/abc123def456')
    result = resolve(params)
    assert result.url == 'https://abc123def456.data-kinesis-queues-fips.us-east-1.amazonaws.com'

def test_queuearn__data_operation_type_with_duals():
    """QueueARN: data operation type with DualStack"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=True, OperationType='data', ResourceType='queue', QueueARN='arn:aws:kinesis:us-west-2:123456789012:queue/abc123def456')
    result = resolve(params)
    assert result.url == 'https://abc123def456.data-kinesis-queues.us-west-2.api.aws'

def test_queuearn__vpce_endpoint_override_is_resp():
    """QueueARN: VPCE endpoint override is respected as-is"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceType='queue', QueueARN='arn:aws:kinesis:us-east-1:123456789012:queue/myQueueId', Endpoint='https://my-vpce-xyz.vpce.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://my-vpce-xyz.vpce.amazonaws.com'

def test_invalid_queuearn__wrong_arn_type():
    """Invalid QueueARN: wrong arn type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceType='queue', QueueARN='arn:aws:kinesis:us-east-1:123456789012:stream/test-stream')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: QueueARN only supports `queue` ARN types, found: `stream`.')):
        resolve(params)

def test_invalid_queuearn__missing_queue_id():
    """Invalid QueueARN: missing queue id"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceType='queue', QueueARN='arn:aws:kinesis:us-east-1:123456789012:queue')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Missing queue id.')):
        resolve(params)

def test_invalid_queuearn__non_kinesis_service():
    """Invalid QueueARN: non-kinesis service"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceType='queue', QueueARN='arn:aws:sqs:us-east-1:123456789012:queue/myQueueId')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The ARN was not for the Kinesis service, found: sqs.')):
        resolve(params)

def test_queue_accountid__basic_endpoint_with_acc():
    """Queue AccountId: basic endpoint with AccountId"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred', ResourceType='queue')
    result = resolve(params)
    assert result.url == 'https://123456789012.control-kinesis-queues.us-east-1.amazonaws.com'

def test_queue_accountid__endpoint_with_fips():
    """Queue AccountId: endpoint with FIPS"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred', ResourceType='queue')
    result = resolve(params)
    assert result.url == 'https://123456789012.control-kinesis-queues-fips.us-east-1.amazonaws.com'

def test_queue_accountid__endpoint_with_dualstack():
    """Queue AccountId: endpoint with DualStack"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=True, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred', ResourceType='queue')
    result = resolve(params)
    assert result.url == 'https://123456789012.control-kinesis-queues.us-west-2.api.aws'

def test_queue_accountid__endpoint_with_fips_and_():
    """Queue AccountId: endpoint with FIPS and DualStack"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred', ResourceType='queue')
    result = resolve(params)
    assert result.url == 'https://123456789012.control-kinesis-queues-fips.us-east-1.api.aws'

def test_queuearn__regular_endpoint_override_is_r():
    """QueueARN: regular endpoint override is respected as-is"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceType='queue', QueueARN='arn:aws:kinesis:us-east-1:123456789012:queue/myQueueId', Endpoint='https://kinesis-queues.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://kinesis-queues.us-east-1.amazonaws.com'

def test_queue_accountid__disabled_mode_falls_bac():
    """Queue AccountId: disabled mode falls back to regional queue endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='disabled', ResourceType='queue')
    result = resolve(params)
    assert result.url == 'https://kinesis-queues.us-east-1.amazonaws.com'

def test_queue_accountid__disabled_mode_with_fips():
    """Queue AccountId: disabled mode with FIPS falls back to regional queue FIPS endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='disabled', ResourceType='queue')
    result = resolve(params)
    assert result.url == 'https://kinesis-queues-fips.us-east-1.amazonaws.com'

def test_queue_accountid__disabled_mode_with_dual():
    """Queue AccountId: disabled mode with DualStack falls back to regional queue DualStack endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='disabled', ResourceType='queue')
    result = resolve(params)
    assert result.url == 'https://kinesis-queues.us-east-1.api.aws'

def test_queue_accountid__disabled_mode_with_fips():
    """Queue AccountId: disabled mode with FIPS and DualStack falls back to regional queue FIPS DualStack endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='disabled', ResourceType='queue')
    result = resolve(params)
    assert result.url == 'https://kinesis-queues-fips.us-east-1.api.aws'

def test_resourcearn_with_queue_type__missing_que():
    """ResourceARN with queue type: missing queue id errors"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:123456789012:queue')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Missing queue id.')):
        resolve(params)

def test_resourcearn_with_channel_type__missing_c():
    """ResourceARN with channel type: missing channel id errors"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:123456789012:channel')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Missing channel id.')):
        resolve(params)

def test_resourcearn_with_unsupported_type__consu():
    """ResourceARN with unsupported type: consumer type is rejected"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:123456789012:consumer/test-consumer')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Unsupported resource type `consumer`. Expected: stream, channel, or queue.')):
        resolve(params)

def test_queuearn_and_streamarn_both_set__streama():
    """QueueARN and StreamARN both set: StreamARN wins by rule ordering today (ResourceType is not yet authoritative on the stream path; revisit if a both-ARN API is introduced)"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream', ResourceType='queue', QueueARN='arn:aws:kinesis:us-east-1:123456789012:queue/myQueueId')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-east-1.amazonaws.com'

def test_queuearn_set_but_resourcetype_absent__er():
    """QueueARN set but ResourceType absent: errors instead of misrouting to the default kinesis endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', QueueARN='arn:aws:kinesis:us-east-1:123456789012:queue/myQueueId')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: ResourceType must be "queue" when QueueARN is set.')):
        resolve(params)

def test_queuearn_set_but_resourcetype_is_not_que():
    """QueueARN set but ResourceType is not queue:  errors instead of misrouting to the default kinesis endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceType='stream', QueueARN='arn:aws:kinesis:us-east-1:123456789012:queue/myQueueId')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: ResourceType must be "queue" when QueueARN is set.')):
        resolve(params)

def test_accountid_without_resourcetype__non_queu():
    """AccountId without ResourceType: non-queue account endpoint is unchanged (no -queues suffix)"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.control-kinesis.us-east-1.amazonaws.com'

def test_queue_accountid__required_mode_with_no_a():
    """Queue AccountId: required mode with no AccountId errors"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', AccountIdEndpointMode='required', ResourceType='queue')
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test_queuearn__operationtype_not_set_errors():
    """QueueARN: OperationType not set errors"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceType='queue', QueueARN='arn:aws:kinesis:us-east-1:123456789012:queue/myQueueId')
    with pytest.raises(EndpointError, match=re.escape('Operation Type is not set. Please contact service team for resolution.')):
        resolve(params)

def test_queuearn__aws_iso_region_falls_back_to_r():
    """QueueARN: aws-iso region falls back to regional queue endpoint"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceType='queue', QueueARN='arn:aws-iso:kinesis:us-iso-east-1:123456789012:queue/myQueueId')
    result = resolve(params)
    assert result.url == 'https://kinesis-queues.us-iso-east-1.c2s.ic.gov'

def test_queuearn__aws_iso_b_region_falls_back_to():
    """QueueARN: aws-iso-b region falls back to regional queue endpoint"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceType='queue', QueueARN='arn:aws-iso-b:kinesis:us-isob-east-1:123456789012:queue/myQueueId')
    result = resolve(params)
    assert result.url == 'https://kinesis-queues.us-isob-east-1.sc2s.sgov.gov'

def test_queue_accountid_in_aws_iso__disabled_mod():
    """Queue AccountId in aws-iso: disabled mode falls back to regional queue endpoint"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='disabled', ResourceType='queue')
    result = resolve(params)
    assert result.url == 'https://kinesis-queues.us-iso-east-1.c2s.ic.gov'

def test_resourcearn_with_queue_type_in_aws_iso__():
    """ResourceARN with queue type in aws-iso: falls back to regional queue endpoint"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-iso:kinesis:us-iso-east-1:123456789012:queue/myQueueId')
    result = resolve(params)
    assert result.url == 'https://kinesis-queues.us-iso-east-1.c2s.ic.gov'

def test_resourcearn_with_queue_type_in_aws_iso_b():
    """ResourceARN with queue type in aws-iso-b: falls back to regional queue endpoint"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-iso-b:kinesis:us-isob-east-1:123456789012:queue/myQueueId')
    result = resolve(params)
    assert result.url == 'https://kinesis-queues.us-isob-east-1.sc2s.sgov.gov'

def test_queue_accountid_in_aws_iso__preferred_mo():
    """Queue AccountId in aws-iso: preferred mode falls back to regional queue endpoint"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred', ResourceType='queue')
    result = resolve(params)
    assert result.url == 'https://kinesis-queues.us-iso-east-1.c2s.ic.gov'

def test_queuearn__aws_iso_region_with_fips_falls():
    """QueueARN: aws-iso region with FIPS falls back to regional queue FIPS endpoint"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', ResourceType='queue', QueueARN='arn:aws-iso:kinesis:us-iso-east-1:123456789012:queue/myQueueId')
    result = resolve(params)
    assert result.url == 'https://kinesis-queues-fips.us-iso-east-1.c2s.ic.gov'

def test_resourcearn_with_queue_type_in_aws_iso_w():
    """ResourceARN with queue type in aws-iso with FIPS: falls back to regional queue FIPS endpoint"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-iso:kinesis:us-iso-east-1:123456789012:queue/myQueueId')
    result = resolve(params)
    assert result.url == 'https://kinesis-queues-fips.us-iso-east-1.c2s.ic.gov'

def test_queuearn__aws_iso_region_with_dualstack_():
    """QueueARN: aws-iso region with DualStack falls back to regional queue DualStack endpoint"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=True, OperationType='control', ResourceType='queue', QueueARN='arn:aws-iso:kinesis:us-iso-east-1:123456789012:queue/myQueueId')
    result = resolve(params)
    assert result.url == 'https://kinesis-queues.us-iso-east-1.api.aws.ic.gov'

def test_queuearn__aws_iso_region_with_fips_and_d():
    """QueueARN: aws-iso region with FIPS and DualStack falls back to regional queue FIPS DualStack endpoint"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', ResourceType='queue', QueueARN='arn:aws-iso:kinesis:us-iso-east-1:123456789012:queue/myQueueId')
    result = resolve(params)
    assert result.url == 'https://kinesis-queues-fips.us-iso-east-1.api.aws.ic.gov'

def test_resourcearn_with_queue_type_in_aws_iso_w():
    """ResourceARN with queue type in aws-iso with DualStack: falls back to regional queue DualStack endpoint"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=True, OperationType='control', ResourceARN='arn:aws-iso:kinesis:us-iso-east-1:123456789012:queue/myQueueId')
    result = resolve(params)
    assert result.url == 'https://kinesis-queues.us-iso-east-1.api.aws.ic.gov'

def test_resourcearn_with_queue_type_in_aws_iso_w():
    """ResourceARN with queue type in aws-iso with FIPS and DualStack: falls back to regional queue FIPS DualStack endpoint"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', ResourceARN='arn:aws-iso:kinesis:us-iso-east-1:123456789012:queue/myQueueId')
    result = resolve(params)
    assert result.url == 'https://kinesis-queues-fips.us-iso-east-1.api.aws.ic.gov'

def test_queue_accountid_in_aws_iso__preferred_mo():
    """Queue AccountId in aws-iso: preferred mode with FIPS falls back to regional queue FIPS endpoint"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='preferred', ResourceType='queue')
    result = resolve(params)
    assert result.url == 'https://kinesis-queues-fips.us-iso-east-1.c2s.ic.gov'

def test_queue_accountid_in_aws_iso__disabled_mod():
    """Queue AccountId in aws-iso: disabled mode with FIPS falls back to regional queue FIPS endpoint"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', AccountId='123456789012', AccountIdEndpointMode='disabled', ResourceType='queue')
    result = resolve(params)
    assert result.url == 'https://kinesis-queues-fips.us-iso-east-1.c2s.ic.gov'

def test_resourcearn_with_channel_type_in_aws_iso():
    """ResourceARN with channel type in aws-iso: falls back to default kinesis endpoint"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-iso:kinesis:us-iso-east-1:123456789012:channel/myChannelId')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-east-1.c2s.ic.gov'

def test_resourcearn_with_channel_type_in_aws_iso():
    """ResourceARN with channel type in aws-iso with FIPS: falls back to default kinesis FIPS endpoint"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-iso:kinesis:us-iso-east-1:123456789012:channel/myChannelId')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-iso-east-1.c2s.ic.gov'

def test_channelarn_in_aws_iso__falls_back_to_def():
    """ChannelARN in aws-iso: falls back to default kinesis endpoint"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ChannelARN='arn:aws-iso:kinesis:us-iso-east-1:123456789012:channel/myChannelId')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-east-1.c2s.ic.gov'

def test_channelarn_in_aws_iso_with_fips__falls_b():
    """ChannelARN in aws-iso with FIPS: falls back to default kinesis FIPS endpoint"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', ChannelARN='arn:aws-iso:kinesis:us-iso-east-1:123456789012:channel/myChannelId')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-iso-east-1.c2s.ic.gov'

def test_resourcearn_queue_in_aws_iso__non_kinesi():
    """ResourceARN queue in aws-iso: non-kinesis service should error"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-iso:sqs:us-iso-east-1:123456789012:queue/myQueueId')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The ARN was not for the Kinesis service, found: sqs.')):
        resolve(params)

def test_resourcearn_queue_in_aws_iso__partition_():
    """ResourceARN queue in aws-iso: partition mismatch should error"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:123456789012:queue/myQueueId')
    with pytest.raises(EndpointError, match=re.escape("Partition: aws from ARN doesn't match with partition name: aws-iso.")):
        resolve(params)

def test_resourcearn_queue_in_aws_iso__missing_qu():
    """ResourceARN queue in aws-iso: missing queue id should error"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-iso:kinesis:us-iso-east-1:123456789012:queue')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Missing queue id.')):
        resolve(params)

def test_resourcearn_queue_in_aws_iso__invalid_ac():
    """ResourceARN queue in aws-iso: invalid account id should error"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-iso:kinesis:us-iso-east-1:invalid..account:queue/myQueueId')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid account id.')):
        resolve(params)

def test_resourcearn_queue_in_aws_iso__operationt():
    """ResourceARN queue in aws-iso: OperationType not set should error"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws-iso:kinesis:us-iso-east-1:123456789012:queue/myQueueId')
    with pytest.raises(EndpointError, match=re.escape('Operation Type is not set. Please contact service team for resolution.')):
        resolve(params)

def test_resourcearn_queue_in_aws_iso__invalid_qu():
    """ResourceARN queue in aws-iso: invalid queue id should error"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-iso:kinesis:us-iso-east-1:123456789012:queue/invalid.queue.id')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid queue id.')):
        resolve(params)

def test_streamarn_in_aws_iso_with_dualstack__fal():
    """StreamARN in aws-iso with DualStack: falls back to default kinesis DualStack endpoint"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=True, OperationType='control', StreamARN='arn:aws-iso:kinesis:us-iso-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-east-1.api.aws.ic.gov'

def test_streamarn_in_aws_iso_with_fips_and_duals():
    """StreamARN in aws-iso with FIPS and DualStack: falls back to default kinesis FIPS DualStack endpoint"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', StreamARN='arn:aws-iso:kinesis:us-iso-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-iso-east-1.api.aws.ic.gov'

def test_streamarn_in_aws_iso__missing_arn_type_f():
    """StreamARN in aws-iso: missing ARN type falls back to default kinesis endpoint"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', StreamARN='arn:aws-iso:kinesis:us-iso-east-1:123456789012:')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-east-1.c2s.ic.gov'

def test_queuearn__partition_mismatch_errors():
    """QueueARN: partition mismatch errors"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceType='queue', QueueARN='arn:aws-cn:kinesis:cn-north-1:123456789012:queue/myQueueId')
    with pytest.raises(EndpointError, match=re.escape("Partition: aws-cn from ARN doesn't match with partition name: aws.")):
        resolve(params)

def test_resourcearn_with_queue_type__fips_and_du():
    """ResourceARN with queue type: FIPS and DualStack"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:123456789012:queue/myQueueId')
    result = resolve(params)
    assert result.url == 'https://myQueueId.control-kinesis-queues-fips.us-east-1.api.aws'

def test_resourcearn_with_queue_type__data_operat():
    """ResourceARN with queue type: data operation type"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='data', ResourceARN='arn:aws:kinesis:us-west-2:123456789012:queue/myQueueId')
    result = resolve(params)
    assert result.url == 'https://myQueueId.data-kinesis-queues.us-west-2.amazonaws.com'