"""Generated from Smithy shape ``com.amazonaws.mgn#LaunchConfigurationTemplate``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.arn
    import capo_mgn.types.boot_mode
    import capo_mgn.types.ec2_launch_configuration_template_id
    import capo_mgn.types.launch_configuration_template_id
    import capo_mgn.types.launch_disposition
    import capo_mgn.types.launch_template_disk_conf
    import capo_mgn.types.licensing
    import capo_mgn.types.positive_integer
    import capo_mgn.types.post_launch_actions
    import capo_mgn.types.tag_value
    import capo_mgn.types.tags_map
    import capo_mgn.types.target_instance_type_right_sizing_method


class LaunchConfigurationTemplate(TypedDict, closed=True):
    launch_configuration_template_id: (
        "capo_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID"
    )
    """<p>ID of the Launch Configuration Template.</p>"""
    arn: NotRequired["capo_mgn.types.arn.ARN"]
    """<p>ARN of the Launch Configuration Template.</p>"""
    post_launch_actions: NotRequired[
        "capo_mgn.types.post_launch_actions.PostLaunchActions"
    ]
    """<p>Post Launch Actions of the Launch Configuration Template.</p>"""
    enable_map_auto_tagging: NotRequired["bool"]
    """<p>Enable map auto tagging.</p>"""
    map_auto_tagging_mpe_id: NotRequired["capo_mgn.types.tag_value.TagValue"]
    """<p>Launch configuration template map auto tagging MPE ID.</p>"""
    tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Tags of the Launch Configuration Template.</p>"""
    ec2_launch_template_id: NotRequired[
        "capo_mgn.types.ec2_launch_configuration_template_id.EC2LaunchConfigurationTemplateID"
    ]
    """<p>EC2 launch template ID.</p>"""
    launch_disposition: NotRequired[
        "capo_mgn.types.launch_disposition.LaunchDisposition"
    ]
    """<p>Launch disposition.</p>"""
    target_instance_type_right_sizing_method: NotRequired[
        "capo_mgn.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
    ]
    """<p>Target instance type right-sizing method.</p>"""
    copy_private_ip: NotRequired["bool"]
    """<p>Copy private Ip.</p>"""
    associate_public_ip_address: NotRequired["bool"]
    """<p>Associate public Ip address.</p>"""
    copy_tags: NotRequired["bool"]
    """<p>Copy tags.</p>"""
    licensing: NotRequired["capo_mgn.types.licensing.Licensing"]
    boot_mode: NotRequired["capo_mgn.types.boot_mode.BootMode"]
    """<p>Launch configuration template boot mode.</p>"""
    small_volume_max_size: "capo_mgn.types.positive_integer.PositiveInteger"
    """<p>Small volume maximum size.</p>"""
    small_volume_conf: NotRequired[
        "capo_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
    ]
    """<p>Small volume config.</p>"""
    large_volume_conf: NotRequired[
        "capo_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
    ]
    """<p>Large volume config.</p>"""
    enable_parameters_encryption: NotRequired["bool"]
    """<p>Enable parameters encryption.</p>"""
    parameters_encryption_key: NotRequired["capo_mgn.types.arn.ARN"]
    """<p>Parameters encryption key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LaunchConfigurationTemplate) -> dict:
    out: dict = {}
    out["launchConfigurationTemplateID"] = value["launch_configuration_template_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "post_launch_actions" in value:
        import capo_mgn.types.post_launch_actions

        out["postLaunchActions"] = capo_mgn.types.post_launch_actions.serialize_json(
            value["post_launch_actions"]
        )
    if "enable_map_auto_tagging" in value:
        out["enableMapAutoTagging"] = value["enable_map_auto_tagging"]
    if "map_auto_tagging_mpe_id" in value:
        out["mapAutoTaggingMpeID"] = value["map_auto_tagging_mpe_id"]
    if "tags" in value:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.serialize_json(value["tags"])
    if "ec2_launch_template_id" in value:
        out["ec2LaunchTemplateID"] = value["ec2_launch_template_id"]
    if "launch_disposition" in value:
        out["launchDisposition"] = value["launch_disposition"]
    if "target_instance_type_right_sizing_method" in value:
        out["targetInstanceTypeRightSizingMethod"] = value[
            "target_instance_type_right_sizing_method"
        ]
    if "copy_private_ip" in value:
        out["copyPrivateIp"] = value["copy_private_ip"]
    if "associate_public_ip_address" in value:
        out["associatePublicIpAddress"] = value["associate_public_ip_address"]
    if "copy_tags" in value:
        out["copyTags"] = value["copy_tags"]
    if "licensing" in value:
        import capo_mgn.types.licensing

        out["licensing"] = capo_mgn.types.licensing.serialize_json(value["licensing"])
    if "boot_mode" in value:
        out["bootMode"] = value["boot_mode"]
    out["smallVolumeMaxSize"] = value.get("small_volume_max_size", 0)
    if "small_volume_conf" in value:
        import capo_mgn.types.launch_template_disk_conf

        out["smallVolumeConf"] = (
            capo_mgn.types.launch_template_disk_conf.serialize_json(
                value["small_volume_conf"]
            )
        )
    if "large_volume_conf" in value:
        import capo_mgn.types.launch_template_disk_conf

        out["largeVolumeConf"] = (
            capo_mgn.types.launch_template_disk_conf.serialize_json(
                value["large_volume_conf"]
            )
        )
    if "enable_parameters_encryption" in value:
        out["enableParametersEncryption"] = value["enable_parameters_encryption"]
    if "parameters_encryption_key" in value:
        out["parametersEncryptionKey"] = value["parameters_encryption_key"]
    return out


def deserialize_json(data: dict) -> LaunchConfigurationTemplate:
    out: LaunchConfigurationTemplate = {}  # type: ignore[typeddict-item]
    if data.get("launchConfigurationTemplateID") is not None:
        out["launch_configuration_template_id"] = data["launchConfigurationTemplateID"]
    else:
        out["launch_configuration_template_id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("postLaunchActions") is not None:
        import capo_mgn.types.post_launch_actions

        out["post_launch_actions"] = (
            capo_mgn.types.post_launch_actions.deserialize_json(
                data["postLaunchActions"]
            )
        )
    if data.get("enableMapAutoTagging") is not None:
        out["enable_map_auto_tagging"] = data["enableMapAutoTagging"]
    if data.get("mapAutoTaggingMpeID") is not None:
        out["map_auto_tagging_mpe_id"] = data["mapAutoTaggingMpeID"]
    if data.get("tags") is not None:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.deserialize_json(data["tags"])
    if data.get("ec2LaunchTemplateID") is not None:
        out["ec2_launch_template_id"] = data["ec2LaunchTemplateID"]
    if data.get("launchDisposition") is not None:
        out["launch_disposition"] = data["launchDisposition"]
    if data.get("targetInstanceTypeRightSizingMethod") is not None:
        out["target_instance_type_right_sizing_method"] = data[
            "targetInstanceTypeRightSizingMethod"
        ]
    if data.get("copyPrivateIp") is not None:
        out["copy_private_ip"] = data["copyPrivateIp"]
    if data.get("associatePublicIpAddress") is not None:
        out["associate_public_ip_address"] = data["associatePublicIpAddress"]
    if data.get("copyTags") is not None:
        out["copy_tags"] = data["copyTags"]
    if data.get("licensing") is not None:
        import capo_mgn.types.licensing

        out["licensing"] = capo_mgn.types.licensing.deserialize_json(data["licensing"])
    if data.get("bootMode") is not None:
        out["boot_mode"] = data["bootMode"]
    if data.get("smallVolumeMaxSize") is not None:
        out["small_volume_max_size"] = data["smallVolumeMaxSize"]
    else:
        out["small_volume_max_size"] = 0
    if data.get("smallVolumeConf") is not None:
        import capo_mgn.types.launch_template_disk_conf

        out["small_volume_conf"] = (
            capo_mgn.types.launch_template_disk_conf.deserialize_json(
                data["smallVolumeConf"]
            )
        )
    if data.get("largeVolumeConf") is not None:
        import capo_mgn.types.launch_template_disk_conf

        out["large_volume_conf"] = (
            capo_mgn.types.launch_template_disk_conf.deserialize_json(
                data["largeVolumeConf"]
            )
        )
    if data.get("enableParametersEncryption") is not None:
        out["enable_parameters_encryption"] = data["enableParametersEncryption"]
    if data.get("parametersEncryptionKey") is not None:
        out["parameters_encryption_key"] = data["parametersEncryptionKey"]
    return out


def redact_sensitive(value: LaunchConfigurationTemplate) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
