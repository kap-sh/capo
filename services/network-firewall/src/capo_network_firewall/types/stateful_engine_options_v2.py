"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StatefulEngineOptionsV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.flow_timeouts
    import capo_network_firewall.types.stream_exception_policy_v2


class StatefulEngineOptionsV2(TypedDict, closed=True):
    stream_exception_policy: NotRequired[
        "capo_network_firewall.types.stream_exception_policy_v2.StreamExceptionPolicyV2"
    ]
    """<p>How Network Firewall handles traffic on a network connection that breaks midstream. A Next Generation policy supports <code>DROP</code> and <code>REJECT</code>. For more information, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/stream-exception-policy.html">Stream exception policy options in your firewall policy</a> in the <i>Network Firewall Developer Guide</i>.</p>"""
    flow_timeouts: NotRequired["capo_network_firewall.types.flow_timeouts.FlowTimeouts"]
    """<p>The amount of time that can pass without any traffic sent through the firewall before the firewall determines that the connection is idle.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatefulEngineOptionsV2) -> dict:
    out: dict = {}
    if "stream_exception_policy" in value:
        import capo_network_firewall.types.stream_exception_policy_v2

        out["StreamExceptionPolicy"] = (
            capo_network_firewall.types.stream_exception_policy_v2.serialize_aws_json_1_0(
                value["stream_exception_policy"]
            )
        )
    if "flow_timeouts" in value:
        import capo_network_firewall.types.flow_timeouts

        out["FlowTimeouts"] = (
            capo_network_firewall.types.flow_timeouts.serialize_aws_json_1_0(
                value["flow_timeouts"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StatefulEngineOptionsV2:
    out: StatefulEngineOptionsV2 = {}  # type: ignore[typeddict-item]
    if data.get("StreamExceptionPolicy") is not None:
        import capo_network_firewall.types.stream_exception_policy_v2

        out["stream_exception_policy"] = (
            capo_network_firewall.types.stream_exception_policy_v2.deserialize_aws_json_1_0(
                data["StreamExceptionPolicy"]
            )
        )
    if data.get("FlowTimeouts") is not None:
        import capo_network_firewall.types.flow_timeouts

        out["flow_timeouts"] = (
            capo_network_firewall.types.flow_timeouts.deserialize_aws_json_1_0(
                data["FlowTimeouts"]
            )
        )
    return out
