"""Generated from Smithy shape ``com.amazonaws.ec2#CopyImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.copy_image_client_token
    import capo_ec2.types.image_description_request
    import capo_ec2.types.image_name_request
    import capo_ec2.types.kms_key_id
    import capo_ec2.types.long
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CopyImageRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_ec2.types.copy_image_client_token.CopyImageClientToken"
    ]
    """<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency in Amazon EC2 API requests</a> in the <i>Amazon EC2 API Reference</i>.</p>"""
    description: NotRequired[
        "capo_ec2.types.image_description_request.ImageDescriptionRequest"
    ]
    """<p>A description for the new AMI.</p>"""
    encrypted: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specifies whether to encrypt the snapshots of the copied image.</p> <p>You can encrypt a copy of an unencrypted snapshot, but you cannot create an unencrypted copy of an encrypted snapshot. The default KMS key for Amazon EBS is used unless you specify a non-default Key Management Service (KMS) KMS key using <code>KmsKeyId</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html">Use encryption with EBS-backed AMIs</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    kms_key_id: NotRequired["capo_ec2.types.kms_key_id.KmsKeyId"]
    """<p>The identifier of the symmetric Key Management Service (KMS) KMS key to use when creating encrypted volumes. If this parameter is not specified, your Amazon Web Services managed KMS key for Amazon EBS is used. If you specify a KMS key, you must also set the encrypted state to <code>true</code>.</p> <p>You can specify a KMS key using any of the following:</p> <ul> <li> <p>Key ID. For example, 1234abcd-12ab-34cd-56ef-1234567890ab.</p> </li> <li> <p>Key alias. For example, alias/ExampleAlias.</p> </li> <li> <p>Key ARN. For example, arn:aws:kms:us-east-1:012345678910:key/1234abcd-12ab-34cd-56ef-1234567890ab.</p> </li> <li> <p>Alias ARN. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias.</p> </li> </ul> <p>Amazon Web Services authenticates the KMS key asynchronously. Therefore, if you specify an identifier that is not valid, the action can appear to complete, but eventually fails.</p> <p>The specified KMS key must exist in the destination Region.</p> <p>Amazon EBS does not support asymmetric KMS keys.</p>"""
    name: NotRequired["capo_ec2.types.image_name_request.ImageNameRequest"]
    """<p>The name of the new AMI.</p>"""
    source_image_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the AMI to copy.</p>"""
    source_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the Region that contains the AMI to copy.</p>"""
    destination_outpost_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Outpost for the new AMI.</p> <p>Only specify this parameter when copying an AMI from an Amazon Web Services Region to an Outpost. The AMI must be in the Region of the destination Outpost. You can't copy an AMI from an Outpost to a Region, from one Outpost to another, or within the same Outpost.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html#copy-amis">Copy AMIs from an Amazon Web Services Region to an Outpost</a> in the <i>Amazon EBS User Guide</i>.</p> <p>Only one of <code>DestinationAvailabilityZone</code>, <code>DestinationAvailabilityZoneId</code>, or <code>DestinationOutpostArn</code> can be specified.</p>"""
    copy_image_tags: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specifies whether to copy your user-defined AMI tags to the new AMI.</p> <p>The following tags are not be copied:</p> <ul> <li> <p>System tags (prefixed with <code>aws:</code>)</p> </li> <li> <p>For public and shared AMIs, user-defined tags that are attached by other Amazon Web Services accounts</p> </li> </ul> <p>Default: Your user-defined AMI tags are not copied.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the new AMI and new snapshots. You can tag the AMI, the snapshots, or both.</p> <ul> <li> <p>To tag the new AMI, the value for <code>ResourceType</code> must be <code>image</code>.</p> </li> <li> <p>To tag the new snapshots, the value for <code>ResourceType</code> must be <code>snapshot</code>. The same tag is applied to all the new snapshots.</p> </li> </ul> <p>If you specify other values for <code>ResourceType</code>, the request fails.</p> <p>To tag an AMI or snapshot after it has been created, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html">CreateTags</a>.</p>"""
    snapshot_copy_completion_duration_minutes: NotRequired["capo_ec2.types.long.Long"]
    """<p>Specify a completion duration, in 15 minute increments, to initiate a time-based AMI copy. The specified completion duration applies to each of the snapshots associated with the AMI. Each snapshot associated with the AMI will be completed within the specified completion duration, with copy throughput automatically adjusted for each snapshot based on its size to meet the timing target.</p> <p>If you do not specify a value, the AMI copy operation is completed on a best-effort basis.</p> <note> <p>This parameter is not supported when copying an AMI to or from a Local Zone, or to an Outpost.</p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/time-based-copies.html">Time-based copies for Amazon EBS snapshots and EBS-backed AMIs</a>.</p>"""
    destination_availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Local Zone for the new AMI (for example, <code>cn-north-1-pkx-1a</code>).</p> <p>Only one of <code>DestinationAvailabilityZone</code>, <code>DestinationAvailabilityZoneId</code>, or <code>DestinationOutpostArn</code> can be specified.</p>"""
    destination_availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Local Zone for the new AMI (for example, <code>cnn1-pkx1-az1</code>).</p> <p>Only one of <code>DestinationAvailabilityZone</code>, <code>DestinationAvailabilityZoneId</code>, or <code>DestinationOutpostArn</code> can be specified.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CopyImageRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "encrypted" in value:
        pairs.append(
            (f"{key_prefix}Encrypted", "true" if value["encrypted"] else "false")
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "source_image_id" in value:
        pairs.append((f"{key_prefix}SourceImageId", str(value["source_image_id"])))
    if "source_region" in value:
        pairs.append((f"{key_prefix}SourceRegion", str(value["source_region"])))
    if "destination_outpost_arn" in value:
        pairs.append(
            (
                f"{key_prefix}DestinationOutpostArn",
                str(value["destination_outpost_arn"]),
            )
        )
    if "copy_image_tags" in value:
        pairs.append(
            (
                f"{key_prefix}CopyImageTags",
                "true" if value["copy_image_tags"] else "false",
            )
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "snapshot_copy_completion_duration_minutes" in value:
        pairs.append(
            (
                f"{key_prefix}SnapshotCopyCompletionDurationMinutes",
                str(value["snapshot_copy_completion_duration_minutes"]),
            )
        )
    if "destination_availability_zone" in value:
        pairs.append(
            (
                f"{key_prefix}DestinationAvailabilityZone",
                str(value["destination_availability_zone"]),
            )
        )
    if "destination_availability_zone_id" in value:
        pairs.append(
            (
                f"{key_prefix}DestinationAvailabilityZoneId",
                str(value["destination_availability_zone_id"]),
            )
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CopyImageRequest:
    out: CopyImageRequest = {}  # type: ignore[typeddict-item]
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_encrypted = el.find("encrypted")
    if child_encrypted is not None:
        out["encrypted"] = (child_encrypted.text or "").lower() == "true"
    child_kms_key_id = el.find("kmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_source_image_id = el.find("SourceImageId")
    if child_source_image_id is not None:
        out["source_image_id"] = str(child_source_image_id.text or "")
    child_source_region = el.find("SourceRegion")
    if child_source_region is not None:
        out["source_region"] = str(child_source_region.text or "")
    child_destination_outpost_arn = el.find("DestinationOutpostArn")
    if child_destination_outpost_arn is not None:
        out["destination_outpost_arn"] = str(child_destination_outpost_arn.text or "")
    child_copy_image_tags = el.find("CopyImageTags")
    if child_copy_image_tags is not None:
        out["copy_image_tags"] = (child_copy_image_tags.text or "").lower() == "true"
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_snapshot_copy_completion_duration_minutes = el.find(
        "SnapshotCopyCompletionDurationMinutes"
    )
    if child_snapshot_copy_completion_duration_minutes is not None:
        out["snapshot_copy_completion_duration_minutes"] = int(
            child_snapshot_copy_completion_duration_minutes.text or ""
        )
    child_destination_availability_zone = el.find("DestinationAvailabilityZone")
    if child_destination_availability_zone is not None:
        out["destination_availability_zone"] = str(
            child_destination_availability_zone.text or ""
        )
    child_destination_availability_zone_id = el.find("DestinationAvailabilityZoneId")
    if child_destination_availability_zone_id is not None:
        out["destination_availability_zone_id"] = str(
            child_destination_availability_zone_id.text or ""
        )
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
