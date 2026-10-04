"""Generated from Smithy shape ``com.amazonaws.identitystore#NetworkConfigurationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_identitystore.types.boolean_type
    import capo_identitystore.types.ip_cidr_list
    import capo_identitystore.types.vpc_id_list


class NetworkConfigurationDetails(TypedDict, closed=True):
    vpce_access_required: "capo_identitystore.types.boolean_type.BooleanType"
    """<p>Specifies whether the identity store can be accessed only through a virtual private cloud (VPC) endpoint. When set to <code>true</code>, requests must originate from a VPC endpoint.</p>"""
    api_restrict_source_vpcs: NotRequired[
        "capo_identitystore.types.vpc_id_list.VpcIdList"
    ]
    """<p>A list of virtual private cloud (VPC) IDs that are allowed to access the identity store API operations. A request is denied unless it originates from a VPC in this list, or from an IP address in <code>ApiAllowSourceIps</code> if one is configured. If this field is empty, access isn't restricted to specific VPCs, but the VPC endpoint requirement from <code>VpceAccessRequired</code> still applies.</p>"""
    api_allow_source_ips: NotRequired[
        "capo_identitystore.types.ip_cidr_list.IpCidrList"
    ]
    """<p>A list of IP address CIDR ranges that are allowed to access the identity store API operations. A request from an IP address in this list bypasses the identity store's other API network controls: it's permitted even if it doesn't come through a VPC endpoint required by <code>VpceAccessRequired</code>, and even if it doesn't originate from a VPC in <code>ApiRestrictSourceVpcs</code>. If this field is empty, no such IP address exception applies.</p>"""
    scim_allow_source_ips: NotRequired[
        "capo_identitystore.types.ip_cidr_list.IpCidrList"
    ]
    """<p>A list of IP address CIDR ranges that are allowed to access the identity store through the System for Cross-domain Identity Management (SCIM) protocol. Requests from IP addresses outside these ranges are denied. If this field is empty, SCIM requests remain subject to the identity store's other network controls, such as the VPC endpoint requirement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkConfigurationDetails) -> dict:
    out: dict = {}
    out["VpceAccessRequired"] = value["vpce_access_required"]
    if "api_restrict_source_vpcs" in value:
        import capo_identitystore.types.vpc_id_list

        out["ApiRestrictSourceVpcs"] = (
            capo_identitystore.types.vpc_id_list.serialize_aws_json_1_1(
                value["api_restrict_source_vpcs"]
            )
        )
    if "api_allow_source_ips" in value:
        import capo_identitystore.types.ip_cidr_list

        out["ApiAllowSourceIps"] = (
            capo_identitystore.types.ip_cidr_list.serialize_aws_json_1_1(
                value["api_allow_source_ips"]
            )
        )
    if "scim_allow_source_ips" in value:
        import capo_identitystore.types.ip_cidr_list

        out["ScimAllowSourceIps"] = (
            capo_identitystore.types.ip_cidr_list.serialize_aws_json_1_1(
                value["scim_allow_source_ips"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkConfigurationDetails:
    out: NetworkConfigurationDetails = {}  # type: ignore[typeddict-item]
    if data.get("VpceAccessRequired") is not None:
        out["vpce_access_required"] = data["VpceAccessRequired"]
    else:
        raise DeserializationError(
            "NetworkConfigurationDetails.vpce_access_required required"
        )
    if data.get("ApiRestrictSourceVpcs") is not None:
        import capo_identitystore.types.vpc_id_list

        out["api_restrict_source_vpcs"] = (
            capo_identitystore.types.vpc_id_list.deserialize_aws_json_1_1(
                data["ApiRestrictSourceVpcs"]
            )
        )
    if data.get("ApiAllowSourceIps") is not None:
        import capo_identitystore.types.ip_cidr_list

        out["api_allow_source_ips"] = (
            capo_identitystore.types.ip_cidr_list.deserialize_aws_json_1_1(
                data["ApiAllowSourceIps"]
            )
        )
    if data.get("ScimAllowSourceIps") is not None:
        import capo_identitystore.types.ip_cidr_list

        out["scim_allow_source_ips"] = (
            capo_identitystore.types.ip_cidr_list.deserialize_aws_json_1_1(
                data["ScimAllowSourceIps"]
            )
        )
    return out
