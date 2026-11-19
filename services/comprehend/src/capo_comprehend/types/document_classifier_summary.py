"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentClassifierSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.comprehend_arn_name
    import capo_comprehend.types.integer
    import capo_comprehend.types.model_status
    import capo_comprehend.types.timestamp
    import capo_comprehend.types.version_name


class DocumentClassifierSummary(TypedDict, closed=True):
    document_classifier_name: NotRequired[
        "capo_comprehend.types.comprehend_arn_name.ComprehendArnName"
    ]
    """<p>The name that you assigned the document classifier.</p>"""
    number_of_versions: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>The number of versions you created.</p>"""
    latest_version_created_at: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>The time that the latest document classifier version was submitted for processing.</p>"""
    latest_version_name: NotRequired["capo_comprehend.types.version_name.VersionName"]
    """<p>The version name you assigned to the latest document classifier version.</p>"""
    latest_version_status: NotRequired["capo_comprehend.types.model_status.ModelStatus"]
    """<p>Provides the status of the latest document classifier version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentClassifierSummary) -> dict:
    out: dict = {}
    if "document_classifier_name" in value:
        out["DocumentClassifierName"] = value["document_classifier_name"]
    if "number_of_versions" in value:
        out["NumberOfVersions"] = value["number_of_versions"]
    if "latest_version_created_at" in value:
        import capo_comprehend.types.timestamp

        out["LatestVersionCreatedAt"] = (
            capo_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["latest_version_created_at"]
            )
        )
    if "latest_version_name" in value:
        out["LatestVersionName"] = value["latest_version_name"]
    if "latest_version_status" in value:
        import capo_comprehend.types.model_status

        out["LatestVersionStatus"] = (
            capo_comprehend.types.model_status.serialize_aws_json_1_1(
                value["latest_version_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentClassifierSummary:
    out: DocumentClassifierSummary = {}  # type: ignore[typeddict-item]
    if data.get("DocumentClassifierName") is not None:
        out["document_classifier_name"] = data["DocumentClassifierName"]
    if data.get("NumberOfVersions") is not None:
        out["number_of_versions"] = data["NumberOfVersions"]
    if data.get("LatestVersionCreatedAt") is not None:
        import capo_comprehend.types.timestamp

        out["latest_version_created_at"] = (
            capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["LatestVersionCreatedAt"]
            )
        )
    if data.get("LatestVersionName") is not None:
        out["latest_version_name"] = data["LatestVersionName"]
    if data.get("LatestVersionStatus") is not None:
        import capo_comprehend.types.model_status

        out["latest_version_status"] = (
            capo_comprehend.types.model_status.deserialize_aws_json_1_1(
                data["LatestVersionStatus"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DocumentClassifierSummary) -> dict:
    out: dict = {}
    if "document_classifier_name" in value:
        out["DocumentClassifierName"] = value["document_classifier_name"]
    if "number_of_versions" in value:
        out["NumberOfVersions"] = value["number_of_versions"]
    if "latest_version_created_at" in value:
        import capo_comprehend.types.timestamp

        out["LatestVersionCreatedAt"] = capo_comprehend.types.timestamp.serialize_cbor(
            value["latest_version_created_at"]
        )
    if "latest_version_name" in value:
        out["LatestVersionName"] = value["latest_version_name"]
    if "latest_version_status" in value:
        import capo_comprehend.types.model_status

        out["LatestVersionStatus"] = capo_comprehend.types.model_status.serialize_cbor(
            value["latest_version_status"]
        )
    return out


def deserialize_cbor(data: dict) -> DocumentClassifierSummary:
    out: DocumentClassifierSummary = {}  # type: ignore[typeddict-item]
    if data.get("DocumentClassifierName") is not None:
        out["document_classifier_name"] = data["DocumentClassifierName"]
    if data.get("NumberOfVersions") is not None:
        out["number_of_versions"] = data["NumberOfVersions"]
    if data.get("LatestVersionCreatedAt") is not None:
        import capo_comprehend.types.timestamp

        out["latest_version_created_at"] = (
            capo_comprehend.types.timestamp.deserialize_cbor(
                data["LatestVersionCreatedAt"]
            )
        )
    if data.get("LatestVersionName") is not None:
        out["latest_version_name"] = data["LatestVersionName"]
    if data.get("LatestVersionStatus") is not None:
        import capo_comprehend.types.model_status

        out["latest_version_status"] = (
            capo_comprehend.types.model_status.deserialize_cbor(
                data["LatestVersionStatus"]
            )
        )
    return out
