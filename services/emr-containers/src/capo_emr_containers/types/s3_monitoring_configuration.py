"""Generated from Smithy shape ``com.amazonaws.emrcontainers#S3MonitoringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.kms_key_arn
    import capo_emr_containers.types.uri_string


class S3MonitoringConfiguration(TypedDict, closed=True):
    log_uri: "capo_emr_containers.types.uri_string.UriString"
    """<p>Amazon S3 destination URI for log publishing.</p>"""
    encryption_key_arn: NotRequired["capo_emr_containers.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the encryption key for logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3MonitoringConfiguration) -> dict:
    out: dict = {}
    out["logUri"] = value["log_uri"]
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    return out


def deserialize_json(data: dict) -> S3MonitoringConfiguration:
    out: S3MonitoringConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("logUri") is not None:
        out["log_uri"] = data["logUri"]
    else:
        out["log_uri"] = ""
    if data.get("encryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    return out
