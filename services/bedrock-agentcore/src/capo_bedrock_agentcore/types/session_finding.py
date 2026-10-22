"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SessionFinding``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.finding_description
    import capo_bedrock_agentcore.types.finding_target_id
    import capo_bedrock_agentcore.types.finding_target_type


class SessionFinding(TypedDict, closed=True):
    target_id: NotRequired[
        "capo_bedrock_agentcore.types.finding_target_id.FindingTargetId"
    ]
    """<p>The identifier or name of the location in the session where the failure was found, interpreted according to <code>targetType</code>.</p>"""
    target_type: NotRequired[
        "capo_bedrock_agentcore.types.finding_target_type.FindingTargetType"
    ]
    """<p>The type of location that <code>targetId</code> refers to.</p>"""
    description: "capo_bedrock_agentcore.types.finding_description.FindingDescription"
    """<p>A description of the failure.</p>"""
    category: NotRequired["str"]
    """<p>The category of the failure.</p>"""
    confidence: NotRequired["float"]
    """<p>The confidence that the finding is a failure, from 0 to 1.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionFinding) -> dict:
    out: dict = {}
    if "target_id" in value:
        out["targetId"] = value["target_id"]
    if "target_type" in value:
        import capo_bedrock_agentcore.types.finding_target_type

        out["targetType"] = (
            capo_bedrock_agentcore.types.finding_target_type.serialize_json(
                value["target_type"]
            )
        )
    out["description"] = value["description"]
    if "category" in value:
        out["category"] = value["category"]
    if "confidence" in value:
        out["confidence"] = (
            "NaN"
            if value["confidence"] != value["confidence"]
            else "Infinity"
            if value["confidence"] == float("inf")
            else "-Infinity"
            if value["confidence"] == float("-inf")
            else value["confidence"]
        )
    return out


def deserialize_json(data: dict) -> SessionFinding:
    out: SessionFinding = {}  # type: ignore[typeddict-item]
    if data.get("targetId") is not None:
        out["target_id"] = data["targetId"]
    if data.get("targetType") is not None:
        import capo_bedrock_agentcore.types.finding_target_type

        out["target_type"] = (
            capo_bedrock_agentcore.types.finding_target_type.deserialize_json(
                data["targetType"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("category") is not None:
        out["category"] = data["category"]
    if data.get("confidence") is not None:
        out["confidence"] = float(data["confidence"])
    return out


def redact_sensitive(value: SessionFinding) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
