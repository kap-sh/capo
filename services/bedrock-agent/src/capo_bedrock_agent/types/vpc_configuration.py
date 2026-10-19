"""Generated from Smithy shape ``com.amazonaws.bedrockagent#VpcConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.host_header
    import capo_bedrock_agent.types.port
    import capo_bedrock_agent.types.resource_target
    import capo_bedrock_agent.types.subnet_id_list
    import capo_bedrock_agent.types.tls_server_name
    import capo_bedrock_agent.types.vpc_configuration_description
    import capo_bedrock_agent.types.vpc_configuration_id
    import capo_bedrock_agent.types.vpc_configuration_name
    import capo_bedrock_agent.types.vpc_configuration_status
    import capo_bedrock_agent.types.vpc_configuration_status_message
    import capo_bedrock_agent.types.vpc_id
    import capo_bedrock_agent.types.vpc_protocol
    import capo_bedrock_agent.types.vpc_resolution_mode


class VpcConfiguration(TypedDict, closed=True):
    vpc_configuration_id: (
        "capo_bedrock_agent.types.vpc_configuration_id.VpcConfigurationId"
    )
    """<p>The unique identifier of the VPC configuration.</p>"""
    status: "capo_bedrock_agent.types.vpc_configuration_status.VpcConfigurationStatus"
    """<p>The current lifecycle status of the VPC configuration.</p>"""
    status_message: NotRequired[
        "capo_bedrock_agent.types.vpc_configuration_status_message.VpcConfigurationStatusMessage"
    ]
    """<p>Additional detail about the current status, such as the cause of a <code>CREATE_FAILED</code> or <code>DELETE_FAILED</code> status.</p>"""
    vpc_id: "capo_bedrock_agent.types.vpc_id.VpcId"
    """<p>The identifier of the VPC that the knowledge base connects through to reach the resource.</p>"""
    subnet_ids: "capo_bedrock_agent.types.subnet_id_list.SubnetIdList"
    """<p>The subnets that the knowledge base uses to connect to the resource.</p>"""
    resource_target: "capo_bedrock_agent.types.resource_target.ResourceTarget"
    """<p>The private IPv4 address or DNS name of the resource.</p>"""
    port: "capo_bedrock_agent.types.port.Port"
    """<p>The port on which the resource is reached.</p>"""
    protocol: "capo_bedrock_agent.types.vpc_protocol.VpcProtocol"
    """<p>The protocol used to connect to the resource.</p>"""
    resolution_mode: "capo_bedrock_agent.types.vpc_resolution_mode.VpcResolutionMode"
    """<p>Specifies how the resource target is resolved.</p>"""
    host_header: NotRequired["capo_bedrock_agent.types.host_header.HostHeader"]
    """<p>The HTTP <code>Host</code> header value sent when invoking the resource, if configured.</p>"""
    tls_server_name: NotRequired[
        "capo_bedrock_agent.types.tls_server_name.TlsServerName"
    ]
    """<p>The expected TLS server name that the service matches against the Subject Alternative Names on the resource's TLS certificate. Present when <code>protocol</code> is <code>HTTPS</code>.</p>"""
    name: NotRequired[
        "capo_bedrock_agent.types.vpc_configuration_name.VpcConfigurationName"
    ]
    """<p>The human-readable name of the VPC configuration, if provided.</p>"""
    description: NotRequired[
        "capo_bedrock_agent.types.vpc_configuration_description.VpcConfigurationDescription"
    ]
    """<p>The description of the VPC configuration, if provided.</p>"""
    created_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the VPC configuration was created.</p>"""
    updated_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the VPC configuration was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfiguration) -> dict:
    out: dict = {}
    out["vpcConfigurationId"] = value["vpc_configuration_id"]
    import capo_bedrock_agent.types.vpc_configuration_status

    out["status"] = capo_bedrock_agent.types.vpc_configuration_status.serialize_json(
        value["status"]
    )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    out["vpcId"] = value["vpc_id"]
    import capo_bedrock_agent.types.subnet_id_list

    out["subnetIds"] = capo_bedrock_agent.types.subnet_id_list.serialize_json(
        value["subnet_ids"]
    )
    out["resourceTarget"] = value["resource_target"]
    out["port"] = value["port"]
    import capo_bedrock_agent.types.vpc_protocol

    out["protocol"] = capo_bedrock_agent.types.vpc_protocol.serialize_json(
        value["protocol"]
    )
    import capo_bedrock_agent.types.vpc_resolution_mode

    out["resolutionMode"] = capo_bedrock_agent.types.vpc_resolution_mode.serialize_json(
        value["resolution_mode"]
    )
    if "host_header" in value:
        out["hostHeader"] = value["host_header"]
    if "tls_server_name" in value:
        out["tlsServerName"] = value["tls_server_name"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agent.types.date_timestamp

    out["createdAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_bedrock_agent.types.date_timestamp

    out["updatedAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> VpcConfiguration:
    out: VpcConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("vpcConfigurationId") is not None:
        out["vpc_configuration_id"] = data["vpcConfigurationId"]
    else:
        out["vpc_configuration_id"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agent.types.vpc_configuration_status

        out["status"] = (
            capo_bedrock_agent.types.vpc_configuration_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agent.types.vpc_configuration_status.VpcConfigurationStatus",
            "",
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    else:
        out["vpc_id"] = ""
    if data.get("subnetIds") is not None:
        import capo_bedrock_agent.types.subnet_id_list

        out["subnet_ids"] = capo_bedrock_agent.types.subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    else:
        out["subnet_ids"] = []
    if data.get("resourceTarget") is not None:
        out["resource_target"] = data["resourceTarget"]
    else:
        out["resource_target"] = ""
    if data.get("port") is not None:
        out["port"] = data["port"]
    else:
        out["port"] = 0
    if data.get("protocol") is not None:
        import capo_bedrock_agent.types.vpc_protocol

        out["protocol"] = capo_bedrock_agent.types.vpc_protocol.deserialize_json(
            data["protocol"]
        )
    else:
        import typing

        out["protocol"] = typing.cast(
            "capo_bedrock_agent.types.vpc_protocol.VpcProtocol", ""
        )
    if data.get("resolutionMode") is not None:
        import capo_bedrock_agent.types.vpc_resolution_mode

        out["resolution_mode"] = (
            capo_bedrock_agent.types.vpc_resolution_mode.deserialize_json(
                data["resolutionMode"]
            )
        )
    else:
        import typing

        out["resolution_mode"] = typing.cast(
            "capo_bedrock_agent.types.vpc_resolution_mode.VpcResolutionMode", ""
        )
    if data.get("hostHeader") is not None:
        out["host_header"] = data["hostHeader"]
    if data.get("tlsServerName") is not None:
        out["tls_server_name"] = data["tlsServerName"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("createdAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["created_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["updated_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
