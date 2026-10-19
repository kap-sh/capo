"""Generated from Smithy shape ``com.amazonaws.support#CompletedUpload``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_support.types.e_tag
    import capo_support.types.field_integer_value


class CompletedUpload(TypedDict, closed=True):
    part_index: "capo_support.types.field_integer_value.FieldIntegerValue"
    """<p>The index of the uploaded part. This is the same <code>partIndex</code> value returned for the corresponding entry in the <code>uploadUrls</code> field of the <code>GetAttachmentUploadLinks</code> response.</p>"""
    e_tag: "capo_support.types.e_tag.ETag"
    """<p>The ETag returned in the response headers when the part was uploaded to Amazon S3. The <code>ETag</code> value identifies the part contents.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompletedUpload) -> dict:
    out: dict = {}
    out["partIndex"] = value["part_index"]
    out["eTag"] = value["e_tag"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CompletedUpload:
    out: CompletedUpload = {}  # type: ignore[typeddict-item]
    if data.get("partIndex") is not None:
        out["part_index"] = data["partIndex"]
    else:
        out["part_index"] = 0
    if data.get("eTag") is not None:
        out["e_tag"] = data["eTag"]
    else:
        out["e_tag"] = ""
    return out
