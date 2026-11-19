"""Generated from Smithy shape ``com.amazonaws.textract#SplitDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.page_list
    import capo_textract.types.u_integer


class SplitDocument(TypedDict, closed=True):
    index: NotRequired["capo_textract.types.u_integer.UInteger"]
    """<p>The index for a given document in a DocumentGroup of a specific Type.</p>"""
    pages: NotRequired["capo_textract.types.page_list.PageList"]
    """<p>An array of page numbers for a for a given document, ordered by logical boundary.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SplitDocument) -> dict:
    out: dict = {}
    if "index" in value:
        out["Index"] = value["index"]
    if "pages" in value:
        import capo_textract.types.page_list

        out["Pages"] = capo_textract.types.page_list.serialize_aws_json_1_1(
            value["pages"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SplitDocument:
    out: SplitDocument = {}  # type: ignore[typeddict-item]
    if data.get("Index") is not None:
        out["index"] = data["Index"]
    if data.get("Pages") is not None:
        import capo_textract.types.page_list

        out["pages"] = capo_textract.types.page_list.deserialize_aws_json_1_1(
            data["Pages"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SplitDocument) -> dict:
    out: dict = {}
    if "index" in value:
        out["Index"] = value["index"]
    if "pages" in value:
        import capo_textract.types.page_list

        out["Pages"] = capo_textract.types.page_list.serialize_cbor(value["pages"])
    return out


def deserialize_cbor(data: dict) -> SplitDocument:
    out: SplitDocument = {}  # type: ignore[typeddict-item]
    if data.get("Index") is not None:
        out["index"] = data["Index"]
    if data.get("Pages") is not None:
        import capo_textract.types.page_list

        out["pages"] = capo_textract.types.page_list.deserialize_cbor(data["Pages"])
    return out
