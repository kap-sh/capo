"""Generated from Smithy shape ``com.amazonaws.securityagent#DescribePrivateConnectionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.host_address
    import capo_securityagent.types.private_connection_name
    import capo_securityagent.types.private_connection_status
    import capo_securityagent.types.private_connection_type
    import capo_securityagent.types.private_connection_vpc_id
    import capo_securityagent.types.resource_config_dns_resolution
    import capo_securityagent.types.resource_configuration_id
    import capo_securityagent.types.resource_gateway_id
    import capo_securityagent.types.tag_map


class DescribePrivateConnectionOutput(TypedDict, closed=True):
    name: "capo_securityagent.types.private_connection_name.PrivateConnectionName"
    """<p>The name of the private connection.</p>"""
    type: "capo_securityagent.types.private_connection_type.PrivateConnectionType"
    """<p>The type of the private connection, indicating whether it is service-managed or self-managed.</p>"""
    status: "capo_securityagent.types.private_connection_status.PrivateConnectionStatus"
    """<p>The current status of the private connection.</p>"""
    resource_gateway_id: NotRequired[
        "capo_securityagent.types.resource_gateway_id.ResourceGatewayId"
    ]
    """<p>The identifier or ARN of the VPC Lattice resource gateway.</p>"""
    host_address: NotRequired["capo_securityagent.types.host_address.HostAddress"]
    """<p>The IP address or DNS name of the target resource.</p>"""
    vpc_id: NotRequired[
        "capo_securityagent.types.private_connection_vpc_id.PrivateConnectionVpcId"
    ]
    """<p>The identifier of the VPC the resource gateway is created in.</p>"""
    resource_configuration_id: NotRequired[
        "capo_securityagent.types.resource_configuration_id.ResourceConfigurationId"
    ]
    """<p>The identifier or ARN of the VPC Lattice resource configuration.</p>"""
    certificate_expiry_time: NotRequired["datetime.datetime"]
    """<p>The date and time the connection's certificate expires, in UTC format.</p>"""
    dns_resolution: NotRequired[
        "capo_securityagent.types.resource_config_dns_resolution.ResourceConfigDnsResolution"
    ]
    """<p>The DNS resolution mode for the resource gateway.</p>"""
    failure_message: NotRequired["str"]
    """<p>A message describing why the private connection entered a failed state, if applicable.</p>"""
    tags: NotRequired["capo_securityagent.types.tag_map.TagMap"]
    """<p>The tags attached to the private connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePrivateConnectionOutput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_securityagent.types.private_connection_type

    out["type"] = capo_securityagent.types.private_connection_type.serialize_json(
        value["type"]
    )
    import capo_securityagent.types.private_connection_status

    out["status"] = capo_securityagent.types.private_connection_status.serialize_json(
        value["status"]
    )
    if "resource_gateway_id" in value:
        out["resourceGatewayId"] = value["resource_gateway_id"]
    if "host_address" in value:
        out["hostAddress"] = value["host_address"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "resource_configuration_id" in value:
        out["resourceConfigurationId"] = value["resource_configuration_id"]
    if "certificate_expiry_time" in value:
        import capo_securityagent._protocol.serialize

        out["certificateExpiryTime"] = (
            capo_securityagent._protocol.serialize.fmt_date_time(
                value["certificate_expiry_time"]
            )
        )
    if "dns_resolution" in value:
        import capo_securityagent.types.resource_config_dns_resolution

        out["dnsResolution"] = (
            capo_securityagent.types.resource_config_dns_resolution.serialize_json(
                value["dns_resolution"]
            )
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    if "tags" in value:
        import capo_securityagent.types.tag_map

        out["tags"] = capo_securityagent.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DescribePrivateConnectionOutput:
    out: DescribePrivateConnectionOutput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        import capo_securityagent.types.private_connection_type

        out["type"] = capo_securityagent.types.private_connection_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_securityagent.types.private_connection_type.PrivateConnectionType", ""
        )
    if data.get("status") is not None:
        import capo_securityagent.types.private_connection_status

        out["status"] = (
            capo_securityagent.types.private_connection_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_securityagent.types.private_connection_status.PrivateConnectionStatus",
            "",
        )
    if data.get("resourceGatewayId") is not None:
        out["resource_gateway_id"] = data["resourceGatewayId"]
    if data.get("hostAddress") is not None:
        out["host_address"] = data["hostAddress"]
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    if data.get("resourceConfigurationId") is not None:
        out["resource_configuration_id"] = data["resourceConfigurationId"]
    if data.get("certificateExpiryTime") is not None:
        import datetime

        out["certificate_expiry_time"] = datetime.datetime.fromisoformat(
            data["certificateExpiryTime"].replace("Z", "+00:00")
        )
    if data.get("dnsResolution") is not None:
        import capo_securityagent.types.resource_config_dns_resolution

        out["dns_resolution"] = (
            capo_securityagent.types.resource_config_dns_resolution.deserialize_json(
                data["dnsResolution"]
            )
        )
    if data.get("failureMessage") is not None:
        out["failure_message"] = data["failureMessage"]
    if data.get("tags") is not None:
        import capo_securityagent.types.tag_map

        out["tags"] = capo_securityagent.types.tag_map.deserialize_json(data["tags"])
    return out
