"""Generated from Smithy shape ``com.amazonaws.supplychain#ListDataIntegrationFlowExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_flow_execution_max_results
    import capo_supplychain.types.data_integration_flow_execution_next_token
    import capo_supplychain.types.data_integration_flow_name
    import capo_supplychain.types.uuid


class ListDataIntegrationFlowExecutionsRequest(TypedDict, closed=True):
    instance_id: "capo_supplychain.types.uuid.UUID"
    """<p>The AWS Supply Chain instance identifier.</p>"""
    flow_name: (
        "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName"
    )
    """<p>The flow name.</p>"""
    next_token: NotRequired[
        "capo_supplychain.types.data_integration_flow_execution_next_token.DataIntegrationFlowExecutionNextToken"
    ]
    """<p>The pagination token to fetch next page of flow executions.</p>"""
    max_results: NotRequired[
        "capo_supplychain.types.data_integration_flow_execution_max_results.DataIntegrationFlowExecutionMaxResults"
    ]
    """<p>The number to specify the max number of flow executions to fetch in this paginated request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataIntegrationFlowExecutionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataIntegrationFlowExecutionsRequest:
    out: ListDataIntegrationFlowExecutionsRequest = {}  # type: ignore[typeddict-item]
    return out
