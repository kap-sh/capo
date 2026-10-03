"""Generated from Smithy shape ``com.amazonaws.textract#Query``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_textract.errors import DeserializationError

if TYPE_CHECKING:
    import capo_textract.types.query_input
    import capo_textract.types.query_pages


class Query(TypedDict, closed=True):
    text: "capo_textract.types.query_input.QueryInput"
    """<p>Question that Amazon Textract will apply to the document. An example would be "What is the customer's SSN?"</p>"""
    alias: NotRequired["capo_textract.types.query_input.QueryInput"]
    """<p>Alias attached to the query, for ease of location.</p>"""
    pages: NotRequired["capo_textract.types.query_pages.QueryPages"]
    """<p>Pages is a parameter that the user inputs to specify which pages to apply a query to. The following is a list of rules for using this parameter.</p> <ul> <li> <p>If a page is not specified, it is set to <code>["1"]</code> by default.</p> </li> <li> <p>The following characters are allowed in the parameter's string: <code>0 1 2 3 4 5 6 7 8 9 - *</code>. No whitespace is allowed.</p> </li> <li> <p>When using * to indicate all pages, it must be the only element in the list.</p> </li> <li> <p>You can use page intervals, such as <code>[“1-3”, “1-1”, “4-*”]</code>. Where <code>*</code> indicates last page of document.</p> </li> <li> <p>Specified pages must be greater than 0 and less than or equal to the number of pages in the document.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Query) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    if "alias" in value:
        out["Alias"] = value["alias"]
    if "pages" in value:
        import capo_textract.types.query_pages

        out["Pages"] = capo_textract.types.query_pages.serialize_aws_json_1_1(
            value["pages"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Query:
    out: Query = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    else:
        raise DeserializationError("Query.text required")
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    if data.get("Pages") is not None:
        import capo_textract.types.query_pages

        out["pages"] = capo_textract.types.query_pages.deserialize_aws_json_1_1(
            data["Pages"]
        )
    return out
