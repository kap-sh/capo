"""Generated from Smithy shape ``com.amazonaws.drs#UpdateLaunchConfigurationTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.arn
    import capo_drs.types.launch_configuration_template_id
    import capo_drs.types.launch_disposition
    import capo_drs.types.licensing
    import capo_drs.types.recovery_mode
    import capo_drs.types.target_instance_type_right_sizing_method


class UpdateLaunchConfigurationTemplateRequest(TypedDict, closed=True):
    launch_configuration_template_id: (
        "capo_drs.types.launch_configuration_template_id.LaunchConfigurationTemplateID"
    )
    """<p>Launch Configuration Template ID.</p>"""
    launch_disposition: NotRequired[
        "capo_drs.types.launch_disposition.LaunchDisposition"
    ]
    """<p>Launch disposition.</p>"""
    target_instance_type_right_sizing_method: NotRequired[
        "capo_drs.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
    ]
    """<p>Target instance type right-sizing method.</p>"""
    copy_private_ip: NotRequired["bool"]
    """<p>Copy private IP.</p>"""
    copy_tags: NotRequired["bool"]
    """<p>Copy tags.</p>"""
    licensing: NotRequired["capo_drs.types.licensing.Licensing"]
    """<p>Licensing.</p>"""
    export_bucket_arn: NotRequired["capo_drs.types.arn.ARN"]
    """<p>S3 bucket ARN to export Source Network templates.</p>"""
    post_launch_enabled: NotRequired["bool"]
    """<p>Whether we want to activate post-launch actions.</p>"""
    launch_into_source_instance: NotRequired["bool"]
    """<p>DRS will set the 'launch into instance ID' of any source server when performing a drill, recovery or failback to the previous region or availability zone, using the instance ID of the source instance.</p>"""
    recovery_mode: NotRequired["capo_drs.types.recovery_mode.RecoveryMode"]
    """<p>Recovery mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLaunchConfigurationTemplateRequest) -> dict:
    out: dict = {}
    out["launchConfigurationTemplateID"] = value["launch_configuration_template_id"]
    if "launch_disposition" in value:
        out["launchDisposition"] = value["launch_disposition"]
    if "target_instance_type_right_sizing_method" in value:
        out["targetInstanceTypeRightSizingMethod"] = value[
            "target_instance_type_right_sizing_method"
        ]
    if "copy_private_ip" in value:
        out["copyPrivateIp"] = value["copy_private_ip"]
    if "copy_tags" in value:
        out["copyTags"] = value["copy_tags"]
    if "licensing" in value:
        import capo_drs.types.licensing

        out["licensing"] = capo_drs.types.licensing.serialize_json(value["licensing"])
    if "export_bucket_arn" in value:
        out["exportBucketArn"] = value["export_bucket_arn"]
    if "post_launch_enabled" in value:
        out["postLaunchEnabled"] = value["post_launch_enabled"]
    if "launch_into_source_instance" in value:
        out["launchIntoSourceInstance"] = value["launch_into_source_instance"]
    if "recovery_mode" in value:
        out["recoveryMode"] = value["recovery_mode"]
    return out


def deserialize_json(data: dict) -> UpdateLaunchConfigurationTemplateRequest:
    out: UpdateLaunchConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("launchConfigurationTemplateID") is not None:
        out["launch_configuration_template_id"] = data["launchConfigurationTemplateID"]
    else:
        out["launch_configuration_template_id"] = ""
    if data.get("launchDisposition") is not None:
        out["launch_disposition"] = data["launchDisposition"]
    if data.get("targetInstanceTypeRightSizingMethod") is not None:
        out["target_instance_type_right_sizing_method"] = data[
            "targetInstanceTypeRightSizingMethod"
        ]
    if data.get("copyPrivateIp") is not None:
        out["copy_private_ip"] = data["copyPrivateIp"]
    if data.get("copyTags") is not None:
        out["copy_tags"] = data["copyTags"]
    if data.get("licensing") is not None:
        import capo_drs.types.licensing

        out["licensing"] = capo_drs.types.licensing.deserialize_json(data["licensing"])
    if data.get("exportBucketArn") is not None:
        out["export_bucket_arn"] = data["exportBucketArn"]
    if data.get("postLaunchEnabled") is not None:
        out["post_launch_enabled"] = data["postLaunchEnabled"]
    if data.get("launchIntoSourceInstance") is not None:
        out["launch_into_source_instance"] = data["launchIntoSourceInstance"]
    if data.get("recoveryMode") is not None:
        out["recovery_mode"] = data["recoveryMode"]
    return out
