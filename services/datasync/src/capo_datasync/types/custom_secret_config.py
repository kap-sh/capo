"""Generated from Smithy shape ``com.amazonaws.datasync#CustomSecretConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.iam_role_arn_or_empty_string
    import capo_datasync.types.secret_arn


class CustomSecretConfig(TypedDict, closed=True):
    secret_arn: NotRequired["capo_datasync.types.secret_arn.SecretArn"]
    """<p>Specifies the ARN for an Secrets Manager secret.</p>"""
    secret_access_role_arn: NotRequired[
        "capo_datasync.types.iam_role_arn_or_empty_string.IamRoleArnOrEmptyString"
    ]
    """<p>Specifies the ARN for the Identity and Access Management role that DataSync uses to access the secret specified for <code>SecretArn</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomSecretConfig) -> dict:
    out: dict = {}
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    if "secret_access_role_arn" in value:
        out["SecretAccessRoleArn"] = value["secret_access_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomSecretConfig:
    out: CustomSecretConfig = {}  # type: ignore[typeddict-item]
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    if data.get("SecretAccessRoleArn") is not None:
        out["secret_access_role_arn"] = data["SecretAccessRoleArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CustomSecretConfig) -> dict:
    out: dict = {}
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    if "secret_access_role_arn" in value:
        out["SecretAccessRoleArn"] = value["secret_access_role_arn"]
    return out


def deserialize_cbor(data: dict) -> CustomSecretConfig:
    out: CustomSecretConfig = {}  # type: ignore[typeddict-item]
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    if data.get("SecretAccessRoleArn") is not None:
        out["secret_access_role_arn"] = data["SecretAccessRoleArn"]
    return out
