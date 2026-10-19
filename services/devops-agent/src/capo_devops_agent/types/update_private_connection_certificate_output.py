"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdatePrivateConnectionCertificateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_devops_agent.types.failure_message
    import capo_devops_agent.types.ip_address_or_dns_name
    import capo_devops_agent.types.private_connection_name
    import capo_devops_agent.types.private_connection_status
    import capo_devops_agent.types.private_connection_type
    import capo_devops_agent.types.resource_config_dns_resolution
    import capo_devops_agent.types.resource_configuration_arn
    import capo_devops_agent.types.resource_gateway_arn
    import capo_devops_agent.types.vpc_id


class UpdatePrivateConnectionCertificateOutput(TypedDict, closed=True):
    name: "capo_devops_agent.types.private_connection_name.PrivateConnectionName"
    """<p>The name of the Private Connection.</p>"""
    type: "capo_devops_agent.types.private_connection_type.PrivateConnectionType"
    """<p>The type of the Private Connection.</p>"""
    resource_gateway_id: NotRequired[
        "capo_devops_agent.types.resource_gateway_arn.ResourceGatewayArn"
    ]
    """<p>The service-managed Resource Gateway ARN. Only present for service-managed Private Connections.</p>"""
    host_address: NotRequired[
        "capo_devops_agent.types.ip_address_or_dns_name.IpAddressOrDnsName"
    ]
    """<p>IP address or DNS name of the target resource. Only present for service-managed Private Connections.</p>"""
    vpc_id: NotRequired["capo_devops_agent.types.vpc_id.VpcId"]
    """<p>VPC identifier of the service-managed Resource Gateway. Only present for service-managed Private Connections.</p>"""
    resource_configuration_id: NotRequired[
        "capo_devops_agent.types.resource_configuration_arn.ResourceConfigurationArn"
    ]
    """<p>The Resource Configuration ARN. Only present for self-managed Private Connections.</p>"""
    status: "capo_devops_agent.types.private_connection_status.PrivateConnectionStatus"
    """<p>The status of the Private Connection.</p>"""
    certificate_expiry_time: NotRequired["datetime.datetime"]
    """<p>The expiry time of the certificate associated with the Private Connection. Only present when a certificate is associated.</p>"""
    dns_resolution: NotRequired[
        "capo_devops_agent.types.resource_config_dns_resolution.ResourceConfigDnsResolution"
    ]
    """<p>DNS resolution mode for the Private Connection's resource gateway.</p>"""
    failure_message: NotRequired[
        "capo_devops_agent.types.failure_message.FailureMessage"
    ]
    """<p>Message describing the reason for a failed Private Connection update, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePrivateConnectionCertificateOutput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_devops_agent.types.private_connection_type

    out["type"] = capo_devops_agent.types.private_connection_type.serialize_json(
        value["type"]
    )
    if "resource_gateway_id" in value:
        out["resourceGatewayId"] = value["resource_gateway_id"]
    if "host_address" in value:
        out["hostAddress"] = value["host_address"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "resource_configuration_id" in value:
        out["resourceConfigurationId"] = value["resource_configuration_id"]
    import capo_devops_agent.types.private_connection_status

    out["status"] = capo_devops_agent.types.private_connection_status.serialize_json(
        value["status"]
    )
    if "certificate_expiry_time" in value:
        import capo_devops_agent._protocol.serialize

        out["certificateExpiryTime"] = (
            capo_devops_agent._protocol.serialize.fmt_date_time(
                value["certificate_expiry_time"]
            )
        )
    if "dns_resolution" in value:
        import capo_devops_agent.types.resource_config_dns_resolution

        out["dnsResolution"] = (
            capo_devops_agent.types.resource_config_dns_resolution.serialize_json(
                value["dns_resolution"]
            )
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    return out


def deserialize_json(data: dict) -> UpdatePrivateConnectionCertificateOutput:
    out: UpdatePrivateConnectionCertificateOutput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        import capo_devops_agent.types.private_connection_type

        out["type"] = capo_devops_agent.types.private_connection_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_devops_agent.types.private_connection_type.PrivateConnectionType", ""
        )
    if data.get("resourceGatewayId") is not None:
        out["resource_gateway_id"] = data["resourceGatewayId"]
    if data.get("hostAddress") is not None:
        out["host_address"] = data["hostAddress"]
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    if data.get("resourceConfigurationId") is not None:
        out["resource_configuration_id"] = data["resourceConfigurationId"]
    if data.get("status") is not None:
        import capo_devops_agent.types.private_connection_status

        out["status"] = (
            capo_devops_agent.types.private_connection_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_devops_agent.types.private_connection_status.PrivateConnectionStatus",
            "",
        )
    if data.get("certificateExpiryTime") is not None:
        import datetime

        out["certificate_expiry_time"] = datetime.datetime.fromisoformat(
            data["certificateExpiryTime"].replace("Z", "+00:00")
        )
    if data.get("dnsResolution") is not None:
        import capo_devops_agent.types.resource_config_dns_resolution

        out["dns_resolution"] = (
            capo_devops_agent.types.resource_config_dns_resolution.deserialize_json(
                data["dnsResolution"]
            )
        )
    if data.get("failureMessage") is not None:
        out["failure_message"] = data["failureMessage"]
    return out
