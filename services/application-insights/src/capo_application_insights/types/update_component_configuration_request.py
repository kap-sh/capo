"""Generated from Smithy shape ``com.amazonaws.applicationinsights#UpdateComponentConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_insights.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_insights.types.auto_config_enabled
    import capo_application_insights.types.component_configuration
    import capo_application_insights.types.component_name
    import capo_application_insights.types.monitor
    import capo_application_insights.types.resource_group_name
    import capo_application_insights.types.tier


class UpdateComponentConfigurationRequest(TypedDict, closed=True):
    resource_group_name: (
        "capo_application_insights.types.resource_group_name.ResourceGroupName"
    )
    """<p>The name of the resource group.</p>"""
    component_name: "capo_application_insights.types.component_name.ComponentName"
    """<p>The name of the component.</p>"""
    monitor: NotRequired["capo_application_insights.types.monitor.Monitor"]
    """<p>Indicates whether the application component is monitored.</p>"""
    tier: NotRequired["capo_application_insights.types.tier.Tier"]
    """<p>The tier of the application component.</p>"""
    component_configuration: NotRequired[
        "capo_application_insights.types.component_configuration.ComponentConfiguration"
    ]
    """<p>The configuration settings of the component. The value is the escaped JSON of the configuration. For more information about the JSON format, see <a href="https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/working-with-json.html">Working with JSON</a>. You can send a request to <code>DescribeComponentConfigurationRecommendation</code> to see the recommended configuration for a component. For the complete format of the component configuration file, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-config.html">Component Configuration</a>.</p>"""
    auto_config_enabled: NotRequired[
        "capo_application_insights.types.auto_config_enabled.AutoConfigEnabled"
    ]
    """<p> Automatically configures the component by applying the recommended configurations. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateComponentConfigurationRequest) -> dict:
    out: dict = {}
    out["ResourceGroupName"] = value["resource_group_name"]
    out["ComponentName"] = value["component_name"]
    if "monitor" in value:
        out["Monitor"] = value["monitor"]
    if "tier" in value:
        import capo_application_insights.types.tier

        out["Tier"] = capo_application_insights.types.tier.serialize_aws_json_1_1(
            value["tier"]
        )
    if "component_configuration" in value:
        out["ComponentConfiguration"] = value["component_configuration"]
    if "auto_config_enabled" in value:
        out["AutoConfigEnabled"] = value["auto_config_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateComponentConfigurationRequest:
    out: UpdateComponentConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    else:
        raise DeserializationError(
            "UpdateComponentConfigurationRequest.resource_group_name required"
        )
    if data.get("ComponentName") is not None:
        out["component_name"] = data["ComponentName"]
    else:
        raise DeserializationError(
            "UpdateComponentConfigurationRequest.component_name required"
        )
    if data.get("Monitor") is not None:
        out["monitor"] = data["Monitor"]
    if data.get("Tier") is not None:
        import capo_application_insights.types.tier

        out["tier"] = capo_application_insights.types.tier.deserialize_aws_json_1_1(
            data["Tier"]
        )
    if data.get("ComponentConfiguration") is not None:
        out["component_configuration"] = data["ComponentConfiguration"]
    if data.get("AutoConfigEnabled") is not None:
        out["auto_config_enabled"] = data["AutoConfigEnabled"]
    return out
