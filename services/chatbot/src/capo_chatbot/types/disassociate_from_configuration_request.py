"""Generated from Smithy shape ``com.amazonaws.chatbot#DisassociateFromConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.chat_configuration_arn
    import capo_chatbot.types.resource_identifier


class DisassociateFromConfigurationRequest(TypedDict, closed=True):
    resource: "capo_chatbot.types.resource_identifier.ResourceIdentifier"
    """<p>The resource (for example, a custom action) Amazon Resource Name (ARN) to unlink.</p>"""
    chat_configuration: "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
    """<p>The channel configuration the resource is being disassociated from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateFromConfigurationRequest) -> dict:
    out: dict = {}
    out["Resource"] = value["resource"]
    out["ChatConfiguration"] = value["chat_configuration"]
    return out


def deserialize_json(data: dict) -> DisassociateFromConfigurationRequest:
    out: DisassociateFromConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Resource") is not None:
        out["resource"] = data["Resource"]
    else:
        out["resource"] = ""
    if data.get("ChatConfiguration") is not None:
        out["chat_configuration"] = data["ChatConfiguration"]
    else:
        out["chat_configuration"] = ""
    return out
