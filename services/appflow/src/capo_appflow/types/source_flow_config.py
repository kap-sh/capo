"""Generated from Smithy shape ``com.amazonaws.appflow#SourceFlowConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.api_version
    import capo_appflow.types.connector_profile_name
    import capo_appflow.types.connector_type
    import capo_appflow.types.incremental_pull_config
    import capo_appflow.types.source_connector_properties


class SourceFlowConfig(TypedDict, closed=True):
    connector_type: "capo_appflow.types.connector_type.ConnectorType"
    """<p> The type of connector, such as Salesforce, Amplitude, and so on. </p>"""
    api_version: NotRequired["capo_appflow.types.api_version.ApiVersion"]
    """<p>The API version of the connector when it's used as a source in the flow.</p>"""
    connector_profile_name: NotRequired[
        "capo_appflow.types.connector_profile_name.ConnectorProfileName"
    ]
    """<p> The name of the connector profile. This name must be unique for each connector profile in the Amazon Web Services account. </p>"""
    source_connector_properties: (
        "capo_appflow.types.source_connector_properties.SourceConnectorProperties"
    )
    """<p> Specifies the information that is required to query a particular source connector. </p>"""
    incremental_pull_config: NotRequired[
        "capo_appflow.types.incremental_pull_config.IncrementalPullConfig"
    ]
    """<p> Defines the configuration for a scheduled incremental data pull. If a valid configuration is provided, the fields specified in the configuration are used when querying for the incremental data pull. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceFlowConfig) -> dict:
    out: dict = {}
    import capo_appflow.types.connector_type

    out["connectorType"] = capo_appflow.types.connector_type.serialize_json(
        value["connector_type"]
    )
    if "api_version" in value:
        out["apiVersion"] = value["api_version"]
    if "connector_profile_name" in value:
        out["connectorProfileName"] = value["connector_profile_name"]
    import capo_appflow.types.source_connector_properties

    out["sourceConnectorProperties"] = (
        capo_appflow.types.source_connector_properties.serialize_json(
            value["source_connector_properties"]
        )
    )
    if "incremental_pull_config" in value:
        import capo_appflow.types.incremental_pull_config

        out["incrementalPullConfig"] = (
            capo_appflow.types.incremental_pull_config.serialize_json(
                value["incremental_pull_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> SourceFlowConfig:
    out: SourceFlowConfig = {}  # type: ignore[typeddict-item]
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
    if data.get("sourceConnectorProperties") is not None:
        import capo_appflow.types.source_connector_properties

        out["source_connector_properties"] = (
            capo_appflow.types.source_connector_properties.deserialize_json(
                data["sourceConnectorProperties"]
            )
        )
    else:
        raise DeserializationError(
            "SourceFlowConfig.source_connector_properties required"
        )
    if data.get("incrementalPullConfig") is not None:
        import capo_appflow.types.incremental_pull_config

        out["incremental_pull_config"] = (
            capo_appflow.types.incremental_pull_config.deserialize_json(
                data["incrementalPullConfig"]
            )
        )
    return out
