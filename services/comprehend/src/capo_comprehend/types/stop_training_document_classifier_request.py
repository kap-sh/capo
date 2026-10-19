"""Generated from Smithy shape ``com.amazonaws.comprehend#StopTrainingDocumentClassifierRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.document_classifier_arn


class StopTrainingDocumentClassifierRequest(TypedDict, closed=True):
    document_classifier_arn: (
        "capo_comprehend.types.document_classifier_arn.DocumentClassifierArn"
    )
    """<p>The Amazon Resource Name (ARN) that identifies the document classifier currently being trained.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopTrainingDocumentClassifierRequest) -> dict:
    out: dict = {}
    out["DocumentClassifierArn"] = value["document_classifier_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopTrainingDocumentClassifierRequest:
    out: StopTrainingDocumentClassifierRequest = {}  # type: ignore[typeddict-item]
    if data.get("DocumentClassifierArn") is not None:
        out["document_classifier_arn"] = data["DocumentClassifierArn"]
    else:
        out["document_classifier_arn"] = ""
    return out
