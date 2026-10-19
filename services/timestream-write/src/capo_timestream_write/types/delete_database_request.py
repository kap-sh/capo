"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#DeleteDatabaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.resource_name


class DeleteDatabaseRequest(TypedDict, closed=True):
    database_name: "capo_timestream_write.types.resource_name.ResourceName"
    """<p>The name of the Timestream database to be deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteDatabaseRequest) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteDatabaseRequest:
    out: DeleteDatabaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    return out
