"""Generated from Smithy shape ``com.amazonaws.mailmanager#UpdateArchiveRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.archive_id_string
    import capo_mailmanager.types.archive_name_string
    import capo_mailmanager.types.archive_retention


class UpdateArchiveRequest(TypedDict, closed=True):
    archive_id: "capo_mailmanager.types.archive_id_string.ArchiveIdString"
    """<p>The identifier of the archive to update.</p>"""
    archive_name: NotRequired[
        "capo_mailmanager.types.archive_name_string.ArchiveNameString"
    ]
    """<p>A new, unique name for the archive.</p>"""
    retention: NotRequired["capo_mailmanager.types.archive_retention.ArchiveRetention"]
    """<p>A new retention period for emails in the archive.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateArchiveRequest) -> dict:
    out: dict = {}
    out["ArchiveId"] = value["archive_id"]
    if "archive_name" in value:
        out["ArchiveName"] = value["archive_name"]
    if "retention" in value:
        import capo_mailmanager.types.archive_retention

        out["Retention"] = (
            capo_mailmanager.types.archive_retention.serialize_aws_json_1_0(
                value["retention"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateArchiveRequest:
    out: UpdateArchiveRequest = {}  # type: ignore[typeddict-item]
    if data.get("ArchiveId") is not None:
        out["archive_id"] = data["ArchiveId"]
    else:
        out["archive_id"] = ""
    if data.get("ArchiveName") is not None:
        out["archive_name"] = data["ArchiveName"]
    if data.get("Retention") is not None:
        import capo_mailmanager.types.archive_retention

        out["retention"] = (
            capo_mailmanager.types.archive_retention.deserialize_aws_json_1_0(
                data["Retention"]
            )
        )
    return out
