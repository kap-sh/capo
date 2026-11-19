"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#RestoreBackupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.backup


class RestoreBackupResponse(TypedDict, closed=True):
    backup: NotRequired["capo_cloudhsm_v2.types.backup.Backup"]
    """<p>Information on the <code>Backup</code> object created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreBackupResponse) -> dict:
    out: dict = {}
    if "backup" in value:
        import capo_cloudhsm_v2.types.backup

        out["Backup"] = capo_cloudhsm_v2.types.backup.serialize_aws_json_1_1(
            value["backup"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RestoreBackupResponse:
    out: RestoreBackupResponse = {}  # type: ignore[typeddict-item]
    if data.get("Backup") is not None:
        import capo_cloudhsm_v2.types.backup

        out["backup"] = capo_cloudhsm_v2.types.backup.deserialize_aws_json_1_1(
            data["Backup"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RestoreBackupResponse) -> dict:
    out: dict = {}
    if "backup" in value:
        import capo_cloudhsm_v2.types.backup

        out["Backup"] = capo_cloudhsm_v2.types.backup.serialize_cbor(value["backup"])
    return out


def deserialize_cbor(data: dict) -> RestoreBackupResponse:
    out: RestoreBackupResponse = {}  # type: ignore[typeddict-item]
    if data.get("Backup") is not None:
        import capo_cloudhsm_v2.types.backup

        out["backup"] = capo_cloudhsm_v2.types.backup.deserialize_cbor(data["Backup"])
    return out
