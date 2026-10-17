"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListAgentSpacesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.next_token


class ListAgentSpacesInput(TypedDict, closed=True):
    max_results: "int"
    """<p>Maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["capo_devops_agent.types.next_token.NextToken"]
    """<p>Token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentSpacesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAgentSpacesInput:
    out: ListAgentSpacesInput = {}  # type: ignore[typeddict-item]
    return out
