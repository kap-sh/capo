"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CommandCapability``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.capability_actions
    import capo_iot_managed_integrations.types.capability_name
    import capo_iot_managed_integrations.types.capability_version
    import capo_iot_managed_integrations.types.schema_versioned_id


class CommandCapability(TypedDict, closed=True):
    id: "capo_iot_managed_integrations.types.schema_versioned_id.SchemaVersionedId"
    """<p>Describe the capability with an id.</p>"""
    name: "capo_iot_managed_integrations.types.capability_name.CapabilityName"
    """<p>Describe the capability with an name.</p>"""
    version: "capo_iot_managed_integrations.types.capability_version.CapabilityVersion"
    """<p>Describe the capability with a version.</p>"""
    actions: "capo_iot_managed_integrations.types.capability_actions.CapabilityActions"
    """<p>Describe the command capability with the actions it supports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommandCapability) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["version"] = value["version"]
    import capo_iot_managed_integrations.types.capability_actions

    out["actions"] = (
        capo_iot_managed_integrations.types.capability_actions.serialize_json(
            value["actions"]
        )
    )
    return out


def deserialize_json(data: dict) -> CommandCapability:
    out: CommandCapability = {}  # type: ignore[typeddict-item]
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
    if data.get("actions") is not None:
        import capo_iot_managed_integrations.types.capability_actions

        out["actions"] = (
            capo_iot_managed_integrations.types.capability_actions.deserialize_json(
                data["actions"]
            )
        )
    else:
        out["actions"] = []
    return out


def redact_sensitive(value: CommandCapability) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "actions" in value:
        import capo_iot_managed_integrations.types.capability_actions

        out["actions"] = (
            capo_iot_managed_integrations.types.capability_actions.redact_sensitive(
                value["actions"]
            )
        )
    return out
