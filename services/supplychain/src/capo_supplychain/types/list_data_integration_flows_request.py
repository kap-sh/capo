"""Generated from Smithy shape ``com.amazonaws.supplychain#ListDataIntegrationFlowsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_flow_max_results
    import capo_supplychain.types.data_integration_flow_next_token
    import capo_supplychain.types.uuid


class ListDataIntegrationFlowsRequest(TypedDict, closed=True):
    instance_id: "capo_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Supply Chain instance identifier.</p>"""
    next_token: NotRequired[
        "capo_supplychain.types.data_integration_flow_next_token.DataIntegrationFlowNextToken"
    ]
    """<p>The pagination token to fetch the next page of the DataIntegrationFlows.</p>"""
    max_results: NotRequired[
        "capo_supplychain.types.data_integration_flow_max_results.DataIntegrationFlowMaxResults"
    ]
    """<p>Specify the maximum number of DataIntegrationFlows to fetch in one paginated request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataIntegrationFlowsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataIntegrationFlowsRequest:
    out: ListDataIntegrationFlowsRequest = {}  # type: ignore[typeddict-item]
    return out
