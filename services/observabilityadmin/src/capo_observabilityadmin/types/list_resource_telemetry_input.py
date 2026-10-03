"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ListResourceTelemetryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.list_resource_telemetry_max_results
    import capo_observabilityadmin.types.next_token
    import capo_observabilityadmin.types.resource_identifier_prefix
    import capo_observabilityadmin.types.resource_types
    import capo_observabilityadmin.types.tag_map_input
    import capo_observabilityadmin.types.telemetry_configuration_state


class ListResourceTelemetryInput(TypedDict, closed=True):
    resource_identifier_prefix: NotRequired[
        "capo_observabilityadmin.types.resource_identifier_prefix.ResourceIdentifierPrefix"
    ]
    """<p> A string used to filter resources which have a <code>ResourceIdentifier</code> starting with the <code>ResourceIdentifierPrefix</code>. </p>"""
    resource_types: NotRequired[
        "capo_observabilityadmin.types.resource_types.ResourceTypes"
    ]
    """<p> A list of resource types used to filter resources supported by telemetry config. If this parameter is provided, the service returns the resources in the same order as specified in the request. Currently supported resource types for discovery are:</p> <ul> <li> <p> <code>AWS::EC2::Instance</code> </p> </li> <li> <p> <code>AWS::EC2::VPC</code> </p> </li> <li> <p> <code>AWS::Lambda::Function</code> </p> </li> <li> <p> <code>AWS::EKS::Cluster</code> </p> </li> <li> <p> <code>AWS::WAFv2::WebACL</code> </p> </li> <li> <p> <code>AWS::ElasticLoadBalancingV2::LoadBalancer</code> (Network Load Balancers only)</p> </li> </ul>"""
    telemetry_configuration_state: NotRequired[
        "capo_observabilityadmin.types.telemetry_configuration_state.TelemetryConfigurationState"
    ]
    """<p> A key-value pair to filter resources based on the telemetry type and the state of the telemetry configuration. The key is the telemetry type and the value is the state. </p>"""
    resource_tags: NotRequired[
        "capo_observabilityadmin.types.tag_map_input.TagMapInput"
    ]
    """<p> A key-value pair to filter resources based on tags associated with the resource. For more information about tags, see <a href="https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html">What are tags?</a> </p>"""
    max_results: NotRequired[
        "capo_observabilityadmin.types.list_resource_telemetry_max_results.ListResourceTelemetryMaxResults"
    ]
    """<p> A number field used to limit the number of results within the returned list. </p>"""
    next_token: NotRequired["capo_observabilityadmin.types.next_token.NextToken"]
    """<p> The token for the next set of items to return. A previous call generates this token. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourceTelemetryInput) -> dict:
    out: dict = {}
    if "resource_identifier_prefix" in value:
        out["ResourceIdentifierPrefix"] = value["resource_identifier_prefix"]
    if "resource_types" in value:
        import capo_observabilityadmin.types.resource_types

        out["ResourceTypes"] = (
            capo_observabilityadmin.types.resource_types.serialize_json(
                value["resource_types"]
            )
        )
    if "telemetry_configuration_state" in value:
        import capo_observabilityadmin.types.telemetry_configuration_state

        out["TelemetryConfigurationState"] = (
            capo_observabilityadmin.types.telemetry_configuration_state.serialize_json(
                value["telemetry_configuration_state"]
            )
        )
    if "resource_tags" in value:
        import capo_observabilityadmin.types.tag_map_input

        out["ResourceTags"] = (
            capo_observabilityadmin.types.tag_map_input.serialize_json(
                value["resource_tags"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourceTelemetryInput:
    out: ListResourceTelemetryInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceIdentifierPrefix") is not None:
        out["resource_identifier_prefix"] = data["ResourceIdentifierPrefix"]
    if data.get("ResourceTypes") is not None:
        import capo_observabilityadmin.types.resource_types

        out["resource_types"] = (
            capo_observabilityadmin.types.resource_types.deserialize_json(
                data["ResourceTypes"]
            )
        )
    if data.get("TelemetryConfigurationState") is not None:
        import capo_observabilityadmin.types.telemetry_configuration_state

        out["telemetry_configuration_state"] = (
            capo_observabilityadmin.types.telemetry_configuration_state.deserialize_json(
                data["TelemetryConfigurationState"]
            )
        )
    if data.get("ResourceTags") is not None:
        import capo_observabilityadmin.types.tag_map_input

        out["resource_tags"] = (
            capo_observabilityadmin.types.tag_map_input.deserialize_json(
                data["ResourceTags"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
