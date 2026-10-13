"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputeNodeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.compute_node

ComputeNodeList: TypeAlias = list["capo_iotsitewise.types.compute_node.ComputeNode"]


# --- restJson1 ser/de ---
def serialize_json(value: ComputeNodeList) -> list:
    import capo_iotsitewise.types.compute_node

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.compute_node.serialize_json(item))
    return out


def deserialize_json(data: list) -> ComputeNodeList:
    import capo_iotsitewise.types.compute_node

    out: ComputeNodeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_iotsitewise.types.compute_node.deserialize_json(item))
    return out


def redact_sensitive(value: ComputeNodeList) -> list[Any]:
    import capo_iotsitewise.types.compute_node

    return [
        capo_iotsitewise.types.compute_node.redact_sensitive(item) for item in value
    ]
