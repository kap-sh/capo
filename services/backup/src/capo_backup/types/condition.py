"""Generated from Smithy shape ``com.amazonaws.backup#Condition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.condition_key
    import capo_backup.types.condition_type
    import capo_backup.types.condition_value


class Condition(TypedDict, closed=True):
    condition_type: "capo_backup.types.condition_type.ConditionType"
    """<p>An operation applied to a key-value pair used to assign resources to your backup plan. Condition only supports <code>StringEquals</code>. For more flexible assignment options, including <code>StringLike</code> and the ability to exclude resources from your backup plan, use <code>Conditions</code> (with an "s" on the end) for your <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BackupSelection.html"> <code>BackupSelection</code> </a>.</p>"""
    condition_key: "capo_backup.types.condition_key.ConditionKey"
    """<p>The key in a key-value pair. For example, in the tag <code>Department: Accounting</code>, <code>Department</code> is the key.</p>"""
    condition_value: "capo_backup.types.condition_value.ConditionValue"
    """<p>The value in a key-value pair. For example, in the tag <code>Department: Accounting</code>, <code>Accounting</code> is the value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Condition) -> dict:
    out: dict = {}
    import capo_backup.types.condition_type

    out["ConditionType"] = capo_backup.types.condition_type.serialize_json(
        value["condition_type"]
    )
    out["ConditionKey"] = value["condition_key"]
    out["ConditionValue"] = value["condition_value"]
    return out


def deserialize_json(data: dict) -> Condition:
    out: Condition = {}  # type: ignore[typeddict-item]
    if data.get("ConditionType") is not None:
        import capo_backup.types.condition_type

        out["condition_type"] = capo_backup.types.condition_type.deserialize_json(
            data["ConditionType"]
        )
    else:
        raise DeserializationError("Condition.condition_type required")
    if data.get("ConditionKey") is not None:
        out["condition_key"] = data["ConditionKey"]
    else:
        raise DeserializationError("Condition.condition_key required")
    if data.get("ConditionValue") is not None:
        out["condition_value"] = data["ConditionValue"]
    else:
        raise DeserializationError("Condition.condition_value required")
    return out
