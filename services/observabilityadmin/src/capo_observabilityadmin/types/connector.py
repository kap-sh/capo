"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#Connector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.connector_configuration
    import capo_observabilityadmin.types.connector_name
    import capo_observabilityadmin.types.connector_provider
    import capo_observabilityadmin.types.resource_arn
    import capo_observabilityadmin.types.role_arn


class Connector(TypedDict, closed=True):
    arn: "capo_observabilityadmin.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the connector.</p>"""
    provider: "capo_observabilityadmin.types.connector_provider.ConnectorProvider"
    """<p>The cloud provider that the connector connects to.</p>"""
    connector_configuration: (
        "capo_observabilityadmin.types.connector_configuration.ConnectorConfiguration"
    )
    """<p>The configuration for connecting to the third-party cloud provider.</p>"""
    role_arn: "capo_observabilityadmin.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) role that CloudWatch assumes to obtain credentials for the third-party cloud provider.</p>"""
    name: NotRequired["capo_observabilityadmin.types.connector_name.ConnectorName"]
    """<p>The name of the connector.</p>"""
    created_time_stamp: NotRequired["int"]
    """<p>The time when the connector was created, in milliseconds since the Unix epoch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Connector) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import capo_observabilityadmin.types.connector_provider

    out["Provider"] = capo_observabilityadmin.types.connector_provider.serialize_json(
        value["provider"]
    )
    import capo_observabilityadmin.types.connector_configuration

    out["ConnectorConfiguration"] = (
        capo_observabilityadmin.types.connector_configuration.serialize_json(
            value["connector_configuration"]
        )
    )
    out["RoleArn"] = value["role_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "created_time_stamp" in value:
        out["CreatedTimeStamp"] = value["created_time_stamp"]
    return out


def deserialize_json(data: dict) -> Connector:
    out: Connector = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Provider") is not None:
        import capo_observabilityadmin.types.connector_provider

        out["provider"] = (
            capo_observabilityadmin.types.connector_provider.deserialize_json(
                data["Provider"]
            )
        )
    else:
        import typing

        out["provider"] = typing.cast(
            "capo_observabilityadmin.types.connector_provider.ConnectorProvider", ""
        )
    if data.get("ConnectorConfiguration") is not None:
        import capo_observabilityadmin.types.connector_configuration

        out["connector_configuration"] = (
            capo_observabilityadmin.types.connector_configuration.deserialize_json(
                data["ConnectorConfiguration"]
            )
        )
    else:
        out["connector_configuration"] = {"$unknown": {"name": ""}}
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("CreatedTimeStamp") is not None:
        out["created_time_stamp"] = data["CreatedTimeStamp"]
    return out
