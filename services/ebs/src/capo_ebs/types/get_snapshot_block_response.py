"""Generated from Smithy shape ``com.amazonaws.ebs#GetSnapshotBlockResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ebs.types.block_data
    import capo_ebs.types.checksum
    import capo_ebs.types.checksum_algorithm
    import capo_ebs.types.data_length


class GetSnapshotBlockResponse(TypedDict, closed=True):
    data_length: NotRequired["capo_ebs.types.data_length.DataLength"]
    """<p>The size of the data in the block.</p>"""
    block_data: "capo_ebs.types.block_data.BlockData"
    """<p>The data content of the block.</p>"""
    checksum: NotRequired["capo_ebs.types.checksum.Checksum"]
    """<p>The checksum generated for the block, which is Base64 encoded.</p>"""
    checksum_algorithm: NotRequired[
        "capo_ebs.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p>The algorithm used to generate the checksum for the block, such as SHA256.</p>"""


def redact_sensitive(value: GetSnapshotBlockResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "block_data" in value:
        out["block_data"] = "*** Sensitive Data Redacted ***"
    return out
