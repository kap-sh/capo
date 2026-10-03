"""Generated from Smithy shape ``com.amazonaws.kms#EnableKeyRotationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kms.types.key_id_type
    import capo_kms.types.rotation_period_in_days_type


class EnableKeyRotationRequest(TypedDict, closed=True):
    key_id: "capo_kms.types.key_id_type.KeyIdType"
    """<p>Identifies a symmetric encryption KMS key. You cannot enable automatic rotation of <a href="https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html">asymmetric KMS keys</a>, <a href="https://docs.aws.amazon.com/kms/latest/developerguide/hmac.html">HMAC KMS keys</a>, KMS keys with <a href="https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html">imported key material</a>, or KMS keys in a <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html">custom key store</a>. To enable or disable automatic rotation of a set of related <a href="https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html#multi-region-rotate">multi-Region keys</a>, set the property on the primary key.</p> <p>Specify the key ID or key ARN of the KMS key.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p>"""
    rotation_period_in_days: NotRequired[
        "capo_kms.types.rotation_period_in_days_type.RotationPeriodInDaysType"
    ]
    """<p>Use this parameter to specify a custom period of time between each rotation date. If no value is specified, the default value is 365 days.</p> <p>The rotation period defines the number of days after you enable automatic key rotation that KMS will rotate your key material, and the number of days between each automatic rotation thereafter.</p> <p>You can use the <a href="https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-rotation-period-in-days"> <code>kms:RotationPeriodInDays</code> </a> condition key to further constrain the values that principals can specify in the <code>RotationPeriodInDays</code> parameter.</p> <p> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableKeyRotationRequest) -> dict:
    out: dict = {}
    out["KeyId"] = value["key_id"]
    if "rotation_period_in_days" in value:
        out["RotationPeriodInDays"] = value["rotation_period_in_days"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableKeyRotationRequest:
    out: EnableKeyRotationRequest = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    else:
        raise DeserializationError("EnableKeyRotationRequest.key_id required")
    if data.get("RotationPeriodInDays") is not None:
        out["rotation_period_in_days"] = data["RotationPeriodInDays"]
    return out
