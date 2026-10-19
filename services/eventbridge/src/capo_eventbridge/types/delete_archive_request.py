"""Generated from Smithy shape ``com.amazonaws.eventbridge#DeleteArchiveRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.archive_name


class DeleteArchiveRequest(TypedDict, closed=True):
    archive_name: "capo_eventbridge.types.archive_name.ArchiveName"
    """<p>The name of the archive to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteArchiveRequest) -> dict:
    out: dict = {}
    out["ArchiveName"] = value["archive_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteArchiveRequest:
    out: DeleteArchiveRequest = {}  # type: ignore[typeddict-item]
    if data.get("ArchiveName") is not None:
        out["archive_name"] = data["ArchiveName"]
    else:
        out["archive_name"] = ""
    return out
