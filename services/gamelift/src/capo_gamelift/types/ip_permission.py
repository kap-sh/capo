"""Generated from Smithy shape ``com.amazonaws.gamelift#IpPermission``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.ip_protocol
    import capo_gamelift.types.ip_range
    import capo_gamelift.types.port_number


class IpPermission(TypedDict, closed=True):
    from_port: NotRequired["capo_gamelift.types.port_number.PortNumber"]
    """<p>A starting value for a range of allowed port numbers.</p> <p>For fleets using Linux builds, only ports <code>22</code> and <code>1026-60000</code> are valid.</p> <p>For fleets using Windows builds, only ports <code>1026-60000</code> are valid.</p>"""
    to_port: NotRequired["capo_gamelift.types.port_number.PortNumber"]
    """<p>An ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be equal to or greater than <code>FromPort</code>.</p> <p>For fleets using Linux builds, only ports <code>22</code> and <code>1026-60000</code> are valid.</p> <p>For fleets using Windows builds, only ports <code>1026-60000</code> are valid.</p>"""
    ip_range: NotRequired["capo_gamelift.types.ip_range.IpRange"]
    """<p>A range of allowed IP addresses. This value must be expressed in CIDR notation. Example: "<code>000.000.000.000/[subnet mask]</code>" or optionally the shortened version "<code>0.0.0.0/[subnet mask]</code>".</p>"""
    protocol: NotRequired["capo_gamelift.types.ip_protocol.IpProtocol"]
    """<p>The network communication protocol used by the fleet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpPermission) -> dict:
    out: dict = {}
    if "from_port" in value:
        out["FromPort"] = value["from_port"]
    if "to_port" in value:
        out["ToPort"] = value["to_port"]
    if "ip_range" in value:
        out["IpRange"] = value["ip_range"]
    if "protocol" in value:
        import capo_gamelift.types.ip_protocol

        out["Protocol"] = capo_gamelift.types.ip_protocol.serialize_aws_json_1_1(
            value["protocol"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IpPermission:
    out: IpPermission = {}  # type: ignore[typeddict-item]
    if data.get("FromPort") is not None:
        out["from_port"] = data["FromPort"]
    if data.get("ToPort") is not None:
        out["to_port"] = data["ToPort"]
    if data.get("IpRange") is not None:
        out["ip_range"] = data["IpRange"]
    if data.get("Protocol") is not None:
        import capo_gamelift.types.ip_protocol

        out["protocol"] = capo_gamelift.types.ip_protocol.deserialize_aws_json_1_1(
            data["Protocol"]
        )
    return out
