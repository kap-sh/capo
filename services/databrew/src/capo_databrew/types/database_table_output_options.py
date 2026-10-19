"""Generated from Smithy shape ``com.amazonaws.databrew#DatabaseTableOutputOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.database_table_name
    import capo_databrew.types.s3_location


class DatabaseTableOutputOptions(TypedDict, closed=True):
    temp_directory: NotRequired["capo_databrew.types.s3_location.S3Location"]
    """<p>Represents an Amazon S3 location (bucket name and object key) where DataBrew can store intermediate results.</p>"""
    table_name: "capo_databrew.types.database_table_name.DatabaseTableName"
    """<p>A prefix for the name of a table DataBrew will create in the database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseTableOutputOptions) -> dict:
    out: dict = {}
    if "temp_directory" in value:
        import capo_databrew.types.s3_location

        out["TempDirectory"] = capo_databrew.types.s3_location.serialize_json(
            value["temp_directory"]
        )
    out["TableName"] = value["table_name"]
    return out


def deserialize_json(data: dict) -> DatabaseTableOutputOptions:
    out: DatabaseTableOutputOptions = {}  # type: ignore[typeddict-item]
    if data.get("TempDirectory") is not None:
        import capo_databrew.types.s3_location

        out["temp_directory"] = capo_databrew.types.s3_location.deserialize_json(
            data["TempDirectory"]
        )
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    return out
