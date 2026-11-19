"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureTelemetrySourceConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.aws_config_connector_arn


class AzureTelemetrySourceConfigurationInput(TypedDict, closed=True):
    aws_config_connector_arn: (
        "capo_observabilityadmin.types.aws_config_connector_arn.AwsConfigConnectorArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Config connector for the Microsoft Azure tenant to collect resource metadata from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureTelemetrySourceConfigurationInput) -> dict:
    out: dict = {}
    out["AwsConfigConnectorArn"] = value["aws_config_connector_arn"]
    return out


def deserialize_json(data: dict) -> AzureTelemetrySourceConfigurationInput:
    out: AzureTelemetrySourceConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("AwsConfigConnectorArn") is not None:
        out["aws_config_connector_arn"] = data["AwsConfigConnectorArn"]
    else:
        out["aws_config_connector_arn"] = ""
    return out
