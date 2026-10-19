"""Generated from Smithy shape ``com.amazonaws.configservice#ConnectorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.amazon_resource_name
    import capo_config_service.types.azure_tenant_identifier
    import capo_config_service.types.connector_name
    import capo_config_service.types.date
    import capo_config_service.types.provider


class ConnectorSummary(TypedDict, closed=True):
    arn: "capo_config_service.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the connector.</p>"""
    name: "capo_config_service.types.connector_name.ConnectorName"
    """<p>The name of the connector.</p>"""
    provider: "capo_config_service.types.provider.Provider"
    """<p>The third-party cloud service provider. Currently, <code>AZURE</code> is supported.</p>"""
    tenant_identifier: (
        "capo_config_service.types.azure_tenant_identifier.AzureTenantIdentifier"
    )
    """<p>The Azure tenant identifier for the connector.</p>"""
    created_time: "capo_config_service.types.date.Date"
    """<p>The date and time that the connector was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import capo_config_service.types.provider

    out["provider"] = capo_config_service.types.provider.serialize_aws_json_1_1(
        value["provider"]
    )
    out["tenantIdentifier"] = value["tenant_identifier"]
    import capo_config_service.types.date

    out["createdTime"] = capo_config_service.types.date.serialize_aws_json_1_1(
        value["created_time"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectorSummary:
    out: ConnectorSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("provider") is not None:
        import capo_config_service.types.provider

        out["provider"] = capo_config_service.types.provider.deserialize_aws_json_1_1(
            data["provider"]
        )
    else:
        import typing

        out["provider"] = typing.cast("capo_config_service.types.provider.Provider", "")
    if data.get("tenantIdentifier") is not None:
        out["tenant_identifier"] = data["tenantIdentifier"]
    else:
        out["tenant_identifier"] = ""
    if data.get("createdTime") is not None:
        import capo_config_service.types.date

        out["created_time"] = capo_config_service.types.date.deserialize_aws_json_1_1(
            data["createdTime"]
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
