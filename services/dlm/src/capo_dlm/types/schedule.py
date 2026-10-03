"""Generated from Smithy shape ``com.amazonaws.dlm#Schedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dlm.types.archive_rule
    import capo_dlm.types.copy_tags
    import capo_dlm.types.create_rule
    import capo_dlm.types.cross_region_copy_rules
    import capo_dlm.types.deprecate_rule
    import capo_dlm.types.fast_restore_rule
    import capo_dlm.types.retain_rule
    import capo_dlm.types.schedule_name
    import capo_dlm.types.share_rules
    import capo_dlm.types.tags_to_add_list
    import capo_dlm.types.variable_tags_list


class Schedule(TypedDict, closed=True):
    name: NotRequired["capo_dlm.types.schedule_name.ScheduleName"]
    """<p>The name of the schedule.</p>"""
    copy_tags: NotRequired["capo_dlm.types.copy_tags.CopyTags"]
    """<p>Copy all user-defined tags on a source volume to snapshots of the volume created by this policy.</p>"""
    tags_to_add: NotRequired["capo_dlm.types.tags_to_add_list.TagsToAddList"]
    """<p>The tags to apply to policy-created resources. These user-defined tags are in addition to the Amazon Web Services-added lifecycle tags.</p>"""
    variable_tags: NotRequired["capo_dlm.types.variable_tags_list.VariableTagsList"]
    """<p> <b>[AMI policies and snapshot policies that target instances only]</b> A collection of key/value pairs with values determined dynamically when the policy is executed. Keys may be any valid Amazon EC2 tag key. Values must be in one of the two following formats: <code>$(instance-id)</code> or <code>$(timestamp)</code>. Variable tags are only valid for EBS Snapshot Management – Instance policies.</p>"""
    create_rule: NotRequired["capo_dlm.types.create_rule.CreateRule"]
    """<p>The creation rule.</p>"""
    retain_rule: NotRequired["capo_dlm.types.retain_rule.RetainRule"]
    """<p>The retention rule for snapshots or AMIs created by the policy.</p>"""
    fast_restore_rule: NotRequired["capo_dlm.types.fast_restore_rule.FastRestoreRule"]
    """<p> <b>[Custom snapshot policies only]</b> The rule for enabling fast snapshot restore.</p>"""
    cross_region_copy_rules: NotRequired[
        "capo_dlm.types.cross_region_copy_rules.CrossRegionCopyRules"
    ]
    """<p>Specifies a rule for copying snapshots or AMIs across Regions.</p> <note> <p>You can't specify cross-Region copy rules for policies that create snapshots on an Outpost or in a Local Zone. If the policy creates snapshots in a Region, then snapshots can be copied to up to three Regions or Outposts.</p> </note>"""
    share_rules: NotRequired["capo_dlm.types.share_rules.ShareRules"]
    """<p> <b>[Custom snapshot policies only]</b> The rule for sharing snapshots with other Amazon Web Services accounts.</p>"""
    deprecate_rule: NotRequired["capo_dlm.types.deprecate_rule.DeprecateRule"]
    """<p> <b>[Custom AMI policies only]</b> The AMI deprecation rule for the schedule.</p>"""
    archive_rule: NotRequired["capo_dlm.types.archive_rule.ArchiveRule"]
    """<p> <b>[Custom snapshot policies that target volumes only]</b> The snapshot archiving rule for the schedule. When you specify an archiving rule, snapshots are automatically moved from the standard tier to the archive tier once the schedule's retention threshold is met. Snapshots are then retained in the archive tier for the archive retention period that you specify. </p> <p>For more information about using snapshot archiving, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-ami-policy.html#dlm-archive">Considerations for snapshot lifecycle policies</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Schedule) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "copy_tags" in value:
        out["CopyTags"] = value["copy_tags"]
    if "tags_to_add" in value:
        import capo_dlm.types.tags_to_add_list

        out["TagsToAdd"] = capo_dlm.types.tags_to_add_list.serialize_json(
            value["tags_to_add"]
        )
    if "variable_tags" in value:
        import capo_dlm.types.variable_tags_list

        out["VariableTags"] = capo_dlm.types.variable_tags_list.serialize_json(
            value["variable_tags"]
        )
    if "create_rule" in value:
        import capo_dlm.types.create_rule

        out["CreateRule"] = capo_dlm.types.create_rule.serialize_json(
            value["create_rule"]
        )
    if "retain_rule" in value:
        import capo_dlm.types.retain_rule

        out["RetainRule"] = capo_dlm.types.retain_rule.serialize_json(
            value["retain_rule"]
        )
    if "fast_restore_rule" in value:
        import capo_dlm.types.fast_restore_rule

        out["FastRestoreRule"] = capo_dlm.types.fast_restore_rule.serialize_json(
            value["fast_restore_rule"]
        )
    if "cross_region_copy_rules" in value:
        import capo_dlm.types.cross_region_copy_rules

        out["CrossRegionCopyRules"] = (
            capo_dlm.types.cross_region_copy_rules.serialize_json(
                value["cross_region_copy_rules"]
            )
        )
    if "share_rules" in value:
        import capo_dlm.types.share_rules

        out["ShareRules"] = capo_dlm.types.share_rules.serialize_json(
            value["share_rules"]
        )
    if "deprecate_rule" in value:
        import capo_dlm.types.deprecate_rule

        out["DeprecateRule"] = capo_dlm.types.deprecate_rule.serialize_json(
            value["deprecate_rule"]
        )
    if "archive_rule" in value:
        import capo_dlm.types.archive_rule

        out["ArchiveRule"] = capo_dlm.types.archive_rule.serialize_json(
            value["archive_rule"]
        )
    return out


def deserialize_json(data: dict) -> Schedule:
    out: Schedule = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("CopyTags") is not None:
        out["copy_tags"] = data["CopyTags"]
    if data.get("TagsToAdd") is not None:
        import capo_dlm.types.tags_to_add_list

        out["tags_to_add"] = capo_dlm.types.tags_to_add_list.deserialize_json(
            data["TagsToAdd"]
        )
    if data.get("VariableTags") is not None:
        import capo_dlm.types.variable_tags_list

        out["variable_tags"] = capo_dlm.types.variable_tags_list.deserialize_json(
            data["VariableTags"]
        )
    if data.get("CreateRule") is not None:
        import capo_dlm.types.create_rule

        out["create_rule"] = capo_dlm.types.create_rule.deserialize_json(
            data["CreateRule"]
        )
    if data.get("RetainRule") is not None:
        import capo_dlm.types.retain_rule

        out["retain_rule"] = capo_dlm.types.retain_rule.deserialize_json(
            data["RetainRule"]
        )
    if data.get("FastRestoreRule") is not None:
        import capo_dlm.types.fast_restore_rule

        out["fast_restore_rule"] = capo_dlm.types.fast_restore_rule.deserialize_json(
            data["FastRestoreRule"]
        )
    if data.get("CrossRegionCopyRules") is not None:
        import capo_dlm.types.cross_region_copy_rules

        out["cross_region_copy_rules"] = (
            capo_dlm.types.cross_region_copy_rules.deserialize_json(
                data["CrossRegionCopyRules"]
            )
        )
    if data.get("ShareRules") is not None:
        import capo_dlm.types.share_rules

        out["share_rules"] = capo_dlm.types.share_rules.deserialize_json(
            data["ShareRules"]
        )
    if data.get("DeprecateRule") is not None:
        import capo_dlm.types.deprecate_rule

        out["deprecate_rule"] = capo_dlm.types.deprecate_rule.deserialize_json(
            data["DeprecateRule"]
        )
    if data.get("ArchiveRule") is not None:
        import capo_dlm.types.archive_rule

        out["archive_rule"] = capo_dlm.types.archive_rule.deserialize_json(
            data["ArchiveRule"]
        )
    return out
