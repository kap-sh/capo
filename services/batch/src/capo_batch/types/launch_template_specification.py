"""Generated from Smithy shape ``com.amazonaws.batch#LaunchTemplateSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.launch_template_specification_override_list
    import capo_batch.types.string
    import capo_batch.types.userdata_type


class LaunchTemplateSpecification(TypedDict, closed=True):
    launch_template_id: NotRequired["capo_batch.types.string.String"]
    """<p>The ID of the launch template.</p>"""
    launch_template_name: NotRequired["capo_batch.types.string.String"]
    """<p>The name of the launch template.</p>"""
    version: NotRequired["capo_batch.types.string.String"]
    """<p>The version number of the launch template, <code>$Default</code>, or <code>$Latest</code>.</p> <p>If the value is <code>$Default</code>, the default version of the launch template is used. If the value is <code>$Latest</code>, the latest version of the launch template is used. </p> <important> <p>If the AMI ID that's used in a compute environment is from the launch template, the AMI isn't changed when the compute environment is updated. It's only changed if the <code>updateToLatestImageVersion</code> parameter for the compute environment is set to <code>true</code>. During an infrastructure update, if either <code>$Default</code> or <code>$Latest</code> is specified, Batch re-evaluates the launch template version, and it might use a different version of the launch template. This is the case even if the launch template isn't specified in the update. When updating a compute environment, changing the launch template requires an infrastructure update of the compute environment. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html">Updating compute environments</a> in the <i>Batch User Guide</i>.</p> </important> <p>Default: <code>$Default</code> </p> <p>Latest: <code>$Latest</code> </p>"""
    overrides: NotRequired[
        "capo_batch.types.launch_template_specification_override_list.LaunchTemplateSpecificationOverrideList"
    ]
    """<p>A launch template to use in place of the default launch template. You must specify either the launch template ID or launch template name in the request, but not both.</p> <p>You can specify up to ten (10) launch template overrides that are associated to unique instance types or families for each compute environment.</p> <note> <p>To unset all override templates for a compute environment, you can pass an empty array to the <a href="https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateComputeEnvironment.html">UpdateComputeEnvironment.overrides</a> parameter, or not include the <code>overrides</code> parameter when submitting the <code>UpdateComputeEnvironment</code> API operation.</p> </note>"""
    userdata_type: NotRequired["capo_batch.types.userdata_type.UserdataType"]
    """<p>The EKS node initialization process to use. You only need to specify this value if you are using a custom AMI. The default value is <code>EKS_BOOTSTRAP_SH</code>. If <i>imageType</i> is a custom AMI based on EKS_AL2023 or EKS_AL2023_NVIDIA then you must choose <code>EKS_NODEADM</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LaunchTemplateSpecification) -> dict:
    out: dict = {}
    if "launch_template_id" in value:
        out["launchTemplateId"] = value["launch_template_id"]
    if "launch_template_name" in value:
        out["launchTemplateName"] = value["launch_template_name"]
    if "version" in value:
        out["version"] = value["version"]
    if "overrides" in value:
        import capo_batch.types.launch_template_specification_override_list

        out["overrides"] = (
            capo_batch.types.launch_template_specification_override_list.serialize_json(
                value["overrides"]
            )
        )
    if "userdata_type" in value:
        import capo_batch.types.userdata_type

        out["userdataType"] = capo_batch.types.userdata_type.serialize_json(
            value["userdata_type"]
        )
    return out


def deserialize_json(data: dict) -> LaunchTemplateSpecification:
    out: LaunchTemplateSpecification = {}  # type: ignore[typeddict-item]
    if data.get("launchTemplateId") is not None:
        out["launch_template_id"] = data["launchTemplateId"]
    if data.get("launchTemplateName") is not None:
        out["launch_template_name"] = data["launchTemplateName"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("overrides") is not None:
        import capo_batch.types.launch_template_specification_override_list

        out["overrides"] = (
            capo_batch.types.launch_template_specification_override_list.deserialize_json(
                data["overrides"]
            )
        )
    if data.get("userdataType") is not None:
        import capo_batch.types.userdata_type

        out["userdata_type"] = capo_batch.types.userdata_type.deserialize_json(
            data["userdataType"]
        )
    return out
