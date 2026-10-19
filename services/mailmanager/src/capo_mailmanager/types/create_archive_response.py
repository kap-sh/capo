"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateArchiveResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.archive_id_string


class CreateArchiveResponse(TypedDict, closed=True):
    archive_id: "capo_mailmanager.types.archive_id_string.ArchiveIdString"
    """<p>The unique identifier for the newly created archive.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateArchiveResponse) -> dict:
    out: dict = {}
    out["ArchiveId"] = value["archive_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateArchiveResponse:
    out: CreateArchiveResponse = {}  # type: ignore[typeddict-item]
    if data.get("ArchiveId") is not None:
        out["archive_id"] = data["ArchiveId"]
    else:
        out["archive_id"] = ""
    return out
