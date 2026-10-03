"""Generated from Smithy shape ``com.amazonaws.kms#ScheduleKeyDeletionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kms.types.key_id_type
    import capo_kms.types.pending_window_in_days_type


class ScheduleKeyDeletionRequest(TypedDict, closed=True):
    key_id: "capo_kms.types.key_id_type.KeyIdType"
    """<p>The unique identifier of the KMS key to delete.</p> <p>Specify the key ID or key ARN of the KMS key.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p>"""
    pending_window_in_days: NotRequired[
        "capo_kms.types.pending_window_in_days_type.PendingWindowInDaysType"
    ]
    """<p>The waiting period, specified in number of days. After the waiting period ends, KMS deletes the KMS key.</p> <p>If the KMS key is a multi-Region primary key with replica keys, the waiting period begins when the last of its replica keys is deleted. Otherwise, the waiting period begins immediately.</p> <p>This value is optional. If you include a value, it must be between 7 and 30, inclusive. If you do not include a value, it defaults to 30. You can use the <a href="https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-schedule-key-deletion-pending-window-in-days"> <code>kms:ScheduleKeyDeletionPendingWindowInDays</code> </a> condition key to further constrain the values that principals can specify in the <code>PendingWindowInDays</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduleKeyDeletionRequest) -> dict:
    out: dict = {}
    out["KeyId"] = value["key_id"]
    if "pending_window_in_days" in value:
        out["PendingWindowInDays"] = value["pending_window_in_days"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScheduleKeyDeletionRequest:
    out: ScheduleKeyDeletionRequest = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    else:
        raise DeserializationError("ScheduleKeyDeletionRequest.key_id required")
    if data.get("PendingWindowInDays") is not None:
        out["pending_window_in_days"] = data["PendingWindowInDays"]
    return out
