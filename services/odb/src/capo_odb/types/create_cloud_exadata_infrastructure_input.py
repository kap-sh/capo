"""Generated from Smithy shape ``com.amazonaws.odb#CreateCloudExadataInfrastructureInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.customer_contacts
    import capo_odb.types.general_input_string
    import capo_odb.types.maintenance_window
    import capo_odb.types.request_tag_map
    import capo_odb.types.resource_display_name


class CreateCloudExadataInfrastructureInput(TypedDict, closed=True):
    display_name: "capo_odb.types.resource_display_name.ResourceDisplayName"
    """<p>A user-friendly name for the Exadata infrastructure.</p>"""
    shape: "capo_odb.types.general_input_string.GeneralInputString"
    """<p>The model name of the Exadata infrastructure. For the list of valid model names, use the <code>ListDbSystemShapes</code> operation.</p>"""
    availability_zone: NotRequired["str"]
    """<p>The name of the Availability Zone (AZ) where the Exadata infrastructure is located.</p> <p>This operation requires that you specify a value for either <code>availabilityZone</code> or <code>availabilityZoneId</code>.</p> <p>Example: <code>us-east-1a</code> </p>"""
    availability_zone_id: NotRequired["str"]
    """<p>The AZ ID of the AZ where the Exadata infrastructure is located.</p> <p>This operation requires that you specify a value for either <code>availabilityZone</code> or <code>availabilityZoneId</code>.</p> <p>Example: <code>use1-az1</code> </p>"""
    tags: NotRequired["capo_odb.types.request_tag_map.RequestTagMap"]
    """<p>The list of resource tags to apply to the Exadata infrastructure.</p>"""
    compute_count: "int"
    """<p>The number of database servers for the Exadata infrastructure. Valid values for this parameter depend on the shape. To get information about the minimum and maximum values, use the <code>ListDbSystemShapes</code> operation.</p>"""
    customer_contacts_to_send_to_oci: NotRequired[
        "capo_odb.types.customer_contacts.CustomerContacts"
    ]
    """<p>The email addresses of contacts to receive notification from Oracle about maintenance updates for the Exadata infrastructure.</p>"""
    maintenance_window: NotRequired[
        "capo_odb.types.maintenance_window.MaintenanceWindow"
    ]
    """<p>The maintenance window configuration for the Exadata Cloud infrastructure.</p> <p>This allows you to define when maintenance operations such as patching and updates can be performed on the infrastructure.</p>"""
    storage_count: "int"
    """<p>The number of storage servers to activate for this Exadata infrastructure. Valid values for this parameter depend on the shape. To get information about the minimum and maximum values, use the <code>ListDbSystemShapes</code> operation.</p>"""
    client_token: NotRequired["capo_odb.types.general_input_string.GeneralInputString"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. The client token is valid for up to 24 hours after it's first used.</p>"""
    database_server_type: NotRequired[
        "capo_odb.types.general_input_string.GeneralInputString"
    ]
    """<p>The database server model type of the Exadata infrastructure. For the list of valid model names, use the <code>ListDbSystemShapes</code> operation.</p>"""
    storage_server_type: NotRequired[
        "capo_odb.types.general_input_string.GeneralInputString"
    ]
    """<p>The storage server model type of the Exadata infrastructure. For the list of valid model names, use the <code>ListDbSystemShapes</code> operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateCloudExadataInfrastructureInput) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    out["shape"] = value["shape"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    if "tags" in value:
        import capo_odb.types.request_tag_map

        out["tags"] = capo_odb.types.request_tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    out["computeCount"] = value["compute_count"]
    if "customer_contacts_to_send_to_oci" in value:
        import capo_odb.types.customer_contacts

        out["customerContactsToSendToOCI"] = (
            capo_odb.types.customer_contacts.serialize_aws_json_1_0(
                value["customer_contacts_to_send_to_oci"]
            )
        )
    if "maintenance_window" in value:
        import capo_odb.types.maintenance_window

        out["maintenanceWindow"] = (
            capo_odb.types.maintenance_window.serialize_aws_json_1_0(
                value["maintenance_window"]
            )
        )
    out["storageCount"] = value["storage_count"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "database_server_type" in value:
        out["databaseServerType"] = value["database_server_type"]
    if "storage_server_type" in value:
        out["storageServerType"] = value["storage_server_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateCloudExadataInfrastructureInput:
    out: CreateCloudExadataInfrastructureInput = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("shape") is not None:
        out["shape"] = data["shape"]
    else:
        out["shape"] = ""
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    if data.get("availabilityZoneId") is not None:
        out["availability_zone_id"] = data["availabilityZoneId"]
    if data.get("tags") is not None:
        import capo_odb.types.request_tag_map

        out["tags"] = capo_odb.types.request_tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    if data.get("computeCount") is not None:
        out["compute_count"] = data["computeCount"]
    else:
        out["compute_count"] = 0
    if data.get("customerContactsToSendToOCI") is not None:
        import capo_odb.types.customer_contacts

        out["customer_contacts_to_send_to_oci"] = (
            capo_odb.types.customer_contacts.deserialize_aws_json_1_0(
                data["customerContactsToSendToOCI"]
            )
        )
    if data.get("maintenanceWindow") is not None:
        import capo_odb.types.maintenance_window

        out["maintenance_window"] = (
            capo_odb.types.maintenance_window.deserialize_aws_json_1_0(
                data["maintenanceWindow"]
            )
        )
    if data.get("storageCount") is not None:
        out["storage_count"] = data["storageCount"]
    else:
        out["storage_count"] = 0
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("databaseServerType") is not None:
        out["database_server_type"] = data["databaseServerType"]
    if data.get("storageServerType") is not None:
        out["storage_server_type"] = data["storageServerType"]
    return out


def redact_sensitive(value: CreateCloudExadataInfrastructureInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customer_contacts_to_send_to_oci" in value:
        import capo_odb.types.customer_contacts

        out["customer_contacts_to_send_to_oci"] = (
            capo_odb.types.customer_contacts.redact_sensitive(
                value["customer_contacts_to_send_to_oci"]
            )
        )
    return out
