"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#ModifyBackupAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.backup


class ModifyBackupAttributesResponse(TypedDict, closed=True):
    backup: NotRequired["capo_cloudhsm_v2.types.backup.Backup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyBackupAttributesResponse) -> dict:
    out: dict = {}
    if "backup" in value:
        import capo_cloudhsm_v2.types.backup

        out["Backup"] = capo_cloudhsm_v2.types.backup.serialize_aws_json_1_1(
            value["backup"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyBackupAttributesResponse:
    out: ModifyBackupAttributesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Backup") is not None:
        import capo_cloudhsm_v2.types.backup

        out["backup"] = capo_cloudhsm_v2.types.backup.deserialize_aws_json_1_1(
            data["Backup"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ModifyBackupAttributesResponse) -> dict:
    out: dict = {}
    if "backup" in value:
        import capo_cloudhsm_v2.types.backup

        out["Backup"] = capo_cloudhsm_v2.types.backup.serialize_cbor(value["backup"])
    return out


def deserialize_cbor(data: dict) -> ModifyBackupAttributesResponse:
    out: ModifyBackupAttributesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Backup") is not None:
        import capo_cloudhsm_v2.types.backup

        out["backup"] = capo_cloudhsm_v2.types.backup.deserialize_cbor(data["Backup"])
    return out
