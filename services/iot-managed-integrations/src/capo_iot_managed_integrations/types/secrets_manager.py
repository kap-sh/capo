"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#SecretsManager``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.secrets_manager_arn
    import capo_iot_managed_integrations.types.secrets_manager_version_id


class SecretsManager(TypedDict, closed=True):
    arn: "capo_iot_managed_integrations.types.secrets_manager_arn.SecretsManagerArn"
    """<p>The Amazon Resource Name (ARN) of the AWS Secrets Manager secret.</p>"""
    version_id: "capo_iot_managed_integrations.types.secrets_manager_version_id.SecretsManagerVersionId"
    """<p>The version ID of the AWS Secrets Manager secret.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecretsManager) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["versionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> SecretsManager:
    out: SecretsManager = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("versionId") is not None:
        out["version_id"] = data["versionId"]
    else:
        out["version_id"] = ""
    return out
