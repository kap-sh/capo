"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSnapshotsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.copy_tags_from_source
    import capo_ec2.types.instance_specification
    import capo_ec2.types.snapshot_location_enum
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateSnapshotsRequest(TypedDict, closed=True):
    description: NotRequired["capo_ec2.types.string.String"]
    """<p> A description propagated to every snapshot specified by the instance.</p>"""
    instance_specification: NotRequired[
        "capo_ec2.types.instance_specification.InstanceSpecification"
    ]
    """<p>The instance to specify which volumes should be included in the snapshots.</p>"""
    outpost_arn: NotRequired["capo_ec2.types.string.String"]
    """<note> <p>Only supported for instances on Outposts. If the source instance is not on an Outpost, omit this parameter.</p> </note> <ul> <li> <p>To create the snapshots on the same Outpost as the source instance, specify the ARN of that Outpost. The snapshots must be created on the same Outpost as the instance.</p> </li> <li> <p>To create the snapshots in the parent Region of the Outpost, omit this parameter.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html#create-snapshot"> Create local snapshots from volumes on an Outpost</a> in the <i>Amazon EBS User Guide</i>.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>Tags to apply to every snapshot specified by the instance.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    copy_tags_from_source: NotRequired[
        "capo_ec2.types.copy_tags_from_source.CopyTagsFromSource"
    ]
    """<p>Copies the tags from the specified volume to corresponding snapshot.</p>"""
    location: NotRequired["capo_ec2.types.snapshot_location_enum.SnapshotLocationEnum"]
    """<note> <p>Only supported for instances in Local Zones. If the source instance is not in a Local Zone, omit this parameter.</p> </note> <ul> <li> <p>To create local snapshots in the same Local Zone as the source instance, specify <code>local</code>.</p> </li> <li> <p>To create regional snapshots in the parent Region of the Local Zone, specify <code>regional</code> or omit this parameter.</p> </li> </ul> <p>Default value: <code>regional</code> </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateSnapshotsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "instance_specification" in value:
        import capo_ec2.types.instance_specification

        capo_ec2.types.instance_specification.serialize_ec2_query(
            value["instance_specification"], pairs, f"{key_prefix}InstanceSpecification"
        )
    if "outpost_arn" in value:
        pairs.append((f"{key_prefix}OutpostArn", str(value["outpost_arn"])))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "copy_tags_from_source" in value:
        import capo_ec2.types.copy_tags_from_source

        capo_ec2.types.copy_tags_from_source.serialize_ec2_query(
            value["copy_tags_from_source"], pairs, f"{key_prefix}CopyTagsFromSource"
        )
    if "location" in value:
        import capo_ec2.types.snapshot_location_enum

        capo_ec2.types.snapshot_location_enum.serialize_ec2_query(
            value["location"], pairs, f"{key_prefix}Location"
        )


def deserialize_ec2_query(el: Element) -> CreateSnapshotsRequest:
    out: CreateSnapshotsRequest = {}  # type: ignore[typeddict-item]
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_instance_specification = el.find("InstanceSpecification")
    if child_instance_specification is not None:
        import capo_ec2.types.instance_specification

        out["instance_specification"] = (
            capo_ec2.types.instance_specification.deserialize_ec2_query(
                child_instance_specification
            )
        )
    child_outpost_arn = el.find("OutpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_copy_tags_from_source = el.find("CopyTagsFromSource")
    if child_copy_tags_from_source is not None:
        import capo_ec2.types.copy_tags_from_source

        out["copy_tags_from_source"] = (
            capo_ec2.types.copy_tags_from_source.deserialize_ec2_query(
                child_copy_tags_from_source
            )
        )
    child_location = el.find("Location")
    if child_location is not None:
        import capo_ec2.types.snapshot_location_enum

        out["location"] = capo_ec2.types.snapshot_location_enum.deserialize_ec2_query(
            child_location
        )
    return out
