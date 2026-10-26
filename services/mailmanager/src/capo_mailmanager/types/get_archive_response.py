"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetArchiveResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mailmanager.types.archive_arn
    import capo_mailmanager.types.archive_id_string
    import capo_mailmanager.types.archive_name_string
    import capo_mailmanager.types.archive_retention
    import capo_mailmanager.types.archive_state
    import capo_mailmanager.types.kms_key_arn


class GetArchiveResponse(TypedDict, closed=True):
    archive_id: "capo_mailmanager.types.archive_id_string.ArchiveIdString"
    """<p>The unique identifier of the archive.</p>"""
    archive_name: "capo_mailmanager.types.archive_name_string.ArchiveNameString"
    """<p>The unique name assigned to the archive.</p>"""
    archive_arn: "capo_mailmanager.types.archive_arn.ArchiveArn"
    """<p>The Amazon Resource Name (ARN) of the archive.</p>"""
    archive_state: "capo_mailmanager.types.archive_state.ArchiveState"
    """<p>The current state of the archive:</p> <ul> <li> <p> <code>ACTIVE</code> – The archive is ready and available for use. </p> </li> <li> <p> <code>PENDING_DELETION</code> – The archive has been marked for deletion and will be permanently deleted in 30 days. No further modifications can be made in this state. </p> </li> </ul>"""
    retention: "capo_mailmanager.types.archive_retention.ArchiveRetention"
    """<p>The retention period for emails in this archive.</p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the archive was created.</p>"""
    last_updated_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the archive was modified.</p>"""
    kms_key_arn: NotRequired["capo_mailmanager.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the archive.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetArchiveResponse) -> dict:
    out: dict = {}
    out["ArchiveId"] = value["archive_id"]
    out["ArchiveName"] = value["archive_name"]
    out["ArchiveArn"] = value["archive_arn"]
    import capo_mailmanager.types.archive_state

    out["ArchiveState"] = capo_mailmanager.types.archive_state.serialize_aws_json_1_0(
        value["archive_state"]
    )
    import capo_mailmanager.types.archive_retention

    out["Retention"] = capo_mailmanager.types.archive_retention.serialize_aws_json_1_0(
        value["retention"]
    )
    if "created_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["CreatedTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["LastUpdatedTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_updated_timestamp"]
            )
        )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetArchiveResponse:
    out: GetArchiveResponse = {}  # type: ignore[typeddict-item]
    if data.get("ArchiveId") is not None:
        out["archive_id"] = data["ArchiveId"]
    else:
        out["archive_id"] = ""
    if data.get("ArchiveName") is not None:
        out["archive_name"] = data["ArchiveName"]
    else:
        out["archive_name"] = ""
    if data.get("ArchiveArn") is not None:
        out["archive_arn"] = data["ArchiveArn"]
    else:
        out["archive_arn"] = ""
    if data.get("ArchiveState") is not None:
        import capo_mailmanager.types.archive_state

        out["archive_state"] = (
            capo_mailmanager.types.archive_state.deserialize_aws_json_1_0(
                data["ArchiveState"]
            )
        )
    else:
        import typing

        out["archive_state"] = typing.cast(
            "capo_mailmanager.types.archive_state.ArchiveState", ""
        )
    if data.get("Retention") is not None:
        import capo_mailmanager.types.archive_retention

        out["retention"] = (
            capo_mailmanager.types.archive_retention.deserialize_aws_json_1_0(
                data["Retention"]
            )
        )
    else:
        out["retention"] = {"$unknown": {"name": ""}}
    if data.get("CreatedTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    if data.get("LastUpdatedTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["last_updated_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["LastUpdatedTimestamp"]
            )
        )
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out
