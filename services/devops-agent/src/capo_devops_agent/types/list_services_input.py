"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListServicesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.next_token
    import capo_devops_agent.types.service


class ListServicesInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>Maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["capo_devops_agent.types.next_token.NextToken"]
    """<p>Token for the next page of results.</p>"""
    filter_service_type: NotRequired["capo_devops_agent.types.service.Service"]
    """<p>Optional filter to list only services of a specific type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServicesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListServicesInput:
    out: ListServicesInput = {}  # type: ignore[typeddict-item]
    return out
