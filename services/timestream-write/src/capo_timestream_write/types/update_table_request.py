"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#UpdateTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.magnetic_store_write_properties
    import capo_timestream_write.types.resource_name
    import capo_timestream_write.types.retention_properties
    import capo_timestream_write.types.schema


class UpdateTableRequest(TypedDict, closed=True):
    database_name: "capo_timestream_write.types.resource_name.ResourceName"
    """<p>The name of the Timestream database.</p>"""
    table_name: "capo_timestream_write.types.resource_name.ResourceName"
    """<p>The name of the Timestream table.</p>"""
    retention_properties: NotRequired[
        "capo_timestream_write.types.retention_properties.RetentionProperties"
    ]
    """<p>The retention duration of the memory store and the magnetic store.</p>"""
    magnetic_store_write_properties: NotRequired[
        "capo_timestream_write.types.magnetic_store_write_properties.MagneticStoreWriteProperties"
    ]
    """<p>Contains properties to set on the table when enabling magnetic store writes.</p>"""
    schema: NotRequired["capo_timestream_write.types.schema.Schema"]
    """<p> The schema of the table. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateTableRequest) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    if "retention_properties" in value:
        import capo_timestream_write.types.retention_properties

        out["RetentionProperties"] = (
            capo_timestream_write.types.retention_properties.serialize_aws_json_1_0(
                value["retention_properties"]
            )
        )
    if "magnetic_store_write_properties" in value:
        import capo_timestream_write.types.magnetic_store_write_properties

        out["MagneticStoreWriteProperties"] = (
            capo_timestream_write.types.magnetic_store_write_properties.serialize_aws_json_1_0(
                value["magnetic_store_write_properties"]
            )
        )
    if "schema" in value:
        import capo_timestream_write.types.schema

        out["Schema"] = capo_timestream_write.types.schema.serialize_aws_json_1_0(
            value["schema"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateTableRequest:
    out: UpdateTableRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("RetentionProperties") is not None:
        import capo_timestream_write.types.retention_properties

        out["retention_properties"] = (
            capo_timestream_write.types.retention_properties.deserialize_aws_json_1_0(
                data["RetentionProperties"]
            )
        )
    if data.get("MagneticStoreWriteProperties") is not None:
        import capo_timestream_write.types.magnetic_store_write_properties

        out["magnetic_store_write_properties"] = (
            capo_timestream_write.types.magnetic_store_write_properties.deserialize_aws_json_1_0(
                data["MagneticStoreWriteProperties"]
            )
        )
    if data.get("Schema") is not None:
        import capo_timestream_write.types.schema

        out["schema"] = capo_timestream_write.types.schema.deserialize_aws_json_1_0(
            data["Schema"]
        )
    return out
