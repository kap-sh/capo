"""Generated from Smithy shape ``com.amazonaws.ssm#CreateDocumentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.attachments_source_list
    import capo_ssm.types.document_content
    import capo_ssm.types.document_display_name
    import capo_ssm.types.document_format
    import capo_ssm.types.document_name
    import capo_ssm.types.document_requires_list
    import capo_ssm.types.document_type
    import capo_ssm.types.document_version_name
    import capo_ssm.types.tag_list
    import capo_ssm.types.target_type


class CreateDocumentRequest(TypedDict, closed=True):
    content: "capo_ssm.types.document_content.DocumentContent"
    """<p>The content for the new SSM document in JSON or YAML format. The content of the document must not exceed 64KB. This quota also includes the content specified for input parameters at runtime. We recommend storing the contents for your new document in an external JSON or YAML file and referencing the file in a command.</p> <p>For examples, see the following topics in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-using.html#create-ssm-console">Create an SSM document (console)</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-using.html#create-ssm-document-cli">Create an SSM document (command line)</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-using.html#create-ssm-document-api">Create an SSM document (API)</a> </p> </li> </ul>"""
    requires: NotRequired["capo_ssm.types.document_requires_list.DocumentRequiresList"]
    """<p>A list of SSM documents required by a document. This parameter is used exclusively by AppConfig. When a user creates an AppConfig configuration in an SSM document, the user must also specify a required document for validation purposes. In this case, an <code>ApplicationConfiguration</code> document requires an <code>ApplicationConfigurationSchema</code> document for validation purposes. For more information, see <a href="https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html">What is AppConfig?</a> in the <i>AppConfig User Guide</i>.</p>"""
    attachments: NotRequired[
        "capo_ssm.types.attachments_source_list.AttachmentsSourceList"
    ]
    """<p>A list of key-value pairs that describe attachments to a version of a document.</p>"""
    name: "capo_ssm.types.document_name.DocumentName"
    """<p>A name for the SSM document.</p> <important> <p>You can't use the following strings as document name prefixes. These are reserved by Amazon Web Services for use as document name prefixes:</p> <ul> <li> <p> <code>aws</code> </p> </li> <li> <p> <code>amazon</code> </p> </li> <li> <p> <code>amzn</code> </p> </li> <li> <p> <code>AWSEC2</code> </p> </li> <li> <p> <code>AWSConfigRemediation</code> </p> </li> <li> <p> <code>AWSSupport</code> </p> </li> </ul> </important>"""
    display_name: NotRequired[
        "capo_ssm.types.document_display_name.DocumentDisplayName"
    ]
    """<p>An optional field where you can specify a friendly name for the SSM document. This value can differ for each version of the document. You can update this value at a later time using the <a>UpdateDocument</a> operation.</p>"""
    version_name: NotRequired[
        "capo_ssm.types.document_version_name.DocumentVersionName"
    ]
    """<p>An optional field specifying the version of the artifact you are creating with the document. For example, <code>Release12.1</code>. This value is unique across all versions of a document, and can't be changed.</p>"""
    document_type: NotRequired["capo_ssm.types.document_type.DocumentType"]
    """<p>The type of document to create.</p> <note> <p>The <code>DeploymentStrategy</code> document type is an internal-use-only document type reserved for AppConfig.</p> </note>"""
    document_format: NotRequired["capo_ssm.types.document_format.DocumentFormat"]
    """<p>Specify the document format for the request. The document format can be JSON, YAML, or TEXT. JSON is the default format.</p>"""
    target_type: NotRequired["capo_ssm.types.target_type.TargetType"]
    """<p>Specify a target type to define the kinds of resources the document can run on. For example, to run a document on EC2 instances, specify the following value: <code>/AWS::EC2::Instance</code>. If you specify a value of '/' the document can run on all types of resources. If you don't specify a value, the document can't run on any resources. For a list of valid resource types, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html">Amazon Web Services resource and property types reference</a> in the <i>CloudFormation User Guide</i>. </p>"""
    tags: NotRequired["capo_ssm.types.tag_list.TagList"]
    """<p>Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag an SSM document to identify the types of targets or the environment where it will run. In this case, you could specify the following key-value pairs:</p> <ul> <li> <p> <code>Key=OS,Value=Windows</code> </p> </li> <li> <p> <code>Key=Environment,Value=Production</code> </p> </li> </ul> <note> <p>To add tags to an existing SSM document, use the <a>AddTagsToResource</a> operation.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDocumentRequest) -> dict:
    out: dict = {}
    out["Content"] = value["content"]
    if "requires" in value:
        import capo_ssm.types.document_requires_list

        out["Requires"] = capo_ssm.types.document_requires_list.serialize_aws_json_1_1(
            value["requires"]
        )
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
    if "target_type" in value:
        out["TargetType"] = value["target_type"]
    if "tags" in value:
        import capo_ssm.types.tag_list

        out["Tags"] = capo_ssm.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDocumentRequest:
    out: CreateDocumentRequest = {}  # type: ignore[typeddict-item]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    else:
        raise DeserializationError("CreateDocumentRequest.content required")
    if data.get("Requires") is not None:
        import capo_ssm.types.document_requires_list

        out["requires"] = (
            capo_ssm.types.document_requires_list.deserialize_aws_json_1_1(
                data["Requires"]
            )
        )
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
        raise DeserializationError("CreateDocumentRequest.name required")
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("VersionName") is not None:
        out["version_name"] = data["VersionName"]
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
    if data.get("TargetType") is not None:
        out["target_type"] = data["TargetType"]
    if data.get("Tags") is not None:
        import capo_ssm.types.tag_list

        out["tags"] = capo_ssm.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
