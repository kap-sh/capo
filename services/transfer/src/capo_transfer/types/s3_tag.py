"""Generated from Smithy shape ``com.amazonaws.transfer#S3Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.s3_tag_key
    import capo_transfer.types.s3_tag_value


class S3Tag(TypedDict, closed=True):
    key: "capo_transfer.types.s3_tag_key.S3TagKey"
    """<p>The name assigned to the tag that you create.</p>"""
    value: "capo_transfer.types.s3_tag_value.S3TagValue"
    """<p>The value that corresponds to the key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Tag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Tag:
    out: S3Tag = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
