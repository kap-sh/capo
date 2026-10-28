"""Generated from Smithy shape ``com.amazonaws.ssmincidents#NotificationTargetItem``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError, SerializationError
from capo_ssm_incidents.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ssm_incidents.types.arn


class NotificationTargetItemSnsTopicArnMember(TypedDict, closed=True):
    snsTopicArn: "capo_ssm_incidents.types.arn.Arn"


NotificationTargetItem: TypeAlias = (
    NotificationTargetItemSnsTopicArnMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: NotificationTargetItem) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"NotificationTargetItem: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "snsTopicArn" in value:
        return {"snsTopicArn": value["snsTopicArn"]}
    else:
        raise SerializationError("NotificationTargetItem: no variant present")


def deserialize_json(data: dict) -> NotificationTargetItem:
    if data.get("snsTopicArn") is not None:
        return {"snsTopicArn": data["snsTopicArn"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("NotificationTargetItem: no recognized variant key")
