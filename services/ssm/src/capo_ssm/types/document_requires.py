"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentRequires``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.document_arn
    import capo_ssm.types.document_version
    import capo_ssm.types.document_version_name
    import capo_ssm.types.require_type


class DocumentRequires(TypedDict, closed=True):
    name: "capo_ssm.types.document_arn.DocumentARN"
    """<p>The name of the required SSM document. The name can be an Amazon Resource Name (ARN).</p>"""
    version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The document version required by the current document.</p>"""
    require_type: NotRequired["capo_ssm.types.require_type.RequireType"]
    """<p>The document type of the required SSM document.</p>"""
    version_name: NotRequired[
        "capo_ssm.types.document_version_name.DocumentVersionName"
    ]
    """<p>An optional field specifying the version of the artifact associated with the document. For example, 12.6. This value is unique across all versions of a document, and can't be changed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentRequires) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "version" in value:
        out["Version"] = value["version"]
    if "require_type" in value:
        out["RequireType"] = value["require_type"]
    if "version_name" in value:
        out["VersionName"] = value["version_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentRequires:
    out: DocumentRequires = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("RequireType") is not None:
        out["require_type"] = data["RequireType"]
    if data.get("VersionName") is not None:
        out["version_name"] = data["VersionName"]
    return out
