"""Generated from Smithy shape ``com.amazonaws.supplychain#ListDataIntegrationFlowsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_flow_list
    import capo_supplychain.types.data_integration_flow_next_token


class ListDataIntegrationFlowsResponse(TypedDict, closed=True):
    flows: "capo_supplychain.types.data_integration_flow_list.DataIntegrationFlowList"
    """<p>The response parameters for ListDataIntegrationFlows.</p>"""
    next_token: NotRequired[
        "capo_supplychain.types.data_integration_flow_next_token.DataIntegrationFlowNextToken"
    ]
    """<p>The pagination token to fetch the next page of the DataIntegrationFlows.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataIntegrationFlowsResponse) -> dict:
    out: dict = {}
    import capo_supplychain.types.data_integration_flow_list

    out["flows"] = capo_supplychain.types.data_integration_flow_list.serialize_json(
        value["flows"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataIntegrationFlowsResponse:
    out: ListDataIntegrationFlowsResponse = {}  # type: ignore[typeddict-item]
    if data.get("flows") is not None:
        import capo_supplychain.types.data_integration_flow_list

        out["flows"] = (
            capo_supplychain.types.data_integration_flow_list.deserialize_json(
                data["flows"]
            )
        )
    else:
        out["flows"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListDataIntegrationFlowsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "flows" in value:
        import capo_supplychain.types.data_integration_flow_list

        out["flows"] = (
            capo_supplychain.types.data_integration_flow_list.redact_sensitive(
                value["flows"]
            )
        )
    return out
