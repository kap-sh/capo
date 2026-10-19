"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.statement


class PolicyStatement(TypedDict, closed=True):
    statement: "capo_bedrock_agentcore_control.types.statement.Statement"
    """<p>The body of the AgentCore Cedar or Dogwood policy statement. Contains the policy logic, which can be a Cedar policy, a temporal policy, or a guardrails definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyStatement) -> dict:
    out: dict = {}
    out["statement"] = value["statement"]
    return out


def deserialize_json(data: dict) -> PolicyStatement:
    out: PolicyStatement = {}  # type: ignore[typeddict-item]
    if data.get("statement") is not None:
        out["statement"] = data["statement"]
    else:
        out["statement"] = ""
    return out
