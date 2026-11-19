"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DescribeComponentConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.component_configuration
    import capo_application_insights.types.monitor
    import capo_application_insights.types.tier


class DescribeComponentConfigurationResponse(TypedDict, closed=True):
    monitor: NotRequired["capo_application_insights.types.monitor.Monitor"]
    """<p>Indicates whether the application component is monitored.</p>"""
    tier: NotRequired["capo_application_insights.types.tier.Tier"]
    """<p>The tier of the application component. Supported tiers include <code>DOT_NET_CORE</code>, <code>DOT_NET_WORKER</code>, <code>DOT_NET_WEB</code>, <code>SQL_SERVER</code>, and <code>DEFAULT</code> </p>"""
    component_configuration: NotRequired[
        "capo_application_insights.types.component_configuration.ComponentConfiguration"
    ]
    """<p>The configuration settings of the component. The value is the escaped JSON of the configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeComponentConfigurationResponse) -> dict:
    out: dict = {}
    if "monitor" in value:
        out["Monitor"] = value["monitor"]
    if "tier" in value:
        import capo_application_insights.types.tier

        out["Tier"] = capo_application_insights.types.tier.serialize_aws_json_1_1(
            value["tier"]
        )
    if "component_configuration" in value:
        out["ComponentConfiguration"] = value["component_configuration"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeComponentConfigurationResponse:
    out: DescribeComponentConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Monitor") is not None:
        out["monitor"] = data["Monitor"]
    if data.get("Tier") is not None:
        import capo_application_insights.types.tier

        out["tier"] = capo_application_insights.types.tier.deserialize_aws_json_1_1(
            data["Tier"]
        )
    if data.get("ComponentConfiguration") is not None:
        out["component_configuration"] = data["ComponentConfiguration"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeComponentConfigurationResponse) -> dict:
    out: dict = {}
    if "monitor" in value:
        out["Monitor"] = value["monitor"]
    if "tier" in value:
        import capo_application_insights.types.tier

        out["Tier"] = capo_application_insights.types.tier.serialize_cbor(value["tier"])
    if "component_configuration" in value:
        out["ComponentConfiguration"] = value["component_configuration"]
    return out


def deserialize_cbor(data: dict) -> DescribeComponentConfigurationResponse:
    out: DescribeComponentConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Monitor") is not None:
        out["monitor"] = data["Monitor"]
    if data.get("Tier") is not None:
        import capo_application_insights.types.tier

        out["tier"] = capo_application_insights.types.tier.deserialize_cbor(
            data["Tier"]
        )
    if data.get("ComponentConfiguration") is not None:
        out["component_configuration"] = data["ComponentConfiguration"]
    return out
