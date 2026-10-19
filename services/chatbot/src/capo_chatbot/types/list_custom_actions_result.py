"""Generated from Smithy shape ``com.amazonaws.chatbot#ListCustomActionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.custom_action_arn_list


class ListCustomActionsResult(TypedDict, closed=True):
    custom_actions: "capo_chatbot.types.custom_action_arn_list.CustomActionArnList"
    """<p>A list of custom actions.</p>"""
    next_token: NotRequired["str"]
    """<p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomActionsResult) -> dict:
    out: dict = {}
    import capo_chatbot.types.custom_action_arn_list

    out["CustomActions"] = capo_chatbot.types.custom_action_arn_list.serialize_json(
        value["custom_actions"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCustomActionsResult:
    out: ListCustomActionsResult = {}  # type: ignore[typeddict-item]
    if data.get("CustomActions") is not None:
        import capo_chatbot.types.custom_action_arn_list

        out["custom_actions"] = (
            capo_chatbot.types.custom_action_arn_list.deserialize_json(
                data["CustomActions"]
            )
        )
    else:
        out["custom_actions"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
