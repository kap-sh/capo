"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.integration_name
    import capo_cloudwatch_logs.types.integration_type
    import capo_cloudwatch_logs.types.resource_config


class PutIntegrationRequest(TypedDict, closed=True):
    integration_name: "capo_cloudwatch_logs.types.integration_name.IntegrationName"
    """<p>A name for the integration.</p>"""
    resource_config: "capo_cloudwatch_logs.types.resource_config.ResourceConfig"
    """<p>A structure that contains configuration information for the integration that you are creating.</p>"""
    integration_type: "capo_cloudwatch_logs.types.integration_type.IntegrationType"
    """<p>The type of integration. Currently, the only supported type is <code>OPENSEARCH</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutIntegrationRequest) -> dict:
    out: dict = {}
    out["integrationName"] = value["integration_name"]
    import capo_cloudwatch_logs.types.resource_config

    out["resourceConfig"] = (
        capo_cloudwatch_logs.types.resource_config.serialize_aws_json_1_1(
            value["resource_config"]
        )
    )
    import capo_cloudwatch_logs.types.integration_type

    out["integrationType"] = (
        capo_cloudwatch_logs.types.integration_type.serialize_aws_json_1_1(
            value["integration_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutIntegrationRequest:
    out: PutIntegrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("integrationName") is not None:
        out["integration_name"] = data["integrationName"]
    else:
        out["integration_name"] = ""
    if data.get("resourceConfig") is not None:
        import capo_cloudwatch_logs.types.resource_config

        out["resource_config"] = (
            capo_cloudwatch_logs.types.resource_config.deserialize_aws_json_1_1(
                data["resourceConfig"]
            )
        )
    else:
        import capo_cloudwatch_logs.types._unknown

        out["resource_config"] = capo_cloudwatch_logs.types._unknown.UnknownUnionMember(
            ""
        )
    if data.get("integrationType") is not None:
        import capo_cloudwatch_logs.types.integration_type

        out["integration_type"] = (
            capo_cloudwatch_logs.types.integration_type.deserialize_aws_json_1_1(
                data["integrationType"]
            )
        )
    else:
        import typing

        out["integration_type"] = typing.cast(
            "capo_cloudwatch_logs.types.integration_type.IntegrationType", ""
        )
    return out
