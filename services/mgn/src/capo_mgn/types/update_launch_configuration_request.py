"""Generated from Smithy shape ``com.amazonaws.mgn#UpdateLaunchConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.boot_mode
    import capo_mgn.types.launch_disposition
    import capo_mgn.types.licensing
    import capo_mgn.types.post_launch_actions
    import capo_mgn.types.small_bounded_string
    import capo_mgn.types.source_server_id
    import capo_mgn.types.tag_value
    import capo_mgn.types.target_instance_type_right_sizing_method


class UpdateLaunchConfigurationRequest(TypedDict, closed=True):
    source_server_id: "capo_mgn.types.source_server_id.SourceServerID"
    """<p>Update Launch configuration by Source Server ID request.</p>"""
    name: NotRequired["capo_mgn.types.small_bounded_string.SmallBoundedString"]
    """<p>Update Launch configuration name request.</p>"""
    launch_disposition: NotRequired[
        "capo_mgn.types.launch_disposition.LaunchDisposition"
    ]
    """<p>Update Launch configuration launch disposition request.</p>"""
    target_instance_type_right_sizing_method: NotRequired[
        "capo_mgn.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
    ]
    """<p>Update Launch configuration Target instance right sizing request.</p>"""
    copy_private_ip: NotRequired["bool"]
    """<p>Update Launch configuration copy Private IP request.</p>"""
    copy_tags: NotRequired["bool"]
    """<p>Update Launch configuration copy Tags request.</p>"""
    licensing: NotRequired["capo_mgn.types.licensing.Licensing"]
    """<p>Update Launch configuration licensing request.</p>"""
    boot_mode: NotRequired["capo_mgn.types.boot_mode.BootMode"]
    """<p>Update Launch configuration boot mode request.</p>"""
    post_launch_actions: NotRequired[
        "capo_mgn.types.post_launch_actions.PostLaunchActions"
    ]
    enable_map_auto_tagging: NotRequired["bool"]
    """<p>Enable map auto tagging.</p>"""
    map_auto_tagging_mpe_id: NotRequired["capo_mgn.types.tag_value.TagValue"]
    """<p>Launch configuration map auto tagging MPE ID.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Update Launch configuration Account ID.</p>"""


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
    if "account_id" in value:
        out["accountID"] = value["account_id"]
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
    if data.get("accountID") is not None:
        out["account_id"] = data["accountID"]
    return out
