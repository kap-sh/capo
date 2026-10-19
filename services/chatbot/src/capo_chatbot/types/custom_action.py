"""Generated from Smithy shape ``com.amazonaws.chatbot#CustomAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chatbot.types.custom_action_alias_name
    import capo_chatbot.types.custom_action_arn
    import capo_chatbot.types.custom_action_attachment_list
    import capo_chatbot.types.custom_action_definition
    import capo_chatbot.types.custom_action_name


class CustomAction(TypedDict, closed=True):
    custom_action_arn: "capo_chatbot.types.custom_action_arn.CustomActionArn"
    """<p>The fully defined Amazon Resource Name (ARN) of the custom action.</p>"""
    definition: "capo_chatbot.types.custom_action_definition.CustomActionDefinition"
    """<p>The definition of the command to run when invoked an alias or as an action button.</p>"""
    alias_name: NotRequired[
        "capo_chatbot.types.custom_action_alias_name.CustomActionAliasName"
    ]
    """<p>The name used to invoke this action in the chat channel. For example, <code>@aws run my-alias</code>.</p>"""
    attachments: NotRequired[
        "capo_chatbot.types.custom_action_attachment_list.CustomActionAttachmentList"
    ]
    """<p>Defines when this custom action button should be attached to a notification.</p>"""
    action_name: NotRequired["capo_chatbot.types.custom_action_name.CustomActionName"]
    """<p>The name of the custom action that is included in the ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomAction) -> dict:
    out: dict = {}
    out["CustomActionArn"] = value["custom_action_arn"]
    import capo_chatbot.types.custom_action_definition

    out["Definition"] = capo_chatbot.types.custom_action_definition.serialize_json(
        value["definition"]
    )
    if "alias_name" in value:
        out["AliasName"] = value["alias_name"]
    if "attachments" in value:
        import capo_chatbot.types.custom_action_attachment_list

        out["Attachments"] = (
            capo_chatbot.types.custom_action_attachment_list.serialize_json(
                value["attachments"]
            )
        )
    if "action_name" in value:
        out["ActionName"] = value["action_name"]
    return out


def deserialize_json(data: dict) -> CustomAction:
    out: CustomAction = {}  # type: ignore[typeddict-item]
    if data.get("CustomActionArn") is not None:
        out["custom_action_arn"] = data["CustomActionArn"]
    else:
        out["custom_action_arn"] = ""
    if data.get("Definition") is not None:
        import capo_chatbot.types.custom_action_definition

        out["definition"] = (
            capo_chatbot.types.custom_action_definition.deserialize_json(
                data["Definition"]
            )
        )
    else:
        raise DeserializationError("CustomAction.definition required")
    if data.get("AliasName") is not None:
        out["alias_name"] = data["AliasName"]
    if data.get("Attachments") is not None:
        import capo_chatbot.types.custom_action_attachment_list

        out["attachments"] = (
            capo_chatbot.types.custom_action_attachment_list.deserialize_json(
                data["Attachments"]
            )
        )
    if data.get("ActionName") is not None:
        out["action_name"] = data["ActionName"]
    return out
