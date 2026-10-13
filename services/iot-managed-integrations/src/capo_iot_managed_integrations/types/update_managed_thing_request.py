"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#UpdateManagedThingRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.brand
    import capo_iot_managed_integrations.types.capabilities
    import capo_iot_managed_integrations.types.capability_report
    import capo_iot_managed_integrations.types.capability_schemas
    import capo_iot_managed_integrations.types.classification
    import capo_iot_managed_integrations.types.credential_locker_id
    import capo_iot_managed_integrations.types.hub_network_mode
    import capo_iot_managed_integrations.types.managed_thing_id
    import capo_iot_managed_integrations.types.meta_data
    import capo_iot_managed_integrations.types.model
    import capo_iot_managed_integrations.types.name
    import capo_iot_managed_integrations.types.owner
    import capo_iot_managed_integrations.types.serial_number
    import capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration


class UpdateManagedThingRequest(TypedDict, closed=True):
    identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    """<p>The id of the managed thing.</p>"""
    owner: NotRequired["capo_iot_managed_integrations.types.owner.Owner"]
    """<p>Owner of the device, usually an indication of whom the device belongs to. This value should not contain personal identifiable information.</p>"""
    credential_locker_id: NotRequired[
        "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
    ]
    """<p>The identifier of the credential for the managed thing.</p>"""
    serial_number: NotRequired[
        "capo_iot_managed_integrations.types.serial_number.SerialNumber"
    ]
    """<p>The serial number of the device.</p>"""
    wi_fi_simple_setup_configuration: NotRequired[
        "capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration.WiFiSimpleSetupConfiguration"
    ]
    """<p>The Wi-Fi Simple Setup configuration for the managed thing, which defines provisioning capabilities and timeout settings.</p>"""
    brand: NotRequired["capo_iot_managed_integrations.types.brand.Brand"]
    """<p>The brand of the device.</p>"""
    model: NotRequired["capo_iot_managed_integrations.types.model.Model"]
    """<p>The model of the device.</p>"""
    name: NotRequired["capo_iot_managed_integrations.types.name.Name"]
    """<p>The name of the managed thing representing the physical device.</p>"""
    capability_report: NotRequired[
        "capo_iot_managed_integrations.types.capability_report.CapabilityReport"
    ]
    """<p>A report of the capabilities for the managed thing.</p>"""
    capability_schemas: NotRequired[
        "capo_iot_managed_integrations.types.capability_schemas.CapabilitySchemas"
    ]
    """<p>The updated capability schemas that define the functionality and features supported by the managed thing.</p>"""
    capabilities: NotRequired[
        "capo_iot_managed_integrations.types.capabilities.Capabilities"
    ]
    """<p>The capabilities of the device such as light bulb.</p>"""
    classification: NotRequired[
        "capo_iot_managed_integrations.types.classification.Classification"
    ]
    """<p>The classification of the managed thing such as light bulb or thermostat.</p>"""
    hub_network_mode: NotRequired[
        "capo_iot_managed_integrations.types.hub_network_mode.HubNetworkMode"
    ]
    """<p>The network mode for the hub-connected device.</p>"""
    meta_data: NotRequired["capo_iot_managed_integrations.types.meta_data.MetaData"]
    """<p>The metadata for the managed thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateManagedThingRequest) -> dict:
    out: dict = {}
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "credential_locker_id" in value:
        out["CredentialLockerId"] = value["credential_locker_id"]
    if "serial_number" in value:
        out["SerialNumber"] = value["serial_number"]
    if "wi_fi_simple_setup_configuration" in value:
        import capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration

        out["WiFiSimpleSetupConfiguration"] = (
            capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration.serialize_json(
                value["wi_fi_simple_setup_configuration"]
            )
        )
    if "brand" in value:
        out["Brand"] = value["brand"]
    if "model" in value:
        out["Model"] = value["model"]
    if "name" in value:
        out["Name"] = value["name"]
    if "capability_report" in value:
        import capo_iot_managed_integrations.types.capability_report

        out["CapabilityReport"] = (
            capo_iot_managed_integrations.types.capability_report.serialize_json(
                value["capability_report"]
            )
        )
    if "capability_schemas" in value:
        import capo_iot_managed_integrations.types.capability_schemas

        out["CapabilitySchemas"] = (
            capo_iot_managed_integrations.types.capability_schemas.serialize_json(
                value["capability_schemas"]
            )
        )
    if "capabilities" in value:
        out["Capabilities"] = value["capabilities"]
    if "classification" in value:
        out["Classification"] = value["classification"]
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
    return out


def deserialize_json(data: dict) -> UpdateManagedThingRequest:
    out: UpdateManagedThingRequest = {}  # type: ignore[typeddict-item]
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("CredentialLockerId") is not None:
        out["credential_locker_id"] = data["CredentialLockerId"]
    if data.get("SerialNumber") is not None:
        out["serial_number"] = data["SerialNumber"]
    if data.get("WiFiSimpleSetupConfiguration") is not None:
        import capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration

        out["wi_fi_simple_setup_configuration"] = (
            capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration.deserialize_json(
                data["WiFiSimpleSetupConfiguration"]
            )
        )
    if data.get("Brand") is not None:
        out["brand"] = data["Brand"]
    if data.get("Model") is not None:
        out["model"] = data["Model"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("CapabilityReport") is not None:
        import capo_iot_managed_integrations.types.capability_report

        out["capability_report"] = (
            capo_iot_managed_integrations.types.capability_report.deserialize_json(
                data["CapabilityReport"]
            )
        )
    if data.get("CapabilitySchemas") is not None:
        import capo_iot_managed_integrations.types.capability_schemas

        out["capability_schemas"] = (
            capo_iot_managed_integrations.types.capability_schemas.deserialize_json(
                data["CapabilitySchemas"]
            )
        )
    if data.get("Capabilities") is not None:
        out["capabilities"] = data["Capabilities"]
    if data.get("Classification") is not None:
        out["classification"] = data["Classification"]
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
    return out


def redact_sensitive(value: UpdateManagedThingRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "owner" in value:
        out["owner"] = "*** Sensitive Data Redacted ***"
    if "serial_number" in value:
        out["serial_number"] = "*** Sensitive Data Redacted ***"
    if "brand" in value:
        out["brand"] = "*** Sensitive Data Redacted ***"
    if "model" in value:
        out["model"] = "*** Sensitive Data Redacted ***"
    if "classification" in value:
        out["classification"] = "*** Sensitive Data Redacted ***"
    return out
