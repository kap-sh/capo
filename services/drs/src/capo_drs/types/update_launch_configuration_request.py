"""Generated from Smithy shape ``com.amazonaws.drs#UpdateLaunchConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.launch_disposition
    import capo_drs.types.launch_into_instance_properties
    import capo_drs.types.licensing
    import capo_drs.types.recovery_mode
    import capo_drs.types.small_bounded_string
    import capo_drs.types.source_server_id
    import capo_drs.types.target_instance_type_right_sizing_method


class UpdateLaunchConfigurationRequest(TypedDict, closed=True):
    source_server_id: "capo_drs.types.source_server_id.SourceServerID"
    """<p>The ID of the Source Server that we want to retrieve a Launch Configuration for.</p>"""
    name: NotRequired["capo_drs.types.small_bounded_string.SmallBoundedString"]
    """<p>The name of the launch configuration.</p>"""
    launch_disposition: NotRequired[
        "capo_drs.types.launch_disposition.LaunchDisposition"
    ]
    """<p>The state of the Recovery Instance in EC2 after the recovery operation.</p>"""
    target_instance_type_right_sizing_method: NotRequired[
        "capo_drs.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
    ]
    """<p>Whether Elastic Disaster Recovery should try to automatically choose the instance type that best matches the OS, CPU, and RAM of your Source Server.</p>"""
    copy_private_ip: NotRequired["bool"]
    """<p>Whether we should copy the Private IP of the Source Server to the Recovery Instance.</p>"""
    copy_tags: NotRequired["bool"]
    """<p>Whether we want to copy the tags of the Source Server to the EC2 machine of the Recovery Instance.</p>"""
    licensing: NotRequired["capo_drs.types.licensing.Licensing"]
    """<p>The licensing configuration to be used for this launch configuration.</p>"""
    post_launch_enabled: NotRequired["bool"]
    """<p>Whether we want to enable post-launch actions for the Source Server.</p>"""
    launch_into_instance_properties: NotRequired[
        "capo_drs.types.launch_into_instance_properties.LaunchIntoInstanceProperties"
    ]
    """<p>Launch into existing instance properties.</p>"""
    recovery_mode: NotRequired["capo_drs.types.recovery_mode.RecoveryMode"]
    """<p>Recovery mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLaunchConfigurationRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    if "name" in value:
        out["name"] = value["name"]
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
    if "post_launch_enabled" in value:
        out["postLaunchEnabled"] = value["post_launch_enabled"]
    if "launch_into_instance_properties" in value:
        import capo_drs.types.launch_into_instance_properties

        out["launchIntoInstanceProperties"] = (
            capo_drs.types.launch_into_instance_properties.serialize_json(
                value["launch_into_instance_properties"]
            )
        )
    if "recovery_mode" in value:
        out["recoveryMode"] = value["recovery_mode"]
    return out


def deserialize_json(data: dict) -> UpdateLaunchConfigurationRequest:
    out: UpdateLaunchConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceServerID") is not None:
        out["source_server_id"] = data["sourceServerID"]
    else:
        out["source_server_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
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
    if data.get("postLaunchEnabled") is not None:
        out["post_launch_enabled"] = data["postLaunchEnabled"]
    if data.get("launchIntoInstanceProperties") is not None:
        import capo_drs.types.launch_into_instance_properties

        out["launch_into_instance_properties"] = (
            capo_drs.types.launch_into_instance_properties.deserialize_json(
                data["launchIntoInstanceProperties"]
            )
        )
    if data.get("recoveryMode") is not None:
        out["recovery_mode"] = data["recoveryMode"]
    return out
