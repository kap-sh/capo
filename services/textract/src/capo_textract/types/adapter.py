"""Generated from Smithy shape ``com.amazonaws.textract#Adapter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_textract.errors import DeserializationError

if TYPE_CHECKING:
    import capo_textract.types.adapter_id
    import capo_textract.types.adapter_pages
    import capo_textract.types.adapter_version


class Adapter(TypedDict, closed=True):
    adapter_id: "capo_textract.types.adapter_id.AdapterId"
    """<p>A unique identifier for the adapter resource.</p>"""
    pages: NotRequired["capo_textract.types.adapter_pages.AdapterPages"]
    """<p>Pages is a parameter that the user inputs to specify which pages to apply an adapter to. The following is a list of rules for using this parameter.</p> <ul> <li> <p>If a page is not specified, it is set to <code>["1"]</code> by default.</p> </li> <li> <p>The following characters are allowed in the parameter's string: <code>0 1 2 3 4 5 6 7 8 9 - *</code>. No whitespace is allowed.</p> </li> <li> <p>When using * to indicate all pages, it must be the only element in the list.</p> </li> <li> <p>You can use page intervals, such as <code>["1-3", "1-1", "4-*"]</code>. Where <code>*</code> indicates last page of document.</p> </li> <li> <p>Specified pages must be greater than 0 and less than or equal to the number of pages in the document.</p> </li> </ul>"""
    version: "capo_textract.types.adapter_version.AdapterVersion"
    """<p>A string that identifies the version of the adapter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Adapter) -> dict:
    out: dict = {}
    out["AdapterId"] = value["adapter_id"]
    if "pages" in value:
        import capo_textract.types.adapter_pages

        out["Pages"] = capo_textract.types.adapter_pages.serialize_aws_json_1_1(
            value["pages"]
        )
    out["Version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Adapter:
    out: Adapter = {}  # type: ignore[typeddict-item]
    if data.get("AdapterId") is not None:
        out["adapter_id"] = data["AdapterId"]
    else:
        raise DeserializationError("Adapter.adapter_id required")
    if data.get("Pages") is not None:
        import capo_textract.types.adapter_pages

        out["pages"] = capo_textract.types.adapter_pages.deserialize_aws_json_1_1(
            data["Pages"]
        )
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    else:
        raise DeserializationError("Adapter.version required")
    return out
