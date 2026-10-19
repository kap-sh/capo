"""Generated from Smithy shape ``com.amazonaws.glue#IcebergInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.create_iceberg_table_input
    import capo_glue.types.metadata_operation
    import capo_glue.types.version_string


class IcebergInput(TypedDict, closed=True):
    metadata_operation: "capo_glue.types.metadata_operation.MetadataOperation"
    """<p>A required metadata operation. Can only be set to <code>CREATE</code>.</p>"""
    version: NotRequired["capo_glue.types.version_string.VersionString"]
    """<p>The table version for the Iceberg table. Defaults to 2.</p>"""
    create_iceberg_table_input: NotRequired[
        "capo_glue.types.create_iceberg_table_input.CreateIcebergTableInput"
    ]
    """<p>The configuration parameters required to create a new Iceberg table in the Glue Data Catalog, including table properties and metadata specifications.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergInput) -> dict:
    out: dict = {}
    import capo_glue.types.metadata_operation

    out["MetadataOperation"] = (
        capo_glue.types.metadata_operation.serialize_aws_json_1_1(
            value["metadata_operation"]
        )
    )
    if "version" in value:
        out["Version"] = value["version"]
    if "create_iceberg_table_input" in value:
        import capo_glue.types.create_iceberg_table_input

        out["CreateIcebergTableInput"] = (
            capo_glue.types.create_iceberg_table_input.serialize_aws_json_1_1(
                value["create_iceberg_table_input"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergInput:
    out: IcebergInput = {}  # type: ignore[typeddict-item]
    if data.get("MetadataOperation") is not None:
        import capo_glue.types.metadata_operation

        out["metadata_operation"] = (
            capo_glue.types.metadata_operation.deserialize_aws_json_1_1(
                data["MetadataOperation"]
            )
        )
    else:
        import typing

        out["metadata_operation"] = typing.cast(
            "capo_glue.types.metadata_operation.MetadataOperation", ""
        )
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("CreateIcebergTableInput") is not None:
        import capo_glue.types.create_iceberg_table_input

        out["create_iceberg_table_input"] = (
            capo_glue.types.create_iceberg_table_input.deserialize_aws_json_1_1(
                data["CreateIcebergTableInput"]
            )
        )
    return out
