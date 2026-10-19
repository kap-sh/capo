"""Generated from Smithy shape ``com.amazonaws.qbusiness#BasicAuthConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.role_arn
    import capo_qbusiness.types.secret_arn


class BasicAuthConfiguration(TypedDict, closed=True):
    secret_arn: "capo_qbusiness.types.secret_arn.SecretArn"
    """<p>The ARN of the Secrets Manager secret that stores the basic authentication credentials used for plugin configuration..</p>"""
    role_arn: "capo_qbusiness.types.role_arn.RoleArn"
    """<p>The ARN of an IAM role used by Amazon Q Business to access the basic authentication credentials stored in a Secrets Manager secret.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BasicAuthConfiguration) -> dict:
    out: dict = {}
    out["secretArn"] = value["secret_arn"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> BasicAuthConfiguration:
    out: BasicAuthConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("secretArn") is not None:
        out["secret_arn"] = data["secretArn"]
    else:
        out["secret_arn"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    return out
