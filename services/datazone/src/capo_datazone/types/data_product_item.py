"""Generated from Smithy shape ``com.amazonaws.datazone#DataProductItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.data_product_item_type
    import capo_datazone.types.entity_identifier
    import capo_datazone.types.item_glossary_terms
    import capo_datazone.types.revision


class DataProductItem(TypedDict, closed=True):
    item_type: "capo_datazone.types.data_product_item_type.DataProductItemType"
    """<p>The type of the data product.</p>"""
    identifier: "capo_datazone.types.entity_identifier.EntityIdentifier"
    """<p>The ID of the data product.</p>"""
    revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision of the data product.</p>"""
    glossary_terms: NotRequired[
        "capo_datazone.types.item_glossary_terms.ItemGlossaryTerms"
    ]
    """<p>The glossary terms of the data product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataProductItem) -> dict:
    out: dict = {}
    import capo_datazone.types.data_product_item_type

    out["itemType"] = capo_datazone.types.data_product_item_type.serialize_json(
        value["item_type"]
    )
    out["identifier"] = value["identifier"]
    if "revision" in value:
        out["revision"] = value["revision"]
    if "glossary_terms" in value:
        import capo_datazone.types.item_glossary_terms

        out["glossaryTerms"] = capo_datazone.types.item_glossary_terms.serialize_json(
            value["glossary_terms"]
        )
    return out


def deserialize_json(data: dict) -> DataProductItem:
    out: DataProductItem = {}  # type: ignore[typeddict-item]
    if data.get("itemType") is not None:
        import capo_datazone.types.data_product_item_type

        out["item_type"] = capo_datazone.types.data_product_item_type.deserialize_json(
            data["itemType"]
        )
    else:
        import typing

        out["item_type"] = typing.cast(
            "capo_datazone.types.data_product_item_type.DataProductItemType", ""
        )
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    if data.get("glossaryTerms") is not None:
        import capo_datazone.types.item_glossary_terms

        out["glossary_terms"] = (
            capo_datazone.types.item_glossary_terms.deserialize_json(
                data["glossaryTerms"]
            )
        )
    return out
