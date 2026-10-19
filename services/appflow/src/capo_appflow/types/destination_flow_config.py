"""Generated from Smithy shape ``com.amazonaws.appflow#DestinationFlowConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.api_version
    import capo_appflow.types.connector_profile_name
    import capo_appflow.types.connector_type
    import capo_appflow.types.destination_connector_properties


class DestinationFlowConfig(TypedDict, closed=True):
    connector_type: "capo_appflow.types.connector_type.ConnectorType"
    """<p> The type of connector, such as Salesforce, Amplitude, and so on. </p>"""
    api_version: NotRequired["capo_appflow.types.api_version.ApiVersion"]
    """<p>The API version that the destination connector uses.</p>"""
    connector_profile_name: NotRequired[
        "capo_appflow.types.connector_profile_name.ConnectorProfileName"
    ]
    """<p> The name of the connector profile. This name must be unique for each connector profile in the Amazon Web Services account. </p>"""
    destination_connector_properties: "capo_appflow.types.destination_connector_properties.DestinationConnectorProperties"
    """<p> This stores the information that is required to query a particular connector. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationFlowConfig) -> dict:
    out: dict = {}
    import capo_appflow.types.connector_type

    out["connectorType"] = capo_appflow.types.connector_type.serialize_json(
        value["connector_type"]
    )
    if "api_version" in value:
        out["apiVersion"] = value["api_version"]
    if "connector_profile_name" in value:
        out["connectorProfileName"] = value["connector_profile_name"]
    import capo_appflow.types.destination_connector_properties

    out["destinationConnectorProperties"] = (
        capo_appflow.types.destination_connector_properties.serialize_json(
            value["destination_connector_properties"]
        )
    )
    return out


def deserialize_json(data: dict) -> DestinationFlowConfig:
    out: DestinationFlowConfig = {}  # type: ignore[typeddict-item]
    if data.get("connectorType") is not None:
        import capo_appflow.types.connector_type

        out["connector_type"] = capo_appflow.types.connector_type.deserialize_json(
            data["connectorType"]
        )
    else:
        import typing

        out["connector_type"] = typing.cast(
            "capo_appflow.types.connector_type.ConnectorType", ""
        )
    if data.get("apiVersion") is not None:
        out["api_version"] = data["apiVersion"]
    if data.get("connectorProfileName") is not None:
        out["connector_profile_name"] = data["connectorProfileName"]
    if data.get("destinationConnectorProperties") is not None:
        import capo_appflow.types.destination_connector_properties

        out["destination_connector_properties"] = (
            capo_appflow.types.destination_connector_properties.deserialize_json(
                data["destinationConnectorProperties"]
            )
        )
    else:
        raise DeserializationError(
            "DestinationFlowConfig.destination_connector_properties required"
        )
    return out
