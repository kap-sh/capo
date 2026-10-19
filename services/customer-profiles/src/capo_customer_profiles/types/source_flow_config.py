"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SourceFlowConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.connector_profile_name
    import capo_customer_profiles.types.incremental_pull_config
    import capo_customer_profiles.types.source_connector_properties
    import capo_customer_profiles.types.source_connector_type


class SourceFlowConfig(TypedDict, closed=True):
    connector_profile_name: NotRequired[
        "capo_customer_profiles.types.connector_profile_name.ConnectorProfileName"
    ]
    """<p>The name of the AppFlow connector profile. This name must be unique for each connector profile in the AWS account.</p>"""
    connector_type: (
        "capo_customer_profiles.types.source_connector_type.SourceConnectorType"
    )
    """<p>The type of connector, such as Salesforce, Marketo, and so on.</p>"""
    incremental_pull_config: NotRequired[
        "capo_customer_profiles.types.incremental_pull_config.IncrementalPullConfig"
    ]
    """<p>Defines the configuration for a scheduled incremental data pull. If a valid configuration is provided, the fields specified in the configuration are used when querying for the incremental data pull.</p>"""
    source_connector_properties: "capo_customer_profiles.types.source_connector_properties.SourceConnectorProperties"
    """<p>Specifies the information that is required to query a particular source connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceFlowConfig) -> dict:
    out: dict = {}
    if "connector_profile_name" in value:
        out["ConnectorProfileName"] = value["connector_profile_name"]
    import capo_customer_profiles.types.source_connector_type

    out["ConnectorType"] = (
        capo_customer_profiles.types.source_connector_type.serialize_json(
            value["connector_type"]
        )
    )
    if "incremental_pull_config" in value:
        import capo_customer_profiles.types.incremental_pull_config

        out["IncrementalPullConfig"] = (
            capo_customer_profiles.types.incremental_pull_config.serialize_json(
                value["incremental_pull_config"]
            )
        )
    import capo_customer_profiles.types.source_connector_properties

    out["SourceConnectorProperties"] = (
        capo_customer_profiles.types.source_connector_properties.serialize_json(
            value["source_connector_properties"]
        )
    )
    return out


def deserialize_json(data: dict) -> SourceFlowConfig:
    out: SourceFlowConfig = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorProfileName") is not None:
        out["connector_profile_name"] = data["ConnectorProfileName"]
    if data.get("ConnectorType") is not None:
        import capo_customer_profiles.types.source_connector_type

        out["connector_type"] = (
            capo_customer_profiles.types.source_connector_type.deserialize_json(
                data["ConnectorType"]
            )
        )
    else:
        import typing

        out["connector_type"] = typing.cast(
            "capo_customer_profiles.types.source_connector_type.SourceConnectorType", ""
        )
    if data.get("IncrementalPullConfig") is not None:
        import capo_customer_profiles.types.incremental_pull_config

        out["incremental_pull_config"] = (
            capo_customer_profiles.types.incremental_pull_config.deserialize_json(
                data["IncrementalPullConfig"]
            )
        )
    if data.get("SourceConnectorProperties") is not None:
        import capo_customer_profiles.types.source_connector_properties

        out["source_connector_properties"] = (
            capo_customer_profiles.types.source_connector_properties.deserialize_json(
                data["SourceConnectorProperties"]
            )
        )
    else:
        raise DeserializationError(
            "SourceFlowConfig.source_connector_properties required"
        )
    return out
