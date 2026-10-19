"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedshiftServerlessAuthConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.redshift_serverless_auth_type
    import capo_bedrock_agent.types.secret_arn


class RedshiftServerlessAuthConfiguration(TypedDict, closed=True):
    type: "capo_bedrock_agent.types.redshift_serverless_auth_type.RedshiftServerlessAuthType"
    """<p>The type of authentication to use.</p>"""
    username_password_secret_arn: NotRequired[
        "capo_bedrock_agent.types.secret_arn.SecretArn"
    ]
    """<p>The ARN of an Secrets Manager secret for authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftServerlessAuthConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.redshift_serverless_auth_type

    out["type"] = capo_bedrock_agent.types.redshift_serverless_auth_type.serialize_json(
        value["type"]
    )
    if "username_password_secret_arn" in value:
        out["usernamePasswordSecretArn"] = value["username_password_secret_arn"]
    return out


def deserialize_json(data: dict) -> RedshiftServerlessAuthConfiguration:
    out: RedshiftServerlessAuthConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent.types.redshift_serverless_auth_type

        out["type"] = (
            capo_bedrock_agent.types.redshift_serverless_auth_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent.types.redshift_serverless_auth_type.RedshiftServerlessAuthType",
            "",
        )
    if data.get("usernamePasswordSecretArn") is not None:
        out["username_password_secret_arn"] = data["usernamePasswordSecretArn"]
    return out
