"""Generated from Smithy shape ``com.amazonaws.datazone#ResultItem``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.lineage_node_item


class _ResultItem_lineageNode(TypedDict, closed=True):
    lineageNode: "capo_datazone.types.lineage_node_item.LineageNodeItem"


ResultItem: TypeAlias = _ResultItem_lineageNode


# --- restJson1 ser/de ---
def serialize_json(value: ResultItem) -> dict:
    if "lineageNode" in value:
        import capo_datazone.types.lineage_node_item

        return {
            "lineageNode": capo_datazone.types.lineage_node_item.serialize_json(
                value["lineageNode"]
            )
        }
    else:
        raise SerializationError("ResultItem: no variant present")


def deserialize_json(data: dict) -> ResultItem:
    if data.get("lineageNode") is not None:
        import capo_datazone.types.lineage_node_item

        return {
            "lineageNode": capo_datazone.types.lineage_node_item.deserialize_json(
                data["lineageNode"]
            )
        }
    else:
        raise DeserializationError("ResultItem: no recognized variant key")


def redact_sensitive(value: ResultItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "lineageNode" in value:
        import capo_datazone.types.lineage_node_item

        out["lineageNode"] = capo_datazone.types.lineage_node_item.redact_sensitive(
            value["lineageNode"]
        )
    return out
