"""Generated from Smithy shape ``com.amazonaws.storagegateway#CreateTapePoolInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.pool_name
    import capo_storage_gateway.types.retention_lock_time_in_days
    import capo_storage_gateway.types.retention_lock_type
    import capo_storage_gateway.types.tags
    import capo_storage_gateway.types.tape_storage_class


class CreateTapePoolInput(TypedDict, closed=True):
    pool_name: "capo_storage_gateway.types.pool_name.PoolName"
    """<p>The name of the new custom tape pool.</p>"""
    storage_class: "capo_storage_gateway.types.tape_storage_class.TapeStorageClass"
    """<p>The storage class that is associated with the new custom pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.</p>"""
    retention_lock_type: NotRequired[
        "capo_storage_gateway.types.retention_lock_type.RetentionLockType"
    ]
    """<p>Tape retention lock can be configured in two modes. When configured in governance mode, Amazon Web Services accounts with specific IAM permissions are authorized to remove the tape retention lock from archived virtual tapes. When configured in compliance mode, the tape retention lock cannot be removed by any user, including the root Amazon Web Services account.</p>"""
    retention_lock_time_in_days: NotRequired[
        "capo_storage_gateway.types.retention_lock_time_in_days.RetentionLockTimeInDays"
    ]
    """<p>Tape retention lock time is set in days. Tape retention lock can be enabled for up to 100 years (36,500 days).</p>"""
    tags: NotRequired["capo_storage_gateway.types.tags.Tags"]
    """<p>A list of up to 50 tags that can be assigned to tape pool. Each tag is a key-value pair.</p> <note> <p>Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTapePoolInput) -> dict:
    out: dict = {}
    out["PoolName"] = value["pool_name"]
    import capo_storage_gateway.types.tape_storage_class

    out["StorageClass"] = (
        capo_storage_gateway.types.tape_storage_class.serialize_aws_json_1_1(
            value["storage_class"]
        )
    )
    if "retention_lock_type" in value:
        import capo_storage_gateway.types.retention_lock_type

        out["RetentionLockType"] = (
            capo_storage_gateway.types.retention_lock_type.serialize_aws_json_1_1(
                value["retention_lock_type"]
            )
        )
    if "retention_lock_time_in_days" in value:
        out["RetentionLockTimeInDays"] = value["retention_lock_time_in_days"]
    if "tags" in value:
        import capo_storage_gateway.types.tags

        out["Tags"] = capo_storage_gateway.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTapePoolInput:
    out: CreateTapePoolInput = {}  # type: ignore[typeddict-item]
    if data.get("PoolName") is not None:
        out["pool_name"] = data["PoolName"]
    else:
        out["pool_name"] = ""
    if data.get("StorageClass") is not None:
        import capo_storage_gateway.types.tape_storage_class

        out["storage_class"] = (
            capo_storage_gateway.types.tape_storage_class.deserialize_aws_json_1_1(
                data["StorageClass"]
            )
        )
    else:
        import typing

        out["storage_class"] = typing.cast(
            "capo_storage_gateway.types.tape_storage_class.TapeStorageClass", ""
        )
    if data.get("RetentionLockType") is not None:
        import capo_storage_gateway.types.retention_lock_type

        out["retention_lock_type"] = (
            capo_storage_gateway.types.retention_lock_type.deserialize_aws_json_1_1(
                data["RetentionLockType"]
            )
        )
    if data.get("RetentionLockTimeInDays") is not None:
        out["retention_lock_time_in_days"] = data["RetentionLockTimeInDays"]
    if data.get("Tags") is not None:
        import capo_storage_gateway.types.tags

        out["tags"] = capo_storage_gateway.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
