"""Generated from Smithy shape ``com.amazonaws.supplychain#ListDataIntegrationFlowExecutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_flow_execution_list
    import capo_supplychain.types.data_integration_flow_execution_next_token


class ListDataIntegrationFlowExecutionsResponse(TypedDict, closed=True):
    flow_executions: "capo_supplychain.types.data_integration_flow_execution_list.DataIntegrationFlowExecutionList"
    """<p>The list of flow executions.</p>"""
    next_token: NotRequired[
        "capo_supplychain.types.data_integration_flow_execution_next_token.DataIntegrationFlowExecutionNextToken"
    ]
    """<p>The pagination token to fetch next page of flow executions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataIntegrationFlowExecutionsResponse) -> dict:
    out: dict = {}
    import capo_supplychain.types.data_integration_flow_execution_list

    out["flowExecutions"] = (
        capo_supplychain.types.data_integration_flow_execution_list.serialize_json(
            value["flow_executions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataIntegrationFlowExecutionsResponse:
    out: ListDataIntegrationFlowExecutionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("flowExecutions") is not None:
        import capo_supplychain.types.data_integration_flow_execution_list

        out["flow_executions"] = (
            capo_supplychain.types.data_integration_flow_execution_list.deserialize_json(
                data["flowExecutions"]
            )
        )
    else:
        out["flow_executions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
