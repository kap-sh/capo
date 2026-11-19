"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#CopyBackupToRegionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.destination_backup


class CopyBackupToRegionResponse(TypedDict, closed=True):
    destination_backup: NotRequired[
        "capo_cloudhsm_v2.types.destination_backup.DestinationBackup"
    ]
    """<p>Information on the backup that will be copied to the destination region, including CreateTimestamp, SourceBackup, SourceCluster, and Source Region. CreateTimestamp of the destination backup will be the same as that of the source backup.</p> <p>You will need to use the <code>sourceBackupID</code> returned in this operation to use the <a>DescribeBackups</a> operation on the backup that will be copied to the destination region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopyBackupToRegionResponse) -> dict:
    out: dict = {}
    if "destination_backup" in value:
        import capo_cloudhsm_v2.types.destination_backup

        out["DestinationBackup"] = (
            capo_cloudhsm_v2.types.destination_backup.serialize_aws_json_1_1(
                value["destination_backup"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CopyBackupToRegionResponse:
    out: CopyBackupToRegionResponse = {}  # type: ignore[typeddict-item]
    if data.get("DestinationBackup") is not None:
        import capo_cloudhsm_v2.types.destination_backup

        out["destination_backup"] = (
            capo_cloudhsm_v2.types.destination_backup.deserialize_aws_json_1_1(
                data["DestinationBackup"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CopyBackupToRegionResponse) -> dict:
    out: dict = {}
    if "destination_backup" in value:
        import capo_cloudhsm_v2.types.destination_backup

        out["DestinationBackup"] = (
            capo_cloudhsm_v2.types.destination_backup.serialize_cbor(
                value["destination_backup"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> CopyBackupToRegionResponse:
    out: CopyBackupToRegionResponse = {}  # type: ignore[typeddict-item]
    if data.get("DestinationBackup") is not None:
        import capo_cloudhsm_v2.types.destination_backup

        out["destination_backup"] = (
            capo_cloudhsm_v2.types.destination_backup.deserialize_cbor(
                data["DestinationBackup"]
            )
        )
    return out
