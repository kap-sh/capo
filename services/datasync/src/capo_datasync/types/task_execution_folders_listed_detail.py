"""Generated from Smithy shape ``com.amazonaws.datasync#TaskExecutionFoldersListedDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.long


class TaskExecutionFoldersListedDetail(TypedDict, closed=True):
    at_source: "capo_datasync.types.long.long"
    """<p>The number of directories that DataSync finds at your source location.</p> <ul> <li> <p>With a <a href="https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html">manifest</a>, DataSync lists only what's in your manifest (and not everything at your source location).</p> </li> <li> <p>With an include <a href="https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html">filter</a>, DataSync lists only what matches the filter at your source location.</p> </li> <li> <p>With an exclude filter, DataSync lists everything at your source location before applying the filter.</p> </li> </ul>"""
    at_destination_for_delete: "capo_datasync.types.long.long"
    """<p>The number of directories that DataSync finds at your destination location. This counter is only applicable if you <a href="https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html#task-option-file-object-handling">configure your task</a> to delete data in the destination that isn't in the source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskExecutionFoldersListedDetail) -> dict:
    out: dict = {}
    out["AtSource"] = value.get("at_source", 0)
    out["AtDestinationForDelete"] = value.get("at_destination_for_delete", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskExecutionFoldersListedDetail:
    out: TaskExecutionFoldersListedDetail = {}  # type: ignore[typeddict-item]
    if data.get("AtSource") is not None:
        out["at_source"] = data["AtSource"]
    else:
        out["at_source"] = 0
    if data.get("AtDestinationForDelete") is not None:
        out["at_destination_for_delete"] = data["AtDestinationForDelete"]
    else:
        out["at_destination_for_delete"] = 0
    return out
