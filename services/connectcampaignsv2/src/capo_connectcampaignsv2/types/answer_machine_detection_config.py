"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#AnswerMachineDetectionConfig``."""

from typing_extensions import NotRequired, TypedDict


class AnswerMachineDetectionConfig(TypedDict, closed=True):
    enable_answer_machine_detection: "bool"
    """Enable or disable answering machine detection"""
    await_answer_machine_prompt: NotRequired["bool"]
    """Enable or disable await answer machine prompt"""


# --- restJson1 ser/de ---
def serialize_json(value: AnswerMachineDetectionConfig) -> dict:
    out: dict = {}
    out["enableAnswerMachineDetection"] = value["enable_answer_machine_detection"]
    if "await_answer_machine_prompt" in value:
        out["awaitAnswerMachinePrompt"] = value["await_answer_machine_prompt"]
    return out


def deserialize_json(data: dict) -> AnswerMachineDetectionConfig:
    out: AnswerMachineDetectionConfig = {}  # type: ignore[typeddict-item]
    if data.get("enableAnswerMachineDetection") is not None:
        out["enable_answer_machine_detection"] = data["enableAnswerMachineDetection"]
    else:
        out["enable_answer_machine_detection"] = False
    if data.get("awaitAnswerMachinePrompt") is not None:
        out["await_answer_machine_prompt"] = data["awaitAnswerMachinePrompt"]
    return out
