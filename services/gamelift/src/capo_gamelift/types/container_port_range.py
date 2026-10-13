"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerPortRange``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.ip_protocol
    import capo_gamelift.types.port_number


class ContainerPortRange(TypedDict, closed=True):
    from_port: NotRequired["capo_gamelift.types.port_number.PortNumber"]
    """<p>A starting value for the range of allowed port numbers.</p>"""
    to_port: NotRequired["capo_gamelift.types.port_number.PortNumber"]
    """<p>An ending value for the range of allowed port numbers. Port numbers are end-inclusive. This value must be equal to or greater than <code>FromPort</code>.</p>"""
    protocol: NotRequired["capo_gamelift.types.ip_protocol.IpProtocol"]
    """<p>The network protocol that these ports support. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerPortRange) -> dict:
    out: dict = {}
    if "from_port" in value:
        out["FromPort"] = value["from_port"]
    if "to_port" in value:
        out["ToPort"] = value["to_port"]
    if "protocol" in value:
        import capo_gamelift.types.ip_protocol

        out["Protocol"] = capo_gamelift.types.ip_protocol.serialize_aws_json_1_1(
            value["protocol"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerPortRange:
    out: ContainerPortRange = {}  # type: ignore[typeddict-item]
    if data.get("FromPort") is not None:
        out["from_port"] = data["FromPort"]
    if data.get("ToPort") is not None:
        out["to_port"] = data["ToPort"]
    if data.get("Protocol") is not None:
        import capo_gamelift.types.ip_protocol

        out["protocol"] = capo_gamelift.types.ip_protocol.deserialize_aws_json_1_1(
            data["Protocol"]
        )
    return out


def redact_sensitive(value: ContainerPortRange) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "from_port" in value:
        out["from_port"] = "*** Sensitive Data Redacted ***"
    if "to_port" in value:
        out["to_port"] = "*** Sensitive Data Redacted ***"
    return out
