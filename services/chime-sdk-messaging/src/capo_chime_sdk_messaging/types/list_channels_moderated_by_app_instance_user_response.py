"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListChannelsModeratedByAppInstanceUserResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_moderated_by_app_instance_user_summary_list
    import capo_chime_sdk_messaging.types.next_token


class ListChannelsModeratedByAppInstanceUserResponse(TypedDict, closed=True):
    channels: NotRequired[
        "capo_chime_sdk_messaging.types.channel_moderated_by_app_instance_user_summary_list.ChannelModeratedByAppInstanceUserSummaryList"
    ]
    """<p>The moderated channels in the request.</p>"""
    next_token: NotRequired["capo_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token returned from previous API requests until the number of channels moderated by the user is reached.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelsModeratedByAppInstanceUserResponse) -> dict:
    out: dict = {}
    if "channels" in value:
        import capo_chime_sdk_messaging.types.channel_moderated_by_app_instance_user_summary_list

        out["Channels"] = (
            capo_chime_sdk_messaging.types.channel_moderated_by_app_instance_user_summary_list.serialize_json(
                value["channels"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChannelsModeratedByAppInstanceUserResponse:
    out: ListChannelsModeratedByAppInstanceUserResponse = {}  # type: ignore[typeddict-item]
    if data.get("Channels") is not None:
        import capo_chime_sdk_messaging.types.channel_moderated_by_app_instance_user_summary_list

        out["channels"] = (
            capo_chime_sdk_messaging.types.channel_moderated_by_app_instance_user_summary_list.deserialize_json(
                data["Channels"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(
    value: ListChannelsModeratedByAppInstanceUserResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channels" in value:
        import capo_chime_sdk_messaging.types.channel_moderated_by_app_instance_user_summary_list

        out["channels"] = (
            capo_chime_sdk_messaging.types.channel_moderated_by_app_instance_user_summary_list.redact_sensitive(
                value["channels"]
            )
        )
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
