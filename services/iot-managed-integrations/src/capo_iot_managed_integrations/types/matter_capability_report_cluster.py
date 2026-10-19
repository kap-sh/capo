"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterCapabilityReportCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.capability_name
    import capo_iot_managed_integrations.types.cluster_id
    import capo_iot_managed_integrations.types.matter_capability_report_attributes
    import capo_iot_managed_integrations.types.matter_capability_report_cluster_revision_id
    import capo_iot_managed_integrations.types.matter_capability_report_commands
    import capo_iot_managed_integrations.types.matter_capability_report_events
    import capo_iot_managed_integrations.types.matter_capability_report_fabric_index
    import capo_iot_managed_integrations.types.matter_capability_report_feature_map
    import capo_iot_managed_integrations.types.matter_capability_report_generated_commands
    import capo_iot_managed_integrations.types.schema_versioned_id
    import capo_iot_managed_integrations.types.spec_version


class MatterCapabilityReportCluster(TypedDict, closed=True):
    id: "capo_iot_managed_integrations.types.cluster_id.ClusterId"
    """<p>The id of the Amazon Web Services Matter capability report cluster.</p>"""
    revision: "capo_iot_managed_integrations.types.matter_capability_report_cluster_revision_id.MatterCapabilityReportClusterRevisionId"
    """<p>The id of the revision for the Amazon Web Services Matter capability report.</p>"""
    public_id: NotRequired[
        "capo_iot_managed_integrations.types.schema_versioned_id.SchemaVersionedId"
    ]
    """<p>The id of the schema version.</p>"""
    name: NotRequired[
        "capo_iot_managed_integrations.types.capability_name.CapabilityName"
    ]
    """<p>The capability name used in the Amazon Web Services Matter capability report.</p>"""
    spec_version: NotRequired[
        "capo_iot_managed_integrations.types.spec_version.SpecVersion"
    ]
    """<p>The spec version used in the Amazon Web Services Matter capability report.</p>"""
    attributes: NotRequired[
        "capo_iot_managed_integrations.types.matter_capability_report_attributes.MatterCapabilityReportAttributes"
    ]
    """<p>The attributes of the Amazon Web Services Matter capability report.</p>"""
    commands: NotRequired[
        "capo_iot_managed_integrations.types.matter_capability_report_commands.MatterCapabilityReportCommands"
    ]
    """<p>The commands used with the Amazon Web Services Matter capability report.</p>"""
    events: NotRequired[
        "capo_iot_managed_integrations.types.matter_capability_report_events.MatterCapabilityReportEvents"
    ]
    """<p>The events used with the Amazon Web Services Matter capability report.</p>"""
    feature_map: NotRequired[
        "capo_iot_managed_integrations.types.matter_capability_report_feature_map.MatterCapabilityReportFeatureMap"
    ]
    """<p>32 bit-map used to indicate which features a cluster supports.</p>"""
    generated_commands: NotRequired[
        "capo_iot_managed_integrations.types.matter_capability_report_generated_commands.MatterCapabilityReportGeneratedCommands"
    ]
    """<p>Matter clusters used in capability report.</p>"""
    fabric_index: NotRequired[
        "capo_iot_managed_integrations.types.matter_capability_report_fabric_index.MatterCapabilityReportFabricIndex"
    ]
    """<p>The fabric index for the Amazon Web Services Matter capability report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatterCapabilityReportCluster) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["revision"] = value["revision"]
    if "public_id" in value:
        out["publicId"] = value["public_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "spec_version" in value:
        out["specVersion"] = value["spec_version"]
    if "attributes" in value:
        import capo_iot_managed_integrations.types.matter_capability_report_attributes

        out["attributes"] = (
            capo_iot_managed_integrations.types.matter_capability_report_attributes.serialize_json(
                value["attributes"]
            )
        )
    if "commands" in value:
        import capo_iot_managed_integrations.types.matter_capability_report_commands

        out["commands"] = (
            capo_iot_managed_integrations.types.matter_capability_report_commands.serialize_json(
                value["commands"]
            )
        )
    if "events" in value:
        import capo_iot_managed_integrations.types.matter_capability_report_events

        out["events"] = (
            capo_iot_managed_integrations.types.matter_capability_report_events.serialize_json(
                value["events"]
            )
        )
    if "feature_map" in value:
        out["featureMap"] = value["feature_map"]
    if "generated_commands" in value:
        import capo_iot_managed_integrations.types.matter_capability_report_generated_commands

        out["generatedCommands"] = (
            capo_iot_managed_integrations.types.matter_capability_report_generated_commands.serialize_json(
                value["generated_commands"]
            )
        )
    if "fabric_index" in value:
        out["fabricIndex"] = value["fabric_index"]
    return out


def deserialize_json(data: dict) -> MatterCapabilityReportCluster:
    out: MatterCapabilityReportCluster = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    else:
        out["revision"] = 0
    if data.get("publicId") is not None:
        out["public_id"] = data["publicId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("specVersion") is not None:
        out["spec_version"] = data["specVersion"]
    if data.get("attributes") is not None:
        import capo_iot_managed_integrations.types.matter_capability_report_attributes

        out["attributes"] = (
            capo_iot_managed_integrations.types.matter_capability_report_attributes.deserialize_json(
                data["attributes"]
            )
        )
    if data.get("commands") is not None:
        import capo_iot_managed_integrations.types.matter_capability_report_commands

        out["commands"] = (
            capo_iot_managed_integrations.types.matter_capability_report_commands.deserialize_json(
                data["commands"]
            )
        )
    if data.get("events") is not None:
        import capo_iot_managed_integrations.types.matter_capability_report_events

        out["events"] = (
            capo_iot_managed_integrations.types.matter_capability_report_events.deserialize_json(
                data["events"]
            )
        )
    if data.get("featureMap") is not None:
        out["feature_map"] = data["featureMap"]
    if data.get("generatedCommands") is not None:
        import capo_iot_managed_integrations.types.matter_capability_report_generated_commands

        out["generated_commands"] = (
            capo_iot_managed_integrations.types.matter_capability_report_generated_commands.deserialize_json(
                data["generatedCommands"]
            )
        )
    if data.get("fabricIndex") is not None:
        out["fabric_index"] = data["fabricIndex"]
    return out
