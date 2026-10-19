"""Generated from Smithy shape ``com.amazonaws.devicefarm#UpdateVPCEConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name
    import capo_device_farm.types.service_dns_name
    import capo_device_farm.types.vpce_configuration_description
    import capo_device_farm.types.vpce_configuration_name
    import capo_device_farm.types.vpce_service_name


class UpdateVPCEConfigurationRequest(TypedDict, closed=True):
    arn: "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the VPC endpoint configuration you want to update.</p>"""
    vpce_configuration_name: NotRequired[
        "capo_device_farm.types.vpce_configuration_name.VPCEConfigurationName"
    ]
    """<p>The friendly name you give to your VPC endpoint configuration to manage your configurations more easily.</p>"""
    vpce_service_name: NotRequired[
        "capo_device_farm.types.vpce_service_name.VPCEServiceName"
    ]
    """<p>The name of the VPC endpoint service running in your AWS account that you want Device Farm to test.</p>"""
    service_dns_name: NotRequired[
        "capo_device_farm.types.service_dns_name.ServiceDnsName"
    ]
    """<p>The DNS (domain) name used to connect to your private service in your VPC. The DNS name must not already be in use on the internet.</p>"""
    vpce_configuration_description: NotRequired[
        "capo_device_farm.types.vpce_configuration_description.VPCEConfigurationDescription"
    ]
    """<p>An optional description that provides details about your VPC endpoint configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateVPCEConfigurationRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "vpce_configuration_name" in value:
        out["vpceConfigurationName"] = value["vpce_configuration_name"]
    if "vpce_service_name" in value:
        out["vpceServiceName"] = value["vpce_service_name"]
    if "service_dns_name" in value:
        out["serviceDnsName"] = value["service_dns_name"]
    if "vpce_configuration_description" in value:
        out["vpceConfigurationDescription"] = value["vpce_configuration_description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateVPCEConfigurationRequest:
    out: UpdateVPCEConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("vpceConfigurationName") is not None:
        out["vpce_configuration_name"] = data["vpceConfigurationName"]
    if data.get("vpceServiceName") is not None:
        out["vpce_service_name"] = data["vpceServiceName"]
    if data.get("serviceDnsName") is not None:
        out["service_dns_name"] = data["serviceDnsName"]
    if data.get("vpceConfigurationDescription") is not None:
        out["vpce_configuration_description"] = data["vpceConfigurationDescription"]
    return out
