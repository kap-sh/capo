"""Generated from Smithy shape ``com.amazonaws.ebs#GetSnapshotBlockRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ebs.types.block_index
    import capo_ebs.types.block_token
    import capo_ebs.types.snapshot_id


class GetSnapshotBlockRequest(TypedDict, closed=True):
    snapshot_id: "capo_ebs.types.snapshot_id.SnapshotId"
    """<p>The ID of the snapshot containing the block from which to get data.</p> <important> <p>If the specified snapshot is encrypted, you must have permission to use the KMS key that was used to encrypt the snapshot. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebsapis-using-encryption.html"> Using encryption</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p> </important>"""
    block_index: "capo_ebs.types.block_index.BlockIndex"
    """<p>The block index of the block in which to read the data. A block index is a logical index in units of <code>512</code> KiB blocks. To identify the block index, divide the logical offset of the data in the logical volume by the block size (logical offset of data/<code>524288</code>). The logical offset of the data must be <code>512</code> KiB aligned.</p>"""
    block_token: "capo_ebs.types.block_token.BlockToken"
    """<p>The block token of the block from which to get data. You can obtain the <code>BlockToken</code> by running the <code>ListChangedBlocks</code> or <code>ListSnapshotBlocks</code> operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSnapshotBlockRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSnapshotBlockRequest:
    out: GetSnapshotBlockRequest = {}  # type: ignore[typeddict-item]
    return out
