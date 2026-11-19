"""Generated from Smithy shape ``com.amazonaws.configservice#ConnectorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.amazon_resource_name
    import capo_config_service.types.azure_tenant_identifier
    import capo_config_service.types.connector_name
    import capo_config_service.types.date
    import capo_config_service.types.gcp_organization_id
    import capo_config_service.types.gcp_service_account_email
    import capo_config_service.types.provider


class ConnectorSummary(TypedDict, closed=True):
    arn: "capo_config_service.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the connector.</p>"""
    name: "capo_config_service.types.connector_name.ConnectorName"
    """<p>The name of the connector.</p>"""
    provider: "capo_config_service.types.provider.Provider"
    """<p>The third-party cloud service provider. Valid values:</p> <ul> <li> <p> <code>AZURE</code> – The connector is for Microsoft Azure</p> </li> <li> <p> <code>GCP</code> – The connector is for Google Cloud</p> </li> </ul>"""
    tenant_identifier: NotRequired[
        "capo_config_service.types.azure_tenant_identifier.AzureTenantIdentifier"
    ]
    """<p>The Azure tenant identifier for the connector. Returned only for Azure connectors.</p>"""
    gcp_organization_id: NotRequired[
        "capo_config_service.types.gcp_organization_id.GcpOrganizationId"
    ]
    """<p>The Google Cloud organization ID for the connector. Returned only for Google Cloud connectors.</p>"""
    service_account_email: NotRequired[
        "capo_config_service.types.gcp_service_account_email.GcpServiceAccountEmail"
    ]
    """<p>The email address of the Google Cloud service account for the connector. Returned only for Google Cloud connectors.</p>"""
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
    if "tenant_identifier" in value:
        out["tenantIdentifier"] = value["tenant_identifier"]
    if "gcp_organization_id" in value:
        out["gcpOrganizationId"] = value["gcp_organization_id"]
    if "service_account_email" in value:
        out["serviceAccountEmail"] = value["service_account_email"]
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
    if data.get("gcpOrganizationId") is not None:
        out["gcp_organization_id"] = data["gcpOrganizationId"]
    if data.get("serviceAccountEmail") is not None:
        out["service_account_email"] = data["serviceAccountEmail"]
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
