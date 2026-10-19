"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateChatResponseConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.chat_response_configuration_arn
    import capo_qbusiness.types.chat_response_configuration_id


class CreateChatResponseConfigurationResponse(TypedDict, closed=True):
    chat_response_configuration_id: "capo_qbusiness.types.chat_response_configuration_id.ChatResponseConfigurationId"
    """<p>The unique identifier assigned to a newly created chat response configuration, used for subsequent operations on this resource.</p>"""
    chat_response_configuration_arn: "capo_qbusiness.types.chat_response_configuration_arn.ChatResponseConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the newly created chat response configuration, which uniquely identifies the resource across all Amazon Web Services services. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChatResponseConfigurationResponse) -> dict:
    out: dict = {}
    out["chatResponseConfigurationId"] = value["chat_response_configuration_id"]
    out["chatResponseConfigurationArn"] = value["chat_response_configuration_arn"]
    return out


def deserialize_json(data: dict) -> CreateChatResponseConfigurationResponse:
    out: CreateChatResponseConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("chatResponseConfigurationId") is not None:
        out["chat_response_configuration_id"] = data["chatResponseConfigurationId"]
    else:
        out["chat_response_configuration_id"] = ""
    if data.get("chatResponseConfigurationArn") is not None:
        out["chat_response_configuration_arn"] = data["chatResponseConfigurationArn"]
    else:
        out["chat_response_configuration_arn"] = ""
    return out
