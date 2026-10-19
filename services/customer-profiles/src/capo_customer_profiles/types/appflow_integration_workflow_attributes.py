"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AppflowIntegrationWorkflowAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.connector_profile_name
    import capo_customer_profiles.types.source_connector_type
    import capo_customer_profiles.types.string1_to255


class AppflowIntegrationWorkflowAttributes(TypedDict, closed=True):
    source_connector_type: (
        "capo_customer_profiles.types.source_connector_type.SourceConnectorType"
    )
    """<p>Specifies the source connector type, such as Salesforce, ServiceNow, and Marketo. Indicates source of ingestion.</p>"""
    connector_profile_name: (
        "capo_customer_profiles.types.connector_profile_name.ConnectorProfileName"
    )
    """<p>The name of the AppFlow connector profile used for ingestion.</p>"""
    role_arn: NotRequired["capo_customer_profiles.types.string1_to255.string1To255"]
    """<p>The Amazon Resource Name (ARN) of the IAM role. Customer Profiles assumes this role to create resources on your behalf as part of workflow execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppflowIntegrationWorkflowAttributes) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.source_connector_type

    out["SourceConnectorType"] = (
        capo_customer_profiles.types.source_connector_type.serialize_json(
            value["source_connector_type"]
        )
    )
    out["ConnectorProfileName"] = value["connector_profile_name"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> AppflowIntegrationWorkflowAttributes:
    out: AppflowIntegrationWorkflowAttributes = {}  # type: ignore[typeddict-item]
    if data.get("SourceConnectorType") is not None:
        import capo_customer_profiles.types.source_connector_type

        out["source_connector_type"] = (
            capo_customer_profiles.types.source_connector_type.deserialize_json(
                data["SourceConnectorType"]
            )
        )
    else:
        import typing

        out["source_connector_type"] = typing.cast(
            "capo_customer_profiles.types.source_connector_type.SourceConnectorType", ""
        )
    if data.get("ConnectorProfileName") is not None:
        out["connector_profile_name"] = data["ConnectorProfileName"]
    else:
        out["connector_profile_name"] = ""
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    return out
