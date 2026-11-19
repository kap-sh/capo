"""Generated from Smithy shape ``com.amazonaws.guardduty#NetworkPorts``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.count
    import capo_guardduty.types.string


class NetworkPorts(TypedDict, closed=True):
    target_port: NotRequired["capo_guardduty.types.string.String"]
    """<p>The port on the target of the activity.</p>"""
    remote_port: NotRequired["capo_guardduty.types.string.String"]
    """<p>The port on the remote host.</p>"""
    resolver_port: NotRequired["capo_guardduty.types.string.String"]
    """<p>The port of the DNS resolver.</p>"""
    ports: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ports that the activity involved.</p>"""
    ports_used: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ports that the activity used.</p>"""
    port_count: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The number of ports that the activity involved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkPorts) -> dict:
    out: dict = {}
    if "target_port" in value:
        out["targetPort"] = value["target_port"]
    if "remote_port" in value:
        out["remotePort"] = value["remote_port"]
    if "resolver_port" in value:
        out["resolverPort"] = value["resolver_port"]
    if "ports" in value:
        out["ports"] = value["ports"]
    if "ports_used" in value:
        out["portsUsed"] = value["ports_used"]
    if "port_count" in value:
        out["portCount"] = value["port_count"]
    return out


def deserialize_json(data: dict) -> NetworkPorts:
    out: NetworkPorts = {}  # type: ignore[typeddict-item]
    if data.get("targetPort") is not None:
        out["target_port"] = data["targetPort"]
    if data.get("remotePort") is not None:
        out["remote_port"] = data["remotePort"]
    if data.get("resolverPort") is not None:
        out["resolver_port"] = data["resolverPort"]
    if data.get("ports") is not None:
        out["ports"] = data["ports"]
    if data.get("portsUsed") is not None:
        out["ports_used"] = data["portsUsed"]
    if data.get("portCount") is not None:
        out["port_count"] = data["portCount"]
    return out
