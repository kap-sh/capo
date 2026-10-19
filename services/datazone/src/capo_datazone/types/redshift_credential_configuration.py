"""Generated from Smithy shape ``com.amazonaws.datazone#RedshiftCredentialConfiguration``."""

from typing_extensions import TypedDict


class RedshiftCredentialConfiguration(TypedDict, closed=True):
    secret_manager_arn: "str"
    """<p>The ARN of a secret manager for an Amazon Redshift cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftCredentialConfiguration) -> dict:
    out: dict = {}
    out["secretManagerArn"] = value["secret_manager_arn"]
    return out


def deserialize_json(data: dict) -> RedshiftCredentialConfiguration:
    out: RedshiftCredentialConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("secretManagerArn") is not None:
        out["secret_manager_arn"] = data["secretManagerArn"]
    else:
        out["secret_manager_arn"] = ""
    return out
