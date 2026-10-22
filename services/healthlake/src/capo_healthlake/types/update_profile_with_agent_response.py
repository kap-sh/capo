"""Generated from Smithy shape ``com.amazonaws.healthlake#UpdateProfileWithAgentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.agent_output_message_stream


class UpdateProfileWithAgentResponse(TypedDict, closed=True):
    agent_response: (
        "capo_healthlake.types.agent_output_message_stream.AgentOutputMessageStream"
    )
    """<p>The streaming response from the agent.</p>"""


def redact_sensitive(value: UpdateProfileWithAgentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "agent_response" in value:
        out["agent_response"] = "*** Streaming Data Redacted ***"
    return out
