"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InsightsFailureSignal``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.insights_failure_category


class InsightsFailureSignal(TypedDict, closed=True):
    category: (
        "capo_bedrock_agentcore.types.insights_failure_category.InsightsFailureCategory"
    )
    """<p>The failure category classification for this signal.</p>"""
    evidence: "str"
    """<p>The evidence supporting the failure detection.</p>"""
    confidence: "float"
    """<p>The confidence score of the failure detection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightsFailureSignal) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.insights_failure_category

    out["category"] = (
        capo_bedrock_agentcore.types.insights_failure_category.serialize_json(
            value["category"]
        )
    )
    out["evidence"] = value["evidence"]
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


def deserialize_json(data: dict) -> InsightsFailureSignal:
    out: InsightsFailureSignal = {}  # type: ignore[typeddict-item]
    if data.get("category") is not None:
        import capo_bedrock_agentcore.types.insights_failure_category

        out["category"] = (
            capo_bedrock_agentcore.types.insights_failure_category.deserialize_json(
                data["category"]
            )
        )
    else:
        import typing

        out["category"] = typing.cast(
            "capo_bedrock_agentcore.types.insights_failure_category.InsightsFailureCategory",
            "",
        )
    if data.get("evidence") is not None:
        out["evidence"] = data["evidence"]
    else:
        out["evidence"] = ""
    if data.get("confidence") is not None:
        out["confidence"] = float(data["confidence"])
    else:
        out["confidence"] = 0.0
    return out
