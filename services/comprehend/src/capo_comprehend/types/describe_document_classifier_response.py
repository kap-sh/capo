"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeDocumentClassifierResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.document_classifier_properties


class DescribeDocumentClassifierResponse(TypedDict, closed=True):
    document_classifier_properties: NotRequired[
        "capo_comprehend.types.document_classifier_properties.DocumentClassifierProperties"
    ]
    """<p>An object that contains the properties associated with a document classifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDocumentClassifierResponse) -> dict:
    out: dict = {}
    if "document_classifier_properties" in value:
        import capo_comprehend.types.document_classifier_properties

        out["DocumentClassifierProperties"] = (
            capo_comprehend.types.document_classifier_properties.serialize_aws_json_1_1(
                value["document_classifier_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDocumentClassifierResponse:
    out: DescribeDocumentClassifierResponse = {}  # type: ignore[typeddict-item]
    if data.get("DocumentClassifierProperties") is not None:
        import capo_comprehend.types.document_classifier_properties

        out["document_classifier_properties"] = (
            capo_comprehend.types.document_classifier_properties.deserialize_aws_json_1_1(
                data["DocumentClassifierProperties"]
            )
        )
    return out


def redact_sensitive(value: DescribeDocumentClassifierResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "document_classifier_properties" in value:
        import capo_comprehend.types.document_classifier_properties

        out["document_classifier_properties"] = (
            capo_comprehend.types.document_classifier_properties.redact_sensitive(
                value["document_classifier_properties"]
            )
        )
    return out
