"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateDocumentDefaultVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.document_name
    import capo_ssm.types.document_version_number


class UpdateDocumentDefaultVersionRequest(TypedDict, closed=True):
    name: "capo_ssm.types.document_name.DocumentName"
    """<p>The name of a custom document that you want to set as the default version.</p>"""
    document_version: "capo_ssm.types.document_version_number.DocumentVersionNumber"
    """<p>The version of a custom document that you want to set as the default version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDocumentDefaultVersionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["DocumentVersion"] = value["document_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDocumentDefaultVersionRequest:
    out: UpdateDocumentDefaultVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("DocumentVersion") is not None:
        out["document_version"] = data["DocumentVersion"]
    else:
        out["document_version"] = ""
    return out
