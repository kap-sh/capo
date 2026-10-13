"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_flow

DataIntegrationFlowList: TypeAlias = list[
    "capo_supplychain.types.data_integration_flow.DataIntegrationFlow"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowList) -> list:
    import capo_supplychain.types.data_integration_flow

    out: list = []
    for item in value:
        out.append(capo_supplychain.types.data_integration_flow.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataIntegrationFlowList:
    import capo_supplychain.types.data_integration_flow

    out: DataIntegrationFlowList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_supplychain.types.data_integration_flow.deserialize_json(item))
    return out


def redact_sensitive(value: DataIntegrationFlowList) -> list[Any]:
    import capo_supplychain.types.data_integration_flow

    return [
        capo_supplychain.types.data_integration_flow.redact_sensitive(item)
        for item in value
    ]
