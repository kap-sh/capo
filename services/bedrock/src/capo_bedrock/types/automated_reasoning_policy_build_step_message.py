"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildStepMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_build_message_type


class AutomatedReasoningPolicyBuildStepMessage(TypedDict, closed=True):
    message: "str"
    """<p>The content of the message, describing what occurred during the build step.</p>"""
    message_type: "capo_bedrock.types.automated_reasoning_policy_build_message_type.AutomatedReasoningPolicyBuildMessageType"
    """<p>The type of message (e.g., INFO, WARNING, ERROR) indicating its severity and purpose.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildStepMessage) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import capo_bedrock.types.automated_reasoning_policy_build_message_type

    out["messageType"] = (
        capo_bedrock.types.automated_reasoning_policy_build_message_type.serialize_json(
            value["message_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyBuildStepMessage:
    out: AutomatedReasoningPolicyBuildStepMessage = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("messageType") is not None:
        import capo_bedrock.types.automated_reasoning_policy_build_message_type

        out["message_type"] = (
            capo_bedrock.types.automated_reasoning_policy_build_message_type.deserialize_json(
                data["messageType"]
            )
        )
    else:
        import typing

        out["message_type"] = typing.cast(
            "capo_bedrock.types.automated_reasoning_policy_build_message_type.AutomatedReasoningPolicyBuildMessageType",
            "",
        )
    return out
