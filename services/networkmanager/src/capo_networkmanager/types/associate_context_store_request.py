"""Generated from Smithy shape ``com.amazonaws.networkmanager#AssociateContextStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.context_store_id
    import capo_networkmanager.types.transit_gateway_arn


class AssociateContextStoreRequest(TypedDict, closed=True):
    context_store_id: "capo_networkmanager.types.context_store_id.ContextStoreId"
    """<p>The ID of the context store.</p>"""
    transit_gateway_arn: NotRequired[
        "capo_networkmanager.types.transit_gateway_arn.TransitGatewayArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the transit gateway to associate with the context store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateContextStoreRequest) -> dict:
    out: dict = {}
    if "transit_gateway_arn" in value:
        out["TransitGatewayArn"] = value["transit_gateway_arn"]
    return out


def deserialize_json(data: dict) -> AssociateContextStoreRequest:
    out: AssociateContextStoreRequest = {}  # type: ignore[typeddict-item]
    if data.get("TransitGatewayArn") is not None:
        out["transit_gateway_arn"] = data["TransitGatewayArn"]
    return out
