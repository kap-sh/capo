"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DuplicateConditionExpressionFlowValidationDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_condition_expression
    import capo_bedrock_agent.types.flow_node_name


class DuplicateConditionExpressionFlowValidationDetails(TypedDict, closed=True):
    node: "capo_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The name of the node containing the duplicate condition expressions.</p>"""
    expression: (
        "capo_bedrock_agent.types.flow_condition_expression.FlowConditionExpression"
    )
    """<p>The duplicated condition expression.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DuplicateConditionExpressionFlowValidationDetails) -> dict:
    out: dict = {}
    out["node"] = value["node"]
    out["expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> DuplicateConditionExpressionFlowValidationDetails:
    out: DuplicateConditionExpressionFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if data.get("node") is not None:
        out["node"] = data["node"]
    else:
        out["node"] = ""
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    else:
        out["expression"] = ""
    return out


def redact_sensitive(
    value: DuplicateConditionExpressionFlowValidationDetails,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    return out
