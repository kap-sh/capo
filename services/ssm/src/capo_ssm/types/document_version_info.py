"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentVersionInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.boolean
    import capo_ssm.types.date_time
    import capo_ssm.types.document_display_name
    import capo_ssm.types.document_format
    import capo_ssm.types.document_name
    import capo_ssm.types.document_status
    import capo_ssm.types.document_status_information
    import capo_ssm.types.document_version
    import capo_ssm.types.document_version_name
    import capo_ssm.types.review_status


class DocumentVersionInfo(TypedDict, closed=True):
    name: NotRequired["capo_ssm.types.document_name.DocumentName"]
    """<p>The document name.</p>"""
    display_name: NotRequired[
        "capo_ssm.types.document_display_name.DocumentDisplayName"
    ]
    """<p>The friendly name of the SSM document. This value can differ for each version of the document. If you want to update this value, see <a>UpdateDocument</a>.</p>"""
    document_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The document version.</p>"""
    version_name: NotRequired[
        "capo_ssm.types.document_version_name.DocumentVersionName"
    ]
    """<p>The version of the artifact associated with the document. For example, 12.6. This value is unique across all versions of a document, and can't be changed.</p>"""
    created_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date the document was created.</p>"""
    is_default_version: "capo_ssm.types.boolean.Boolean"
    """<p>An identifier for the default version of the document.</p>"""
    document_format: NotRequired["capo_ssm.types.document_format.DocumentFormat"]
    """<p>The document format, either JSON or YAML.</p>"""
    status: NotRequired["capo_ssm.types.document_status.DocumentStatus"]
    """<p>The status of the SSM document, such as <code>Creating</code>, <code>Active</code>, <code>Failed</code>, and <code>Deleting</code>.</p>"""
    status_information: NotRequired[
        "capo_ssm.types.document_status_information.DocumentStatusInformation"
    ]
    """<p>A message returned by Amazon Web Services Systems Manager that explains the <code>Status</code> value. For example, a <code>Failed</code> status might be explained by the <code>StatusInformation</code> message, "The specified S3 bucket doesn't exist. Verify that the URL of the S3 bucket is correct."</p>"""
    review_status: NotRequired["capo_ssm.types.review_status.ReviewStatus"]
    """<p>The current status of the approval review for the latest version of the document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentVersionInfo) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "version_name" in value:
        out["VersionName"] = value["version_name"]
    if "created_date" in value:
        import capo_ssm.types.date_time

        out["CreatedDate"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["created_date"]
        )
    out["IsDefaultVersion"] = value.get("is_default_version", False)
    if "document_format" in value:
        import capo_ssm.types.document_format

        out["DocumentFormat"] = capo_ssm.types.document_format.serialize_aws_json_1_1(
            value["document_format"]
        )
    if "status" in value:
        import capo_ssm.types.document_status

        out["Status"] = capo_ssm.types.document_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_information" in value:
        out["StatusInformation"] = value["status_information"]
    if "review_status" in value:
        import capo_ssm.types.review_status

        out["ReviewStatus"] = capo_ssm.types.review_status.serialize_aws_json_1_1(
            value["review_status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentVersionInfo:
    out: DocumentVersionInfo = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("DocumentVersion") is not None:
        out["document_version"] = data["DocumentVersion"]
    if data.get("VersionName") is not None:
        out["version_name"] = data["VersionName"]
    if data.get("CreatedDate") is not None:
        import capo_ssm.types.date_time

        out["created_date"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["CreatedDate"]
        )
    if data.get("IsDefaultVersion") is not None:
        out["is_default_version"] = data["IsDefaultVersion"]
    else:
        out["is_default_version"] = False
    if data.get("DocumentFormat") is not None:
        import capo_ssm.types.document_format

        out["document_format"] = (
            capo_ssm.types.document_format.deserialize_aws_json_1_1(
                data["DocumentFormat"]
            )
        )
    if data.get("Status") is not None:
        import capo_ssm.types.document_status

        out["status"] = capo_ssm.types.document_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("StatusInformation") is not None:
        out["status_information"] = data["StatusInformation"]
    if data.get("ReviewStatus") is not None:
        import capo_ssm.types.review_status

        out["review_status"] = capo_ssm.types.review_status.deserialize_aws_json_1_1(
            data["ReviewStatus"]
        )
    return out
