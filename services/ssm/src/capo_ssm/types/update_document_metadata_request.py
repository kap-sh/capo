"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateDocumentMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.document_name
    import capo_ssm.types.document_reviews
    import capo_ssm.types.document_version


class UpdateDocumentMetadataRequest(TypedDict, closed=True):
    name: "capo_ssm.types.document_name.DocumentName"
    """<p>The name of the change template for which a version's metadata is to be updated.</p>"""
    document_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The version of a change template in which to update approval metadata.</p>"""
    document_reviews: "capo_ssm.types.document_reviews.DocumentReviews"
    """<p>The change template review details to update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDocumentMetadataRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    import capo_ssm.types.document_reviews

    out["DocumentReviews"] = capo_ssm.types.document_reviews.serialize_aws_json_1_1(
        value["document_reviews"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDocumentMetadataRequest:
    out: UpdateDocumentMetadataRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("DocumentVersion") is not None:
        out["document_version"] = data["DocumentVersion"]
    if data.get("DocumentReviews") is not None:
        import capo_ssm.types.document_reviews

        out["document_reviews"] = (
            capo_ssm.types.document_reviews.deserialize_aws_json_1_1(
                data["DocumentReviews"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDocumentMetadataRequest.document_reviews required"
        )
    return out
