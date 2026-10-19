"""Generated from Smithy shape ``com.amazonaws.entityresolution#SchemaMappingSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_entityresolution.types.entity_name
    import capo_entityresolution.types.schema_mapping_arn


class SchemaMappingSummary(TypedDict, closed=True):
    schema_name: "capo_entityresolution.types.entity_name.EntityName"
    """<p>The name of the schema.</p>"""
    schema_arn: "capo_entityresolution.types.schema_mapping_arn.SchemaMappingArn"
    """<p>The ARN (Amazon Resource Name) that Entity Resolution generated for the <code>SchemaMapping</code>.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp of when the <code>SchemaMapping</code> was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp of when the <code>SchemaMapping</code> was last updated.</p>"""
    has_workflows: "bool"
    """<p>Specifies whether the schema mapping has been applied to a workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaMappingSummary) -> dict:
    out: dict = {}
    out["schemaName"] = value["schema_name"]
    out["schemaArn"] = value["schema_arn"]
    import capo_entityresolution.types._prelude.timestamp

    out["createdAt"] = capo_entityresolution.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_entityresolution.types._prelude.timestamp

    out["updatedAt"] = capo_entityresolution.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    out["hasWorkflows"] = value["has_workflows"]
    return out


def deserialize_json(data: dict) -> SchemaMappingSummary:
    out: SchemaMappingSummary = {}  # type: ignore[typeddict-item]
    if data.get("schemaName") is not None:
        out["schema_name"] = data["schemaName"]
    else:
        out["schema_name"] = ""
    if data.get("schemaArn") is not None:
        out["schema_arn"] = data["schemaArn"]
    else:
        out["schema_arn"] = ""
    if data.get("createdAt") is not None:
        import capo_entityresolution.types._prelude.timestamp

        out["created_at"] = (
            capo_entityresolution.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_entityresolution.types._prelude.timestamp

        out["updated_at"] = (
            capo_entityresolution.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("hasWorkflows") is not None:
        out["has_workflows"] = data["hasWorkflows"]
    else:
        out["has_workflows"] = False
    return out
