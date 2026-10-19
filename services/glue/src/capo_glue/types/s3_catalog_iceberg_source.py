"""Generated from Smithy shape ``com.amazonaws.glue#S3CatalogIcebergSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.additional_options
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.glue_schemas
    import capo_glue.types.node_name


class S3CatalogIcebergSource(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the Iceberg data source.</p>"""
    database: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the database to read from.</p>"""
    table: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the table in the database to read from.</p>"""
    additional_iceberg_options: NotRequired[
        "capo_glue.types.additional_options.AdditionalOptions"
    ]
    """<p>Specifies additional connection options for the Iceberg data source.</p>"""
    output_schemas: NotRequired["capo_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the Iceberg source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3CatalogIcebergSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Database"] = value["database"]
    out["Table"] = value["table"]
    if "additional_iceberg_options" in value:
        import capo_glue.types.additional_options

        out["AdditionalIcebergOptions"] = (
            capo_glue.types.additional_options.serialize_aws_json_1_1(
                value["additional_iceberg_options"]
            )
        )
    if "output_schemas" in value:
        import capo_glue.types.glue_schemas

        out["OutputSchemas"] = capo_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3CatalogIcebergSource:
    out: S3CatalogIcebergSource = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Database") is not None:
        out["database"] = data["Database"]
    else:
        out["database"] = ""
    if data.get("Table") is not None:
        out["table"] = data["Table"]
    else:
        out["table"] = ""
    if data.get("AdditionalIcebergOptions") is not None:
        import capo_glue.types.additional_options

        out["additional_iceberg_options"] = (
            capo_glue.types.additional_options.deserialize_aws_json_1_1(
                data["AdditionalIcebergOptions"]
            )
        )
    if data.get("OutputSchemas") is not None:
        import capo_glue.types.glue_schemas

        out["output_schemas"] = capo_glue.types.glue_schemas.deserialize_aws_json_1_1(
            data["OutputSchemas"]
        )
    return out
