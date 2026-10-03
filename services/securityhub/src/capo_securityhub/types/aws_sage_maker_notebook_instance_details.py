"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsSageMakerNotebookInstanceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_sage_maker_notebook_instance_metadata_service_configuration_details
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class AwsSageMakerNotebookInstanceDetails(TypedDict, closed=True):
    accelerator_types: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p> A list of Amazon Elastic Inference instance types to associate with the notebook instance. Currently, only one instance type can be associated with a notebook instance. </p>"""
    additional_code_repositories: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p> An array of up to three Git repositories associated with the notebook instance. These can be either the names of Git repositories stored as resources in your account, or the URL of Git repositories in <a href="https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html">CodeCommit</a> or in any other Git repository. These repositories are cloned at the same level as the default repository of your notebook instance. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html">Associating Git repositories with SageMaker AI notebook instances</a> in the <i>Amazon SageMaker AI Developer Guide</i>. </p>"""
    default_code_repository: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Git repository associated with the notebook instance as its default code repository. This can be either the name of a Git repository stored as a resource in your account, or the URL of a Git repository in <a href="https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html">CodeCommit</a> or in any other Git repository. When you open a notebook instance, it opens in the directory that contains this repository. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html">Associating Git repositories with SageMaker AI notebook instances</a> in the <i>Amazon SageMaker AI Developer Guide</i>. </p>"""
    direct_internet_access: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> Sets whether SageMaker AI provides internet access to the notebook instance. If you set this to <code>Disabled</code>, this notebook instance is able to access resources only in your VPC, and is not be able to connect to SageMaker AI training and endpoint services unless you configure a Network Address Translation (NAT) Gateway in your VPC. </p>"""
    failure_reason: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> If status of the instance is <code>Failed</code>, the reason it failed. </p>"""
    instance_metadata_service_configuration: NotRequired[
        "capo_securityhub.types.aws_sage_maker_notebook_instance_metadata_service_configuration_details.AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetails"
    ]
    """<p> Information on the IMDS configuration of the notebook instance. </p>"""
    instance_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The type of machine learning (ML) compute instance to launch for the notebook instance. </p>"""
    kms_key_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) of an Key Management Service (KMS) key that SageMaker AI uses to encrypt data on the storage volume attached to your notebook instance. The KMS key you provide must be enabled. For information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html">Enabling and disabling keys</a> in the <i>Key Management Service Developer Guide</i>. </p>"""
    network_interface_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The network interface ID that SageMaker AI created when the instance was created. </p>"""
    notebook_instance_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of the notebook instance. </p>"""
    notebook_instance_lifecycle_config_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The name of a notebook instance lifecycle configuration. </p>"""
    notebook_instance_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The name of the new notebook instance. </p>"""
    notebook_instance_status: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The status of the notebook instance. </p>"""
    platform_identifier: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The platform identifier of the notebook instance runtime environment. </p>"""
    role_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) of the IAM role associated with the instance. </p>"""
    root_access: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> Whether root access is enabled or disabled for users of the notebook instance. </p>"""
    security_groups: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p> The VPC security group IDs. </p>"""
    subnet_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The ID of the VPC subnet to which you have a connectivity from your ML compute instance. </p>"""
    url: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The URL that you use to connect to the Jupyter notebook that is running in your notebook instance. </p>"""
    volume_size_in_gb: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The size, in GB, of the ML storage volume to attach to the notebook instance. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsSageMakerNotebookInstanceDetails) -> dict:
    out: dict = {}
    if "accelerator_types" in value:
        import capo_securityhub.types.non_empty_string_list

        out["AcceleratorTypes"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["accelerator_types"]
            )
        )
    if "additional_code_repositories" in value:
        import capo_securityhub.types.non_empty_string_list

        out["AdditionalCodeRepositories"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["additional_code_repositories"]
            )
        )
    if "default_code_repository" in value:
        out["DefaultCodeRepository"] = value["default_code_repository"]
    if "direct_internet_access" in value:
        out["DirectInternetAccess"] = value["direct_internet_access"]
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "instance_metadata_service_configuration" in value:
        import capo_securityhub.types.aws_sage_maker_notebook_instance_metadata_service_configuration_details

        out["InstanceMetadataServiceConfiguration"] = (
            capo_securityhub.types.aws_sage_maker_notebook_instance_metadata_service_configuration_details.serialize_json(
                value["instance_metadata_service_configuration"]
            )
        )
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "network_interface_id" in value:
        out["NetworkInterfaceId"] = value["network_interface_id"]
    if "notebook_instance_arn" in value:
        out["NotebookInstanceArn"] = value["notebook_instance_arn"]
    if "notebook_instance_lifecycle_config_name" in value:
        out["NotebookInstanceLifecycleConfigName"] = value[
            "notebook_instance_lifecycle_config_name"
        ]
    if "notebook_instance_name" in value:
        out["NotebookInstanceName"] = value["notebook_instance_name"]
    if "notebook_instance_status" in value:
        out["NotebookInstanceStatus"] = value["notebook_instance_status"]
    if "platform_identifier" in value:
        out["PlatformIdentifier"] = value["platform_identifier"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "root_access" in value:
        out["RootAccess"] = value["root_access"]
    if "security_groups" in value:
        import capo_securityhub.types.non_empty_string_list

        out["SecurityGroups"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["security_groups"]
            )
        )
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "url" in value:
        out["Url"] = value["url"]
    if "volume_size_in_gb" in value:
        out["VolumeSizeInGB"] = value["volume_size_in_gb"]
    return out


def deserialize_json(data: dict) -> AwsSageMakerNotebookInstanceDetails:
    out: AwsSageMakerNotebookInstanceDetails = {}  # type: ignore[typeddict-item]
    if data.get("AcceleratorTypes") is not None:
        import capo_securityhub.types.non_empty_string_list

        out["accelerator_types"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["AcceleratorTypes"]
            )
        )
    if data.get("AdditionalCodeRepositories") is not None:
        import capo_securityhub.types.non_empty_string_list

        out["additional_code_repositories"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["AdditionalCodeRepositories"]
            )
        )
    if data.get("DefaultCodeRepository") is not None:
        out["default_code_repository"] = data["DefaultCodeRepository"]
    if data.get("DirectInternetAccess") is not None:
        out["direct_internet_access"] = data["DirectInternetAccess"]
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("InstanceMetadataServiceConfiguration") is not None:
        import capo_securityhub.types.aws_sage_maker_notebook_instance_metadata_service_configuration_details

        out["instance_metadata_service_configuration"] = (
            capo_securityhub.types.aws_sage_maker_notebook_instance_metadata_service_configuration_details.deserialize_json(
                data["InstanceMetadataServiceConfiguration"]
            )
        )
    if data.get("InstanceType") is not None:
        out["instance_type"] = data["InstanceType"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("NetworkInterfaceId") is not None:
        out["network_interface_id"] = data["NetworkInterfaceId"]
    if data.get("NotebookInstanceArn") is not None:
        out["notebook_instance_arn"] = data["NotebookInstanceArn"]
    if data.get("NotebookInstanceLifecycleConfigName") is not None:
        out["notebook_instance_lifecycle_config_name"] = data[
            "NotebookInstanceLifecycleConfigName"
        ]
    if data.get("NotebookInstanceName") is not None:
        out["notebook_instance_name"] = data["NotebookInstanceName"]
    if data.get("NotebookInstanceStatus") is not None:
        out["notebook_instance_status"] = data["NotebookInstanceStatus"]
    if data.get("PlatformIdentifier") is not None:
        out["platform_identifier"] = data["PlatformIdentifier"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("RootAccess") is not None:
        out["root_access"] = data["RootAccess"]
    if data.get("SecurityGroups") is not None:
        import capo_securityhub.types.non_empty_string_list

        out["security_groups"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["SecurityGroups"]
            )
        )
    if data.get("SubnetId") is not None:
        out["subnet_id"] = data["SubnetId"]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    if data.get("VolumeSizeInGB") is not None:
        out["volume_size_in_gb"] = data["VolumeSizeInGB"]
    return out
