"""Generated from Smithy shape ``com.amazonaws.datazone#ResultItem``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.lineage_node_item


class _ResultItem_lineageNode(TypedDict, closed=True):
    lineageNode: "capo_datazone.types.lineage_node_item.LineageNodeItem"


ResultItem: TypeAlias = _ResultItem_lineageNode | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ResultItem) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ResultItem: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "lineageNode" in value:
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
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ResultItem: no recognized variant key")


def redact_sensitive(value: ResultItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "lineageNode" in value:
        import capo_datazone.types.lineage_node_item

        out["lineageNode"] = capo_datazone.types.lineage_node_item.redact_sensitive(
            value["lineageNode"]
        )
    return out
