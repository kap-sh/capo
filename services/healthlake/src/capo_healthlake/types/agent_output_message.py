"""Generated from Smithy shape ``com.amazonaws.healthlake#AgentOutputMessage``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.agent_message_string
    import capo_healthlake.types.agent_output_message_type
    import capo_healthlake.types.data_transformation_chat_options_list


class AgentOutputMessage(TypedDict, closed=True):
    body: "capo_healthlake.types.agent_message_string.AgentMessageString"
    """<p>The text of the agent's response.</p>"""
    type: "capo_healthlake.types.agent_output_message_type.AgentOutputMessageType"
    """<p>The type of output message, which indicates how to interpret the agent's response.</p>"""
    options_list: NotRequired[
        "capo_healthlake.types.data_transformation_chat_options_list.DataTransformationChatOptionsList"
    ]
    """<p>A list of selectable options presented when the response type is <code>options</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgentOutputMessage) -> dict:
    out: dict = {}
    out["Body"] = value["body"]
    import capo_healthlake.types.agent_output_message_type

    out["Type"] = (
        capo_healthlake.types.agent_output_message_type.serialize_aws_json_1_0(
            value["type"]
        )
    )
    if "options_list" in value:
        import capo_healthlake.types.data_transformation_chat_options_list

        out["OptionsList"] = (
            capo_healthlake.types.data_transformation_chat_options_list.serialize_aws_json_1_0(
                value["options_list"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AgentOutputMessage:
    out: AgentOutputMessage = {}  # type: ignore[typeddict-item]
    if data.get("Body") is not None:
        out["body"] = data["Body"]
    else:
        out["body"] = ""
    if data.get("Type") is not None:
        import capo_healthlake.types.agent_output_message_type

        out["type"] = (
            capo_healthlake.types.agent_output_message_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_healthlake.types.agent_output_message_type.AgentOutputMessageType", ""
        )
    if data.get("OptionsList") is not None:
        import capo_healthlake.types.data_transformation_chat_options_list

        out["options_list"] = (
            capo_healthlake.types.data_transformation_chat_options_list.deserialize_aws_json_1_0(
                data["OptionsList"]
            )
        )
    return out


def redact_sensitive(value: AgentOutputMessage) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "body" in value:
        out["body"] = "*** Sensitive Data Redacted ***"
    if "options_list" in value:
        import capo_healthlake.types.data_transformation_chat_options_list

        out["options_list"] = (
            capo_healthlake.types.data_transformation_chat_options_list.redact_sensitive(
                value["options_list"]
            )
        )
    return out
