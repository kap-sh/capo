"""Generated from Smithy shape ``com.amazonaws.kms#UpdateKeyDescriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kms.types.description_type
    import capo_kms.types.key_id_type


class UpdateKeyDescriptionRequest(TypedDict, closed=True):
    key_id: "capo_kms.types.key_id_type.KeyIdType"
    """<p>Updates the description of the specified KMS key.</p> <p>Specify the key ID or key ARN of the KMS key.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p>"""
    description: "capo_kms.types.description_type.DescriptionType"
    """<p>New description for the KMS key.</p> <important> <p>Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateKeyDescriptionRequest) -> dict:
    out: dict = {}
    out["KeyId"] = value["key_id"]
    out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateKeyDescriptionRequest:
    out: UpdateKeyDescriptionRequest = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    else:
        out["key_id"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        out["description"] = ""
    return out
