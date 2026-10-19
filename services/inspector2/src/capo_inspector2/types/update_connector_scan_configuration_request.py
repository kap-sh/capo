"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateConnectorScanConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.aws_config_connector_arn
    import capo_inspector2.types.connector_scan_configuration


class UpdateConnectorScanConfigurationRequest(TypedDict, closed=True):
    aws_config_connector_arn: (
        "capo_inspector2.types.aws_config_connector_arn.AwsConfigConnectorArn"
    )
    """<p>The ARN of the Amazon Web Services Config connector.</p>"""
    scan_configuration: (
        "capo_inspector2.types.connector_scan_configuration.ConnectorScanConfiguration"
    )
    """<p>The scan configuration settings to apply.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectorScanConfigurationRequest) -> dict:
    out: dict = {}
    out["awsConfigConnectorArn"] = value["aws_config_connector_arn"]
    import capo_inspector2.types.connector_scan_configuration

    out["scanConfiguration"] = (
        capo_inspector2.types.connector_scan_configuration.serialize_json(
            value["scan_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateConnectorScanConfigurationRequest:
    out: UpdateConnectorScanConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("awsConfigConnectorArn") is not None:
        out["aws_config_connector_arn"] = data["awsConfigConnectorArn"]
    else:
        out["aws_config_connector_arn"] = ""
    if data.get("scanConfiguration") is not None:
        import capo_inspector2.types.connector_scan_configuration

        out["scan_configuration"] = (
            capo_inspector2.types.connector_scan_configuration.deserialize_json(
                data["scanConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateConnectorScanConfigurationRequest.scan_configuration required"
        )
    return out
