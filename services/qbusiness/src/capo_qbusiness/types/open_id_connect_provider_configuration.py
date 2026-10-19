"""Generated from Smithy shape ``com.amazonaws.qbusiness#OpenIDConnectProviderConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.role_arn
    import capo_qbusiness.types.secret_arn


class OpenIDConnectProviderConfiguration(TypedDict, closed=True):
    secrets_arn: "capo_qbusiness.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of a Secrets Manager secret containing the OIDC client secret.</p>"""
    secrets_role: "capo_qbusiness.types.role_arn.RoleArn"
    """<p>An IAM role with permissions to access KMS to decrypt the Secrets Manager secret containing your OIDC client secret.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OpenIDConnectProviderConfiguration) -> dict:
    out: dict = {}
    out["secretsArn"] = value["secrets_arn"]
    out["secretsRole"] = value["secrets_role"]
    return out


def deserialize_json(data: dict) -> OpenIDConnectProviderConfiguration:
    out: OpenIDConnectProviderConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("secretsArn") is not None:
        out["secrets_arn"] = data["secretsArn"]
    else:
        out["secrets_arn"] = ""
    if data.get("secretsRole") is not None:
        out["secrets_role"] = data["secretsRole"]
    else:
        out["secrets_role"] = ""
    return out
