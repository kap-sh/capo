"""Generated from Smithy shape ``com.amazonaws.ssm#GetDocumentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.attachment_content_list
    import capo_ssm.types.date_time
    import capo_ssm.types.document_arn
    import capo_ssm.types.document_content
    import capo_ssm.types.document_display_name
    import capo_ssm.types.document_format
    import capo_ssm.types.document_requires_list
    import capo_ssm.types.document_status
    import capo_ssm.types.document_status_information
    import capo_ssm.types.document_type
    import capo_ssm.types.document_version
    import capo_ssm.types.document_version_name
    import capo_ssm.types.review_status


class GetDocumentResult(TypedDict, closed=True):
    name: NotRequired["capo_ssm.types.document_arn.DocumentARN"]
    """<p>The name of the SSM document.</p>"""
    created_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date the SSM document was created.</p>"""
    display_name: NotRequired[
        "capo_ssm.types.document_display_name.DocumentDisplayName"
    ]
    """<p>The friendly name of the SSM document. This value can differ for each version of the document. If you want to update this value, see <a>UpdateDocument</a>.</p>"""
    version_name: NotRequired[
        "capo_ssm.types.document_version_name.DocumentVersionName"
    ]
    """<p>The version of the artifact associated with the document. For example, 12.6. This value is unique across all versions of a document, and can't be changed.</p>"""
    document_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The document version.</p>"""
    status: NotRequired["capo_ssm.types.document_status.DocumentStatus"]
    """<p>The status of the SSM document, such as <code>Creating</code>, <code>Active</code>, <code>Updating</code>, <code>Failed</code>, and <code>Deleting</code>.</p>"""
    status_information: NotRequired[
        "capo_ssm.types.document_status_information.DocumentStatusInformation"
    ]
    """<p>A message returned by Amazon Web Services Systems Manager that explains the <code>Status</code> value. For example, a <code>Failed</code> status might be explained by the <code>StatusInformation</code> message, "The specified S3 bucket doesn't exist. Verify that the URL of the S3 bucket is correct."</p>"""
    content: NotRequired["capo_ssm.types.document_content.DocumentContent"]
    """<p>The contents of the SSM document.</p>"""
    document_type: NotRequired["capo_ssm.types.document_type.DocumentType"]
    """<p>The document type.</p>"""
    document_format: NotRequired["capo_ssm.types.document_format.DocumentFormat"]
    """<p>The document format, either JSON or YAML.</p>"""
    requires: NotRequired["capo_ssm.types.document_requires_list.DocumentRequiresList"]
    """<p>A list of SSM documents required by a document. For example, an <code>ApplicationConfiguration</code> document requires an <code>ApplicationConfigurationSchema</code> document.</p>"""
    attachments_content: NotRequired[
        "capo_ssm.types.attachment_content_list.AttachmentContentList"
    ]
    """<p>A description of the document attachments, including names, locations, sizes, and so on.</p>"""
    review_status: NotRequired["capo_ssm.types.review_status.ReviewStatus"]
    """<p>The current review status of a new custom Systems Manager document (SSM document) created by a member of your organization, or of the latest version of an existing SSM document.</p> <p>Only one version of an SSM document can be in the APPROVED state at a time. When a new version is approved, the status of the previous version changes to REJECTED.</p> <p>Only one version of an SSM document can be in review, or PENDING, at a time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDocumentResult) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "created_date" in value:
        import capo_ssm.types.date_time

        out["CreatedDate"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["created_date"]
        )
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "version_name" in value:
        out["VersionName"] = value["version_name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "status" in value:
        import capo_ssm.types.document_status

        out["Status"] = capo_ssm.types.document_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_information" in value:
        out["StatusInformation"] = value["status_information"]
    if "content" in value:
        out["Content"] = value["content"]
    if "document_type" in value:
        import capo_ssm.types.document_type

        out["DocumentType"] = capo_ssm.types.document_type.serialize_aws_json_1_1(
            value["document_type"]
        )
    if "document_format" in value:
        import capo_ssm.types.document_format

        out["DocumentFormat"] = capo_ssm.types.document_format.serialize_aws_json_1_1(
            value["document_format"]
        )
    if "requires" in value:
        import capo_ssm.types.document_requires_list

        out["Requires"] = capo_ssm.types.document_requires_list.serialize_aws_json_1_1(
            value["requires"]
        )
    if "attachments_content" in value:
        import capo_ssm.types.attachment_content_list

        out["AttachmentsContent"] = (
            capo_ssm.types.attachment_content_list.serialize_aws_json_1_1(
                value["attachments_content"]
            )
        )
    if "review_status" in value:
        import capo_ssm.types.review_status

        out["ReviewStatus"] = capo_ssm.types.review_status.serialize_aws_json_1_1(
            value["review_status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDocumentResult:
    out: GetDocumentResult = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("CreatedDate") is not None:
        import capo_ssm.types.date_time

        out["created_date"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["CreatedDate"]
        )
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("VersionName") is not None:
        out["version_name"] = data["VersionName"]
    if data.get("DocumentVersion") is not None:
        out["document_version"] = data["DocumentVersion"]
    if data.get("Status") is not None:
        import capo_ssm.types.document_status

        out["status"] = capo_ssm.types.document_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("StatusInformation") is not None:
        out["status_information"] = data["StatusInformation"]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    if data.get("DocumentType") is not None:
        import capo_ssm.types.document_type

        out["document_type"] = capo_ssm.types.document_type.deserialize_aws_json_1_1(
            data["DocumentType"]
        )
    if data.get("DocumentFormat") is not None:
        import capo_ssm.types.document_format

        out["document_format"] = (
            capo_ssm.types.document_format.deserialize_aws_json_1_1(
                data["DocumentFormat"]
            )
        )
    if data.get("Requires") is not None:
        import capo_ssm.types.document_requires_list

        out["requires"] = (
            capo_ssm.types.document_requires_list.deserialize_aws_json_1_1(
                data["Requires"]
            )
        )
    if data.get("AttachmentsContent") is not None:
        import capo_ssm.types.attachment_content_list

        out["attachments_content"] = (
            capo_ssm.types.attachment_content_list.deserialize_aws_json_1_1(
                data["AttachmentsContent"]
            )
        )
    if data.get("ReviewStatus") is not None:
        import capo_ssm.types.review_status

        out["review_status"] = capo_ssm.types.review_status.deserialize_aws_json_1_1(
            data["ReviewStatus"]
        )
    return out
