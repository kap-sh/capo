"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CreateWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.boolean
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.inline_workflow_data
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.tag_map
    import capo_imagebuilder.types.uri
    import capo_imagebuilder.types.version_number
    import capo_imagebuilder.types.workflow_type


class CreateWorkflowRequest(TypedDict, closed=True):
    name: "capo_imagebuilder.types.resource_name.ResourceName"
    """<p>The name of the workflow to create. Image Builder generates the workflow ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name. If a workflow with the same name and semantic version already exists in your account in the same Amazon Web Services Region, the request creates a new build version for it. If the content is also identical to the latest build version, the request fails because the workflow already exists.</p>"""
    semantic_version: "capo_imagebuilder.types.version_number.VersionNumber"
    """<p>The semantic version of this workflow resource. The semantic version syntax adheres to the following rules.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> </note>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>Describes the workflow.</p>"""
    change_description: NotRequired[
        "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>Describes what change has been made in this version of the workflow, or what makes this version different from other versions of the workflow.</p>"""
    data: NotRequired["capo_imagebuilder.types.inline_workflow_data.InlineWorkflowData"]
    """<p>The UTF-8 encoded YAML document content for the workflow, up to 16,000 characters. For larger documents, store the document in Amazon S3 and specify the <code>uri</code> property instead. You must specify exactly one of the <code>data</code> or <code>uri</code> properties.</p>"""
    uri: NotRequired["capo_imagebuilder.types.uri.Uri"]
    """<p>The <code>uri</code> of a YAML workflow document file stored in Amazon S3. This must be an S3 URL (<code>s3://bucket/key</code>), and you must have permission to access the S3 bucket it points to. A workflow document that you provide from Amazon S3 can be up to your service quota for workflow size.</p> <p>Alternatively, you can specify the YAML document inline, using the workflow <code>data</code> property. You must specify exactly one of the <code>data</code> or <code>uri</code> properties.</p>"""
    kms_key_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the KMS key used to encrypt this workflow resource. This can be either the Key ARN or the Alias ARN. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN">Key identifiers (KeyId)</a> in the <i>Key Management Service Developer Guide</i>. If you don't specify a key, Image Builder encrypts the workflow document with a KMS key that Image Builder owns.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>Tags that apply to the workflow resource.</p>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""
    type: "capo_imagebuilder.types.workflow_type.WorkflowType"
    """<p>The image creation stage that this workflow applies to. Image Builder validates the workflow document steps against the stage you specify.</p>"""
    dry_run: "capo_imagebuilder.types.boolean.Boolean"
    """<p>Validates the required permissions and request parameters without performing the operation. If validation succeeds, the operation returns a <code>DryRunOperationException</code> error response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkflowRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["semanticVersion"] = value["semantic_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "change_description" in value:
        out["changeDescription"] = value["change_description"]
    if "data" in value:
        out["data"] = value["data"]
    if "uri" in value:
        out["uri"] = value["uri"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    out["clientToken"] = value["client_token"]
    import capo_imagebuilder.types.workflow_type

    out["type"] = capo_imagebuilder.types.workflow_type.serialize_json(value["type"])
    out["dryRun"] = value.get("dry_run", False)
    return out


def deserialize_json(data: dict) -> CreateWorkflowRequest:
    out: CreateWorkflowRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateWorkflowRequest.name required")
    if data.get("semanticVersion") is not None:
        out["semantic_version"] = data["semanticVersion"]
    else:
        raise DeserializationError("CreateWorkflowRequest.semantic_version required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("changeDescription") is not None:
        out["change_description"] = data["changeDescription"]
    if data.get("data") is not None:
        out["data"] = data["data"]
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("tags") is not None:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateWorkflowRequest.client_token required")
    if data.get("type") is not None:
        import capo_imagebuilder.types.workflow_type

        out["type"] = capo_imagebuilder.types.workflow_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("CreateWorkflowRequest.type required")
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    else:
        out["dry_run"] = False
    return out
