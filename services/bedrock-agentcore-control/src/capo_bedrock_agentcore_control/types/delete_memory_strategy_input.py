"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteMemoryStrategyInput``."""

from typing_extensions import TypedDict


class DeleteMemoryStrategyInput(TypedDict, closed=True):
    memory_strategy_id: "str"
    """<p>The unique identifier of the memory strategy to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMemoryStrategyInput) -> dict:
    out: dict = {}
    out["memoryStrategyId"] = value["memory_strategy_id"]
    return out


def deserialize_json(data: dict) -> DeleteMemoryStrategyInput:
    out: DeleteMemoryStrategyInput = {}  # type: ignore[typeddict-item]
    if data.get("memoryStrategyId") is not None:
        out["memory_strategy_id"] = data["memoryStrategyId"]
    else:
        out["memory_strategy_id"] = ""
    return out
