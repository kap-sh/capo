"""Generated from Smithy shape ``com.amazonaws.ssm#CreateActivationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.activation_description
    import capo_ssm.types.default_instance_name
    import capo_ssm.types.expiration_date
    import capo_ssm.types.iam_role
    import capo_ssm.types.registration_limit
    import capo_ssm.types.registration_metadata_list
    import capo_ssm.types.tag_list


class CreateActivationRequest(TypedDict, closed=True):
    description: NotRequired[
        "capo_ssm.types.activation_description.ActivationDescription"
    ]
    """<p>A user-defined description of the resource that you want to register with Systems Manager. </p> <important> <p>Don't enter personally identifiable information in this field.</p> </important>"""
    default_instance_name: NotRequired[
        "capo_ssm.types.default_instance_name.DefaultInstanceName"
    ]
    """<p>The name of the registered, managed node as it will appear in the Amazon Web Services Systems Manager console or when you use the Amazon Web Services command line tools to list Systems Manager resources.</p> <important> <p>Don't enter personally identifiable information in this field.</p> </important>"""
    iam_role: "capo_ssm.types.iam_role.IamRole"
    """<p>The name of the Identity and Access Management (IAM) role that you want to assign to the managed node. This IAM role must provide AssumeRole permissions for the Amazon Web Services Systems Manager service principal <code>ssm.amazonaws.com</code>. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/hybrid-multicloud-service-role.html">Create the IAM service role required for Systems Manager in a hybrid and multicloud environments</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> <note> <p>You can't specify an IAM service-linked role for this parameter. You must create a unique role.</p> </note>"""
    registration_limit: NotRequired[
        "capo_ssm.types.registration_limit.RegistrationLimit"
    ]
    """<p>Specify the maximum number of managed nodes you want to register. The default value is <code>1</code>.</p>"""
    expiration_date: NotRequired["capo_ssm.types.expiration_date.ExpirationDate"]
    """<p>The date by which this activation request should expire, in timestamp format, such as "2024-07-07T00:00:00". You can specify a date up to 30 days in advance. If you don't provide an expiration date, the activation code expires in 24 hours.</p>"""
    tags: NotRequired["capo_ssm.types.tag_list.TagList"]
    """<p>Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag an activation to identify which servers or virtual machines (VMs) in your on-premises environment you intend to activate. In this case, you could specify the following key-value pairs:</p> <ul> <li> <p> <code>Key=OS,Value=Windows</code> </p> </li> <li> <p> <code>Key=Environment,Value=Production</code> </p> </li> </ul> <important> <p>When you install SSM Agent on your on-premises servers and VMs, you specify an activation ID and code. When you specify the activation ID and code, tags assigned to the activation are automatically applied to the on-premises servers or VMs.</p> </important> <p>You can't add tags to or delete tags from an existing activation. You can tag your on-premises servers, edge devices, and VMs after they connect to Systems Manager for the first time and are assigned a managed node ID. This means they are listed in the Amazon Web Services Systems Manager console with an ID that is prefixed with "mi-". For information about how to add tags to your managed nodes, see <a>AddTagsToResource</a>. For information about how to remove tags from your managed nodes, see <a>RemoveTagsFromResource</a>.</p>"""
    registration_metadata: NotRequired[
        "capo_ssm.types.registration_metadata_list.RegistrationMetadataList"
    ]
    """<p>Reserved for internal use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateActivationRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "default_instance_name" in value:
        out["DefaultInstanceName"] = value["default_instance_name"]
    out["IamRole"] = value["iam_role"]
    if "registration_limit" in value:
        out["RegistrationLimit"] = value["registration_limit"]
    if "expiration_date" in value:
        import capo_ssm.types.expiration_date

        out["ExpirationDate"] = capo_ssm.types.expiration_date.serialize_aws_json_1_1(
            value["expiration_date"]
        )
    if "tags" in value:
        import capo_ssm.types.tag_list

        out["Tags"] = capo_ssm.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "registration_metadata" in value:
        import capo_ssm.types.registration_metadata_list

        out["RegistrationMetadata"] = (
            capo_ssm.types.registration_metadata_list.serialize_aws_json_1_1(
                value["registration_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateActivationRequest:
    out: CreateActivationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DefaultInstanceName") is not None:
        out["default_instance_name"] = data["DefaultInstanceName"]
    if data.get("IamRole") is not None:
        out["iam_role"] = data["IamRole"]
    else:
        raise DeserializationError("CreateActivationRequest.iam_role required")
    if data.get("RegistrationLimit") is not None:
        out["registration_limit"] = data["RegistrationLimit"]
    if data.get("ExpirationDate") is not None:
        import capo_ssm.types.expiration_date

        out["expiration_date"] = (
            capo_ssm.types.expiration_date.deserialize_aws_json_1_1(
                data["ExpirationDate"]
            )
        )
    if data.get("Tags") is not None:
        import capo_ssm.types.tag_list

        out["tags"] = capo_ssm.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if data.get("RegistrationMetadata") is not None:
        import capo_ssm.types.registration_metadata_list

        out["registration_metadata"] = (
            capo_ssm.types.registration_metadata_list.deserialize_aws_json_1_1(
                data["RegistrationMetadata"]
            )
        )
    return out
