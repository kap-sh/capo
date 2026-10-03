"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateWorkforceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.oidc_config
    import capo_sagemaker.types.source_ip_config
    import capo_sagemaker.types.workforce_ip_address_type
    import capo_sagemaker.types.workforce_name
    import capo_sagemaker.types.workforce_vpc_config_request


class UpdateWorkforceRequest(TypedDict, closed=True):
    workforce_name: NotRequired["capo_sagemaker.types.workforce_name.WorkforceName"]
    """<p>The name of the private workforce that you want to update. You can find your workforce name by using the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListWorkforces.html">ListWorkforces</a> operation.</p>"""
    source_ip_config: NotRequired[
        "capo_sagemaker.types.source_ip_config.SourceIpConfig"
    ]
    """<p>A list of one to ten worker IP address ranges (<a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html">CIDRs</a>) that can be used to access tasks assigned to this workforce.</p> <p>Maximum: Ten CIDR values</p>"""
    oidc_config: NotRequired["capo_sagemaker.types.oidc_config.OidcConfig"]
    """<p>Use this parameter to update your OIDC Identity Provider (IdP) configuration for a workforce made using your own IdP.</p>"""
    workforce_vpc_config: NotRequired[
        "capo_sagemaker.types.workforce_vpc_config_request.WorkforceVpcConfigRequest"
    ]
    """<p>Use this parameter to update your VPC configuration for a workforce.</p>"""
    ip_address_type: NotRequired[
        "capo_sagemaker.types.workforce_ip_address_type.WorkforceIpAddressType"
    ]
    """<p>Use this parameter to specify whether you want <code>IPv4</code> only or <code>dualstack</code> (<code>IPv4</code> and <code>IPv6</code>) to support your labeling workforce.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWorkforceRequest) -> dict:
    out: dict = {}
    if "workforce_name" in value:
        out["WorkforceName"] = value["workforce_name"]
    if "source_ip_config" in value:
        import capo_sagemaker.types.source_ip_config

        out["SourceIpConfig"] = (
            capo_sagemaker.types.source_ip_config.serialize_aws_json_1_1(
                value["source_ip_config"]
            )
        )
    if "oidc_config" in value:
        import capo_sagemaker.types.oidc_config

        out["OidcConfig"] = capo_sagemaker.types.oidc_config.serialize_aws_json_1_1(
            value["oidc_config"]
        )
    if "workforce_vpc_config" in value:
        import capo_sagemaker.types.workforce_vpc_config_request

        out["WorkforceVpcConfig"] = (
            capo_sagemaker.types.workforce_vpc_config_request.serialize_aws_json_1_1(
                value["workforce_vpc_config"]
            )
        )
    if "ip_address_type" in value:
        import capo_sagemaker.types.workforce_ip_address_type

        out["IpAddressType"] = (
            capo_sagemaker.types.workforce_ip_address_type.serialize_aws_json_1_1(
                value["ip_address_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateWorkforceRequest:
    out: UpdateWorkforceRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkforceName") is not None:
        out["workforce_name"] = data["WorkforceName"]
    if data.get("SourceIpConfig") is not None:
        import capo_sagemaker.types.source_ip_config

        out["source_ip_config"] = (
            capo_sagemaker.types.source_ip_config.deserialize_aws_json_1_1(
                data["SourceIpConfig"]
            )
        )
    if data.get("OidcConfig") is not None:
        import capo_sagemaker.types.oidc_config

        out["oidc_config"] = capo_sagemaker.types.oidc_config.deserialize_aws_json_1_1(
            data["OidcConfig"]
        )
    if data.get("WorkforceVpcConfig") is not None:
        import capo_sagemaker.types.workforce_vpc_config_request

        out["workforce_vpc_config"] = (
            capo_sagemaker.types.workforce_vpc_config_request.deserialize_aws_json_1_1(
                data["WorkforceVpcConfig"]
            )
        )
    if data.get("IpAddressType") is not None:
        import capo_sagemaker.types.workforce_ip_address_type

        out["ip_address_type"] = (
            capo_sagemaker.types.workforce_ip_address_type.deserialize_aws_json_1_1(
                data["IpAddressType"]
            )
        )
    return out
