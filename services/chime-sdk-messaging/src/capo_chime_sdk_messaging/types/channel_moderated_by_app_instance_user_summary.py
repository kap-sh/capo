"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelModeratedByAppInstanceUserSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_summary


class ChannelModeratedByAppInstanceUserSummary(TypedDict, closed=True):
    channel_summary: NotRequired[
        "capo_chime_sdk_messaging.types.channel_summary.ChannelSummary"
    ]
    """<p>Summary of the details of a <code>Channel</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelModeratedByAppInstanceUserSummary) -> dict:
    out: dict = {}
    if "channel_summary" in value:
        import capo_chime_sdk_messaging.types.channel_summary

        out["ChannelSummary"] = (
            capo_chime_sdk_messaging.types.channel_summary.serialize_json(
                value["channel_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChannelModeratedByAppInstanceUserSummary:
    out: ChannelModeratedByAppInstanceUserSummary = {}  # type: ignore[typeddict-item]
    if data.get("ChannelSummary") is not None:
        import capo_chime_sdk_messaging.types.channel_summary

        out["channel_summary"] = (
            capo_chime_sdk_messaging.types.channel_summary.deserialize_json(
                data["ChannelSummary"]
            )
        )
    return out


def redact_sensitive(value: ChannelModeratedByAppInstanceUserSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel_summary" in value:
        import capo_chime_sdk_messaging.types.channel_summary

        out["channel_summary"] = (
            capo_chime_sdk_messaging.types.channel_summary.redact_sensitive(
                value["channel_summary"]
            )
        )
    return out
