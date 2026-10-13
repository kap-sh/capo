"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetDestinationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.delivery_destination_arn
    import capo_iot_managed_integrations.types.delivery_destination_role_arn
    import capo_iot_managed_integrations.types.delivery_destination_type
    import capo_iot_managed_integrations.types.destination_created_at
    import capo_iot_managed_integrations.types.destination_description
    import capo_iot_managed_integrations.types.destination_name
    import capo_iot_managed_integrations.types.destination_updated_at
    import capo_iot_managed_integrations.types.tags_map


class GetDestinationResponse(TypedDict, closed=True):
    description: NotRequired[
        "capo_iot_managed_integrations.types.destination_description.DestinationDescription"
    ]
    """<p>The description of the customer-managed destination.</p>"""
    delivery_destination_arn: NotRequired[
        "capo_iot_managed_integrations.types.delivery_destination_arn.DeliveryDestinationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the customer-managed destination.</p>"""
    delivery_destination_type: NotRequired[
        "capo_iot_managed_integrations.types.delivery_destination_type.DeliveryDestinationType"
    ]
    """<p>The destination type for the customer-managed destination.</p>"""
    name: NotRequired[
        "capo_iot_managed_integrations.types.destination_name.DestinationName"
    ]
    """<p>The name of the customer-managed destination.</p>"""
    role_arn: NotRequired[
        "capo_iot_managed_integrations.types.delivery_destination_role_arn.DeliveryDestinationRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the delivery destination role.</p>"""
    created_at: NotRequired[
        "capo_iot_managed_integrations.types.destination_created_at.DestinationCreatedAt"
    ]
    """<p>The timestamp value of when the destination creation requset occurred.</p>"""
    updated_at: NotRequired[
        "capo_iot_managed_integrations.types.destination_updated_at.DestinationUpdatedAt"
    ]
    """<p>The timestamp value of when the destination update requset occurred.</p>"""
    tags: NotRequired["capo_iot_managed_integrations.types.tags_map.TagsMap"]
    """<p>A set of key/value pairs that are used to manage the customer-managed destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDestinationResponse) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "delivery_destination_arn" in value:
        out["DeliveryDestinationArn"] = value["delivery_destination_arn"]
    if "delivery_destination_type" in value:
        import capo_iot_managed_integrations.types.delivery_destination_type

        out["DeliveryDestinationType"] = (
            capo_iot_managed_integrations.types.delivery_destination_type.serialize_json(
                value["delivery_destination_type"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "created_at" in value:
        import capo_iot_managed_integrations.types.destination_created_at

        out["CreatedAt"] = (
            capo_iot_managed_integrations.types.destination_created_at.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import capo_iot_managed_integrations.types.destination_updated_at

        out["UpdatedAt"] = (
            capo_iot_managed_integrations.types.destination_updated_at.serialize_json(
                value["updated_at"]
            )
        )
    if "tags" in value:
        import capo_iot_managed_integrations.types.tags_map

        out["Tags"] = capo_iot_managed_integrations.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetDestinationResponse:
    out: GetDestinationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DeliveryDestinationArn") is not None:
        out["delivery_destination_arn"] = data["DeliveryDestinationArn"]
    if data.get("DeliveryDestinationType") is not None:
        import capo_iot_managed_integrations.types.delivery_destination_type

        out["delivery_destination_type"] = (
            capo_iot_managed_integrations.types.delivery_destination_type.deserialize_json(
                data["DeliveryDestinationType"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("CreatedAt") is not None:
        import capo_iot_managed_integrations.types.destination_created_at

        out["created_at"] = (
            capo_iot_managed_integrations.types.destination_created_at.deserialize_json(
                data["CreatedAt"]
            )
        )
    if data.get("UpdatedAt") is not None:
        import capo_iot_managed_integrations.types.destination_updated_at

        out["updated_at"] = (
            capo_iot_managed_integrations.types.destination_updated_at.deserialize_json(
                data["UpdatedAt"]
            )
        )
    if data.get("Tags") is not None:
        import capo_iot_managed_integrations.types.tags_map

        out["tags"] = capo_iot_managed_integrations.types.tags_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: GetDestinationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
