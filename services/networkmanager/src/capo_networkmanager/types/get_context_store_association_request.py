"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetContextStoreAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.context_store_id
    import capo_networkmanager.types.transit_gateway_arn


class GetContextStoreAssociationRequest(TypedDict, closed=True):
    context_store_id: "capo_networkmanager.types.context_store_id.ContextStoreId"
    """<p>The ID of the context store.</p>"""
    transit_gateway_arn: (
        "capo_networkmanager.types.transit_gateway_arn.TransitGatewayArn"
    )
    """<p>The Amazon Resource Name (ARN) of the transit gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContextStoreAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetContextStoreAssociationRequest:
    out: GetContextStoreAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
