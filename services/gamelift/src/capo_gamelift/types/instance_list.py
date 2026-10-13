"""Generated from Smithy shape ``com.amazonaws.gamelift#InstanceList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.instance

InstanceList: TypeAlias = list["capo_gamelift.types.instance.Instance"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceList) -> list:
    import capo_gamelift.types.instance

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.instance.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceList:
    import capo_gamelift.types.instance

    out: InstanceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.instance.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: InstanceList) -> list[Any]:
    import capo_gamelift.types.instance

    return [capo_gamelift.types.instance.redact_sensitive(item) for item in value]
