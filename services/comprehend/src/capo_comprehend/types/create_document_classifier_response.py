"""Generated from Smithy shape ``com.amazonaws.comprehend#CreateDocumentClassifierResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.document_classifier_arn


class CreateDocumentClassifierResponse(TypedDict, closed=True):
    document_classifier_arn: NotRequired[
        "capo_comprehend.types.document_classifier_arn.DocumentClassifierArn"
    ]
    """<p>The Amazon Resource Name (ARN) that identifies the document classifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDocumentClassifierResponse) -> dict:
    out: dict = {}
    if "document_classifier_arn" in value:
        out["DocumentClassifierArn"] = value["document_classifier_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDocumentClassifierResponse:
    out: CreateDocumentClassifierResponse = {}  # type: ignore[typeddict-item]
    if data.get("DocumentClassifierArn") is not None:
        out["document_classifier_arn"] = data["DocumentClassifierArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateDocumentClassifierResponse) -> dict:
    out: dict = {}
    if "document_classifier_arn" in value:
        out["DocumentClassifierArn"] = value["document_classifier_arn"]
    return out


def deserialize_cbor(data: dict) -> CreateDocumentClassifierResponse:
    out: CreateDocumentClassifierResponse = {}  # type: ignore[typeddict-item]
    if data.get("DocumentClassifierArn") is not None:
        out["document_classifier_arn"] = data["DocumentClassifierArn"]
    return out
