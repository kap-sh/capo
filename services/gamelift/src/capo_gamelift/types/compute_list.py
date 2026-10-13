"""Generated from Smithy shape ``com.amazonaws.gamelift#ComputeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.compute

ComputeList: TypeAlias = list["capo_gamelift.types.compute.Compute"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeList) -> list:
    import capo_gamelift.types.compute

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.compute.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ComputeList:
    import capo_gamelift.types.compute

    out: ComputeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.compute.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: ComputeList) -> list[Any]:
    import capo_gamelift.types.compute

    return [capo_gamelift.types.compute.redact_sensitive(item) for item in value]
