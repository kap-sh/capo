"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeDocumentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.document_arn
    import capo_ssm.types.document_version
    import capo_ssm.types.document_version_name


class DescribeDocumentRequest(TypedDict, closed=True):
    name: "capo_ssm.types.document_arn.DocumentARN"
    """<p>The name of the SSM document.</p> <note> <p>If you're calling a shared SSM document from a different Amazon Web Services account, <code>Name</code> is the full Amazon Resource Name (ARN) of the document.</p> </note>"""
    document_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The document version for which you want information. Can be a specific version or the default version.</p>"""
    version_name: NotRequired[
        "capo_ssm.types.document_version_name.DocumentVersionName"
    ]
    """<p>An optional field specifying the version of the artifact associated with the document. For example, 12.6. This value is unique across all versions of a document, and can't be changed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDocumentRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "version_name" in value:
        out["VersionName"] = value["version_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDocumentRequest:
    out: DescribeDocumentRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("DocumentVersion") is not None:
        out["document_version"] = data["DocumentVersion"]
    if data.get("VersionName") is not None:
        out["version_name"] = data["VersionName"]
    return out
