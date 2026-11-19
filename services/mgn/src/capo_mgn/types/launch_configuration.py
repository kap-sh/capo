"""Generated from Smithy shape ``com.amazonaws.mgn#LaunchConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.boot_mode
    import capo_mgn.types.bounded_string
    import capo_mgn.types.launch_disposition
    import capo_mgn.types.licensing
    import capo_mgn.types.post_launch_actions
    import capo_mgn.types.small_bounded_string
    import capo_mgn.types.source_server_id
    import capo_mgn.types.tag_key
    import capo_mgn.types.tag_value
    import capo_mgn.types.target_instance_type_right_sizing_method


class LaunchConfiguration(TypedDict, closed=True):
    source_server_id: NotRequired["capo_mgn.types.source_server_id.SourceServerID"]
    """<p>Launch configuration Source Server ID.</p>"""
    name: NotRequired["capo_mgn.types.small_bounded_string.SmallBoundedString"]
    """<p>Launch configuration name.</p>"""
    ec2_launch_template_id: NotRequired["capo_mgn.types.bounded_string.BoundedString"]
    """<p>Launch configuration EC2 Launch template ID.</p>"""
    launch_disposition: NotRequired[
        "capo_mgn.types.launch_disposition.LaunchDisposition"
    ]
    """<p>Launch disposition for launch configuration.</p>"""
    target_instance_type_right_sizing_method: NotRequired[
        "capo_mgn.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
    ]
    """<p>Launch configuration Target instance type right sizing method.</p>"""
    copy_private_ip: NotRequired["bool"]
    """<p>Copy Private IP during Launch Configuration.</p>"""
    copy_tags: NotRequired["bool"]
    """<p>Copy Tags during Launch Configuration.</p>"""
    licensing: NotRequired["capo_mgn.types.licensing.Licensing"]
    """<p>Launch configuration OS licensing.</p>"""
    boot_mode: NotRequired["capo_mgn.types.boot_mode.BootMode"]
    """<p>Launch configuration boot mode.</p>"""
    post_launch_actions: NotRequired[
        "capo_mgn.types.post_launch_actions.PostLaunchActions"
    ]
    enable_map_auto_tagging: NotRequired["bool"]
    """<p>Enable map auto tagging.</p>"""
    map_auto_tagging_mpe_id: NotRequired["capo_mgn.types.tag_value.TagValue"]
    """<p>Map auto tagging MPE ID.</p>"""
    map_auto_tagging_key: NotRequired["capo_mgn.types.tag_key.TagKey"]
    """<p>Map auto tagging key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LaunchConfiguration) -> dict:
    out: dict = {}
    if "source_server_id" in value:
        out["sourceServerID"] = value["source_server_id"]
    if "name" in value:
        out["name"] = value["name"]
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
    if "copy_tags" in value:
        out["copyTags"] = value["copy_tags"]
    if "licensing" in value:
        import capo_mgn.types.licensing

        out["licensing"] = capo_mgn.types.licensing.serialize_json(value["licensing"])
    if "boot_mode" in value:
        out["bootMode"] = value["boot_mode"]
    if "post_launch_actions" in value:
        import capo_mgn.types.post_launch_actions

        out["postLaunchActions"] = capo_mgn.types.post_launch_actions.serialize_json(
            value["post_launch_actions"]
        )
    if "enable_map_auto_tagging" in value:
        out["enableMapAutoTagging"] = value["enable_map_auto_tagging"]
    if "map_auto_tagging_mpe_id" in value:
        out["mapAutoTaggingMpeID"] = value["map_auto_tagging_mpe_id"]
    if "map_auto_tagging_key" in value:
        out["mapAutoTaggingKey"] = value["map_auto_tagging_key"]
    return out


def deserialize_json(data: dict) -> LaunchConfiguration:
    out: LaunchConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("sourceServerID") is not None:
        out["source_server_id"] = data["sourceServerID"]
    if data.get("name") is not None:
        out["name"] = data["name"]
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
    if data.get("copyTags") is not None:
        out["copy_tags"] = data["copyTags"]
    if data.get("licensing") is not None:
        import capo_mgn.types.licensing

        out["licensing"] = capo_mgn.types.licensing.deserialize_json(data["licensing"])
    if data.get("bootMode") is not None:
        out["boot_mode"] = data["bootMode"]
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
    if data.get("mapAutoTaggingKey") is not None:
        out["map_auto_tagging_key"] = data["mapAutoTaggingKey"]
    return out
