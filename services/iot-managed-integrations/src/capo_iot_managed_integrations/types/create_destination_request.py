"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateDestinationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.client_token
    import capo_iot_managed_integrations.types.delivery_destination_arn
    import capo_iot_managed_integrations.types.delivery_destination_role_arn
    import capo_iot_managed_integrations.types.delivery_destination_type
    import capo_iot_managed_integrations.types.destination_description
    import capo_iot_managed_integrations.types.destination_name
    import capo_iot_managed_integrations.types.tags_map


class CreateDestinationRequest(TypedDict, closed=True):
    delivery_destination_arn: "capo_iot_managed_integrations.types.delivery_destination_arn.DeliveryDestinationArn"
    """<p>The Amazon Resource Name (ARN) of the customer-managed destination.</p>"""
    delivery_destination_type: "capo_iot_managed_integrations.types.delivery_destination_type.DeliveryDestinationType"
    """<p>The destination type for the customer-managed destination.</p>"""
    name: "capo_iot_managed_integrations.types.destination_name.DestinationName"
    """<p>The name of the customer-managed destination.</p>"""
    role_arn: "capo_iot_managed_integrations.types.delivery_destination_role_arn.DeliveryDestinationRoleArn"
    """<p>The Amazon Resource Name (ARN) of the delivery destination role.</p>"""
    client_token: NotRequired[
        "capo_iot_managed_integrations.types.client_token.ClientToken"
    ]
    """<p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>"""
    description: NotRequired[
        "capo_iot_managed_integrations.types.destination_description.DestinationDescription"
    ]
    """<p>The description of the customer-managed destination.</p>"""
    tags: NotRequired["capo_iot_managed_integrations.types.tags_map.TagsMap"]
    """<p>A set of key/value pairs that are used to manage the destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDestinationRequest) -> dict:
    out: dict = {}
    out["DeliveryDestinationArn"] = value["delivery_destination_arn"]
    import capo_iot_managed_integrations.types.delivery_destination_type

    out["DeliveryDestinationType"] = (
        capo_iot_managed_integrations.types.delivery_destination_type.serialize_json(
            value["delivery_destination_type"]
        )
    )
    out["Name"] = value["name"]
    out["RoleArn"] = value["role_arn"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_iot_managed_integrations.types.tags_map

        out["Tags"] = capo_iot_managed_integrations.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateDestinationRequest:
    out: CreateDestinationRequest = {}  # type: ignore[typeddict-item]
    if data.get("DeliveryDestinationArn") is not None:
        out["delivery_destination_arn"] = data["DeliveryDestinationArn"]
    else:
        out["delivery_destination_arn"] = ""
    if data.get("DeliveryDestinationType") is not None:
        import capo_iot_managed_integrations.types.delivery_destination_type

        out["delivery_destination_type"] = (
            capo_iot_managed_integrations.types.delivery_destination_type.deserialize_json(
                data["DeliveryDestinationType"]
            )
        )
    else:
        import typing

        out["delivery_destination_type"] = typing.cast(
            "capo_iot_managed_integrations.types.delivery_destination_type.DeliveryDestinationType",
            "",
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_iot_managed_integrations.types.tags_map

        out["tags"] = capo_iot_managed_integrations.types.tags_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: CreateDestinationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
