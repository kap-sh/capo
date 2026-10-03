"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ManagedThingSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.advertised_product_id
    import capo_iot_managed_integrations.types.brand
    import capo_iot_managed_integrations.types.classification
    import capo_iot_managed_integrations.types.connector_destination_id
    import capo_iot_managed_integrations.types.connector_device_id
    import capo_iot_managed_integrations.types.connector_policy_id
    import capo_iot_managed_integrations.types.created_at
    import capo_iot_managed_integrations.types.credential_locker_id
    import capo_iot_managed_integrations.types.managed_thing_arn
    import capo_iot_managed_integrations.types.managed_thing_id
    import capo_iot_managed_integrations.types.model
    import capo_iot_managed_integrations.types.name
    import capo_iot_managed_integrations.types.owner
    import capo_iot_managed_integrations.types.parent_controller_id
    import capo_iot_managed_integrations.types.provisioning_status
    import capo_iot_managed_integrations.types.role
    import capo_iot_managed_integrations.types.serial_number
    import capo_iot_managed_integrations.types.setup_at


class ManagedThingSummary(TypedDict, closed=True):
    id: NotRequired[
        "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    ]
    """<p>The id of the device.</p>"""
    arn: NotRequired[
        "capo_iot_managed_integrations.types.managed_thing_arn.ManagedThingArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the managed thing.</p>"""
    advertised_product_id: NotRequired[
        "capo_iot_managed_integrations.types.advertised_product_id.AdvertisedProductId"
    ]
    """<p>The id of the advertised product.</p>"""
    brand: NotRequired["capo_iot_managed_integrations.types.brand.Brand"]
    """<p>The brand of the device.</p>"""
    classification: NotRequired[
        "capo_iot_managed_integrations.types.classification.Classification"
    ]
    """<p>The classification of the managed thing such as light bulb or thermostat.</p>"""
    connector_device_id: NotRequired[
        "capo_iot_managed_integrations.types.connector_device_id.ConnectorDeviceId"
    ]
    """<p>The third-party device id as defined by the connector. This device id must not contain personal identifiable information (PII).</p> <note> <p>This parameter is used for cloud-to-cloud devices only.</p> </note>"""
    connector_policy_id: NotRequired[
        "capo_iot_managed_integrations.types.connector_policy_id.ConnectorPolicyId"
    ]
    """<p>The id of the connector policy.</p> <note> <p>This parameter is used for cloud-to-cloud devices only.</p> </note>"""
    connector_destination_id: NotRequired[
        "capo_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
    ]
    """<p>The identifier of the connector destination associated with this managed thing, if applicable.</p>"""
    model: NotRequired["capo_iot_managed_integrations.types.model.Model"]
    """<p>The model of the device.</p>"""
    name: NotRequired["capo_iot_managed_integrations.types.name.Name"]
    """<p>The name of the managed thing representing the physical device.</p>"""
    owner: NotRequired["capo_iot_managed_integrations.types.owner.Owner"]
    """<p>Owner of the device, usually an indication of whom the device belongs to. This value should not contain personal identifiable information.</p>"""
    credential_locker_id: NotRequired[
        "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
    ]
    """<p>The identifier of the credential locker for the managed thing.</p>"""
    parent_controller_id: NotRequired[
        "capo_iot_managed_integrations.types.parent_controller_id.ParentControllerId"
    ]
    """<p>Id of the controller device used for the discovery job.</p>"""
    provisioning_status: NotRequired[
        "capo_iot_managed_integrations.types.provisioning_status.ProvisioningStatus"
    ]
    """<p>The provisioning status of the device in the provisioning workflow for onboarding to IoT managed integrations. For more information, see <a href="https://docs.aws.amazon.com/iot-mi/latest/devguide/device-provisioning.html">Device Provisioning</a>.</p>"""
    role: NotRequired["capo_iot_managed_integrations.types.role.Role"]
    """<p>The type of device used. This will be the Amazon Web Services hub controller, cloud device, or IoT device.</p>"""
    serial_number: NotRequired[
        "capo_iot_managed_integrations.types.serial_number.SerialNumber"
    ]
    """<p>The serial number of the device.</p>"""
    created_at: NotRequired["capo_iot_managed_integrations.types.created_at.CreatedAt"]
    """<p>The timestamp value of when the device creation request occurred.</p>"""
    updated_at: NotRequired["capo_iot_managed_integrations.types.created_at.CreatedAt"]
    """<p>The timestamp value of when the managed thing was last updated at.</p>"""
    activated_at: NotRequired["capo_iot_managed_integrations.types.setup_at.SetupAt"]
    """<p>The timestampe value of when the managed thing was activated at.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedThingSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "advertised_product_id" in value:
        out["AdvertisedProductId"] = value["advertised_product_id"]
    if "brand" in value:
        out["Brand"] = value["brand"]
    if "classification" in value:
        out["Classification"] = value["classification"]
    if "connector_device_id" in value:
        out["ConnectorDeviceId"] = value["connector_device_id"]
    if "connector_policy_id" in value:
        out["ConnectorPolicyId"] = value["connector_policy_id"]
    if "connector_destination_id" in value:
        out["ConnectorDestinationId"] = value["connector_destination_id"]
    if "model" in value:
        out["Model"] = value["model"]
    if "name" in value:
        out["Name"] = value["name"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "credential_locker_id" in value:
        out["CredentialLockerId"] = value["credential_locker_id"]
    if "parent_controller_id" in value:
        out["ParentControllerId"] = value["parent_controller_id"]
    if "provisioning_status" in value:
        import capo_iot_managed_integrations.types.provisioning_status

        out["ProvisioningStatus"] = (
            capo_iot_managed_integrations.types.provisioning_status.serialize_json(
                value["provisioning_status"]
            )
        )
    if "role" in value:
        import capo_iot_managed_integrations.types.role

        out["Role"] = capo_iot_managed_integrations.types.role.serialize_json(
            value["role"]
        )
    if "serial_number" in value:
        out["SerialNumber"] = value["serial_number"]
    if "created_at" in value:
        import capo_iot_managed_integrations.types.created_at

        out["CreatedAt"] = (
            capo_iot_managed_integrations.types.created_at.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import capo_iot_managed_integrations.types.created_at

        out["UpdatedAt"] = (
            capo_iot_managed_integrations.types.created_at.serialize_json(
                value["updated_at"]
            )
        )
    if "activated_at" in value:
        import capo_iot_managed_integrations.types.setup_at

        out["ActivatedAt"] = (
            capo_iot_managed_integrations.types.setup_at.serialize_json(
                value["activated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> ManagedThingSummary:
    out: ManagedThingSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("AdvertisedProductId") is not None:
        out["advertised_product_id"] = data["AdvertisedProductId"]
    if data.get("Brand") is not None:
        out["brand"] = data["Brand"]
    if data.get("Classification") is not None:
        out["classification"] = data["Classification"]
    if data.get("ConnectorDeviceId") is not None:
        out["connector_device_id"] = data["ConnectorDeviceId"]
    if data.get("ConnectorPolicyId") is not None:
        out["connector_policy_id"] = data["ConnectorPolicyId"]
    if data.get("ConnectorDestinationId") is not None:
        out["connector_destination_id"] = data["ConnectorDestinationId"]
    if data.get("Model") is not None:
        out["model"] = data["Model"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("CredentialLockerId") is not None:
        out["credential_locker_id"] = data["CredentialLockerId"]
    if data.get("ParentControllerId") is not None:
        out["parent_controller_id"] = data["ParentControllerId"]
    if data.get("ProvisioningStatus") is not None:
        import capo_iot_managed_integrations.types.provisioning_status

        out["provisioning_status"] = (
            capo_iot_managed_integrations.types.provisioning_status.deserialize_json(
                data["ProvisioningStatus"]
            )
        )
    if data.get("Role") is not None:
        import capo_iot_managed_integrations.types.role

        out["role"] = capo_iot_managed_integrations.types.role.deserialize_json(
            data["Role"]
        )
    if data.get("SerialNumber") is not None:
        out["serial_number"] = data["SerialNumber"]
    if data.get("CreatedAt") is not None:
        import capo_iot_managed_integrations.types.created_at

        out["created_at"] = (
            capo_iot_managed_integrations.types.created_at.deserialize_json(
                data["CreatedAt"]
            )
        )
    if data.get("UpdatedAt") is not None:
        import capo_iot_managed_integrations.types.created_at

        out["updated_at"] = (
            capo_iot_managed_integrations.types.created_at.deserialize_json(
                data["UpdatedAt"]
            )
        )
    if data.get("ActivatedAt") is not None:
        import capo_iot_managed_integrations.types.setup_at

        out["activated_at"] = (
            capo_iot_managed_integrations.types.setup_at.deserialize_json(
                data["ActivatedAt"]
            )
        )
    return out
