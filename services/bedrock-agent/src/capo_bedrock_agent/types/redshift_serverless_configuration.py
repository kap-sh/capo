"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedshiftServerlessConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.redshift_serverless_auth_configuration
    import capo_bedrock_agent.types.workgroup_arn


class RedshiftServerlessConfiguration(TypedDict, closed=True):
    workgroup_arn: "capo_bedrock_agent.types.workgroup_arn.WorkgroupArn"
    """<p>The ARN of the Amazon Redshift workgroup.</p>"""
    auth_configuration: "capo_bedrock_agent.types.redshift_serverless_auth_configuration.RedshiftServerlessAuthConfiguration"
    """<p>Specifies configurations for authentication to an Amazon Redshift provisioned data warehouse.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftServerlessConfiguration) -> dict:
    out: dict = {}
    out["workgroupArn"] = value["workgroup_arn"]
    import capo_bedrock_agent.types.redshift_serverless_auth_configuration

    out["authConfiguration"] = (
        capo_bedrock_agent.types.redshift_serverless_auth_configuration.serialize_json(
            value["auth_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> RedshiftServerlessConfiguration:
    out: RedshiftServerlessConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("workgroupArn") is not None:
        out["workgroup_arn"] = data["workgroupArn"]
    else:
        out["workgroup_arn"] = ""
    if data.get("authConfiguration") is not None:
        import capo_bedrock_agent.types.redshift_serverless_auth_configuration

        out["auth_configuration"] = (
            capo_bedrock_agent.types.redshift_serverless_auth_configuration.deserialize_json(
                data["authConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "RedshiftServerlessConfiguration.auth_configuration required"
        )
    return out
