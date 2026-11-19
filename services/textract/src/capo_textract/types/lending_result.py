"""Generated from Smithy shape ``com.amazonaws.textract#LendingResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.extraction_list
    import capo_textract.types.page_classification
    import capo_textract.types.u_integer


class LendingResult(TypedDict, closed=True):
    page: NotRequired["capo_textract.types.u_integer.UInteger"]
    """<p>The page number for a page, with regard to whole submission.</p>"""
    page_classification: NotRequired[
        "capo_textract.types.page_classification.PageClassification"
    ]
    """<p>The classifier result for a given page.</p>"""
    extractions: NotRequired["capo_textract.types.extraction_list.ExtractionList"]
    """<p>An array of Extraction to hold structured data. e.g. normalized key value pairs instead of raw OCR detections .</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LendingResult) -> dict:
    out: dict = {}
    if "page" in value:
        out["Page"] = value["page"]
    if "page_classification" in value:
        import capo_textract.types.page_classification

        out["PageClassification"] = (
            capo_textract.types.page_classification.serialize_aws_json_1_1(
                value["page_classification"]
            )
        )
    if "extractions" in value:
        import capo_textract.types.extraction_list

        out["Extractions"] = capo_textract.types.extraction_list.serialize_aws_json_1_1(
            value["extractions"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LendingResult:
    out: LendingResult = {}  # type: ignore[typeddict-item]
    if data.get("Page") is not None:
        out["page"] = data["Page"]
    if data.get("PageClassification") is not None:
        import capo_textract.types.page_classification

        out["page_classification"] = (
            capo_textract.types.page_classification.deserialize_aws_json_1_1(
                data["PageClassification"]
            )
        )
    if data.get("Extractions") is not None:
        import capo_textract.types.extraction_list

        out["extractions"] = (
            capo_textract.types.extraction_list.deserialize_aws_json_1_1(
                data["Extractions"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LendingResult) -> dict:
    out: dict = {}
    if "page" in value:
        out["Page"] = value["page"]
    if "page_classification" in value:
        import capo_textract.types.page_classification

        out["PageClassification"] = (
            capo_textract.types.page_classification.serialize_cbor(
                value["page_classification"]
            )
        )
    if "extractions" in value:
        import capo_textract.types.extraction_list

        out["Extractions"] = capo_textract.types.extraction_list.serialize_cbor(
            value["extractions"]
        )
    return out


def deserialize_cbor(data: dict) -> LendingResult:
    out: LendingResult = {}  # type: ignore[typeddict-item]
    if data.get("Page") is not None:
        out["page"] = data["Page"]
    if data.get("PageClassification") is not None:
        import capo_textract.types.page_classification

        out["page_classification"] = (
            capo_textract.types.page_classification.deserialize_cbor(
                data["PageClassification"]
            )
        )
    if data.get("Extractions") is not None:
        import capo_textract.types.extraction_list

        out["extractions"] = capo_textract.types.extraction_list.deserialize_cbor(
            data["Extractions"]
        )
    return out
