"""Generated from Smithy shape ``com.amazonaws.health#ImpactRiskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.string

ImpactRiskList: TypeAlias = list["capo_health.types.string.string"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImpactRiskList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ImpactRiskList:
    return [item for item in data if item is not None]
