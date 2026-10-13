"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ListEdgeAgentConfigurationsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.list_edge_agent_configurations_edge_config_list
    import capo_kinesis_video.types.next_token


class ListEdgeAgentConfigurationsOutput(TypedDict, closed=True):
    edge_configs: NotRequired[
        "capo_kinesis_video.types.list_edge_agent_configurations_edge_config_list.ListEdgeAgentConfigurationsEdgeConfigList"
    ]
    """<p>A description of a single stream's edge configuration.</p>"""
    next_token: NotRequired["capo_kinesis_video.types.next_token.NextToken"]
    """<p>If the response is truncated, the call returns this element with a given token. To get the next batch of edge configurations, use this token in your next request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEdgeAgentConfigurationsOutput) -> dict:
    out: dict = {}
    if "edge_configs" in value:
        import capo_kinesis_video.types.list_edge_agent_configurations_edge_config_list

        out["EdgeConfigs"] = (
            capo_kinesis_video.types.list_edge_agent_configurations_edge_config_list.serialize_json(
                value["edge_configs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEdgeAgentConfigurationsOutput:
    out: ListEdgeAgentConfigurationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("EdgeConfigs") is not None:
        import capo_kinesis_video.types.list_edge_agent_configurations_edge_config_list

        out["edge_configs"] = (
            capo_kinesis_video.types.list_edge_agent_configurations_edge_config_list.deserialize_json(
                data["EdgeConfigs"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListEdgeAgentConfigurationsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "edge_configs" in value:
        import capo_kinesis_video.types.list_edge_agent_configurations_edge_config_list

        out["edge_configs"] = (
            capo_kinesis_video.types.list_edge_agent_configurations_edge_config_list.redact_sensitive(
                value["edge_configs"]
            )
        )
    return out
