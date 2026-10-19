"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Insight``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.insight_id


class Insight(TypedDict, closed=True):
    insight_id: "capo_bedrock_agentcore.types.insight_id.InsightId"
    """<p>The unique identifier of the insight to run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Insight) -> dict:
    out: dict = {}
    out["insightId"] = value["insight_id"]
    return out


def deserialize_json(data: dict) -> Insight:
    out: Insight = {}  # type: ignore[typeddict-item]
    if data.get("insightId") is not None:
        out["insight_id"] = data["insightId"]
    else:
        out["insight_id"] = ""
    return out
