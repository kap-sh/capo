"""Generated from Smithy shape ``com.amazonaws.quicksight#SharedColumnSemanticMetadata``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_name_list
    import capo_quicksight.types.column_semantic_property_list


class SharedColumnSemanticMetadata(TypedDict, closed=True):
    column_names: NotRequired["capo_quicksight.types.column_name_list.ColumnNameList"]
    """<p>The names of the columns this metadata applies to.</p>"""
    column_properties: (
        "capo_quicksight.types.column_semantic_property_list.ColumnSemanticPropertyList"
    )
    """<p>The semantic properties for the specified columns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SharedColumnSemanticMetadata) -> dict:
    out: dict = {}
    if "column_names" in value:
        import capo_quicksight.types.column_name_list

        out["ColumnNames"] = capo_quicksight.types.column_name_list.serialize_json(
            value["column_names"]
        )
    import capo_quicksight.types.column_semantic_property_list

    out["ColumnProperties"] = (
        capo_quicksight.types.column_semantic_property_list.serialize_json(
            value["column_properties"]
        )
    )
    return out


def deserialize_json(data: dict) -> SharedColumnSemanticMetadata:
    out: SharedColumnSemanticMetadata = {}  # type: ignore[typeddict-item]
    if data.get("ColumnNames") is not None:
        import capo_quicksight.types.column_name_list

        out["column_names"] = capo_quicksight.types.column_name_list.deserialize_json(
            data["ColumnNames"]
        )
    if data.get("ColumnProperties") is not None:
        import capo_quicksight.types.column_semantic_property_list

        out["column_properties"] = (
            capo_quicksight.types.column_semantic_property_list.deserialize_json(
                data["ColumnProperties"]
            )
        )
    else:
        out["column_properties"] = []
    return out


def redact_sensitive(value: SharedColumnSemanticMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "column_properties" in value:
        import capo_quicksight.types.column_semantic_property_list

        out["column_properties"] = (
            capo_quicksight.types.column_semantic_property_list.redact_sensitive(
                value["column_properties"]
            )
        )
    return out
