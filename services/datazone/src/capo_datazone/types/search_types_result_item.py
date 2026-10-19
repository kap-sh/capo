"""Generated from Smithy shape ``com.amazonaws.datazone#SearchTypesResultItem``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.asset_type_item
    import capo_datazone.types.form_type_data
    import capo_datazone.types.lineage_node_type_item


class _SearchTypesResultItem_assetTypeItem(TypedDict, closed=True):
    assetTypeItem: "capo_datazone.types.asset_type_item.AssetTypeItem"


class _SearchTypesResultItem_formTypeItem(TypedDict, closed=True):
    formTypeItem: "capo_datazone.types.form_type_data.FormTypeData"


class _SearchTypesResultItem_lineageNodeTypeItem(TypedDict, closed=True):
    lineageNodeTypeItem: (
        "capo_datazone.types.lineage_node_type_item.LineageNodeTypeItem"
    )


SearchTypesResultItem: TypeAlias = (
    _SearchTypesResultItem_assetTypeItem
    | _SearchTypesResultItem_formTypeItem
    | _SearchTypesResultItem_lineageNodeTypeItem
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SearchTypesResultItem) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"SearchTypesResultItem: cannot serialize unknown variant {value.name!r}"
        )
    elif "assetTypeItem" in value:
        import capo_datazone.types.asset_type_item

        return {
            "assetTypeItem": capo_datazone.types.asset_type_item.serialize_json(
                value["assetTypeItem"]
            )
        }
    elif "formTypeItem" in value:
        import capo_datazone.types.form_type_data

        return {
            "formTypeItem": capo_datazone.types.form_type_data.serialize_json(
                value["formTypeItem"]
            )
        }
    elif "lineageNodeTypeItem" in value:
        import capo_datazone.types.lineage_node_type_item

        return {
            "lineageNodeTypeItem": capo_datazone.types.lineage_node_type_item.serialize_json(
                value["lineageNodeTypeItem"]
            )
        }
    else:
        raise SerializationError("SearchTypesResultItem: no variant present")


def deserialize_json(data: dict) -> SearchTypesResultItem:
    if data.get("assetTypeItem") is not None:
        import capo_datazone.types.asset_type_item

        return {
            "assetTypeItem": capo_datazone.types.asset_type_item.deserialize_json(
                data["assetTypeItem"]
            )
        }
    elif data.get("formTypeItem") is not None:
        import capo_datazone.types.form_type_data

        return {
            "formTypeItem": capo_datazone.types.form_type_data.deserialize_json(
                data["formTypeItem"]
            )
        }
    elif data.get("lineageNodeTypeItem") is not None:
        import capo_datazone.types.lineage_node_type_item

        return {
            "lineageNodeTypeItem": capo_datazone.types.lineage_node_type_item.deserialize_json(
                data["lineageNodeTypeItem"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("SearchTypesResultItem: no recognized variant key")


def redact_sensitive(
    value: SearchTypesResultItem,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "assetTypeItem" in value:
        import capo_datazone.types.asset_type_item

        out["assetTypeItem"] = capo_datazone.types.asset_type_item.redact_sensitive(
            value["assetTypeItem"]
        )
    if "formTypeItem" in value:
        import capo_datazone.types.form_type_data

        out["formTypeItem"] = capo_datazone.types.form_type_data.redact_sensitive(
            value["formTypeItem"]
        )
    if "lineageNodeTypeItem" in value:
        import capo_datazone.types.lineage_node_type_item

        out["lineageNodeTypeItem"] = (
            capo_datazone.types.lineage_node_type_item.redact_sensitive(
                value["lineageNodeTypeItem"]
            )
        )
    return out
