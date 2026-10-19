"""Generated from Smithy shape ``com.amazonaws.firehose#SecretsManagerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.boolean_object
    import capo_firehose.types.role_arn
    import capo_firehose.types.secret_arn


class SecretsManagerConfiguration(TypedDict, closed=True):
    secret_arn: NotRequired["capo_firehose.types.secret_arn.SecretARN"]
    """<p>The ARN of the secret that stores your credentials. It must be in the same region as the Firehose stream and the role. The secret ARN can reside in a different account than the Firehose stream and role as Firehose supports cross-account secret access. This parameter is required when <b>Enabled</b> is set to <code>True</code>.</p>"""
    role_arn: NotRequired["capo_firehose.types.role_arn.RoleARN"]
    """<p> Specifies the role that Firehose assumes when calling the Secrets Manager API operation. When you provide the role, it overrides any destination specific role defined in the destination configuration. If you do not provide the then we use the destination specific role. This parameter is required for Splunk. </p>"""
    enabled: "capo_firehose.types.boolean_object.BooleanObject"
    """<p>Specifies whether you want to use the secrets manager feature. When set as <code>True</code> the secrets manager configuration overwrites the existing secrets in the destination configuration. When it's set to <code>False</code> Firehose falls back to the credentials in the destination configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecretsManagerConfiguration) -> dict:
    out: dict = {}
    if "secret_arn" in value:
        out["SecretARN"] = value["secret_arn"]
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    out["Enabled"] = value["enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SecretsManagerConfiguration:
    out: SecretsManagerConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SecretARN") is not None:
        out["secret_arn"] = data["SecretARN"]
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    return out
