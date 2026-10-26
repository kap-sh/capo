"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveRetention``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError
from capo_mailmanager.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mailmanager.types.retention_period


class _ArchiveRetention_RetentionPeriod(TypedDict, closed=True):
    RetentionPeriod: "capo_mailmanager.types.retention_period.RetentionPeriod"


ArchiveRetention: TypeAlias = _ArchiveRetention_RetentionPeriod | UnknownUnionMember


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArchiveRetention) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ArchiveRetention: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "RetentionPeriod" in value:
        import capo_mailmanager.types.retention_period

        return {
            "RetentionPeriod": capo_mailmanager.types.retention_period.serialize_aws_json_1_0(
                value["RetentionPeriod"]
            )
        }
    else:
        raise SerializationError("ArchiveRetention: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ArchiveRetention:
    if data.get("RetentionPeriod") is not None:
        import capo_mailmanager.types.retention_period

        return {
            "RetentionPeriod": capo_mailmanager.types.retention_period.deserialize_aws_json_1_0(
                data["RetentionPeriod"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ArchiveRetention: no recognized variant key")
