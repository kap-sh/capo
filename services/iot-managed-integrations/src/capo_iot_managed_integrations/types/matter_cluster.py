"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterCluster``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.cluster_id
    import capo_iot_managed_integrations.types.matter_attributes
    import capo_iot_managed_integrations.types.matter_commands
    import capo_iot_managed_integrations.types.matter_events


class MatterCluster(TypedDict, closed=True):
    id: NotRequired["capo_iot_managed_integrations.types.cluster_id.ClusterId"]
    """<p>The cluster id.</p>"""
    attributes: NotRequired[
        "capo_iot_managed_integrations.types.matter_attributes.MatterAttributes"
    ]
    """<p>The Matter attributes.</p>"""
    commands: NotRequired[
        "capo_iot_managed_integrations.types.matter_commands.MatterCommands"
    ]
    """<p>Describe the Matter commands with the Matter command identifier mapped to the command fields.</p>"""
    events: NotRequired[
        "capo_iot_managed_integrations.types.matter_events.MatterEvents"
    ]
    """<p>Describe the Matter events with the Matter event identifier mapped to the event fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatterCluster) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "attributes" in value:
        out["attributes"] = value["attributes"]
    if "commands" in value:
        import capo_iot_managed_integrations.types.matter_commands

        out["commands"] = (
            capo_iot_managed_integrations.types.matter_commands.serialize_json(
                value["commands"]
            )
        )
    if "events" in value:
        import capo_iot_managed_integrations.types.matter_events

        out["events"] = (
            capo_iot_managed_integrations.types.matter_events.serialize_json(
                value["events"]
            )
        )
    return out


def deserialize_json(data: dict) -> MatterCluster:
    out: MatterCluster = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("attributes") is not None:
        out["attributes"] = data["attributes"]
    if data.get("commands") is not None:
        import capo_iot_managed_integrations.types.matter_commands

        out["commands"] = (
            capo_iot_managed_integrations.types.matter_commands.deserialize_json(
                data["commands"]
            )
        )
    if data.get("events") is not None:
        import capo_iot_managed_integrations.types.matter_events

        out["events"] = (
            capo_iot_managed_integrations.types.matter_events.deserialize_json(
                data["events"]
            )
        )
    return out


def redact_sensitive(value: MatterCluster) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "attributes" in value:
        out["attributes"] = "*** Sensitive Data Redacted ***"
    if "commands" in value:
        import capo_iot_managed_integrations.types.matter_commands

        out["commands"] = (
            capo_iot_managed_integrations.types.matter_commands.redact_sensitive(
                value["commands"]
            )
        )
    if "events" in value:
        import capo_iot_managed_integrations.types.matter_events

        out["events"] = (
            capo_iot_managed_integrations.types.matter_events.redact_sensitive(
                value["events"]
            )
        )
    return out
