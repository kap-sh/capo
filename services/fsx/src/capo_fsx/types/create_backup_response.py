"""Generated from Smithy shape ``com.amazonaws.fsx#CreateBackupResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.backup


class CreateBackupResponse(TypedDict, closed=True):
    backup: NotRequired["capo_fsx.types.backup.Backup"]
    """<p>A description of the backup.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBackupResponse) -> dict:
    out: dict = {}
    if "backup" in value:
        import capo_fsx.types.backup

        out["Backup"] = capo_fsx.types.backup.serialize_aws_json_1_1(value["backup"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBackupResponse:
    out: CreateBackupResponse = {}  # type: ignore[typeddict-item]
    if data.get("Backup") is not None:
        import capo_fsx.types.backup

        out["backup"] = capo_fsx.types.backup.deserialize_aws_json_1_1(data["Backup"])
    return out


def redact_sensitive(value: CreateBackupResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "backup" in value:
        import capo_fsx.types.backup

        out["backup"] = capo_fsx.types.backup.redact_sensitive(value["backup"])
    return out
