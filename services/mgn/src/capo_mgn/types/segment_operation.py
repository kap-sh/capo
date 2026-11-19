"""Generated from Smithy shape ``com.amazonaws.mgn#SegmentOperation``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_mgn.errors import DeserializationError, SerializationError
from capo_mgn.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mgn.types.segment_create_operation
    import capo_mgn.types.segment_delete_operation
    import capo_mgn.types.segment_update_operation


class SegmentOperationCreateMember(TypedDict, closed=True):
    create: "capo_mgn.types.segment_create_operation.SegmentCreateOperation"


class SegmentOperationUpdateMember(TypedDict, closed=True):
    update: "capo_mgn.types.segment_update_operation.SegmentUpdateOperation"


class SegmentOperationDeleteMember(TypedDict, closed=True):
    delete: "capo_mgn.types.segment_delete_operation.SegmentDeleteOperation"


SegmentOperation: TypeAlias = (
    SegmentOperationCreateMember
    | SegmentOperationUpdateMember
    | SegmentOperationDeleteMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SegmentOperation) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SegmentOperation: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "create" in value:
        import capo_mgn.types.segment_create_operation

        return {
            "create": capo_mgn.types.segment_create_operation.serialize_json(
                value["create"]
            )
        }
    elif "update" in value:
        import capo_mgn.types.segment_update_operation

        return {
            "update": capo_mgn.types.segment_update_operation.serialize_json(
                value["update"]
            )
        }
    elif "delete" in value:
        import capo_mgn.types.segment_delete_operation

        return {
            "delete": capo_mgn.types.segment_delete_operation.serialize_json(
                value["delete"]
            )
        }
    else:
        raise SerializationError("SegmentOperation: no variant present")


def deserialize_json(data: dict) -> SegmentOperation:
    if data.get("create") is not None:
        import capo_mgn.types.segment_create_operation

        return {
            "create": capo_mgn.types.segment_create_operation.deserialize_json(
                data["create"]
            )
        }
    elif data.get("update") is not None:
        import capo_mgn.types.segment_update_operation

        return {
            "update": capo_mgn.types.segment_update_operation.deserialize_json(
                data["update"]
            )
        }
    elif data.get("delete") is not None:
        import capo_mgn.types.segment_delete_operation

        return {
            "delete": capo_mgn.types.segment_delete_operation.deserialize_json(
                data["delete"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SegmentOperation: no recognized variant key")


def redact_sensitive(value: SegmentOperation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "create" in value:
        import capo_mgn.types.segment_create_operation

        out["create"] = capo_mgn.types.segment_create_operation.redact_sensitive(
            value["create"]
        )
    if "update" in value:
        import capo_mgn.types.segment_update_operation

        out["update"] = capo_mgn.types.segment_update_operation.redact_sensitive(
            value["update"]
        )
    return out
