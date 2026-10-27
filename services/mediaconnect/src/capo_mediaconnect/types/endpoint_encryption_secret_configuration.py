"""Generated from Smithy shape ``com.amazonaws.mediaconnect#EndpointEncryptionSecretConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.secret_arn


class EndpointEncryptionSecretConfiguration(TypedDict, closed=True):
    secret_arn: "capo_mediaconnect.types.secret_arn.SecretArn"
    """<p>The ARN of the Secrets Manager secret that holds the key or passphrase. The secret must be encrypted with a customer managed Amazon Web Services KMS key that is enabled and symmetric; it cannot use the Amazon Web Services managed key <code>aws/secretsmanager</code>. The secret must be in the same Amazon Web Services account and Region as the endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointEncryptionSecretConfiguration) -> dict:
    out: dict = {}
    out["secretArn"] = value["secret_arn"]
    return out


def deserialize_json(data: dict) -> EndpointEncryptionSecretConfiguration:
    out: EndpointEncryptionSecretConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("secretArn") is not None:
        out["secret_arn"] = data["secretArn"]
    else:
        out["secret_arn"] = ""
    return out
