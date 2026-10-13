"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMembershipSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.identity


class ChannelMembershipSummary(TypedDict, closed=True):
    member: NotRequired["capo_chime_sdk_messaging.types.identity.Identity"]
    """<p>A member's summary data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMembershipSummary) -> dict:
    out: dict = {}
    if "member" in value:
        import capo_chime_sdk_messaging.types.identity

        out["Member"] = capo_chime_sdk_messaging.types.identity.serialize_json(
            value["member"]
        )
    return out


def deserialize_json(data: dict) -> ChannelMembershipSummary:
    out: ChannelMembershipSummary = {}  # type: ignore[typeddict-item]
    if data.get("Member") is not None:
        import capo_chime_sdk_messaging.types.identity

        out["member"] = capo_chime_sdk_messaging.types.identity.deserialize_json(
            data["Member"]
        )
    return out


def redact_sensitive(value: ChannelMembershipSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "member" in value:
        import capo_chime_sdk_messaging.types.identity

        out["member"] = capo_chime_sdk_messaging.types.identity.redact_sensitive(
            value["member"]
        )
    return out
