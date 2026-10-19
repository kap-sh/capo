"""Generated from Smithy shape ``com.amazonaws.iotwireless#CreateWirelessGatewayTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.wireless_gateway_id
    import capo_iot_wireless.types.wireless_gateway_task_definition_id


class CreateWirelessGatewayTaskRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.wireless_gateway_id.WirelessGatewayId"
    """<p>The ID of the resource to update.</p>"""
    wireless_gateway_task_definition_id: "capo_iot_wireless.types.wireless_gateway_task_definition_id.WirelessGatewayTaskDefinitionId"
    """<p>The ID of the WirelessGatewayTaskDefinition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWirelessGatewayTaskRequest) -> dict:
    out: dict = {}
    out["WirelessGatewayTaskDefinitionId"] = value[
        "wireless_gateway_task_definition_id"
    ]
    return out


def deserialize_json(data: dict) -> CreateWirelessGatewayTaskRequest:
    out: CreateWirelessGatewayTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("WirelessGatewayTaskDefinitionId") is not None:
        out["wireless_gateway_task_definition_id"] = data[
            "WirelessGatewayTaskDefinitionId"
        ]
    else:
        out["wireless_gateway_task_definition_id"] = ""
    return out
