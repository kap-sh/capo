"""Generated from Smithy shape ``com.amazonaws.gamelift#ConnectionPortRange``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.port_number


class ConnectionPortRange(TypedDict, closed=True):
    from_port: NotRequired["capo_gamelift.types.port_number.PortNumber"]
    """<p>Starting value for the port range.</p>"""
    to_port: NotRequired["capo_gamelift.types.port_number.PortNumber"]
    """<p>Ending value for the port. Port numbers are end-inclusive. This value must be equal to or greater than <code>FromPort</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionPortRange) -> dict:
    out: dict = {}
    if "from_port" in value:
        out["FromPort"] = value["from_port"]
    if "to_port" in value:
        out["ToPort"] = value["to_port"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionPortRange:
    out: ConnectionPortRange = {}  # type: ignore[typeddict-item]
    if data.get("FromPort") is not None:
        out["from_port"] = data["FromPort"]
    if data.get("ToPort") is not None:
        out["to_port"] = data["ToPort"]
    return out


def redact_sensitive(value: ConnectionPortRange) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "from_port" in value:
        out["from_port"] = "*** Sensitive Data Redacted ***"
    if "to_port" in value:
        out["to_port"] = "*** Sensitive Data Redacted ***"
    return out
