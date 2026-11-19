"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FlowOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.age
    import capo_network_firewall.types.flow_filters


class FlowOperation(TypedDict, closed=True):
    minimum_flow_age_in_seconds: NotRequired["capo_network_firewall.types.age.Age"]
    """<p>The reqested <code>FlowOperation</code> ignores flows with an age (in seconds) lower than <code>MinimumFlowAgeInSeconds</code>. You provide this for start commands.</p>"""
    flow_filters: NotRequired["capo_network_firewall.types.flow_filters.FlowFilters"]
    """<p>Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FlowOperation) -> dict:
    out: dict = {}
    if "minimum_flow_age_in_seconds" in value:
        out["MinimumFlowAgeInSeconds"] = value["minimum_flow_age_in_seconds"]
    if "flow_filters" in value:
        import capo_network_firewall.types.flow_filters

        out["FlowFilters"] = (
            capo_network_firewall.types.flow_filters.serialize_aws_json_1_0(
                value["flow_filters"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FlowOperation:
    out: FlowOperation = {}  # type: ignore[typeddict-item]
    if data.get("MinimumFlowAgeInSeconds") is not None:
        out["minimum_flow_age_in_seconds"] = data["MinimumFlowAgeInSeconds"]
    if data.get("FlowFilters") is not None:
        import capo_network_firewall.types.flow_filters

        out["flow_filters"] = (
            capo_network_firewall.types.flow_filters.deserialize_aws_json_1_0(
                data["FlowFilters"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FlowOperation) -> dict:
    out: dict = {}
    if "minimum_flow_age_in_seconds" in value:
        out["MinimumFlowAgeInSeconds"] = value["minimum_flow_age_in_seconds"]
    if "flow_filters" in value:
        import capo_network_firewall.types.flow_filters

        out["FlowFilters"] = capo_network_firewall.types.flow_filters.serialize_cbor(
            value["flow_filters"]
        )
    return out


def deserialize_cbor(data: dict) -> FlowOperation:
    out: FlowOperation = {}  # type: ignore[typeddict-item]
    if data.get("MinimumFlowAgeInSeconds") is not None:
        out["minimum_flow_age_in_seconds"] = data["MinimumFlowAgeInSeconds"]
    if data.get("FlowFilters") is not None:
        import capo_network_firewall.types.flow_filters

        out["flow_filters"] = capo_network_firewall.types.flow_filters.deserialize_cbor(
            data["FlowFilters"]
        )
    return out
