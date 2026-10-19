"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#StateCapability``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.capability_name
    import capo_iot_managed_integrations.types.capability_properties
    import capo_iot_managed_integrations.types.capability_version
    import capo_iot_managed_integrations.types.schema_versioned_id


class StateCapability(TypedDict, closed=True):
    id: "capo_iot_managed_integrations.types.schema_versioned_id.SchemaVersionedId"
    """<p>The id of the managed thing in the capability report.</p>"""
    name: "capo_iot_managed_integrations.types.capability_name.CapabilityName"
    """<p>Name for the Amazon Web Services capability.</p>"""
    version: "capo_iot_managed_integrations.types.capability_version.CapabilityVersion"
    """<p>Version for the Amazon Web Services capability.</p>"""
    properties: NotRequired[
        "capo_iot_managed_integrations.types.capability_properties.CapabilityProperties"
    ]
    """<p>Describe the command capability with the properties it supports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StateCapability) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["version"] = value["version"]
    if "properties" in value:
        out["properties"] = value["properties"]
    return out


def deserialize_json(data: dict) -> StateCapability:
    out: StateCapability = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    if data.get("properties") is not None:
        out["properties"] = data["properties"]
    return out


def redact_sensitive(value: StateCapability) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "properties" in value:
        out["properties"] = "*** Sensitive Data Redacted ***"
    return out
