"""Generated from Smithy shape ``com.amazonaws.supplychain#GetDataIntegrationFlowResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_flow


class GetDataIntegrationFlowResponse(TypedDict, closed=True):
    flow: "capo_supplychain.types.data_integration_flow.DataIntegrationFlow"
    """<p>The details of the DataIntegrationFlow returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataIntegrationFlowResponse) -> dict:
    out: dict = {}
    import capo_supplychain.types.data_integration_flow

    out["flow"] = capo_supplychain.types.data_integration_flow.serialize_json(
        value["flow"]
    )
    return out


def deserialize_json(data: dict) -> GetDataIntegrationFlowResponse:
    out: GetDataIntegrationFlowResponse = {}  # type: ignore[typeddict-item]
    if data.get("flow") is not None:
        import capo_supplychain.types.data_integration_flow

        out["flow"] = capo_supplychain.types.data_integration_flow.deserialize_json(
            data["flow"]
        )
    else:
        raise DeserializationError("GetDataIntegrationFlowResponse.flow required")
    return out


def redact_sensitive(value: GetDataIntegrationFlowResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "flow" in value:
        import capo_supplychain.types.data_integration_flow

        out["flow"] = capo_supplychain.types.data_integration_flow.redact_sensitive(
            value["flow"]
        )
    return out
