"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedshiftProvisionedAuthConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.redshift_provisioned_auth_type
    import capo_bedrock_agent.types.secret_arn


class RedshiftProvisionedAuthConfiguration(TypedDict, closed=True):
    type: "capo_bedrock_agent.types.redshift_provisioned_auth_type.RedshiftProvisionedAuthType"
    """<p>The type of authentication to use.</p>"""
    database_user: NotRequired["str"]
    """<p>The database username for authentication to an Amazon Redshift provisioned data warehouse.</p>"""
    username_password_secret_arn: NotRequired[
        "capo_bedrock_agent.types.secret_arn.SecretArn"
    ]
    """<p>The ARN of an Secrets Manager secret for authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftProvisionedAuthConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.redshift_provisioned_auth_type

    out["type"] = (
        capo_bedrock_agent.types.redshift_provisioned_auth_type.serialize_json(
            value["type"]
        )
    )
    if "database_user" in value:
        out["databaseUser"] = value["database_user"]
    if "username_password_secret_arn" in value:
        out["usernamePasswordSecretArn"] = value["username_password_secret_arn"]
    return out


def deserialize_json(data: dict) -> RedshiftProvisionedAuthConfiguration:
    out: RedshiftProvisionedAuthConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent.types.redshift_provisioned_auth_type

        out["type"] = (
            capo_bedrock_agent.types.redshift_provisioned_auth_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent.types.redshift_provisioned_auth_type.RedshiftProvisionedAuthType",
            "",
        )
    if data.get("databaseUser") is not None:
        out["database_user"] = data["databaseUser"]
    if data.get("usernamePasswordSecretArn") is not None:
        out["username_password_secret_arn"] = data["usernamePasswordSecretArn"]
    return out
