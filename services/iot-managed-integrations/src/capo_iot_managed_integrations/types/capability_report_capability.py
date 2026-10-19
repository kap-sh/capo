"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CapabilityReportCapability``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.capability_name
    import capo_iot_managed_integrations.types.capability_report_actions
    import capo_iot_managed_integrations.types.capability_report_events
    import capo_iot_managed_integrations.types.capability_report_properties
    import capo_iot_managed_integrations.types.capability_version
    import capo_iot_managed_integrations.types.schema_versioned_id


class CapabilityReportCapability(TypedDict, closed=True):
    id: "capo_iot_managed_integrations.types.schema_versioned_id.SchemaVersionedId"
    """<p>The id of the schema version.</p>"""
    name: "capo_iot_managed_integrations.types.capability_name.CapabilityName"
    """<p>The name of the capability.</p>"""
    version: "capo_iot_managed_integrations.types.capability_version.CapabilityVersion"
    """<p>The version of the capability.</p>"""
    properties: "capo_iot_managed_integrations.types.capability_report_properties.CapabilityReportProperties"
    """<p>The capability properties used in the capability report.</p>"""
    actions: "capo_iot_managed_integrations.types.capability_report_actions.CapabilityReportActions"
    """<p>The capability actions used in the capability report.</p>"""
    events: "capo_iot_managed_integrations.types.capability_report_events.CapabilityReportEvents"
    """<p>The capability events used in the capability report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityReportCapability) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["version"] = value["version"]
    import capo_iot_managed_integrations.types.capability_report_properties

    out["properties"] = (
        capo_iot_managed_integrations.types.capability_report_properties.serialize_json(
            value["properties"]
        )
    )
    import capo_iot_managed_integrations.types.capability_report_actions

    out["actions"] = (
        capo_iot_managed_integrations.types.capability_report_actions.serialize_json(
            value["actions"]
        )
    )
    import capo_iot_managed_integrations.types.capability_report_events

    out["events"] = (
        capo_iot_managed_integrations.types.capability_report_events.serialize_json(
            value["events"]
        )
    )
    return out


def deserialize_json(data: dict) -> CapabilityReportCapability:
    out: CapabilityReportCapability = {}  # type: ignore[typeddict-item]
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
        import capo_iot_managed_integrations.types.capability_report_properties

        out["properties"] = (
            capo_iot_managed_integrations.types.capability_report_properties.deserialize_json(
                data["properties"]
            )
        )
    else:
        out["properties"] = []
    if data.get("actions") is not None:
        import capo_iot_managed_integrations.types.capability_report_actions

        out["actions"] = (
            capo_iot_managed_integrations.types.capability_report_actions.deserialize_json(
                data["actions"]
            )
        )
    else:
        out["actions"] = []
    if data.get("events") is not None:
        import capo_iot_managed_integrations.types.capability_report_events

        out["events"] = (
            capo_iot_managed_integrations.types.capability_report_events.deserialize_json(
                data["events"]
            )
        )
    else:
        out["events"] = []
    return out
