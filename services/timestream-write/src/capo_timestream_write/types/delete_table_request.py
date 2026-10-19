"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#DeleteTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.resource_name


class DeleteTableRequest(TypedDict, closed=True):
    database_name: "capo_timestream_write.types.resource_name.ResourceName"
    """<p>The name of the database where the Timestream database is to be deleted.</p>"""
    table_name: "capo_timestream_write.types.resource_name.ResourceName"
    """<p>The name of the Timestream table to be deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteTableRequest) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteTableRequest:
    out: DeleteTableRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    return out
