"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#StrategySelector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.memory_type
    import capo_opensearchmemory.types.strategy_name_list


class StrategySelector(TypedDict, closed=True):
    memory_type: "capo_opensearchmemory.types.memory_type.MemoryType"
    """<p>The memory type to search or list.</p>"""
    memory_strategy_names: NotRequired[
        "capo_opensearchmemory.types.strategy_name_list.StrategyNameList"
    ]
    """<p>Specific strategy names of <code>memoryType</code>. Omit it to include every strategy of that type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StrategySelector) -> dict:
    out: dict = {}
    import capo_opensearchmemory.types.memory_type

    out["memoryType"] = capo_opensearchmemory.types.memory_type.serialize_aws_json_1_0(
        value["memory_type"]
    )
    if "memory_strategy_names" in value:
        import capo_opensearchmemory.types.strategy_name_list

        out["memoryStrategyNames"] = (
            capo_opensearchmemory.types.strategy_name_list.serialize_aws_json_1_0(
                value["memory_strategy_names"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StrategySelector:
    out: StrategySelector = {}  # type: ignore[typeddict-item]
    if data.get("memoryType") is not None:
        import capo_opensearchmemory.types.memory_type

        out["memory_type"] = (
            capo_opensearchmemory.types.memory_type.deserialize_aws_json_1_0(
                data["memoryType"]
            )
        )
    else:
        import typing

        out["memory_type"] = typing.cast(
            "capo_opensearchmemory.types.memory_type.MemoryType", ""
        )
    if data.get("memoryStrategyNames") is not None:
        import capo_opensearchmemory.types.strategy_name_list

        out["memory_strategy_names"] = (
            capo_opensearchmemory.types.strategy_name_list.deserialize_aws_json_1_0(
                data["memoryStrategyNames"]
            )
        )
    return out
