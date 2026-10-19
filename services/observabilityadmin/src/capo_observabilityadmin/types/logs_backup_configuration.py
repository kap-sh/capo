"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#LogsBackupConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.region
    import capo_observabilityadmin.types.resource_arn


class LogsBackupConfiguration(TypedDict, closed=True):
    region: "capo_observabilityadmin.types.region.Region"
    """<p>Logs specific backup destination region within the primary destination account to which log data should be centralized.</p>"""
    kms_key_arn: NotRequired["capo_observabilityadmin.types.resource_arn.ResourceArn"]
    """<p>KMS Key ARN belonging to the primary destination account and backup region, to encrypt newly created central log groups in the backup destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogsBackupConfiguration) -> dict:
    out: dict = {}
    out["Region"] = value["region"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> LogsBackupConfiguration:
    out: LogsBackupConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    else:
        out["region"] = ""
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out
