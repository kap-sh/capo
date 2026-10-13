"""Generated from Smithy shape ``com.amazonaws.eventbridge#TargetList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridge.types.target

TargetList: TypeAlias = list["capo_eventbridge.types.target.Target"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetList) -> list:
    import capo_eventbridge.types.target

    out: list = []
    for item in value:
        out.append(capo_eventbridge.types.target.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TargetList:
    import capo_eventbridge.types.target

    out: TargetList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_eventbridge.types.target.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: TargetList) -> list[Any]:
    import capo_eventbridge.types.target

    return [capo_eventbridge.types.target.redact_sensitive(item) for item in value]
