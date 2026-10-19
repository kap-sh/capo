"""Generated from Smithy shape ``com.amazonaws.textract#AnalyzeIDRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_textract.types.document_pages


class AnalyzeIDRequest(TypedDict, closed=True):
    document_pages: "capo_textract.types.document_pages.DocumentPages"
    """<p>The document being passed to AnalyzeID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalyzeIDRequest) -> dict:
    out: dict = {}
    import capo_textract.types.document_pages

    out["DocumentPages"] = capo_textract.types.document_pages.serialize_aws_json_1_1(
        value["document_pages"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AnalyzeIDRequest:
    out: AnalyzeIDRequest = {}  # type: ignore[typeddict-item]
    if data.get("DocumentPages") is not None:
        import capo_textract.types.document_pages

        out["document_pages"] = (
            capo_textract.types.document_pages.deserialize_aws_json_1_1(
                data["DocumentPages"]
            )
        )
    else:
        out["document_pages"] = []
    return out
