"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksSensitiveInformationResultEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_entity_type


class GuardrailChecksSensitiveInformationResultEntry(TypedDict, closed=True):
    type: "capo_bedrock_runtime.types.guardrail_checks_sensitive_information_entity_type.GuardrailChecksSensitiveInformationEntityType"
    """<p>The PII entity type that was detected.</p>"""
    confidence_score: "float"
    """<p>The confidence score for the detection, ranging from 0.0 to 1.0. Higher values indicate greater confidence.</p>"""
    begin_offset: "int"
    """<p>The start character offset of the detected entity within the content block.</p>"""
    end_offset: "int"
    """<p>The end character offset of the detected entity within the content block.</p>"""
    message_index: "int"
    """<p>The zero-based index of the message in the input messages array where the entity was detected.</p>"""
    content_index: "int"
    """<p>The zero-based index of the content block within the message where the entity was detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksSensitiveInformationResultEntry) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_entity_type

    out["type"] = (
        capo_bedrock_runtime.types.guardrail_checks_sensitive_information_entity_type.serialize_json(
            value["type"]
        )
    )
    out["confidenceScore"] = (
        "NaN"
        if value["confidence_score"] != value["confidence_score"]
        else "Infinity"
        if value["confidence_score"] == float("inf")
        else "-Infinity"
        if value["confidence_score"] == float("-inf")
        else value["confidence_score"]
    )
    out["beginOffset"] = value["begin_offset"]
    out["endOffset"] = value["end_offset"]
    out["messageIndex"] = value["message_index"]
    out["contentIndex"] = value["content_index"]
    return out


def deserialize_json(data: dict) -> GuardrailChecksSensitiveInformationResultEntry:
    out: GuardrailChecksSensitiveInformationResultEntry = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_entity_type

        out["type"] = (
            capo_bedrock_runtime.types.guardrail_checks_sensitive_information_entity_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_runtime.types.guardrail_checks_sensitive_information_entity_type.GuardrailChecksSensitiveInformationEntityType",
            "",
        )
    if data.get("confidenceScore") is not None:
        out["confidence_score"] = float(data["confidenceScore"])
    else:
        out["confidence_score"] = 0.0
    if data.get("beginOffset") is not None:
        out["begin_offset"] = data["beginOffset"]
    else:
        out["begin_offset"] = 0
    if data.get("endOffset") is not None:
        out["end_offset"] = data["endOffset"]
    else:
        out["end_offset"] = 0
    if data.get("messageIndex") is not None:
        out["message_index"] = data["messageIndex"]
    else:
        out["message_index"] = 0
    if data.get("contentIndex") is not None:
        out["content_index"] = data["contentIndex"]
    else:
        out["content_index"] = 0
    return out
