"""Generated from Smithy shape ``com.amazonaws.comprehend#ListDocumentClassifiersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.document_classifier_properties_list
    import capo_comprehend.types.string


class ListDocumentClassifiersResponse(TypedDict, closed=True):
    document_classifier_properties_list: NotRequired[
        "capo_comprehend.types.document_classifier_properties_list.DocumentClassifierPropertiesList"
    ]
    """<p>A list containing the properties of each job returned.</p>"""
    next_token: NotRequired["capo_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDocumentClassifiersResponse) -> dict:
    out: dict = {}
    if "document_classifier_properties_list" in value:
        import capo_comprehend.types.document_classifier_properties_list

        out["DocumentClassifierPropertiesList"] = (
            capo_comprehend.types.document_classifier_properties_list.serialize_aws_json_1_1(
                value["document_classifier_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDocumentClassifiersResponse:
    out: ListDocumentClassifiersResponse = {}  # type: ignore[typeddict-item]
    if data.get("DocumentClassifierPropertiesList") is not None:
        import capo_comprehend.types.document_classifier_properties_list

        out["document_classifier_properties_list"] = (
            capo_comprehend.types.document_classifier_properties_list.deserialize_aws_json_1_1(
                data["DocumentClassifierPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListDocumentClassifiersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "document_classifier_properties_list" in value:
        import capo_comprehend.types.document_classifier_properties_list

        out["document_classifier_properties_list"] = (
            capo_comprehend.types.document_classifier_properties_list.redact_sensitive(
                value["document_classifier_properties_list"]
            )
        )
    return out
