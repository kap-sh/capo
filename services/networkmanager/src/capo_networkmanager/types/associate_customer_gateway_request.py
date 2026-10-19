"""Generated from Smithy shape ``com.amazonaws.networkmanager#AssociateCustomerGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.customer_gateway_arn
    import capo_networkmanager.types.device_id
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.link_id


class AssociateCustomerGatewayRequest(TypedDict, closed=True):
    customer_gateway_arn: (
        "capo_networkmanager.types.customer_gateway_arn.CustomerGatewayArn"
    )
    """<p>The Amazon Resource Name (ARN) of the customer gateway.</p>"""
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    device_id: "capo_networkmanager.types.device_id.DeviceId"
    """<p>The ID of the device.</p>"""
    link_id: NotRequired["capo_networkmanager.types.link_id.LinkId"]
    """<p>The ID of the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateCustomerGatewayRequest) -> dict:
    out: dict = {}
    out["CustomerGatewayArn"] = value["customer_gateway_arn"]
    out["DeviceId"] = value["device_id"]
    if "link_id" in value:
        out["LinkId"] = value["link_id"]
    return out


def deserialize_json(data: dict) -> AssociateCustomerGatewayRequest:
    out: AssociateCustomerGatewayRequest = {}  # type: ignore[typeddict-item]
    if data.get("CustomerGatewayArn") is not None:
        out["customer_gateway_arn"] = data["CustomerGatewayArn"]
    else:
        out["customer_gateway_arn"] = ""
    if data.get("DeviceId") is not None:
        out["device_id"] = data["DeviceId"]
    else:
        out["device_id"] = ""
    if data.get("LinkId") is not None:
        out["link_id"] = data["LinkId"]
    return out
