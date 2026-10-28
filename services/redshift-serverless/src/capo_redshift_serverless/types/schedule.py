"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#Schedule``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_redshift_serverless.errors import DeserializationError, SerializationError
from capo_redshift_serverless.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import datetime


class ScheduleAtMember(TypedDict, closed=True):
    at: "datetime.datetime"


class ScheduleCronMember(TypedDict, closed=True):
    cron: "str"


Schedule: TypeAlias = ScheduleAtMember | ScheduleCronMember | UnknownUnionMember


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Schedule) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Schedule: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "at" in value:
        import capo_redshift_serverless.types._prelude.timestamp

        return {
            "at": capo_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["at"]
            )
        }
    elif "cron" in value:
        return {"cron": value["cron"]}
    else:
        raise SerializationError("Schedule: no variant present")


def deserialize_aws_json_1_1(data: dict) -> Schedule:
    if data.get("at") is not None:
        import capo_redshift_serverless.types._prelude.timestamp

        return {
            "at": capo_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["at"]
            )
        }
    elif data.get("cron") is not None:
        return {"cron": data["cron"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Schedule: no recognized variant key")
