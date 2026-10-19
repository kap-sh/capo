"""Generated from Smithy shape ``com.amazonaws.ecs#HostEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class HostEntry(TypedDict, closed=True):
    hostname: "capo_ecs.types.string.String"
    """<p>The hostname to use in the <code>/etc/hosts</code> entry.</p>"""
    ip_address: "capo_ecs.types.string.String"
    """<p>The IP address to use in the <code>/etc/hosts</code> entry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HostEntry) -> dict:
    out: dict = {}
    out["hostname"] = value["hostname"]
    out["ipAddress"] = value["ip_address"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HostEntry:
    out: HostEntry = {}  # type: ignore[typeddict-item]
    if data.get("hostname") is not None:
        out["hostname"] = data["hostname"]
    else:
        out["hostname"] = ""
    if data.get("ipAddress") is not None:
        out["ip_address"] = data["ipAddress"]
    else:
        out["ip_address"] = ""
    return out
