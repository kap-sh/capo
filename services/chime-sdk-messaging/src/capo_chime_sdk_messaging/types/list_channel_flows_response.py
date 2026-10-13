"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListChannelFlowsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_flow_summary_list
    import capo_chime_sdk_messaging.types.next_token


class ListChannelFlowsResponse(TypedDict, closed=True):
    channel_flows: NotRequired[
        "capo_chime_sdk_messaging.types.channel_flow_summary_list.ChannelFlowSummaryList"
    ]
    """<p>The information about each channel flow.</p>"""
    next_token: NotRequired["capo_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested channels are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelFlowsResponse) -> dict:
    out: dict = {}
    if "channel_flows" in value:
        import capo_chime_sdk_messaging.types.channel_flow_summary_list

        out["ChannelFlows"] = (
            capo_chime_sdk_messaging.types.channel_flow_summary_list.serialize_json(
                value["channel_flows"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChannelFlowsResponse:
    out: ListChannelFlowsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ChannelFlows") is not None:
        import capo_chime_sdk_messaging.types.channel_flow_summary_list

        out["channel_flows"] = (
            capo_chime_sdk_messaging.types.channel_flow_summary_list.deserialize_json(
                data["ChannelFlows"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListChannelFlowsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel_flows" in value:
        import capo_chime_sdk_messaging.types.channel_flow_summary_list

        out["channel_flows"] = (
            capo_chime_sdk_messaging.types.channel_flow_summary_list.redact_sensitive(
                value["channel_flows"]
            )
        )
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
