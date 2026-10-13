"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateManagedThingRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.auth_material_string
    import capo_iot_managed_integrations.types.auth_material_type
    import capo_iot_managed_integrations.types.brand
    import capo_iot_managed_integrations.types.capabilities
    import capo_iot_managed_integrations.types.capability_report
    import capo_iot_managed_integrations.types.capability_schemas
    import capo_iot_managed_integrations.types.classification
    import capo_iot_managed_integrations.types.client_token
    import capo_iot_managed_integrations.types.credential_locker_id
    import capo_iot_managed_integrations.types.meta_data
    import capo_iot_managed_integrations.types.model
    import capo_iot_managed_integrations.types.name
    import capo_iot_managed_integrations.types.owner
    import capo_iot_managed_integrations.types.role
    import capo_iot_managed_integrations.types.serial_number
    import capo_iot_managed_integrations.types.tags_map
    import capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration


class CreateManagedThingRequest(TypedDict, closed=True):
    role: "capo_iot_managed_integrations.types.role.Role"
    """<p>The type of device used. This will be the hub controller, cloud device, or AWS IoT device.</p>"""
    owner: NotRequired["capo_iot_managed_integrations.types.owner.Owner"]
    """<p>Owner of the device, usually an indication of whom the device belongs to. This value should not contain personal identifiable information.</p>"""
    credential_locker_id: NotRequired[
        "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
    ]
    """<p>The identifier of the credential for the managed thing.</p>"""
    authentication_material: (
        "capo_iot_managed_integrations.types.auth_material_string.AuthMaterialString"
    )
    """<p>The authentication material defining the device connectivity setup requests. The authorization materials used are the device bar code.</p>"""
    authentication_material_type: (
        "capo_iot_managed_integrations.types.auth_material_type.AuthMaterialType"
    )
    """<p>The type of authentication material used for device connectivity setup requests.</p>"""
    wi_fi_simple_setup_configuration: NotRequired[
        "capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration.WiFiSimpleSetupConfiguration"
    ]
    """<p>The Wi-Fi Simple Setup configuration for the managed thing, which defines provisioning capabilities and timeout settings.</p>"""
    serial_number: NotRequired[
        "capo_iot_managed_integrations.types.serial_number.SerialNumber"
    ]
    """<p>The serial number of the device.</p>"""
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
    """<p>The capability schemas that define the functionality and features supported by the managed thing, including device capabilities and their associated properties.</p>"""
    capabilities: NotRequired[
        "capo_iot_managed_integrations.types.capabilities.Capabilities"
    ]
    """<p>The capabilities of the device such as light bulb.</p>"""
    client_token: NotRequired[
        "capo_iot_managed_integrations.types.client_token.ClientToken"
    ]
    """<p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>"""
    classification: NotRequired[
        "capo_iot_managed_integrations.types.classification.Classification"
    ]
    """<p>The classification of the managed thing such as light bulb or thermostat.</p>"""
    tags: NotRequired["capo_iot_managed_integrations.types.tags_map.TagsMap"]
    """<p>A set of key/value pairs that are used to manage the managed thing.</p>"""
    meta_data: NotRequired["capo_iot_managed_integrations.types.meta_data.MetaData"]
    """<p>The metadata for the managed thing.</p> <note> <p>The <code>managedThing</code> <code>metadata</code> parameter is used for associating attributes with a <code>managedThing</code> that can be used for grouping over-the-air (OTA) tasks. Name value pairs in <code>metadata</code> can be used in the <code>OtaTargetQueryString</code> parameter for the <code>CreateOtaTask</code> API operation.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateManagedThingRequest) -> dict:
    out: dict = {}
    import capo_iot_managed_integrations.types.role

    out["Role"] = capo_iot_managed_integrations.types.role.serialize_json(value["role"])
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "credential_locker_id" in value:
        out["CredentialLockerId"] = value["credential_locker_id"]
    out["AuthenticationMaterial"] = value["authentication_material"]
    import capo_iot_managed_integrations.types.auth_material_type

    out["AuthenticationMaterialType"] = (
        capo_iot_managed_integrations.types.auth_material_type.serialize_json(
            value["authentication_material_type"]
        )
    )
    if "wi_fi_simple_setup_configuration" in value:
        import capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration

        out["WiFiSimpleSetupConfiguration"] = (
            capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration.serialize_json(
                value["wi_fi_simple_setup_configuration"]
            )
        )
    if "serial_number" in value:
        out["SerialNumber"] = value["serial_number"]
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
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "classification" in value:
        out["Classification"] = value["classification"]
    if "tags" in value:
        import capo_iot_managed_integrations.types.tags_map

        out["Tags"] = capo_iot_managed_integrations.types.tags_map.serialize_json(
            value["tags"]
        )
    if "meta_data" in value:
        import capo_iot_managed_integrations.types.meta_data

        out["MetaData"] = capo_iot_managed_integrations.types.meta_data.serialize_json(
            value["meta_data"]
        )
    return out


def deserialize_json(data: dict) -> CreateManagedThingRequest:
    out: CreateManagedThingRequest = {}  # type: ignore[typeddict-item]
    if data.get("Role") is not None:
        import capo_iot_managed_integrations.types.role

        out["role"] = capo_iot_managed_integrations.types.role.deserialize_json(
            data["Role"]
        )
    else:
        raise DeserializationError("CreateManagedThingRequest.role required")
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("CredentialLockerId") is not None:
        out["credential_locker_id"] = data["CredentialLockerId"]
    if data.get("AuthenticationMaterial") is not None:
        out["authentication_material"] = data["AuthenticationMaterial"]
    else:
        raise DeserializationError(
            "CreateManagedThingRequest.authentication_material required"
        )
    if data.get("AuthenticationMaterialType") is not None:
        import capo_iot_managed_integrations.types.auth_material_type

        out["authentication_material_type"] = (
            capo_iot_managed_integrations.types.auth_material_type.deserialize_json(
                data["AuthenticationMaterialType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateManagedThingRequest.authentication_material_type required"
        )
    if data.get("WiFiSimpleSetupConfiguration") is not None:
        import capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration

        out["wi_fi_simple_setup_configuration"] = (
            capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration.deserialize_json(
                data["WiFiSimpleSetupConfiguration"]
            )
        )
    if data.get("SerialNumber") is not None:
        out["serial_number"] = data["SerialNumber"]
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
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Classification") is not None:
        out["classification"] = data["Classification"]
    if data.get("Tags") is not None:
        import capo_iot_managed_integrations.types.tags_map

        out["tags"] = capo_iot_managed_integrations.types.tags_map.deserialize_json(
            data["Tags"]
        )
    if data.get("MetaData") is not None:
        import capo_iot_managed_integrations.types.meta_data

        out["meta_data"] = (
            capo_iot_managed_integrations.types.meta_data.deserialize_json(
                data["MetaData"]
            )
        )
    return out


def redact_sensitive(value: CreateManagedThingRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "owner" in value:
        out["owner"] = "*** Sensitive Data Redacted ***"
    if "authentication_material" in value:
        out["authentication_material"] = "*** Sensitive Data Redacted ***"
    if "serial_number" in value:
        out["serial_number"] = "*** Sensitive Data Redacted ***"
    if "brand" in value:
        out["brand"] = "*** Sensitive Data Redacted ***"
    if "model" in value:
        out["model"] = "*** Sensitive Data Redacted ***"
    if "classification" in value:
        out["classification"] = "*** Sensitive Data Redacted ***"
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
