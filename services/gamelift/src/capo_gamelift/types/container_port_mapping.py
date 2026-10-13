"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerPortMapping``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.ip_protocol
    import capo_gamelift.types.port_number


class ContainerPortMapping(TypedDict, closed=True):
    container_port: NotRequired["capo_gamelift.types.port_number.PortNumber"]
    """<p>The port number on the container. This port is defined in the container group definition. Container port numbers must be unique within a container group definition.</p>"""
    connection_port: NotRequired["capo_gamelift.types.port_number.PortNumber"]
    """<p>The port number on the fleet instance that maps to the container port. Connection ports are assigned by Amazon GameLift Servers when the container group is deployed to an instance.</p>"""
    protocol: NotRequired["capo_gamelift.types.ip_protocol.IpProtocol"]
    """<p>The network protocol for the port mapping. Valid values are <code>TCP</code> or <code>UDP</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerPortMapping) -> dict:
    out: dict = {}
    if "container_port" in value:
        out["ContainerPort"] = value["container_port"]
    if "connection_port" in value:
        out["ConnectionPort"] = value["connection_port"]
    if "protocol" in value:
        import capo_gamelift.types.ip_protocol

        out["Protocol"] = capo_gamelift.types.ip_protocol.serialize_aws_json_1_1(
            value["protocol"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerPortMapping:
    out: ContainerPortMapping = {}  # type: ignore[typeddict-item]
    if data.get("ContainerPort") is not None:
        out["container_port"] = data["ContainerPort"]
    if data.get("ConnectionPort") is not None:
        out["connection_port"] = data["ConnectionPort"]
    if data.get("Protocol") is not None:
        import capo_gamelift.types.ip_protocol

        out["protocol"] = capo_gamelift.types.ip_protocol.deserialize_aws_json_1_1(
            data["Protocol"]
        )
    return out


def redact_sensitive(value: ContainerPortMapping) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "container_port" in value:
        out["container_port"] = "*** Sensitive Data Redacted ***"
    if "connection_port" in value:
        out["connection_port"] = "*** Sensitive Data Redacted ***"
    return out
