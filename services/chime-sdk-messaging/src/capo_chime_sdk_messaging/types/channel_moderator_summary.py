"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelModeratorSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.identity


class ChannelModeratorSummary(TypedDict, closed=True):
    moderator: NotRequired["capo_chime_sdk_messaging.types.identity.Identity"]
    """<p>The data for a moderator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelModeratorSummary) -> dict:
    out: dict = {}
    if "moderator" in value:
        import capo_chime_sdk_messaging.types.identity

        out["Moderator"] = capo_chime_sdk_messaging.types.identity.serialize_json(
            value["moderator"]
        )
    return out


def deserialize_json(data: dict) -> ChannelModeratorSummary:
    out: ChannelModeratorSummary = {}  # type: ignore[typeddict-item]
    if data.get("Moderator") is not None:
        import capo_chime_sdk_messaging.types.identity

        out["moderator"] = capo_chime_sdk_messaging.types.identity.deserialize_json(
            data["Moderator"]
        )
    return out


def redact_sensitive(value: ChannelModeratorSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "moderator" in value:
        import capo_chime_sdk_messaging.types.identity

        out["moderator"] = capo_chime_sdk_messaging.types.identity.redact_sensitive(
            value["moderator"]
        )
    return out
