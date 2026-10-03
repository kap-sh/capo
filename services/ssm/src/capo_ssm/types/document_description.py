"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.attachment_information_list
    import capo_ssm.types.category_enum_list
    import capo_ssm.types.category_list
    import capo_ssm.types.date_time
    import capo_ssm.types.description_in_document
    import capo_ssm.types.document_arn
    import capo_ssm.types.document_author
    import capo_ssm.types.document_display_name
    import capo_ssm.types.document_format
    import capo_ssm.types.document_hash
    import capo_ssm.types.document_hash_type
    import capo_ssm.types.document_owner
    import capo_ssm.types.document_parameter_list
    import capo_ssm.types.document_requires_list
    import capo_ssm.types.document_schema_version
    import capo_ssm.types.document_sha1
    import capo_ssm.types.document_status
    import capo_ssm.types.document_status_information
    import capo_ssm.types.document_type
    import capo_ssm.types.document_version
    import capo_ssm.types.document_version_name
    import capo_ssm.types.platform_type_list
    import capo_ssm.types.review_information_list
    import capo_ssm.types.review_status
    import capo_ssm.types.tag_list
    import capo_ssm.types.target_type


class DocumentDescription(TypedDict, closed=True):
    sha1: NotRequired["capo_ssm.types.document_sha1.DocumentSha1"]
    """<p>The SHA1 hash of the document, which you can use for verification.</p>"""
    hash: NotRequired["capo_ssm.types.document_hash.DocumentHash"]
    """<p>The Sha256 or Sha1 hash created by the system when the document was created. </p> <note> <p>Sha1 hashes have been deprecated.</p> </note>"""
    hash_type: NotRequired["capo_ssm.types.document_hash_type.DocumentHashType"]
    """<p>The hash type of the document. Valid values include <code>Sha256</code> or <code>Sha1</code>.</p> <note> <p>Sha1 hashes have been deprecated.</p> </note>"""
    name: NotRequired["capo_ssm.types.document_arn.DocumentARN"]
    """<p>The name of the SSM document.</p>"""
    display_name: NotRequired[
        "capo_ssm.types.document_display_name.DocumentDisplayName"
    ]
    """<p>The friendly name of the SSM document. This value can differ for each version of the document. If you want to update this value, see <a>UpdateDocument</a>.</p>"""
    version_name: NotRequired[
        "capo_ssm.types.document_version_name.DocumentVersionName"
    ]
    """<p>The version of the artifact associated with the document.</p>"""
    owner: NotRequired["capo_ssm.types.document_owner.DocumentOwner"]
    """<p>The Amazon Web Services user that created the document.</p>"""
    created_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date when the document was created.</p>"""
    status: NotRequired["capo_ssm.types.document_status.DocumentStatus"]
    """<p>The status of the SSM document.</p>"""
    status_information: NotRequired[
        "capo_ssm.types.document_status_information.DocumentStatusInformation"
    ]
    """<p>A message returned by Amazon Web Services Systems Manager that explains the <code>Status</code> value. For example, a <code>Failed</code> status might be explained by the <code>StatusInformation</code> message, "The specified S3 bucket doesn't exist. Verify that the URL of the S3 bucket is correct."</p>"""
    document_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The document version.</p>"""
    description: NotRequired[
        "capo_ssm.types.description_in_document.DescriptionInDocument"
    ]
    """<p>A description of the document. </p>"""
    parameters: NotRequired[
        "capo_ssm.types.document_parameter_list.DocumentParameterList"
    ]
    """<p>A description of the parameters for a document.</p>"""
    platform_types: NotRequired["capo_ssm.types.platform_type_list.PlatformTypeList"]
    """<p>The list of operating system (OS) platforms compatible with this SSM document. </p>"""
    document_type: NotRequired["capo_ssm.types.document_type.DocumentType"]
    """<p>The type of document.</p>"""
    schema_version: NotRequired[
        "capo_ssm.types.document_schema_version.DocumentSchemaVersion"
    ]
    """<p>The schema version.</p>"""
    latest_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The latest version of the document.</p>"""
    default_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The default version.</p>"""
    document_format: NotRequired["capo_ssm.types.document_format.DocumentFormat"]
    """<p>The document format, either JSON or YAML.</p>"""
    target_type: NotRequired["capo_ssm.types.target_type.TargetType"]
    """<p>The target type which defines the kinds of resources the document can run on. For example, <code>/AWS::EC2::Instance</code>. For a list of valid resource types, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html">Amazon Web Services resource and property types reference</a> in the <i>CloudFormation User Guide</i>. </p>"""
    tags: NotRequired["capo_ssm.types.tag_list.TagList"]
    """<p>The tags, or metadata, that have been applied to the document.</p>"""
    attachments_information: NotRequired[
        "capo_ssm.types.attachment_information_list.AttachmentInformationList"
    ]
    """<p>Details about the document attachments, including names, locations, sizes, and so on.</p>"""
    requires: NotRequired["capo_ssm.types.document_requires_list.DocumentRequiresList"]
    """<p>A list of SSM documents required by a document. For example, an <code>ApplicationConfiguration</code> document requires an <code>ApplicationConfigurationSchema</code> document.</p>"""
    author: NotRequired["capo_ssm.types.document_author.DocumentAuthor"]
    """<p>The user in your organization who created the document.</p>"""
    review_information: NotRequired[
        "capo_ssm.types.review_information_list.ReviewInformationList"
    ]
    """<p>Details about the review of a document.</p>"""
    approved_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The version of the document currently approved for use in the organization.</p>"""
    pending_review_version: NotRequired[
        "capo_ssm.types.document_version.DocumentVersion"
    ]
    """<p>The version of the document that is currently under review.</p>"""
    review_status: NotRequired["capo_ssm.types.review_status.ReviewStatus"]
    """<p>The current status of the review.</p>"""
    category: NotRequired["capo_ssm.types.category_list.CategoryList"]
    """<p>The classification of a document to help you identify and categorize its use.</p>"""
    category_enum: NotRequired["capo_ssm.types.category_enum_list.CategoryEnumList"]
    """<p>The value that identifies a document's category.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentDescription) -> dict:
    out: dict = {}
    if "sha1" in value:
        out["Sha1"] = value["sha1"]
    if "hash" in value:
        out["Hash"] = value["hash"]
    if "hash_type" in value:
        import capo_ssm.types.document_hash_type

        out["HashType"] = capo_ssm.types.document_hash_type.serialize_aws_json_1_1(
            value["hash_type"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "version_name" in value:
        out["VersionName"] = value["version_name"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "created_date" in value:
        import capo_ssm.types.date_time

        out["CreatedDate"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["created_date"]
        )
    if "status" in value:
        import capo_ssm.types.document_status

        out["Status"] = capo_ssm.types.document_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_information" in value:
        out["StatusInformation"] = value["status_information"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "description" in value:
        out["Description"] = value["description"]
    if "parameters" in value:
        import capo_ssm.types.document_parameter_list

        out["Parameters"] = (
            capo_ssm.types.document_parameter_list.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    if "platform_types" in value:
        import capo_ssm.types.platform_type_list

        out["PlatformTypes"] = capo_ssm.types.platform_type_list.serialize_aws_json_1_1(
            value["platform_types"]
        )
    if "document_type" in value:
        import capo_ssm.types.document_type

        out["DocumentType"] = capo_ssm.types.document_type.serialize_aws_json_1_1(
            value["document_type"]
        )
    if "schema_version" in value:
        out["SchemaVersion"] = value["schema_version"]
    if "latest_version" in value:
        out["LatestVersion"] = value["latest_version"]
    if "default_version" in value:
        out["DefaultVersion"] = value["default_version"]
    if "document_format" in value:
        import capo_ssm.types.document_format

        out["DocumentFormat"] = capo_ssm.types.document_format.serialize_aws_json_1_1(
            value["document_format"]
        )
    if "target_type" in value:
        out["TargetType"] = value["target_type"]
    if "tags" in value:
        import capo_ssm.types.tag_list

        out["Tags"] = capo_ssm.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "attachments_information" in value:
        import capo_ssm.types.attachment_information_list

        out["AttachmentsInformation"] = (
            capo_ssm.types.attachment_information_list.serialize_aws_json_1_1(
                value["attachments_information"]
            )
        )
    if "requires" in value:
        import capo_ssm.types.document_requires_list

        out["Requires"] = capo_ssm.types.document_requires_list.serialize_aws_json_1_1(
            value["requires"]
        )
    if "author" in value:
        out["Author"] = value["author"]
    if "review_information" in value:
        import capo_ssm.types.review_information_list

        out["ReviewInformation"] = (
            capo_ssm.types.review_information_list.serialize_aws_json_1_1(
                value["review_information"]
            )
        )
    if "approved_version" in value:
        out["ApprovedVersion"] = value["approved_version"]
    if "pending_review_version" in value:
        out["PendingReviewVersion"] = value["pending_review_version"]
    if "review_status" in value:
        import capo_ssm.types.review_status

        out["ReviewStatus"] = capo_ssm.types.review_status.serialize_aws_json_1_1(
            value["review_status"]
        )
    if "category" in value:
        import capo_ssm.types.category_list

        out["Category"] = capo_ssm.types.category_list.serialize_aws_json_1_1(
            value["category"]
        )
    if "category_enum" in value:
        import capo_ssm.types.category_enum_list

        out["CategoryEnum"] = capo_ssm.types.category_enum_list.serialize_aws_json_1_1(
            value["category_enum"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentDescription:
    out: DocumentDescription = {}  # type: ignore[typeddict-item]
    if data.get("Sha1") is not None:
        out["sha1"] = data["Sha1"]
    if data.get("Hash") is not None:
        out["hash"] = data["Hash"]
    if data.get("HashType") is not None:
        import capo_ssm.types.document_hash_type

        out["hash_type"] = capo_ssm.types.document_hash_type.deserialize_aws_json_1_1(
            data["HashType"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("VersionName") is not None:
        out["version_name"] = data["VersionName"]
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("CreatedDate") is not None:
        import capo_ssm.types.date_time

        out["created_date"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["CreatedDate"]
        )
    if data.get("Status") is not None:
        import capo_ssm.types.document_status

        out["status"] = capo_ssm.types.document_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("StatusInformation") is not None:
        out["status_information"] = data["StatusInformation"]
    if data.get("DocumentVersion") is not None:
        out["document_version"] = data["DocumentVersion"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Parameters") is not None:
        import capo_ssm.types.document_parameter_list

        out["parameters"] = (
            capo_ssm.types.document_parameter_list.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    if data.get("PlatformTypes") is not None:
        import capo_ssm.types.platform_type_list

        out["platform_types"] = (
            capo_ssm.types.platform_type_list.deserialize_aws_json_1_1(
                data["PlatformTypes"]
            )
        )
    if data.get("DocumentType") is not None:
        import capo_ssm.types.document_type

        out["document_type"] = capo_ssm.types.document_type.deserialize_aws_json_1_1(
            data["DocumentType"]
        )
    if data.get("SchemaVersion") is not None:
        out["schema_version"] = data["SchemaVersion"]
    if data.get("LatestVersion") is not None:
        out["latest_version"] = data["LatestVersion"]
    if data.get("DefaultVersion") is not None:
        out["default_version"] = data["DefaultVersion"]
    if data.get("DocumentFormat") is not None:
        import capo_ssm.types.document_format

        out["document_format"] = (
            capo_ssm.types.document_format.deserialize_aws_json_1_1(
                data["DocumentFormat"]
            )
        )
    if data.get("TargetType") is not None:
        out["target_type"] = data["TargetType"]
    if data.get("Tags") is not None:
        import capo_ssm.types.tag_list

        out["tags"] = capo_ssm.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if data.get("AttachmentsInformation") is not None:
        import capo_ssm.types.attachment_information_list

        out["attachments_information"] = (
            capo_ssm.types.attachment_information_list.deserialize_aws_json_1_1(
                data["AttachmentsInformation"]
            )
        )
    if data.get("Requires") is not None:
        import capo_ssm.types.document_requires_list

        out["requires"] = (
            capo_ssm.types.document_requires_list.deserialize_aws_json_1_1(
                data["Requires"]
            )
        )
    if data.get("Author") is not None:
        out["author"] = data["Author"]
    if data.get("ReviewInformation") is not None:
        import capo_ssm.types.review_information_list

        out["review_information"] = (
            capo_ssm.types.review_information_list.deserialize_aws_json_1_1(
                data["ReviewInformation"]
            )
        )
    if data.get("ApprovedVersion") is not None:
        out["approved_version"] = data["ApprovedVersion"]
    if data.get("PendingReviewVersion") is not None:
        out["pending_review_version"] = data["PendingReviewVersion"]
    if data.get("ReviewStatus") is not None:
        import capo_ssm.types.review_status

        out["review_status"] = capo_ssm.types.review_status.deserialize_aws_json_1_1(
            data["ReviewStatus"]
        )
    if data.get("Category") is not None:
        import capo_ssm.types.category_list

        out["category"] = capo_ssm.types.category_list.deserialize_aws_json_1_1(
            data["Category"]
        )
    if data.get("CategoryEnum") is not None:
        import capo_ssm.types.category_enum_list

        out["category_enum"] = (
            capo_ssm.types.category_enum_list.deserialize_aws_json_1_1(
                data["CategoryEnum"]
            )
        )
    return out
