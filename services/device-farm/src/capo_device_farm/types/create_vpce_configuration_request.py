"""Generated from Smithy shape ``com.amazonaws.devicefarm#CreateVPCEConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.service_dns_name
    import capo_device_farm.types.vpce_configuration_description
    import capo_device_farm.types.vpce_configuration_name
    import capo_device_farm.types.vpce_service_name


class CreateVPCEConfigurationRequest(TypedDict, closed=True):
    vpce_configuration_name: (
        "capo_device_farm.types.vpce_configuration_name.VPCEConfigurationName"
    )
    """<p>The friendly name you give to your VPC endpoint configuration, to manage your configurations more easily.</p>"""
    vpce_service_name: "capo_device_farm.types.vpce_service_name.VPCEServiceName"
    """<p>The name of the VPC endpoint service running in your AWS account that you want Device Farm to test.</p>"""
    service_dns_name: "capo_device_farm.types.service_dns_name.ServiceDnsName"
    """<p>The DNS name of the service running in your VPC that you want Device Farm to test.</p>"""
    vpce_configuration_description: NotRequired[
        "capo_device_farm.types.vpce_configuration_description.VPCEConfigurationDescription"
    ]
    """<p>An optional description that provides details about your VPC endpoint configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateVPCEConfigurationRequest) -> dict:
    out: dict = {}
    out["vpceConfigurationName"] = value["vpce_configuration_name"]
    out["vpceServiceName"] = value["vpce_service_name"]
    out["serviceDnsName"] = value["service_dns_name"]
    if "vpce_configuration_description" in value:
        out["vpceConfigurationDescription"] = value["vpce_configuration_description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateVPCEConfigurationRequest:
    out: CreateVPCEConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("vpceConfigurationName") is not None:
        out["vpce_configuration_name"] = data["vpceConfigurationName"]
    else:
        out["vpce_configuration_name"] = ""
    if data.get("vpceServiceName") is not None:
        out["vpce_service_name"] = data["vpceServiceName"]
    else:
        out["vpce_service_name"] = ""
    if data.get("serviceDnsName") is not None:
        out["service_dns_name"] = data["serviceDnsName"]
    else:
        out["service_dns_name"] = ""
    if data.get("vpceConfigurationDescription") is not None:
        out["vpce_configuration_description"] = data["vpceConfigurationDescription"]
    return out
