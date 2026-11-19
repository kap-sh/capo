"""Generated from Smithy shape ``com.amazonaws.mgn#OperationUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mgn.errors import DeserializationError, SerializationError
from capo_mgn.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mgn.types.create_operation
    import capo_mgn.types.delete_operation
    import capo_mgn.types.merge_operation
    import capo_mgn.types.split_operation
    import capo_mgn.types.update_operation
    import capo_mgn.types.update_operation_v2


class OperationUnionMergeMember(TypedDict, closed=True):
    merge: "capo_mgn.types.merge_operation.MergeOperation"


class OperationUnionSplitMember(TypedDict, closed=True):
    split: "capo_mgn.types.split_operation.SplitOperation"


class OperationUnionDeleteMember(TypedDict, closed=True):
    delete: "capo_mgn.types.delete_operation.DeleteOperation"


class OperationUnionUpdateMember(TypedDict, closed=True):
    update: "capo_mgn.types.update_operation.UpdateOperation"


class OperationUnionUpdateV2Member(TypedDict, closed=True):
    updateV2: "capo_mgn.types.update_operation_v2.UpdateOperationV2"


class OperationUnionCreateMember(TypedDict, closed=True):
    create: "capo_mgn.types.create_operation.CreateOperation"


OperationUnion: TypeAlias = (
    OperationUnionMergeMember
    | OperationUnionSplitMember
    | OperationUnionDeleteMember
    | OperationUnionUpdateMember
    | OperationUnionUpdateV2Member
    | OperationUnionCreateMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: OperationUnion) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"OperationUnion: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "merge" in value:
        import capo_mgn.types.merge_operation

        return {"merge": capo_mgn.types.merge_operation.serialize_json(value["merge"])}
    elif "split" in value:
        import capo_mgn.types.split_operation

        return {"split": capo_mgn.types.split_operation.serialize_json(value["split"])}
    elif "delete" in value:
        import capo_mgn.types.delete_operation

        return {
            "delete": capo_mgn.types.delete_operation.serialize_json(value["delete"])
        }
    elif "update" in value:
        import capo_mgn.types.update_operation

        return {
            "update": capo_mgn.types.update_operation.serialize_json(value["update"])
        }
    elif "updateV2" in value:
        import capo_mgn.types.update_operation_v2

        return {
            "updateV2": capo_mgn.types.update_operation_v2.serialize_json(
                value["updateV2"]
            )
        }
    elif "create" in value:
        import capo_mgn.types.create_operation

        return {
            "create": capo_mgn.types.create_operation.serialize_json(value["create"])
        }
    else:
        raise SerializationError("OperationUnion: no variant present")


def deserialize_json(data: dict) -> OperationUnion:
    if data.get("merge") is not None:
        import capo_mgn.types.merge_operation

        return {"merge": capo_mgn.types.merge_operation.deserialize_json(data["merge"])}
    elif data.get("split") is not None:
        import capo_mgn.types.split_operation

        return {"split": capo_mgn.types.split_operation.deserialize_json(data["split"])}
    elif data.get("delete") is not None:
        import capo_mgn.types.delete_operation

        return {
            "delete": capo_mgn.types.delete_operation.deserialize_json(data["delete"])
        }
    elif data.get("update") is not None:
        import capo_mgn.types.update_operation

        return {
            "update": capo_mgn.types.update_operation.deserialize_json(data["update"])
        }
    elif data.get("updateV2") is not None:
        import capo_mgn.types.update_operation_v2

        return {
            "updateV2": capo_mgn.types.update_operation_v2.deserialize_json(
                data["updateV2"]
            )
        }
    elif data.get("create") is not None:
        import capo_mgn.types.create_operation

        return {
            "create": capo_mgn.types.create_operation.deserialize_json(data["create"])
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("OperationUnion: no recognized variant key")
