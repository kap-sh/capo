"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#ListAppInstanceBotsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.app_instance_bot_list
    import capo_chime_sdk_identity.types.chime_arn
    import capo_chime_sdk_identity.types.next_token


class ListAppInstanceBotsResponse(TypedDict, closed=True):
    app_instance_arn: NotRequired["capo_chime_sdk_identity.types.chime_arn.ChimeArn"]
    """<p>The ARN of the AppInstance.</p>"""
    app_instance_bots: NotRequired[
        "capo_chime_sdk_identity.types.app_instance_bot_list.AppInstanceBotList"
    ]
    """<p>The information for each requested <code>AppInstanceBot</code>.</p>"""
    next_token: NotRequired["capo_chime_sdk_identity.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested bots are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppInstanceBotsResponse) -> dict:
    out: dict = {}
    if "app_instance_arn" in value:
        out["AppInstanceArn"] = value["app_instance_arn"]
    if "app_instance_bots" in value:
        import capo_chime_sdk_identity.types.app_instance_bot_list

        out["AppInstanceBots"] = (
            capo_chime_sdk_identity.types.app_instance_bot_list.serialize_json(
                value["app_instance_bots"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppInstanceBotsResponse:
    out: ListAppInstanceBotsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AppInstanceArn") is not None:
        out["app_instance_arn"] = data["AppInstanceArn"]
    if data.get("AppInstanceBots") is not None:
        import capo_chime_sdk_identity.types.app_instance_bot_list

        out["app_instance_bots"] = (
            capo_chime_sdk_identity.types.app_instance_bot_list.deserialize_json(
                data["AppInstanceBots"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListAppInstanceBotsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "app_instance_bots" in value:
        import capo_chime_sdk_identity.types.app_instance_bot_list

        out["app_instance_bots"] = (
            capo_chime_sdk_identity.types.app_instance_bot_list.redact_sensitive(
                value["app_instance_bots"]
            )
        )
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
