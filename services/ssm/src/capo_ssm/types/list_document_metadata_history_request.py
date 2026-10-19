"""Generated from Smithy shape ``com.amazonaws.ssm#ListDocumentMetadataHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.document_metadata_enum
    import capo_ssm.types.document_name
    import capo_ssm.types.document_version
    import capo_ssm.types.max_results
    import capo_ssm.types.next_token


class ListDocumentMetadataHistoryRequest(TypedDict, closed=True):
    name: "capo_ssm.types.document_name.DocumentName"
    """<p>The name of the change template.</p>"""
    document_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The version of the change template.</p>"""
    metadata: "capo_ssm.types.document_metadata_enum.DocumentMetadataEnum"
    """<p>The type of data for which details are being requested. Currently, the only supported value is <code>DocumentReviews</code>.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_results: NotRequired["capo_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDocumentMetadataHistoryRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    import capo_ssm.types.document_metadata_enum

    out["Metadata"] = capo_ssm.types.document_metadata_enum.serialize_aws_json_1_1(
        value["metadata"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDocumentMetadataHistoryRequest:
    out: ListDocumentMetadataHistoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("DocumentVersion") is not None:
        out["document_version"] = data["DocumentVersion"]
    if data.get("Metadata") is not None:
        import capo_ssm.types.document_metadata_enum

        out["metadata"] = (
            capo_ssm.types.document_metadata_enum.deserialize_aws_json_1_1(
                data["Metadata"]
            )
        )
    else:
        import typing

        out["metadata"] = typing.cast(
            "capo_ssm.types.document_metadata_enum.DocumentMetadataEnum", ""
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
