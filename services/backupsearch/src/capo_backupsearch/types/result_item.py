"""Generated from Smithy shape ``com.amazonaws.backupsearch#ResultItem``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_backupsearch.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_backupsearch.types.ebs_result_item
    import capo_backupsearch.types.s3_result_item


class _ResultItem_S3ResultItem(TypedDict, closed=True):
    S3ResultItem: "capo_backupsearch.types.s3_result_item.S3ResultItem"


class _ResultItem_EBSResultItem(TypedDict, closed=True):
    EBSResultItem: "capo_backupsearch.types.ebs_result_item.EBSResultItem"


ResultItem: TypeAlias = _ResultItem_S3ResultItem | _ResultItem_EBSResultItem


# --- restJson1 ser/de ---
def serialize_json(value: ResultItem) -> dict:
    if "S3ResultItem" in value:
        import capo_backupsearch.types.s3_result_item

        return {
            "S3ResultItem": capo_backupsearch.types.s3_result_item.serialize_json(
                value["S3ResultItem"]
            )
        }
    elif "EBSResultItem" in value:
        import capo_backupsearch.types.ebs_result_item

        return {
            "EBSResultItem": capo_backupsearch.types.ebs_result_item.serialize_json(
                value["EBSResultItem"]
            )
        }
    else:
        raise SerializationError("ResultItem: no variant present")


def deserialize_json(data: dict) -> ResultItem:
    if data.get("S3ResultItem") is not None:
        import capo_backupsearch.types.s3_result_item

        return {
            "S3ResultItem": capo_backupsearch.types.s3_result_item.deserialize_json(
                data["S3ResultItem"]
            )
        }
    elif data.get("EBSResultItem") is not None:
        import capo_backupsearch.types.ebs_result_item

        return {
            "EBSResultItem": capo_backupsearch.types.ebs_result_item.deserialize_json(
                data["EBSResultItem"]
            )
        }
    else:
        raise DeserializationError("ResultItem: no recognized variant key")


def redact_sensitive(value: ResultItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "S3ResultItem" in value:
        import capo_backupsearch.types.s3_result_item

        out["S3ResultItem"] = capo_backupsearch.types.s3_result_item.redact_sensitive(
            value["S3ResultItem"]
        )
    if "EBSResultItem" in value:
        import capo_backupsearch.types.ebs_result_item

        out["EBSResultItem"] = capo_backupsearch.types.ebs_result_item.redact_sensitive(
            value["EBSResultItem"]
        )
    return out
