"""Generated from Smithy shape ``com.amazonaws.workspaces#ActiveDirectoryConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.domain_name
    import capo_workspaces.types.secrets_manager_arn


class ActiveDirectoryConfig(TypedDict, closed=True):
    domain_name: "capo_workspaces.types.domain_name.DomainName"
    """<p>The name of the domain.</p>"""
    service_account_secret_arn: (
        "capo_workspaces.types.secrets_manager_arn.SecretsManagerArn"
    )
    """<p>Indicates the secret ARN on the service account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActiveDirectoryConfig) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    out["ServiceAccountSecretArn"] = value["service_account_secret_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActiveDirectoryConfig:
    out: ActiveDirectoryConfig = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("ServiceAccountSecretArn") is not None:
        out["service_account_secret_arn"] = data["ServiceAccountSecretArn"]
    else:
        out["service_account_secret_arn"] = ""
    return out
