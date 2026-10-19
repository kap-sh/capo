"""Generated from Smithy shape ``com.amazonaws.inspector2#ConnectorScanConfigurationItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.aws_config_connector_arn
    import capo_inspector2.types.connector_arn_list
    import capo_inspector2.types.connector_scan_configuration


class ConnectorScanConfigurationItem(TypedDict, closed=True):
    aws_config_connector_arn: (
        "capo_inspector2.types.aws_config_connector_arn.AwsConfigConnectorArn"
    )
    """<p>The ARN of the Amazon Web Services Config connector.</p>"""
    connector_arns: "capo_inspector2.types.connector_arn_list.ConnectorArnList"
    """<p>The list of connector ARNs associated with this Amazon Web Services Config connector.</p>"""
    scan_configuration: (
        "capo_inspector2.types.connector_scan_configuration.ConnectorScanConfiguration"
    )
    """<p>The scan configuration settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorScanConfigurationItem) -> dict:
    out: dict = {}
    out["awsConfigConnectorArn"] = value["aws_config_connector_arn"]
    import capo_inspector2.types.connector_arn_list

    out["connectorArns"] = capo_inspector2.types.connector_arn_list.serialize_json(
        value["connector_arns"]
    )
    import capo_inspector2.types.connector_scan_configuration

    out["scanConfiguration"] = (
        capo_inspector2.types.connector_scan_configuration.serialize_json(
            value["scan_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConnectorScanConfigurationItem:
    out: ConnectorScanConfigurationItem = {}  # type: ignore[typeddict-item]
    if data.get("awsConfigConnectorArn") is not None:
        out["aws_config_connector_arn"] = data["awsConfigConnectorArn"]
    else:
        out["aws_config_connector_arn"] = ""
    if data.get("connectorArns") is not None:
        import capo_inspector2.types.connector_arn_list

        out["connector_arns"] = (
            capo_inspector2.types.connector_arn_list.deserialize_json(
                data["connectorArns"]
            )
        )
    else:
        out["connector_arns"] = []
    if data.get("scanConfiguration") is not None:
        import capo_inspector2.types.connector_scan_configuration

        out["scan_configuration"] = (
            capo_inspector2.types.connector_scan_configuration.deserialize_json(
                data["scanConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "ConnectorScanConfigurationItem.scan_configuration required"
        )
    return out
