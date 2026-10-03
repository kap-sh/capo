"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetManagedThingResponse``."""

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
    import capo_iot_managed_integrations.types.device_specific_key
    import capo_iot_managed_integrations.types.hub_network_mode
    import capo_iot_managed_integrations.types.international_article_number
    import capo_iot_managed_integrations.types.mac_address
    import capo_iot_managed_integrations.types.managed_thing_arn
    import capo_iot_managed_integrations.types.managed_thing_id
    import capo_iot_managed_integrations.types.meta_data
    import capo_iot_managed_integrations.types.model
    import capo_iot_managed_integrations.types.name
    import capo_iot_managed_integrations.types.owner
    import capo_iot_managed_integrations.types.parent_controller_id
    import capo_iot_managed_integrations.types.provisioning_status
    import capo_iot_managed_integrations.types.role
    import capo_iot_managed_integrations.types.serial_number
    import capo_iot_managed_integrations.types.setup_at
    import capo_iot_managed_integrations.types.tags_map
    import capo_iot_managed_integrations.types.universal_product_code
    import capo_iot_managed_integrations.types.updated_at
    import capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration


class GetManagedThingResponse(TypedDict, closed=True):
    id: NotRequired[
        "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    ]
    """<p>The id of the managed thing.</p>"""
    arn: NotRequired[
        "capo_iot_managed_integrations.types.managed_thing_arn.ManagedThingArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the managed thing.</p>"""
    owner: NotRequired["capo_iot_managed_integrations.types.owner.Owner"]
    """<p>Owner of the device, usually an indication of whom the device belongs to. This value should not contain personal identifiable information.</p>"""
    credential_locker_id: NotRequired[
        "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
    ]
    """<p>The identifier of the credential locker for the managed thing.</p>"""
    advertised_product_id: NotRequired[
        "capo_iot_managed_integrations.types.advertised_product_id.AdvertisedProductId"
    ]
    """<p>The id of the advertised product.</p>"""
    role: NotRequired["capo_iot_managed_integrations.types.role.Role"]
    """<p>The type of device used. This will be the Amazon Web Services hub controller, cloud device, or IoT device.</p>"""
    provisioning_status: NotRequired[
        "capo_iot_managed_integrations.types.provisioning_status.ProvisioningStatus"
    ]
    """<p>The provisioning status of the device in the provisioning workflow for onboarding to IoT managed integrations. For more information, see <a href="https://docs.aws.amazon.com/iot-mi/latest/devguide/device-provisioning.html">Device Provisioning</a>.</p>"""
    name: NotRequired["capo_iot_managed_integrations.types.name.Name"]
    """<p>The name of the managed thing representing the physical device.</p>"""
    model: NotRequired["capo_iot_managed_integrations.types.model.Model"]
    """<p>The model of the device.</p>"""
    brand: NotRequired["capo_iot_managed_integrations.types.brand.Brand"]
    """<p>The brand of the device.</p>"""
    serial_number: NotRequired[
        "capo_iot_managed_integrations.types.serial_number.SerialNumber"
    ]
    """<p>The serial number of the device.</p>"""
    universal_product_code: NotRequired[
        "capo_iot_managed_integrations.types.universal_product_code.UniversalProductCode"
    ]
    """<p>The universal product code (UPC) of the device model. The UPC is typically used in the United States of America and Canada.</p>"""
    international_article_number: NotRequired[
        "capo_iot_managed_integrations.types.international_article_number.InternationalArticleNumber"
    ]
    """<p>The unique 13 digit number that identifies the managed thing.</p>"""
    connector_policy_id: NotRequired[
        "capo_iot_managed_integrations.types.connector_policy_id.ConnectorPolicyId"
    ]
    """<p>The id of the connector policy.</p> <note> <p>This parameter is used for cloud-to-cloud devices only.</p> </note>"""
    connector_destination_id: NotRequired[
        "capo_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
    ]
    """<p>The identifier of the connector destination associated with this managed thing.</p>"""
    connector_device_id: NotRequired[
        "capo_iot_managed_integrations.types.connector_device_id.ConnectorDeviceId"
    ]
    """<p>The third-party device id as defined by the connector. This device id must not contain personal identifiable information (PII).</p> <note> <p>This parameter is used for cloud-to-cloud devices only.</p> </note>"""
    device_specific_key: NotRequired[
        "capo_iot_managed_integrations.types.device_specific_key.DeviceSpecificKey"
    ]
    """<p>A Zwave device-specific key used during device activation.</p> <note> <p>This parameter is used for Zwave devices only.</p> </note>"""
    mac_address: NotRequired[
        "capo_iot_managed_integrations.types.mac_address.MacAddress"
    ]
    """<p>The media access control (MAC) address for the device represented by the managed thing.</p> <note> <p>This parameter is used for Zigbee devices only.</p> </note>"""
    parent_controller_id: NotRequired[
        "capo_iot_managed_integrations.types.parent_controller_id.ParentControllerId"
    ]
    """<p>Id of the controller device used for the discovery job.</p>"""
    classification: NotRequired[
        "capo_iot_managed_integrations.types.classification.Classification"
    ]
    """<p>The classification of the managed thing such as light bulb or thermostat.</p>"""
    created_at: NotRequired["capo_iot_managed_integrations.types.created_at.CreatedAt"]
    """<p>The timestamp value of when the device creation request occurred.</p>"""
    updated_at: NotRequired["capo_iot_managed_integrations.types.updated_at.UpdatedAt"]
    """<p>The timestamp value of when the managed thing was last updated at.</p>"""
    activated_at: NotRequired["capo_iot_managed_integrations.types.setup_at.SetupAt"]
    """<p>The timestampe value of when the device was activated.</p>"""
    hub_network_mode: NotRequired[
        "capo_iot_managed_integrations.types.hub_network_mode.HubNetworkMode"
    ]
    """<p>The network mode for the hub-connected device.</p>"""
    meta_data: NotRequired["capo_iot_managed_integrations.types.meta_data.MetaData"]
    """<p>The metadata for the managed thing.</p>"""
    tags: NotRequired["capo_iot_managed_integrations.types.tags_map.TagsMap"]
    """<p>A set of key/value pairs that are used to manage the managed thing.</p>"""
    wi_fi_simple_setup_configuration: NotRequired[
        "capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration.WiFiSimpleSetupConfiguration"
    ]
    """<p>The Wi-Fi Simple Setup configuration for the managed thing, which defines provisioning capabilities and timeout settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedThingResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "credential_locker_id" in value:
        out["CredentialLockerId"] = value["credential_locker_id"]
    if "advertised_product_id" in value:
        out["AdvertisedProductId"] = value["advertised_product_id"]
    if "role" in value:
        import capo_iot_managed_integrations.types.role

        out["Role"] = capo_iot_managed_integrations.types.role.serialize_json(
            value["role"]
        )
    if "provisioning_status" in value:
        import capo_iot_managed_integrations.types.provisioning_status

        out["ProvisioningStatus"] = (
            capo_iot_managed_integrations.types.provisioning_status.serialize_json(
                value["provisioning_status"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "model" in value:
        out["Model"] = value["model"]
    if "brand" in value:
        out["Brand"] = value["brand"]
    if "serial_number" in value:
        out["SerialNumber"] = value["serial_number"]
    if "universal_product_code" in value:
        out["UniversalProductCode"] = value["universal_product_code"]
    if "international_article_number" in value:
        out["InternationalArticleNumber"] = value["international_article_number"]
    if "connector_policy_id" in value:
        out["ConnectorPolicyId"] = value["connector_policy_id"]
    if "connector_destination_id" in value:
        out["ConnectorDestinationId"] = value["connector_destination_id"]
    if "connector_device_id" in value:
        out["ConnectorDeviceId"] = value["connector_device_id"]
    if "device_specific_key" in value:
        out["DeviceSpecificKey"] = value["device_specific_key"]
    if "mac_address" in value:
        out["MacAddress"] = value["mac_address"]
    if "parent_controller_id" in value:
        out["ParentControllerId"] = value["parent_controller_id"]
    if "classification" in value:
        out["Classification"] = value["classification"]
    if "created_at" in value:
        import capo_iot_managed_integrations.types.created_at

        out["CreatedAt"] = (
            capo_iot_managed_integrations.types.created_at.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import capo_iot_managed_integrations.types.updated_at

        out["UpdatedAt"] = (
            capo_iot_managed_integrations.types.updated_at.serialize_json(
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
    if "hub_network_mode" in value:
        import capo_iot_managed_integrations.types.hub_network_mode

        out["HubNetworkMode"] = (
            capo_iot_managed_integrations.types.hub_network_mode.serialize_json(
                value["hub_network_mode"]
            )
        )
    if "meta_data" in value:
        import capo_iot_managed_integrations.types.meta_data

        out["MetaData"] = capo_iot_managed_integrations.types.meta_data.serialize_json(
            value["meta_data"]
        )
    if "tags" in value:
        import capo_iot_managed_integrations.types.tags_map

        out["Tags"] = capo_iot_managed_integrations.types.tags_map.serialize_json(
            value["tags"]
        )
    if "wi_fi_simple_setup_configuration" in value:
        import capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration

        out["WiFiSimpleSetupConfiguration"] = (
            capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration.serialize_json(
                value["wi_fi_simple_setup_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetManagedThingResponse:
    out: GetManagedThingResponse = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("CredentialLockerId") is not None:
        out["credential_locker_id"] = data["CredentialLockerId"]
    if data.get("AdvertisedProductId") is not None:
        out["advertised_product_id"] = data["AdvertisedProductId"]
    if data.get("Role") is not None:
        import capo_iot_managed_integrations.types.role

        out["role"] = capo_iot_managed_integrations.types.role.deserialize_json(
            data["Role"]
        )
    if data.get("ProvisioningStatus") is not None:
        import capo_iot_managed_integrations.types.provisioning_status

        out["provisioning_status"] = (
            capo_iot_managed_integrations.types.provisioning_status.deserialize_json(
                data["ProvisioningStatus"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Model") is not None:
        out["model"] = data["Model"]
    if data.get("Brand") is not None:
        out["brand"] = data["Brand"]
    if data.get("SerialNumber") is not None:
        out["serial_number"] = data["SerialNumber"]
    if data.get("UniversalProductCode") is not None:
        out["universal_product_code"] = data["UniversalProductCode"]
    if data.get("InternationalArticleNumber") is not None:
        out["international_article_number"] = data["InternationalArticleNumber"]
    if data.get("ConnectorPolicyId") is not None:
        out["connector_policy_id"] = data["ConnectorPolicyId"]
    if data.get("ConnectorDestinationId") is not None:
        out["connector_destination_id"] = data["ConnectorDestinationId"]
    if data.get("ConnectorDeviceId") is not None:
        out["connector_device_id"] = data["ConnectorDeviceId"]
    if data.get("DeviceSpecificKey") is not None:
        out["device_specific_key"] = data["DeviceSpecificKey"]
    if data.get("MacAddress") is not None:
        out["mac_address"] = data["MacAddress"]
    if data.get("ParentControllerId") is not None:
        out["parent_controller_id"] = data["ParentControllerId"]
    if data.get("Classification") is not None:
        out["classification"] = data["Classification"]
    if data.get("CreatedAt") is not None:
        import capo_iot_managed_integrations.types.created_at

        out["created_at"] = (
            capo_iot_managed_integrations.types.created_at.deserialize_json(
                data["CreatedAt"]
            )
        )
    if data.get("UpdatedAt") is not None:
        import capo_iot_managed_integrations.types.updated_at

        out["updated_at"] = (
            capo_iot_managed_integrations.types.updated_at.deserialize_json(
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
    if data.get("HubNetworkMode") is not None:
        import capo_iot_managed_integrations.types.hub_network_mode

        out["hub_network_mode"] = (
            capo_iot_managed_integrations.types.hub_network_mode.deserialize_json(
                data["HubNetworkMode"]
            )
        )
    if data.get("MetaData") is not None:
        import capo_iot_managed_integrations.types.meta_data

        out["meta_data"] = (
            capo_iot_managed_integrations.types.meta_data.deserialize_json(
                data["MetaData"]
            )
        )
    if data.get("Tags") is not None:
        import capo_iot_managed_integrations.types.tags_map

        out["tags"] = capo_iot_managed_integrations.types.tags_map.deserialize_json(
            data["Tags"]
        )
    if data.get("WiFiSimpleSetupConfiguration") is not None:
        import capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration

        out["wi_fi_simple_setup_configuration"] = (
            capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration.deserialize_json(
                data["WiFiSimpleSetupConfiguration"]
            )
        )
    return out
