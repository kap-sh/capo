"""Generated from Smithy shape ``com.amazonaws.kms#ScheduleKeyDeletionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.date_type
    import capo_kms.types.key_id_type
    import capo_kms.types.key_state
    import capo_kms.types.pending_window_in_days_type


class ScheduleKeyDeletionResponse(TypedDict, closed=True):
    key_id: NotRequired["capo_kms.types.key_id_type.KeyIdType"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN">key ARN</a>) of the KMS key whose deletion is scheduled.</p>"""
    deletion_date: NotRequired["capo_kms.types.date_type.DateType"]
    """<p>The date and time after which KMS deletes the KMS key.</p> <p>If the KMS key is a multi-Region primary key with replica keys, this field does not appear. The deletion date for the primary key isn't known until its last replica key is deleted.</p>"""
    key_state: NotRequired["capo_kms.types.key_state.KeyState"]
    """<p>The current status of the KMS key.</p> <p>For more information about how key state affects the use of a KMS key, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html">Key states of KMS keys</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    pending_window_in_days: NotRequired[
        "capo_kms.types.pending_window_in_days_type.PendingWindowInDaysType"
    ]
    """<p>The waiting period before the KMS key is deleted. </p> <p>If the KMS key is a multi-Region primary key with replicas, the waiting period begins when the last of its replica keys is deleted. Otherwise, the waiting period begins immediately.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduleKeyDeletionResponse) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "deletion_date" in value:
        import capo_kms.types.date_type

        out["DeletionDate"] = capo_kms.types.date_type.serialize_aws_json_1_1(
            value["deletion_date"]
        )
    if "key_state" in value:
        import capo_kms.types.key_state

        out["KeyState"] = capo_kms.types.key_state.serialize_aws_json_1_1(
            value["key_state"]
        )
    if "pending_window_in_days" in value:
        out["PendingWindowInDays"] = value["pending_window_in_days"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScheduleKeyDeletionResponse:
    out: ScheduleKeyDeletionResponse = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    if data.get("DeletionDate") is not None:
        import capo_kms.types.date_type

        out["deletion_date"] = capo_kms.types.date_type.deserialize_aws_json_1_1(
            data["DeletionDate"]
        )
    if data.get("KeyState") is not None:
        import capo_kms.types.key_state

        out["key_state"] = capo_kms.types.key_state.deserialize_aws_json_1_1(
            data["KeyState"]
        )
    if data.get("PendingWindowInDays") is not None:
        out["pending_window_in_days"] = data["PendingWindowInDays"]
    return out
