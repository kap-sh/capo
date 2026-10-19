"""Generated from Smithy shape ``com.amazonaws.ssm#DeleteDocumentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.boolean
    import capo_ssm.types.document_name
    import capo_ssm.types.document_version
    import capo_ssm.types.document_version_name


class DeleteDocumentRequest(TypedDict, closed=True):
    name: "capo_ssm.types.document_name.DocumentName"
    """<p>The name of the document.</p>"""
    document_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The version of the document that you want to delete. If not provided, all versions of the document are deleted.</p>"""
    version_name: NotRequired[
        "capo_ssm.types.document_version_name.DocumentVersionName"
    ]
    """<p>The version name of the document that you want to delete. If not provided, all versions of the document are deleted.</p>"""
    force: NotRequired["capo_ssm.types.boolean.Boolean"]
    """<p>Some SSM document types require that you specify a <code>Force</code> flag before you can delete the document. For example, you must specify a <code>Force</code> flag to delete a document of type <code>ApplicationConfigurationSchema</code>. You can restrict access to the <code>Force</code> flag in an Identity and Access Management (IAM) policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDocumentRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "version_name" in value:
        out["VersionName"] = value["version_name"]
    if "force" in value:
        out["Force"] = value["force"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDocumentRequest:
    out: DeleteDocumentRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteDocumentRequest.name required")
    if data.get("DocumentVersion") is not None:
        out["document_version"] = data["DocumentVersion"]
    if data.get("VersionName") is not None:
        out["version_name"] = data["VersionName"]
    if data.get("Force") is not None:
        out["force"] = data["Force"]
    return out
