"""Generated from Smithy shape ``com.amazonaws.textract#DocumentGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.detected_signature_list
    import capo_textract.types.non_empty_string
    import capo_textract.types.split_document_list
    import capo_textract.types.undetected_signature_list


class DocumentGroup(TypedDict, closed=True):
    type: NotRequired["capo_textract.types.non_empty_string.NonEmptyString"]
    """<p>The type of document that Amazon Textract has detected. See <a href="https://docs.aws.amazon.com/textract/latest/dg/lending-response-objects.html">Analyze Lending Response Objects</a> for a list of all types returned by Textract.</p>"""
    split_documents: NotRequired[
        "capo_textract.types.split_document_list.SplitDocumentList"
    ]
    """<p>An array that contains information about the pages of a document, defined by logical boundary.</p>"""
    detected_signatures: NotRequired[
        "capo_textract.types.detected_signature_list.DetectedSignatureList"
    ]
    """<p>A list of the detected signatures found in a document group.</p>"""
    undetected_signatures: NotRequired[
        "capo_textract.types.undetected_signature_list.UndetectedSignatureList"
    ]
    """<p>A list of any expected signatures not found in a document group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentGroup) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "split_documents" in value:
        import capo_textract.types.split_document_list

        out["SplitDocuments"] = (
            capo_textract.types.split_document_list.serialize_aws_json_1_1(
                value["split_documents"]
            )
        )
    if "detected_signatures" in value:
        import capo_textract.types.detected_signature_list

        out["DetectedSignatures"] = (
            capo_textract.types.detected_signature_list.serialize_aws_json_1_1(
                value["detected_signatures"]
            )
        )
    if "undetected_signatures" in value:
        import capo_textract.types.undetected_signature_list

        out["UndetectedSignatures"] = (
            capo_textract.types.undetected_signature_list.serialize_aws_json_1_1(
                value["undetected_signatures"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentGroup:
    out: DocumentGroup = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("SplitDocuments") is not None:
        import capo_textract.types.split_document_list

        out["split_documents"] = (
            capo_textract.types.split_document_list.deserialize_aws_json_1_1(
                data["SplitDocuments"]
            )
        )
    if data.get("DetectedSignatures") is not None:
        import capo_textract.types.detected_signature_list

        out["detected_signatures"] = (
            capo_textract.types.detected_signature_list.deserialize_aws_json_1_1(
                data["DetectedSignatures"]
            )
        )
    if data.get("UndetectedSignatures") is not None:
        import capo_textract.types.undetected_signature_list

        out["undetected_signatures"] = (
            capo_textract.types.undetected_signature_list.deserialize_aws_json_1_1(
                data["UndetectedSignatures"]
            )
        )
    return out
