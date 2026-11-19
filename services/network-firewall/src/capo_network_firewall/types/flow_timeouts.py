"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FlowTimeouts``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.tcp_idle_timeout_range_bound


class FlowTimeouts(TypedDict, closed=True):
    tcp_idle_timeout_seconds: NotRequired[
        "capo_network_firewall.types.tcp_idle_timeout_range_bound.TcpIdleTimeoutRangeBound"
    ]
    """<p>The number of seconds that can pass without any TCP traffic sent through the firewall before the firewall determines that the connection is idle. After the idle timeout passes, data packets are dropped, however, the next TCP SYN packet is considered a new flow and is processed by the firewall. Clients or targets can use TCP keepalive packets to reset the idle timeout. </p> <p>You can define the <code>TcpIdleTimeoutSeconds</code> value to be between 60 and 6000 seconds. If no value is provided, it defaults to 350 seconds. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FlowTimeouts) -> dict:
    out: dict = {}
    if "tcp_idle_timeout_seconds" in value:
        out["TcpIdleTimeoutSeconds"] = value["tcp_idle_timeout_seconds"]
    return out


def deserialize_aws_json_1_0(data: dict) -> FlowTimeouts:
    out: FlowTimeouts = {}  # type: ignore[typeddict-item]
    if data.get("TcpIdleTimeoutSeconds") is not None:
        out["tcp_idle_timeout_seconds"] = data["TcpIdleTimeoutSeconds"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FlowTimeouts) -> dict:
    out: dict = {}
    if "tcp_idle_timeout_seconds" in value:
        out["TcpIdleTimeoutSeconds"] = value["tcp_idle_timeout_seconds"]
    return out


def deserialize_cbor(data: dict) -> FlowTimeouts:
    out: FlowTimeouts = {}  # type: ignore[typeddict-item]
    if data.get("TcpIdleTimeoutSeconds") is not None:
        out["tcp_idle_timeout_seconds"] = data["TcpIdleTimeoutSeconds"]
    return out
