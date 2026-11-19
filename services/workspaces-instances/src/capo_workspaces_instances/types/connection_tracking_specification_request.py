"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ConnectionTrackingSpecificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.non_negative_integer


class ConnectionTrackingSpecificationRequest(TypedDict, closed=True):
    tcp_established_timeout: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Timeout for established TCP connections.</p>"""
    udp_stream_timeout: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Timeout for UDP stream connections.</p>"""
    udp_timeout: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>General timeout for UDP connections.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectionTrackingSpecificationRequest) -> dict:
    out: dict = {}
    if "tcp_established_timeout" in value:
        out["TcpEstablishedTimeout"] = value["tcp_established_timeout"]
    if "udp_stream_timeout" in value:
        out["UdpStreamTimeout"] = value["udp_stream_timeout"]
    if "udp_timeout" in value:
        out["UdpTimeout"] = value["udp_timeout"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ConnectionTrackingSpecificationRequest:
    out: ConnectionTrackingSpecificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("TcpEstablishedTimeout") is not None:
        out["tcp_established_timeout"] = data["TcpEstablishedTimeout"]
    if data.get("UdpStreamTimeout") is not None:
        out["udp_stream_timeout"] = data["UdpStreamTimeout"]
    if data.get("UdpTimeout") is not None:
        out["udp_timeout"] = data["UdpTimeout"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConnectionTrackingSpecificationRequest) -> dict:
    out: dict = {}
    if "tcp_established_timeout" in value:
        out["TcpEstablishedTimeout"] = value["tcp_established_timeout"]
    if "udp_stream_timeout" in value:
        out["UdpStreamTimeout"] = value["udp_stream_timeout"]
    if "udp_timeout" in value:
        out["UdpTimeout"] = value["udp_timeout"]
    return out


def deserialize_cbor(data: dict) -> ConnectionTrackingSpecificationRequest:
    out: ConnectionTrackingSpecificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("TcpEstablishedTimeout") is not None:
        out["tcp_established_timeout"] = data["TcpEstablishedTimeout"]
    if data.get("UdpStreamTimeout") is not None:
        out["udp_stream_timeout"] = data["UdpStreamTimeout"]
    if data.get("UdpTimeout") is not None:
        out["udp_timeout"] = data["UdpTimeout"]
    return out
