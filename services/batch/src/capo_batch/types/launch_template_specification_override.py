"""Generated from Smithy shape ``com.amazonaws.batch#LaunchTemplateSpecificationOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.string
    import capo_batch.types.string_list
    import capo_batch.types.userdata_type


class LaunchTemplateSpecificationOverride(TypedDict, closed=True):
    launch_template_id: NotRequired["capo_batch.types.string.String"]
    """<p>The ID of the launch template.</p> <p> <b>Note:</b> If you specify the <code>launchTemplateId</code> you can't specify the <code>launchTemplateName</code> as well.</p>"""
    launch_template_name: NotRequired["capo_batch.types.string.String"]
    """<p>The name of the launch template.</p> <p> <b>Note:</b> If you specify the <code>launchTemplateName</code> you can't specify the <code>launchTemplateId</code> as well.</p>"""
    version: NotRequired["capo_batch.types.string.String"]
    """<p>The version number of the launch template, <code>$Default</code>, or <code>$Latest</code>.</p> <p>If the value is <code>$Default</code>, the default version of the launch template is used. If the value is <code>$Latest</code>, the latest version of the launch template is used. </p> <important> <p>If the AMI ID that's used in a compute environment is from the launch template, the AMI isn't changed when the compute environment is updated. It's only changed if the <code>updateToLatestImageVersion</code> parameter for the compute environment is set to <code>true</code>. During an infrastructure update, if either <code>$Default</code> or <code>$Latest</code> is specified, Batch re-evaluates the launch template version, and it might use a different version of the launch template. This is the case even if the launch template isn't specified in the update. When updating a compute environment, changing the launch template requires an infrastructure update of the compute environment. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html">Updating compute environments</a> in the <i>Batch User Guide</i>.</p> </important> <p>Default: <code>$Default</code> </p> <p>Latest: <code>$Latest</code> </p>"""
    target_instance_types: NotRequired["capo_batch.types.string_list.StringList"]
    """<p>The instance type or family that this override launch template should be applied to.</p> <p>This parameter is required when defining a launch template override.</p> <p>Information included in this parameter must meet the following requirements:</p> <ul> <li> <p>Must be a valid Amazon EC2 instance type or family.</p> </li> <li> <p>The following Batch <code>InstanceTypes</code> are not allowed: <code>optimal</code>, <code>default_x86_64</code>, and <code>default_arm64</code>.</p> </li> <li> <p> <code>targetInstanceTypes</code> can target only instance types and families that are included within the <a href="https://docs.aws.amazon.com/batch/latest/APIReference/API_ComputeResource.html#Batch-Type-ComputeResource-instanceTypes"> <code>ComputeResource.instanceTypes</code> </a> set. <code>targetInstanceTypes</code> doesn't need to include all of the instances from the <code>instanceType</code> set, but at least a subset. For example, if <code>ComputeResource.instanceTypes</code> includes <code>[m5, g5]</code>, <code>targetInstanceTypes</code> can include <code>[m5.2xlarge]</code> and <code>[m5.large]</code> but not <code>[c5.large]</code>.</p> </li> <li> <p> <code>targetInstanceTypes</code> included within the same launch template override or across launch template overrides can't overlap for the same compute environment. For example, you can't define one launch template override to target an instance family and another define an instance type within this same family.</p> </li> </ul>"""
    userdata_type: NotRequired["capo_batch.types.userdata_type.UserdataType"]
    """<p>The EKS node initialization process to use. You only need to specify this value if you are using a custom AMI. The default value is <code>EKS_BOOTSTRAP_SH</code>. If <i>imageType</i> is a custom AMI based on EKS_AL2023 or EKS_AL2023_NVIDIA then you must choose <code>EKS_NODEADM</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LaunchTemplateSpecificationOverride) -> dict:
    out: dict = {}
    if "launch_template_id" in value:
        out["launchTemplateId"] = value["launch_template_id"]
    if "launch_template_name" in value:
        out["launchTemplateName"] = value["launch_template_name"]
    if "version" in value:
        out["version"] = value["version"]
    if "target_instance_types" in value:
        import capo_batch.types.string_list

        out["targetInstanceTypes"] = capo_batch.types.string_list.serialize_json(
            value["target_instance_types"]
        )
    if "userdata_type" in value:
        import capo_batch.types.userdata_type

        out["userdataType"] = capo_batch.types.userdata_type.serialize_json(
            value["userdata_type"]
        )
    return out


def deserialize_json(data: dict) -> LaunchTemplateSpecificationOverride:
    out: LaunchTemplateSpecificationOverride = {}  # type: ignore[typeddict-item]
    if data.get("launchTemplateId") is not None:
        out["launch_template_id"] = data["launchTemplateId"]
    if data.get("launchTemplateName") is not None:
        out["launch_template_name"] = data["launchTemplateName"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("targetInstanceTypes") is not None:
        import capo_batch.types.string_list

        out["target_instance_types"] = capo_batch.types.string_list.deserialize_json(
            data["targetInstanceTypes"]
        )
    if data.get("userdataType") is not None:
        import capo_batch.types.userdata_type

        out["userdata_type"] = capo_batch.types.userdata_type.deserialize_json(
            data["userdataType"]
        )
    return out
