"""Generated from Smithy shape ``com.amazonaws.glue#S3HudiCatalogTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.additional_options
    import capo_glue.types.auto_data_quality
    import capo_glue.types.catalog_schema_change_policy
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.glue_schemas
    import capo_glue.types.glue_studio_path_list
    import capo_glue.types.node_name
    import capo_glue.types.one_input


class S3HudiCatalogTarget(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the data target.</p>"""
    inputs: "capo_glue.types.one_input.OneInput"
    """<p>The nodes that are inputs to the data target.</p>"""
    partition_keys: NotRequired[
        "capo_glue.types.glue_studio_path_list.GlueStudioPathList"
    ]
    """<p>Specifies native partitioning using a sequence of keys.</p>"""
    table: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the table in the database to write to.</p>"""
    database: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the database to write to.</p>"""
    additional_options: "capo_glue.types.additional_options.AdditionalOptions"
    """<p>Specifies additional connection options for the connector.</p>"""
    schema_change_policy: NotRequired[
        "capo_glue.types.catalog_schema_change_policy.CatalogSchemaChangePolicy"
    ]
    """<p>A policy that specifies update behavior for the crawler.</p>"""
    auto_data_quality: NotRequired["capo_glue.types.auto_data_quality.AutoDataQuality"]
    """<p>Specifies whether to automatically enable data quality evaluation for the S3 Hudi catalog target. When set to <code>true</code>, data quality checks are performed automatically during the write operation.</p>"""
    output_schemas: NotRequired["capo_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the S3 Hudi catalog target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3HudiCatalogTarget) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.one_input

    out["Inputs"] = capo_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    if "partition_keys" in value:
        import capo_glue.types.glue_studio_path_list

        out["PartitionKeys"] = (
            capo_glue.types.glue_studio_path_list.serialize_aws_json_1_1(
                value["partition_keys"]
            )
        )
    out["Table"] = value["table"]
    out["Database"] = value["database"]
    import capo_glue.types.additional_options

    out["AdditionalOptions"] = (
        capo_glue.types.additional_options.serialize_aws_json_1_1(
            value["additional_options"]
        )
    )
    if "schema_change_policy" in value:
        import capo_glue.types.catalog_schema_change_policy

        out["SchemaChangePolicy"] = (
            capo_glue.types.catalog_schema_change_policy.serialize_aws_json_1_1(
                value["schema_change_policy"]
            )
        )
    if "auto_data_quality" in value:
        import capo_glue.types.auto_data_quality

        out["AutoDataQuality"] = (
            capo_glue.types.auto_data_quality.serialize_aws_json_1_1(
                value["auto_data_quality"]
            )
        )
    if "output_schemas" in value:
        import capo_glue.types.glue_schemas

        out["OutputSchemas"] = capo_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3HudiCatalogTarget:
    out: S3HudiCatalogTarget = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Inputs") is not None:
        import capo_glue.types.one_input

        out["inputs"] = capo_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        out["inputs"] = []
    if data.get("PartitionKeys") is not None:
        import capo_glue.types.glue_studio_path_list

        out["partition_keys"] = (
            capo_glue.types.glue_studio_path_list.deserialize_aws_json_1_1(
                data["PartitionKeys"]
            )
        )
    if data.get("Table") is not None:
        out["table"] = data["Table"]
    else:
        out["table"] = ""
    if data.get("Database") is not None:
        out["database"] = data["Database"]
    else:
        out["database"] = ""
    if data.get("AdditionalOptions") is not None:
        import capo_glue.types.additional_options

        out["additional_options"] = (
            capo_glue.types.additional_options.deserialize_aws_json_1_1(
                data["AdditionalOptions"]
            )
        )
    else:
        out["additional_options"] = {}
    if data.get("SchemaChangePolicy") is not None:
        import capo_glue.types.catalog_schema_change_policy

        out["schema_change_policy"] = (
            capo_glue.types.catalog_schema_change_policy.deserialize_aws_json_1_1(
                data["SchemaChangePolicy"]
            )
        )
    if data.get("AutoDataQuality") is not None:
        import capo_glue.types.auto_data_quality

        out["auto_data_quality"] = (
            capo_glue.types.auto_data_quality.deserialize_aws_json_1_1(
                data["AutoDataQuality"]
            )
        )
    if data.get("OutputSchemas") is not None:
        import capo_glue.types.glue_schemas

        out["output_schemas"] = capo_glue.types.glue_schemas.deserialize_aws_json_1_1(
            data["OutputSchemas"]
        )
    return out
