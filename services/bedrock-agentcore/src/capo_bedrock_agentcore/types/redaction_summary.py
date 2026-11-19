"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RedactionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.finding_count_map


class RedactionSummary(TypedDict, closed=True):
    scenarios_scanned: NotRequired["int"]
    """<p>The number of scenarios scanned for sensitive data.</p>"""
    finding_counts: NotRequired[
        "capo_bedrock_agentcore.types.finding_count_map.FindingCountMap"
    ]
    """<p>The number of matches for each data identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedactionSummary) -> dict:
    out: dict = {}
    if "scenarios_scanned" in value:
        out["scenariosScanned"] = value["scenarios_scanned"]
    if "finding_counts" in value:
        import capo_bedrock_agentcore.types.finding_count_map

        out["findingCounts"] = (
            capo_bedrock_agentcore.types.finding_count_map.serialize_json(
                value["finding_counts"]
            )
        )
    return out


def deserialize_json(data: dict) -> RedactionSummary:
    out: RedactionSummary = {}  # type: ignore[typeddict-item]
    if data.get("scenariosScanned") is not None:
        out["scenarios_scanned"] = data["scenariosScanned"]
    if data.get("findingCounts") is not None:
        import capo_bedrock_agentcore.types.finding_count_map

        out["finding_counts"] = (
            capo_bedrock_agentcore.types.finding_count_map.deserialize_json(
                data["findingCounts"]
            )
        )
    return out
