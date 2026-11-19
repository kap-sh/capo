"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureTelemetrySourceConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.aws_config_connector_arn
    import capo_observabilityadmin.types.service_linked_recorder_arn


class AzureTelemetrySourceConfigurationOutput(TypedDict, closed=True):
    aws_config_connector_arn: NotRequired[
        "capo_observabilityadmin.types.aws_config_connector_arn.AwsConfigConnectorArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Config connector that the enrichment uses.</p>"""
    service_linked_recorder_arn: NotRequired[
        "capo_observabilityadmin.types.service_linked_recorder_arn.ServiceLinkedRecorderArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the service-linked configuration recorder that CloudWatch created in your account for the enrichment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureTelemetrySourceConfigurationOutput) -> dict:
    out: dict = {}
    if "aws_config_connector_arn" in value:
        out["AwsConfigConnectorArn"] = value["aws_config_connector_arn"]
    if "service_linked_recorder_arn" in value:
        out["ServiceLinkedRecorderArn"] = value["service_linked_recorder_arn"]
    return out


def deserialize_json(data: dict) -> AzureTelemetrySourceConfigurationOutput:
    out: AzureTelemetrySourceConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("AwsConfigConnectorArn") is not None:
        out["aws_config_connector_arn"] = data["AwsConfigConnectorArn"]
    if data.get("ServiceLinkedRecorderArn") is not None:
        out["service_linked_recorder_arn"] = data["ServiceLinkedRecorderArn"]
    return out
