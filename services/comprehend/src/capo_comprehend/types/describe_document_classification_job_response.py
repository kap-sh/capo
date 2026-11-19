"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeDocumentClassificationJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.document_classification_job_properties


class DescribeDocumentClassificationJobResponse(TypedDict, closed=True):
    document_classification_job_properties: NotRequired[
        "capo_comprehend.types.document_classification_job_properties.DocumentClassificationJobProperties"
    ]
    """<p>An object that describes the properties associated with the document classification job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDocumentClassificationJobResponse) -> dict:
    out: dict = {}
    if "document_classification_job_properties" in value:
        import capo_comprehend.types.document_classification_job_properties

        out["DocumentClassificationJobProperties"] = (
            capo_comprehend.types.document_classification_job_properties.serialize_aws_json_1_1(
                value["document_classification_job_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDocumentClassificationJobResponse:
    out: DescribeDocumentClassificationJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("DocumentClassificationJobProperties") is not None:
        import capo_comprehend.types.document_classification_job_properties

        out["document_classification_job_properties"] = (
            capo_comprehend.types.document_classification_job_properties.deserialize_aws_json_1_1(
                data["DocumentClassificationJobProperties"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeDocumentClassificationJobResponse) -> dict:
    out: dict = {}
    if "document_classification_job_properties" in value:
        import capo_comprehend.types.document_classification_job_properties

        out["DocumentClassificationJobProperties"] = (
            capo_comprehend.types.document_classification_job_properties.serialize_cbor(
                value["document_classification_job_properties"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeDocumentClassificationJobResponse:
    out: DescribeDocumentClassificationJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("DocumentClassificationJobProperties") is not None:
        import capo_comprehend.types.document_classification_job_properties

        out["document_classification_job_properties"] = (
            capo_comprehend.types.document_classification_job_properties.deserialize_cbor(
                data["DocumentClassificationJobProperties"]
            )
        )
    return out
