"""Generated from Smithy shape ``com.amazonaws.ec2#CopySnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.copy_snapshot_request_psu
    import capo_ec2.types.kms_key_id
    import capo_ec2.types.snapshot_completion_duration_minutes_request
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CopySnapshotRequest(TypedDict, closed=True):
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the EBS snapshot.</p>"""
    destination_outpost_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Outpost to which to copy the snapshot.</p> <note> <p>Only supported when copying a snapshot to an Outpost.</p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html#copy-snapshots"> Copy snapshots from an Amazon Web Services Region to an Outpost</a> in the <i>Amazon EBS User Guide</i>.</p>"""
    destination_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The destination Region to use in the <code>PresignedUrl</code> parameter of a snapshot copy operation. This parameter is only valid for specifying the destination Region in a <code>PresignedUrl</code> parameter, where it is required.</p> <p>The snapshot copy is sent to the regional endpoint that you sent the HTTP request to (for example, <code>ec2.us-east-1.amazonaws.com</code>). With the CLI, this is specified using the <code>--region</code> parameter or the default Region in your Amazon Web Services configuration file.</p>"""
    encrypted: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>To encrypt a copy of an unencrypted snapshot if encryption by default is not enabled, enable encryption using this parameter. Otherwise, omit this parameter. Copies of encrypted snapshots are encrypted, even if you omit this parameter and encryption by default is not enabled. You cannot set this parameter to false. For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html">Amazon EBS encryption</a> in the <i>Amazon EBS User Guide</i>.</p>"""
    kms_key_id: NotRequired["capo_ec2.types.kms_key_id.KmsKeyId"]
    """<p>The identifier of the KMS key to use for Amazon EBS encryption. If this parameter is not specified, your KMS key for Amazon EBS is used. If <code>KmsKeyId</code> is specified, the encrypted state must be <code>true</code>.</p> <p>You can specify the KMS key using any of the following:</p> <ul> <li> <p>Key ID. For example, 1234abcd-12ab-34cd-56ef-1234567890ab.</p> </li> <li> <p>Key alias. For example, alias/ExampleAlias.</p> </li> <li> <p>Key ARN. For example, arn:aws:kms:us-east-1:012345678910:key/1234abcd-12ab-34cd-56ef-1234567890ab.</p> </li> <li> <p>Alias ARN. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias.</p> </li> </ul> <p>Amazon Web Services authenticates the KMS key asynchronously. Therefore, if you specify an ID, alias, or ARN that is not valid, the action can appear to complete, but eventually fails.</p>"""
    presigned_url: NotRequired[
        "capo_ec2.types.copy_snapshot_request_psu.CopySnapshotRequestPSU"
    ]
    """<p>When you copy an encrypted source snapshot using the Amazon EC2 Query API, you must supply a pre-signed URL. This parameter is optional for unencrypted snapshots. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html">Query requests</a>.</p> <p>The <code>PresignedUrl</code> should use the snapshot source endpoint, the <code>CopySnapshot</code> action, and include the <code>SourceRegion</code>, <code>SourceSnapshotId</code>, and <code>DestinationRegion</code> parameters. The <code>PresignedUrl</code> must be signed using Amazon Web Services Signature Version 4. Because EBS snapshots are stored in Amazon S3, the signing algorithm for this parameter uses the same logic that is described in <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html"> Authenticating Requests: Using Query Parameters (Amazon Web Services Signature Version 4)</a> in the <i>Amazon S3 API Reference</i>. An invalid or improperly signed <code>PresignedUrl</code> will cause the copy operation to fail asynchronously, and the snapshot will move to an <code>error</code> state.</p>"""
    source_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Region that contains the snapshot to be copied.</p>"""
    source_snapshot_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the EBS snapshot to copy.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the new snapshot.</p>"""
    completion_duration_minutes: NotRequired[
        "capo_ec2.types.snapshot_completion_duration_minutes_request.SnapshotCompletionDurationMinutesRequest"
    ]
    """<note> <p>Not supported when copying snapshots to or from Local Zones or Outposts.</p> </note> <p>Specify a completion duration, in 15 minute increments, to initiate a time-based snapshot copy. Time-based snapshot copy operations complete within the specified duration. For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/time-based-copies.html"> Time-based copies</a>.</p> <p>If you do not specify a value, the snapshot copy operation is completed on a best-effort basis.</p>"""
    destination_availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Local Zone, for example, <code>cn-north-1-pkx-1a</code> to which to copy the snapshot.</p> <note> <p>Only supported when copying a snapshot to a Local Zone.</p> </note>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CopySnapshotRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "destination_outpost_arn" in value:
        pairs.append(
            (
                f"{key_prefix}DestinationOutpostArn",
                str(value["destination_outpost_arn"]),
            )
        )
    if "destination_region" in value:
        pairs.append(
            (f"{key_prefix}DestinationRegion", str(value["destination_region"]))
        )
    if "encrypted" in value:
        pairs.append(
            (f"{key_prefix}Encrypted", "true" if value["encrypted"] else "false")
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "presigned_url" in value:
        pairs.append((f"{key_prefix}PresignedUrl", str(value["presigned_url"])))
    if "source_region" in value:
        pairs.append((f"{key_prefix}SourceRegion", str(value["source_region"])))
    if "source_snapshot_id" in value:
        pairs.append(
            (f"{key_prefix}SourceSnapshotId", str(value["source_snapshot_id"]))
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "completion_duration_minutes" in value:
        pairs.append(
            (
                f"{key_prefix}CompletionDurationMinutes",
                str(value["completion_duration_minutes"]),
            )
        )
    if "destination_availability_zone" in value:
        pairs.append(
            (
                f"{key_prefix}DestinationAvailabilityZone",
                str(value["destination_availability_zone"]),
            )
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CopySnapshotRequest:
    out: CopySnapshotRequest = {}  # type: ignore[typeddict-item]
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_destination_outpost_arn = el.find("DestinationOutpostArn")
    if child_destination_outpost_arn is not None:
        out["destination_outpost_arn"] = str(child_destination_outpost_arn.text or "")
    child_destination_region = el.find("destinationRegion")
    if child_destination_region is not None:
        out["destination_region"] = str(child_destination_region.text or "")
    child_encrypted = el.find("encrypted")
    if child_encrypted is not None:
        out["encrypted"] = (child_encrypted.text or "").lower() == "true"
    child_kms_key_id = el.find("kmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_presigned_url = el.find("presignedUrl")
    if child_presigned_url is not None:
        out["presigned_url"] = str(child_presigned_url.text or "")
    child_source_region = el.find("SourceRegion")
    if child_source_region is not None:
        out["source_region"] = str(child_source_region.text or "")
    child_source_snapshot_id = el.find("SourceSnapshotId")
    if child_source_snapshot_id is not None:
        out["source_snapshot_id"] = str(child_source_snapshot_id.text or "")
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_completion_duration_minutes = el.find("CompletionDurationMinutes")
    if child_completion_duration_minutes is not None:
        out["completion_duration_minutes"] = int(
            child_completion_duration_minutes.text or ""
        )
    child_destination_availability_zone = el.find("DestinationAvailabilityZone")
    if child_destination_availability_zone is not None:
        out["destination_availability_zone"] = str(
            child_destination_availability_zone.text or ""
        )
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
