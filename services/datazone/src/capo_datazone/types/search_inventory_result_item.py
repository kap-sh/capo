"""Generated from Smithy shape ``com.amazonaws.datazone#SearchInventoryResultItem``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.asset_item
    import capo_datazone.types.data_product_result_item
    import capo_datazone.types.glossary_item
    import capo_datazone.types.glossary_term_item


class _SearchInventoryResultItem_glossaryItem(TypedDict, closed=True):
    glossaryItem: "capo_datazone.types.glossary_item.GlossaryItem"


class _SearchInventoryResultItem_glossaryTermItem(TypedDict, closed=True):
    glossaryTermItem: "capo_datazone.types.glossary_term_item.GlossaryTermItem"


class _SearchInventoryResultItem_assetItem(TypedDict, closed=True):
    assetItem: "capo_datazone.types.asset_item.AssetItem"


class _SearchInventoryResultItem_dataProductItem(TypedDict, closed=True):
    dataProductItem: (
        "capo_datazone.types.data_product_result_item.DataProductResultItem"
    )


SearchInventoryResultItem: TypeAlias = (
    _SearchInventoryResultItem_glossaryItem
    | _SearchInventoryResultItem_glossaryTermItem
    | _SearchInventoryResultItem_assetItem
    | _SearchInventoryResultItem_dataProductItem
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SearchInventoryResultItem) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SearchInventoryResultItem: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "glossaryItem" in value:
        import capo_datazone.types.glossary_item

        return {
            "glossaryItem": capo_datazone.types.glossary_item.serialize_json(
                value["glossaryItem"]
            )
        }
    elif "glossaryTermItem" in value:
        import capo_datazone.types.glossary_term_item

        return {
            "glossaryTermItem": capo_datazone.types.glossary_term_item.serialize_json(
                value["glossaryTermItem"]
            )
        }
    elif "assetItem" in value:
        import capo_datazone.types.asset_item

        return {
            "assetItem": capo_datazone.types.asset_item.serialize_json(
                value["assetItem"]
            )
        }
    elif "dataProductItem" in value:
        import capo_datazone.types.data_product_result_item

        return {
            "dataProductItem": capo_datazone.types.data_product_result_item.serialize_json(
                value["dataProductItem"]
            )
        }
    else:
        raise SerializationError("SearchInventoryResultItem: no variant present")


def deserialize_json(data: dict) -> SearchInventoryResultItem:
    if data.get("glossaryItem") is not None:
        import capo_datazone.types.glossary_item

        return {
            "glossaryItem": capo_datazone.types.glossary_item.deserialize_json(
                data["glossaryItem"]
            )
        }
    elif data.get("glossaryTermItem") is not None:
        import capo_datazone.types.glossary_term_item

        return {
            "glossaryTermItem": capo_datazone.types.glossary_term_item.deserialize_json(
                data["glossaryTermItem"]
            )
        }
    elif data.get("assetItem") is not None:
        import capo_datazone.types.asset_item

        return {
            "assetItem": capo_datazone.types.asset_item.deserialize_json(
                data["assetItem"]
            )
        }
    elif data.get("dataProductItem") is not None:
        import capo_datazone.types.data_product_result_item

        return {
            "dataProductItem": capo_datazone.types.data_product_result_item.deserialize_json(
                data["dataProductItem"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "SearchInventoryResultItem: no recognized variant key"
        )


def redact_sensitive(value: SearchInventoryResultItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "glossaryItem" in value:
        import capo_datazone.types.glossary_item

        out["glossaryItem"] = capo_datazone.types.glossary_item.redact_sensitive(
            value["glossaryItem"]
        )
    if "glossaryTermItem" in value:
        import capo_datazone.types.glossary_term_item

        out["glossaryTermItem"] = (
            capo_datazone.types.glossary_term_item.redact_sensitive(
                value["glossaryTermItem"]
            )
        )
    if "assetItem" in value:
        import capo_datazone.types.asset_item

        out["assetItem"] = capo_datazone.types.asset_item.redact_sensitive(
            value["assetItem"]
        )
    if "dataProductItem" in value:
        import capo_datazone.types.data_product_result_item

        out["dataProductItem"] = (
            capo_datazone.types.data_product_result_item.redact_sensitive(
                value["dataProductItem"]
            )
        )
    return out
