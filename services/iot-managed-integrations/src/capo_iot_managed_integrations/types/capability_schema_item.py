"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CapabilitySchemaItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.extrinsic_schema_id
    import capo_iot_managed_integrations.types.matter_capability_report_cluster_revision_id
    import capo_iot_managed_integrations.types.schema_version_format
    import capo_iot_managed_integrations.types.schema_versioned_id
    import capo_iot_managed_integrations.types.validation_schema


class CapabilitySchemaItem(TypedDict, closed=True):
    format: (
        "capo_iot_managed_integrations.types.schema_version_format.SchemaVersionFormat"
    )
    """<p>The format of the capability schema, which defines how the schema is structured and interpreted.</p>"""
    capability_id: (
        "capo_iot_managed_integrations.types.schema_versioned_id.SchemaVersionedId"
    )
    """<p>The unique identifier of the capability defined in the schema.</p>"""
    extrinsic_id: (
        "capo_iot_managed_integrations.types.extrinsic_schema_id.ExtrinsicSchemaId"
    )
    """<p>The external identifier for the capability, used when referencing the capability outside of the AWS ecosystem.</p>"""
    extrinsic_version: "capo_iot_managed_integrations.types.matter_capability_report_cluster_revision_id.MatterCapabilityReportClusterRevisionId"
    """<p>The version of the external capability definition, used to track compatibility with external systems.</p>"""
    schema: "capo_iot_managed_integrations.types.validation_schema.ValidationSchema"
    """<p>The actual schema definition that describes the capability's properties, actions, and events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapabilitySchemaItem) -> dict:
    out: dict = {}
    import capo_iot_managed_integrations.types.schema_version_format

    out["Format"] = (
        capo_iot_managed_integrations.types.schema_version_format.serialize_json(
            value["format"]
        )
    )
    out["CapabilityId"] = value["capability_id"]
    out["ExtrinsicId"] = value["extrinsic_id"]
    out["ExtrinsicVersion"] = value["extrinsic_version"]
    out["Schema"] = value["schema"]
    return out


def deserialize_json(data: dict) -> CapabilitySchemaItem:
    out: CapabilitySchemaItem = {}  # type: ignore[typeddict-item]
    if data.get("Format") is not None:
        import capo_iot_managed_integrations.types.schema_version_format

        out["format"] = (
            capo_iot_managed_integrations.types.schema_version_format.deserialize_json(
                data["Format"]
            )
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_iot_managed_integrations.types.schema_version_format.SchemaVersionFormat",
            "",
        )
    if data.get("CapabilityId") is not None:
        out["capability_id"] = data["CapabilityId"]
    else:
        out["capability_id"] = ""
    if data.get("ExtrinsicId") is not None:
        out["extrinsic_id"] = data["ExtrinsicId"]
    else:
        out["extrinsic_id"] = ""
    if data.get("ExtrinsicVersion") is not None:
        out["extrinsic_version"] = data["ExtrinsicVersion"]
    else:
        out["extrinsic_version"] = 0
    if data.get("Schema") is not None:
        out["schema"] = data["Schema"]
    else:
        out["schema"] = None
    return out
