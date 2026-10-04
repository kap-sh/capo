"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateDocumentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.attachments_source_list
    import capo_ssm.types.document_content
    import capo_ssm.types.document_display_name
    import capo_ssm.types.document_format
    import capo_ssm.types.document_name
    import capo_ssm.types.document_version
    import capo_ssm.types.document_version_name
    import capo_ssm.types.target_type


class UpdateDocumentRequest(TypedDict, closed=True):
    content: "capo_ssm.types.document_content.DocumentContent"
    """<p>A valid JSON or YAML string.</p>"""
    attachments: NotRequired[
        "capo_ssm.types.attachments_source_list.AttachmentsSourceList"
    ]
    """<p>A list of key-value pairs that describe attachments to a version of a document.</p>"""
    name: "capo_ssm.types.document_name.DocumentName"
    """<p>The name of the SSM document that you want to update.</p>"""
    display_name: NotRequired[
        "capo_ssm.types.document_display_name.DocumentDisplayName"
    ]
    """<p>The friendly name of the SSM document that you want to update. This value can differ for each version of the document. If you don't specify a value for this parameter in your request, the existing value is applied to the new document version.</p>"""
    version_name: NotRequired[
        "capo_ssm.types.document_version_name.DocumentVersionName"
    ]
    """<p>An optional field specifying the version of the artifact you are updating with the document. For example, 12.6. This value is unique across all versions of a document, and can't be changed.</p>"""
    document_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The version of the document that you want to update. Currently, Systems Manager supports updating only the latest version of the document. You can specify the version number of the latest version or use the <code>$LATEST</code> variable.</p> <note> <p>If you change a document version for a State Manager association, Systems Manager immediately runs the association unless you previously specifed the <code>apply-only-at-cron-interval</code> parameter.</p> </note>"""
    document_format: NotRequired["capo_ssm.types.document_format.DocumentFormat"]
    """<p>Specify the document format for the new document version. The document format can be JSON, YAML, or TEXT. JSON is the default format.</p>"""
    target_type: NotRequired["capo_ssm.types.target_type.TargetType"]
    """<p>Specify a new target type for the document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDocumentRequest) -> dict:
    out: dict = {}
    out["Content"] = value["content"]
    if "attachments" in value:
        import capo_ssm.types.attachments_source_list

        out["Attachments"] = (
            capo_ssm.types.attachments_source_list.serialize_aws_json_1_1(
                value["attachments"]
            )
        )
    out["Name"] = value["name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "version_name" in value:
        out["VersionName"] = value["version_name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "document_format" in value:
        import capo_ssm.types.document_format

        out["DocumentFormat"] = capo_ssm.types.document_format.serialize_aws_json_1_1(
            value["document_format"]
        )
    if "target_type" in value:
        out["TargetType"] = value["target_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDocumentRequest:
    out: UpdateDocumentRequest = {}  # type: ignore[typeddict-item]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    else:
        raise DeserializationError("UpdateDocumentRequest.content required")
    if data.get("Attachments") is not None:
        import capo_ssm.types.attachments_source_list

        out["attachments"] = (
            capo_ssm.types.attachments_source_list.deserialize_aws_json_1_1(
                data["Attachments"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateDocumentRequest.name required")
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("VersionName") is not None:
        out["version_name"] = data["VersionName"]
    if data.get("DocumentVersion") is not None:
        out["document_version"] = data["DocumentVersion"]
    if data.get("DocumentFormat") is not None:
        import capo_ssm.types.document_format

        out["document_format"] = (
            capo_ssm.types.document_format.deserialize_aws_json_1_1(
                data["DocumentFormat"]
            )
        )
    if data.get("TargetType") is not None:
        out["target_type"] = data["TargetType"]
    return out
