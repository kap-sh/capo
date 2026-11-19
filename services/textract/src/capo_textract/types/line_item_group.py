"""Generated from Smithy shape ``com.amazonaws.textract#LineItemGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.line_item_list
    import capo_textract.types.u_integer


class LineItemGroup(TypedDict, closed=True):
    line_item_group_index: NotRequired["capo_textract.types.u_integer.UInteger"]
    """<p>The number used to identify a specific table in a document. The first table encountered will have a LineItemGroupIndex of 1, the second 2, etc.</p>"""
    line_items: NotRequired["capo_textract.types.line_item_list.LineItemList"]
    """<p>The breakdown of information on a particular line of a table. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LineItemGroup) -> dict:
    out: dict = {}
    if "line_item_group_index" in value:
        out["LineItemGroupIndex"] = value["line_item_group_index"]
    if "line_items" in value:
        import capo_textract.types.line_item_list

        out["LineItems"] = capo_textract.types.line_item_list.serialize_aws_json_1_1(
            value["line_items"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LineItemGroup:
    out: LineItemGroup = {}  # type: ignore[typeddict-item]
    if data.get("LineItemGroupIndex") is not None:
        out["line_item_group_index"] = data["LineItemGroupIndex"]
    if data.get("LineItems") is not None:
        import capo_textract.types.line_item_list

        out["line_items"] = capo_textract.types.line_item_list.deserialize_aws_json_1_1(
            data["LineItems"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LineItemGroup) -> dict:
    out: dict = {}
    if "line_item_group_index" in value:
        out["LineItemGroupIndex"] = value["line_item_group_index"]
    if "line_items" in value:
        import capo_textract.types.line_item_list

        out["LineItems"] = capo_textract.types.line_item_list.serialize_cbor(
            value["line_items"]
        )
    return out


def deserialize_cbor(data: dict) -> LineItemGroup:
    out: LineItemGroup = {}  # type: ignore[typeddict-item]
    if data.get("LineItemGroupIndex") is not None:
        out["line_item_group_index"] = data["LineItemGroupIndex"]
    if data.get("LineItems") is not None:
        import capo_textract.types.line_item_list

        out["line_items"] = capo_textract.types.line_item_list.deserialize_cbor(
            data["LineItems"]
        )
    return out
