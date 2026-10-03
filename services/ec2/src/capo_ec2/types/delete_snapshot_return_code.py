"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteSnapshotReturnCode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.snapshot_id
    import capo_ec2.types.snapshot_return_codes


class DeleteSnapshotReturnCode(TypedDict, closed=True):
    snapshot_id: NotRequired["capo_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot.</p>"""
    return_code: NotRequired["capo_ec2.types.snapshot_return_codes.SnapshotReturnCodes"]
    """<p>The result code from the snapshot deletion attempt. Possible values:</p> <ul> <li> <p> <code>success</code> - The snapshot was successfully deleted.</p> </li> <li> <p> <code>skipped</code> - The snapshot was not deleted because it's associated with other AMIs.</p> </li> <li> <p> <code>missing-permissions</code> - The snapshot was not deleted because the role lacks <code>DeleteSnapshot</code> permissions. For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/security_iam_service-with-iam.html">How Amazon EBS works with IAM</a>.</p> </li> <li> <p> <code>internal-error</code> - The snapshot was not deleted due to a server error.</p> </li> <li> <p> <code>client-error</code> - The snapshot was not deleted due to a client configuration error.</p> </li> </ul> <p>For details about an error, check the <code>DeleteSnapshot</code> event in the CloudTrail event history. For more information, see <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/tutorial-event-history.html">View event history</a> in the <i>Amazon Web Services CloudTrail User Guide</i>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteSnapshotReturnCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "snapshot_id" in value:
        pairs.append((f"{key_prefix}SnapshotId", str(value["snapshot_id"])))
    if "return_code" in value:
        import capo_ec2.types.snapshot_return_codes

        capo_ec2.types.snapshot_return_codes.serialize_ec2_query(
            value["return_code"], pairs, f"{key_prefix}ReturnCode"
        )


def deserialize_ec2_query(el: Element) -> DeleteSnapshotReturnCode:
    out: DeleteSnapshotReturnCode = {}  # type: ignore[typeddict-item]
    child_snapshot_id = el.find("snapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_return_code = el.find("returnCode")
    if child_return_code is not None:
        import capo_ec2.types.snapshot_return_codes

        out["return_code"] = capo_ec2.types.snapshot_return_codes.deserialize_ec2_query(
            child_return_code
        )
    return out
