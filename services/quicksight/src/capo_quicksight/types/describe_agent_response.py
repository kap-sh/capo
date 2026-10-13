"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAgentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.agent


class DescribeAgentResponse(TypedDict, closed=True):
    agent: "capo_quicksight.types.agent.Agent"
    """<p>The full details of the agent, including its configuration, status, and associations.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAgentResponse) -> dict:
    out: dict = {}
    import capo_quicksight.types.agent

    out["Agent"] = capo_quicksight.types.agent.serialize_json(value["agent"])
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeAgentResponse:
    out: DescribeAgentResponse = {}  # type: ignore[typeddict-item]
    if data.get("Agent") is not None:
        import capo_quicksight.types.agent

        out["agent"] = capo_quicksight.types.agent.deserialize_json(data["Agent"])
    else:
        raise DeserializationError("DescribeAgentResponse.agent required")
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out


def redact_sensitive(value: DescribeAgentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "agent" in value:
        import capo_quicksight.types.agent

        out["agent"] = capo_quicksight.types.agent.redact_sensitive(value["agent"])
    return out
