"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ResourceConfiguration``."""

from typing_extensions import TypedDict


class ResourceConfiguration(TypedDict, closed=True):
    minimum_memory_in_mi_b: "int"
    """<p>The minimum amount of memory, in mebibytes, to allocate to the AgentCore Runtime.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceConfiguration) -> dict:
    out: dict = {}
    out["minimumMemoryInMiB"] = value["minimum_memory_in_mi_b"]
    return out


def deserialize_json(data: dict) -> ResourceConfiguration:
    out: ResourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("minimumMemoryInMiB") is not None:
        out["minimum_memory_in_mi_b"] = data["minimumMemoryInMiB"]
    else:
        out["minimum_memory_in_mi_b"] = 0
    return out
