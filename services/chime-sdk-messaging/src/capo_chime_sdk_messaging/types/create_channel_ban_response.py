"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#CreateChannelBanResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.identity


class CreateChannelBanResponse(TypedDict, closed=True):
    channel_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the response to the ban request.</p>"""
    member: NotRequired["capo_chime_sdk_messaging.types.identity.Identity"]
    """<p>The <code>ChannelArn</code> and <code>BannedIdentity</code> of the member in the ban response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelBanResponse) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "member" in value:
        import capo_chime_sdk_messaging.types.identity

        out["Member"] = capo_chime_sdk_messaging.types.identity.serialize_json(
            value["member"]
        )
    return out


def deserialize_json(data: dict) -> CreateChannelBanResponse:
    out: CreateChannelBanResponse = {}  # type: ignore[typeddict-item]
    if data.get("ChannelArn") is not None:
        out["channel_arn"] = data["ChannelArn"]
    if data.get("Member") is not None:
        import capo_chime_sdk_messaging.types.identity

        out["member"] = capo_chime_sdk_messaging.types.identity.deserialize_json(
            data["Member"]
        )
    return out


def redact_sensitive(value: CreateChannelBanResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "member" in value:
        import capo_chime_sdk_messaging.types.identity

        out["member"] = capo_chime_sdk_messaging.types.identity.redact_sensitive(
            value["member"]
        )
    return out
