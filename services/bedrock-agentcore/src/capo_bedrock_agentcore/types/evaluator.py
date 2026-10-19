"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Evaluator``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.evaluator_id


class Evaluator(TypedDict, closed=True):
    evaluator_id: "capo_bedrock_agentcore.types.evaluator_id.EvaluatorId"
    """<p>The unique identifier of the evaluator. Can reference built-in evaluators (e.g., <code>Builtin.Helpfulness</code>) or custom evaluators.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Evaluator) -> dict:
    out: dict = {}
    out["evaluatorId"] = value["evaluator_id"]
    return out


def deserialize_json(data: dict) -> Evaluator:
    out: Evaluator = {}  # type: ignore[typeddict-item]
    if data.get("evaluatorId") is not None:
        out["evaluator_id"] = data["evaluatorId"]
    else:
        out["evaluator_id"] = ""
    return out
