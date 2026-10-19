"""Generated from Smithy shape ``com.amazonaws.inspector2#Connector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_inspector2.types.aws_config_connector_arn
    import capo_inspector2.types.azure_region_list
    import capo_inspector2.types.azure_scope_configuration
    import capo_inspector2.types.connector_arn
    import capo_inspector2.types.connector_cloud_provider
    import capo_inspector2.types.connector_description
    import capo_inspector2.types.connector_health
    import capo_inspector2.types.connector_name
    import capo_inspector2.types.connector_tag_map
    import capo_inspector2.types.enablement_status


class Connector(TypedDict, closed=True):
    connector_arn: "capo_inspector2.types.connector_arn.ConnectorArn"
    """<p>The Amazon Resource Name (ARN) of the connector.</p>"""
    name: NotRequired["capo_inspector2.types.connector_name.ConnectorName"]
    """<p>The name of the connector.</p>"""
    description: NotRequired[
        "capo_inspector2.types.connector_description.ConnectorDescription"
    ]
    """<p>A description of the connector.</p>"""
    provider: "capo_inspector2.types.connector_cloud_provider.ConnectorCloudProvider"
    """<p>The cloud provider for the connector.</p>"""
    enablement_status: NotRequired[
        "capo_inspector2.types.enablement_status.EnablementStatus"
    ]
    """<p>The enablement status of the connector, which indicates whether the connector is active and scanning resources.</p>"""
    enablement_status_reason: NotRequired["str"]
    """<p>Additional information about the current enablement status of the connector.</p>"""
    health: NotRequired["capo_inspector2.types.connector_health.ConnectorHealth"]
    """<p>The health of the connector, which indicates whether Amazon Inspector can reach and scan the connected resources.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time when the connector was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The date and time when the connector was last updated.</p>"""
    azure_regions: NotRequired[
        "capo_inspector2.types.azure_region_list.AzureRegionList"
    ]
    """<p>The Azure regions configured for the connector.</p>"""
    aws_config_connector_arn: NotRequired[
        "capo_inspector2.types.aws_config_connector_arn.AwsConfigConnectorArn"
    ]
    """<p>The ARN of the Amazon Web Services Config connector associated with this connector.</p>"""
    scope_configuration: NotRequired[
        "capo_inspector2.types.azure_scope_configuration.AzureScopeConfiguration"
    ]
    """<p>The Azure scope configuration for the connector.</p>"""
    tags: NotRequired["capo_inspector2.types.connector_tag_map.ConnectorTagMap"]
    """<p>The tags associated with the connector.</p>"""
    auto_install_vm_scanner: NotRequired["bool"]
    """<p>Specifies whether the VM scanner is automatically installed on connected resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Connector) -> dict:
    out: dict = {}
    out["connectorArn"] = value["connector_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_inspector2.types.connector_cloud_provider

    out["provider"] = capo_inspector2.types.connector_cloud_provider.serialize_json(
        value["provider"]
    )
    if "enablement_status" in value:
        import capo_inspector2.types.enablement_status

        out["enablementStatus"] = (
            capo_inspector2.types.enablement_status.serialize_json(
                value["enablement_status"]
            )
        )
    if "enablement_status_reason" in value:
        out["enablementStatusReason"] = value["enablement_status_reason"]
    if "health" in value:
        import capo_inspector2.types.connector_health

        out["health"] = capo_inspector2.types.connector_health.serialize_json(
            value["health"]
        )
    import capo_inspector2._protocol.serialize

    out["createdAt"] = capo_inspector2._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    import capo_inspector2._protocol.serialize

    out["updatedAt"] = capo_inspector2._protocol.serialize.fmt_date_time(
        value["updated_at"]
    )
    if "azure_regions" in value:
        import capo_inspector2.types.azure_region_list

        out["azureRegions"] = capo_inspector2.types.azure_region_list.serialize_json(
            value["azure_regions"]
        )
    if "aws_config_connector_arn" in value:
        out["awsConfigConnectorArn"] = value["aws_config_connector_arn"]
    if "scope_configuration" in value:
        import capo_inspector2.types.azure_scope_configuration

        out["scopeConfiguration"] = (
            capo_inspector2.types.azure_scope_configuration.serialize_json(
                value["scope_configuration"]
            )
        )
    if "tags" in value:
        import capo_inspector2.types.connector_tag_map

        out["tags"] = capo_inspector2.types.connector_tag_map.serialize_json(
            value["tags"]
        )
    if "auto_install_vm_scanner" in value:
        out["autoInstallVMScanner"] = value["auto_install_vm_scanner"]
    return out


def deserialize_json(data: dict) -> Connector:
    out: Connector = {}  # type: ignore[typeddict-item]
    if data.get("connectorArn") is not None:
        out["connector_arn"] = data["connectorArn"]
    else:
        out["connector_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("provider") is not None:
        import capo_inspector2.types.connector_cloud_provider

        out["provider"] = (
            capo_inspector2.types.connector_cloud_provider.deserialize_json(
                data["provider"]
            )
        )
    else:
        import typing

        out["provider"] = typing.cast(
            "capo_inspector2.types.connector_cloud_provider.ConnectorCloudProvider", ""
        )
    if data.get("enablementStatus") is not None:
        import capo_inspector2.types.enablement_status

        out["enablement_status"] = (
            capo_inspector2.types.enablement_status.deserialize_json(
                data["enablementStatus"]
            )
        )
    if data.get("enablementStatusReason") is not None:
        out["enablement_status_reason"] = data["enablementStatusReason"]
    if data.get("health") is not None:
        import capo_inspector2.types.connector_health

        out["health"] = capo_inspector2.types.connector_health.deserialize_json(
            data["health"]
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("azureRegions") is not None:
        import capo_inspector2.types.azure_region_list

        out["azure_regions"] = capo_inspector2.types.azure_region_list.deserialize_json(
            data["azureRegions"]
        )
    if data.get("awsConfigConnectorArn") is not None:
        out["aws_config_connector_arn"] = data["awsConfigConnectorArn"]
    if data.get("scopeConfiguration") is not None:
        import capo_inspector2.types.azure_scope_configuration

        out["scope_configuration"] = (
            capo_inspector2.types.azure_scope_configuration.deserialize_json(
                data["scopeConfiguration"]
            )
        )
    if data.get("tags") is not None:
        import capo_inspector2.types.connector_tag_map

        out["tags"] = capo_inspector2.types.connector_tag_map.deserialize_json(
            data["tags"]
        )
    if data.get("autoInstallVMScanner") is not None:
        out["auto_install_vm_scanner"] = data["autoInstallVMScanner"]
    return out
