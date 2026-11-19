"""Generated from Smithy shape ``com.amazonaws.workspaces#MicrosoftEntraConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.microsoft_entra_config_tenant_id
    import capo_workspaces.types.secrets_manager_arn


class MicrosoftEntraConfig(TypedDict, closed=True):
    tenant_id: NotRequired[
        "capo_workspaces.types.microsoft_entra_config_tenant_id.MicrosoftEntraConfigTenantId"
    ]
    """<p>The identifier of the tenant.</p>"""
    application_config_secret_arn: NotRequired[
        "capo_workspaces.types.secrets_manager_arn.SecretsManagerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the application config.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MicrosoftEntraConfig) -> dict:
    out: dict = {}
    if "tenant_id" in value:
        out["TenantId"] = value["tenant_id"]
    if "application_config_secret_arn" in value:
        out["ApplicationConfigSecretArn"] = value["application_config_secret_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MicrosoftEntraConfig:
    out: MicrosoftEntraConfig = {}  # type: ignore[typeddict-item]
    if data.get("TenantId") is not None:
        out["tenant_id"] = data["TenantId"]
    if data.get("ApplicationConfigSecretArn") is not None:
        out["application_config_secret_arn"] = data["ApplicationConfigSecretArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MicrosoftEntraConfig) -> dict:
    out: dict = {}
    if "tenant_id" in value:
        out["TenantId"] = value["tenant_id"]
    if "application_config_secret_arn" in value:
        out["ApplicationConfigSecretArn"] = value["application_config_secret_arn"]
    return out


def deserialize_cbor(data: dict) -> MicrosoftEntraConfig:
    out: MicrosoftEntraConfig = {}  # type: ignore[typeddict-item]
    if data.get("TenantId") is not None:
        out["tenant_id"] = data["TenantId"]
    if data.get("ApplicationConfigSecretArn") is not None:
        out["application_config_secret_arn"] = data["ApplicationConfigSecretArn"]
    return out
