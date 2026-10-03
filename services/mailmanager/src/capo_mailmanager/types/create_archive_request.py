"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateArchiveRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.archive_name_string
    import capo_mailmanager.types.archive_retention
    import capo_mailmanager.types.idempotency_token
    import capo_mailmanager.types.kms_key_arn
    import capo_mailmanager.types.tag_list


class CreateArchiveRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_mailmanager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique token Amazon SES uses to recognize retries of this request.</p>"""
    archive_name: "capo_mailmanager.types.archive_name_string.ArchiveNameString"
    """<p>A unique name for the new archive.</p>"""
    retention: NotRequired["capo_mailmanager.types.archive_retention.ArchiveRetention"]
    """<p>The period for retaining emails in the archive before automatic deletion.</p>"""
    kms_key_arn: NotRequired["capo_mailmanager.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key for encrypting emails in the archive.</p>"""
    tags: NotRequired["capo_mailmanager.types.tag_list.TagList"]
    """<p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateArchiveRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["ArchiveName"] = value["archive_name"]
    if "retention" in value:
        import capo_mailmanager.types.archive_retention

        out["Retention"] = (
            capo_mailmanager.types.archive_retention.serialize_aws_json_1_0(
                value["retention"]
            )
        )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "tags" in value:
        import capo_mailmanager.types.tag_list

        out["Tags"] = capo_mailmanager.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateArchiveRequest:
    out: CreateArchiveRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("ArchiveName") is not None:
        out["archive_name"] = data["ArchiveName"]
    else:
        raise DeserializationError("CreateArchiveRequest.archive_name required")
    if data.get("Retention") is not None:
        import capo_mailmanager.types.archive_retention

        out["retention"] = (
            capo_mailmanager.types.archive_retention.deserialize_aws_json_1_0(
                data["Retention"]
            )
        )
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if data.get("Tags") is not None:
        import capo_mailmanager.types.tag_list

        out["tags"] = capo_mailmanager.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
