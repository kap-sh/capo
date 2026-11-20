"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#StrategySelectorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchmemory.types.strategy_selector

StrategySelectorList: TypeAlias = list[
    "capo_opensearchmemory.types.strategy_selector.StrategySelector"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StrategySelectorList) -> list:
    import capo_opensearchmemory.types.strategy_selector

    out: list = []
    for item in value:
        out.append(
            capo_opensearchmemory.types.strategy_selector.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> StrategySelectorList:
    import capo_opensearchmemory.types.strategy_selector

    out: StrategySelectorList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_opensearchmemory.types.strategy_selector.deserialize_aws_json_1_0(item)
        )
    return out
