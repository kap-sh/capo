"""Generated from Smithy shape ``com.amazonaws.networkmanager#ContextStoreAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.context_store_association_state
    import capo_networkmanager.types.context_store_id
    import capo_networkmanager.types.date_time
    import capo_networkmanager.types.transit_gateway_arn


class ContextStoreAssociation(TypedDict, closed=True):
    context_store_id: NotRequired[
        "capo_networkmanager.types.context_store_id.ContextStoreId"
    ]
    """<p>The ID of the context store.</p>"""
    transit_gateway_arn: NotRequired[
        "capo_networkmanager.types.transit_gateway_arn.TransitGatewayArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the transit gateway.</p>"""
    created_at: NotRequired["capo_networkmanager.types.date_time.DateTime"]
    """<p>The date and time that the association was created.</p>"""
    state: NotRequired[
        "capo_networkmanager.types.context_store_association_state.ContextStoreAssociationState"
    ]
    """<p>The state of the association. The possible values are the following:</p> <ul> <li> <p> <code>ASSOCIATING</code>: The transit gateway is being associated with the context store.</p> </li> <li> <p> <code>ASSOCIATED</code>: The transit gateway is associated with the context store.</p> </li> <li> <p> <code>DISASSOCIATING</code>: The transit gateway is being disassociated from the context store.</p> </li> <li> <p> <code>FAILED</code>: The association failed. To remove it, disassociate the transit gateway.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContextStoreAssociation) -> dict:
    out: dict = {}
    if "context_store_id" in value:
        out["ContextStoreId"] = value["context_store_id"]
    if "transit_gateway_arn" in value:
        out["TransitGatewayArn"] = value["transit_gateway_arn"]
    if "created_at" in value:
        import capo_networkmanager.types.date_time

        out["CreatedAt"] = capo_networkmanager.types.date_time.serialize_json(
            value["created_at"]
        )
    if "state" in value:
        import capo_networkmanager.types.context_store_association_state

        out["State"] = (
            capo_networkmanager.types.context_store_association_state.serialize_json(
                value["state"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContextStoreAssociation:
    out: ContextStoreAssociation = {}  # type: ignore[typeddict-item]
    if data.get("ContextStoreId") is not None:
        out["context_store_id"] = data["ContextStoreId"]
    if data.get("TransitGatewayArn") is not None:
        out["transit_gateway_arn"] = data["TransitGatewayArn"]
    if data.get("CreatedAt") is not None:
        import capo_networkmanager.types.date_time

        out["created_at"] = capo_networkmanager.types.date_time.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("State") is not None:
        import capo_networkmanager.types.context_store_association_state

        out["state"] = (
            capo_networkmanager.types.context_store_association_state.deserialize_json(
                data["State"]
            )
        )
    return out
