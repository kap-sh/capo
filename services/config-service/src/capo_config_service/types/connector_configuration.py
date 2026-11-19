"""Generated from Smithy shape ``com.amazonaws.configservice#ConnectorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.azure_connector_configuration
    import capo_config_service.types.gcp_connector_configuration


class ConnectorConfiguration(TypedDict, closed=True):
    azure: NotRequired[
        "capo_config_service.types.azure_connector_configuration.AzureConnectorConfiguration"
    ]
    """<p>The configuration for an Azure connector.</p>"""
    gcp: NotRequired[
        "capo_config_service.types.gcp_connector_configuration.GcpConnectorConfiguration"
    ]
    """<p>The configuration for a Google Cloud connector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorConfiguration) -> dict:
    out: dict = {}
    if "azure" in value:
        import capo_config_service.types.azure_connector_configuration

        out["azure"] = (
            capo_config_service.types.azure_connector_configuration.serialize_aws_json_1_1(
                value["azure"]
            )
        )
    if "gcp" in value:
        import capo_config_service.types.gcp_connector_configuration

        out["gcp"] = (
            capo_config_service.types.gcp_connector_configuration.serialize_aws_json_1_1(
                value["gcp"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectorConfiguration:
    out: ConnectorConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("azure") is not None:
        import capo_config_service.types.azure_connector_configuration

        out["azure"] = (
            capo_config_service.types.azure_connector_configuration.deserialize_aws_json_1_1(
                data["azure"]
            )
        )
    if data.get("gcp") is not None:
        import capo_config_service.types.gcp_connector_configuration

        out["gcp"] = (
            capo_config_service.types.gcp_connector_configuration.deserialize_aws_json_1_1(
                data["gcp"]
            )
        )
    return out
