"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#MemoryStrategyList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchmemory.types.memory_strategy

MemoryStrategyList: TypeAlias = list[
    "capo_opensearchmemory.types.memory_strategy.MemoryStrategy"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MemoryStrategyList) -> list:
    import capo_opensearchmemory.types.memory_strategy

    out: list = []
    for item in value:
        out.append(
            capo_opensearchmemory.types.memory_strategy.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> MemoryStrategyList:
    import capo_opensearchmemory.types.memory_strategy

    out: MemoryStrategyList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_opensearchmemory.types.memory_strategy.deserialize_aws_json_1_0(item)
        )
    return out


def redact_sensitive(value: MemoryStrategyList) -> list[Any]:
    import capo_opensearchmemory.types.memory_strategy

    return [
        capo_opensearchmemory.types.memory_strategy.redact_sensitive(item)
        for item in value
    ]
