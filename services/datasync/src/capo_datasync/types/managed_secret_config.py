"""Generated from Smithy shape ``com.amazonaws.datasync#ManagedSecretConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.secret_arn


class ManagedSecretConfig(TypedDict, closed=True):
    secret_arn: NotRequired["capo_datasync.types.secret_arn.SecretArn"]
    """<p>Specifies the ARN for an Secrets Manager secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedSecretConfig) -> dict:
    out: dict = {}
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedSecretConfig:
    out: ManagedSecretConfig = {}  # type: ignore[typeddict-item]
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ManagedSecretConfig) -> dict:
    out: dict = {}
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    return out


def deserialize_cbor(data: dict) -> ManagedSecretConfig:
    out: ManagedSecretConfig = {}  # type: ignore[typeddict-item]
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    return out
