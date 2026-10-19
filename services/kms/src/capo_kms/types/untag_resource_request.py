"""Generated from Smithy shape ``com.amazonaws.kms#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kms.types.key_id_type
    import capo_kms.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    key_id: "capo_kms.types.key_id_type.KeyIdType"
    """<p>Identifies the KMS key from which you are removing tags.</p> <p>Specify the key ID or key ARN of the KMS key.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p>"""
    tag_keys: "capo_kms.types.tag_key_list.TagKeyList"
    """<p>One or more tag keys. Specify only the tag keys, not the tag values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["KeyId"] = value["key_id"]
    import capo_kms.types.tag_key_list

    out["TagKeys"] = capo_kms.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    else:
        out["key_id"] = ""
    if data.get("TagKeys") is not None:
        import capo_kms.types.tag_key_list

        out["tag_keys"] = capo_kms.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
