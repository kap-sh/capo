"""Generated from Smithy shape ``com.amazonaws.comprehend#ListDocumentClassificationJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.document_classification_job_properties_list
    import capo_comprehend.types.string


class ListDocumentClassificationJobsResponse(TypedDict, closed=True):
    document_classification_job_properties_list: NotRequired[
        "capo_comprehend.types.document_classification_job_properties_list.DocumentClassificationJobPropertiesList"
    ]
    """<p>A list containing the properties of each job returned.</p>"""
    next_token: NotRequired["capo_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDocumentClassificationJobsResponse) -> dict:
    out: dict = {}
    if "document_classification_job_properties_list" in value:
        import capo_comprehend.types.document_classification_job_properties_list

        out["DocumentClassificationJobPropertiesList"] = (
            capo_comprehend.types.document_classification_job_properties_list.serialize_aws_json_1_1(
                value["document_classification_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDocumentClassificationJobsResponse:
    out: ListDocumentClassificationJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("DocumentClassificationJobPropertiesList") is not None:
        import capo_comprehend.types.document_classification_job_properties_list

        out["document_classification_job_properties_list"] = (
            capo_comprehend.types.document_classification_job_properties_list.deserialize_aws_json_1_1(
                data["DocumentClassificationJobPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListDocumentClassificationJobsResponse) -> dict:
    out: dict = {}
    if "document_classification_job_properties_list" in value:
        import capo_comprehend.types.document_classification_job_properties_list

        out["DocumentClassificationJobPropertiesList"] = (
            capo_comprehend.types.document_classification_job_properties_list.serialize_cbor(
                value["document_classification_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListDocumentClassificationJobsResponse:
    out: ListDocumentClassificationJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("DocumentClassificationJobPropertiesList") is not None:
        import capo_comprehend.types.document_classification_job_properties_list

        out["document_classification_job_properties_list"] = (
            capo_comprehend.types.document_classification_job_properties_list.deserialize_cbor(
                data["DocumentClassificationJobPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
