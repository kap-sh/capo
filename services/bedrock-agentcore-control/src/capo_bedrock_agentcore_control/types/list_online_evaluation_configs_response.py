"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListOnlineEvaluationConfigsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.online_evaluation_config_summary_list


class ListOnlineEvaluationConfigsResponse(TypedDict, closed=True):
    online_evaluation_configs: "capo_bedrock_agentcore_control.types.online_evaluation_config_summary_list.OnlineEvaluationConfigSummaryList"
    """<p> The list of online evaluation configuration summaries containing basic information about each configuration. </p>"""
    next_token: NotRequired["str"]
    """<p> The pagination token to use in a subsequent request to retrieve the next page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOnlineEvaluationConfigsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.online_evaluation_config_summary_list

    out["onlineEvaluationConfigs"] = (
        capo_bedrock_agentcore_control.types.online_evaluation_config_summary_list.serialize_json(
            value["online_evaluation_configs"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOnlineEvaluationConfigsResponse:
    out: ListOnlineEvaluationConfigsResponse = {}  # type: ignore[typeddict-item]
    if data.get("onlineEvaluationConfigs") is not None:
        import capo_bedrock_agentcore_control.types.online_evaluation_config_summary_list

        out["online_evaluation_configs"] = (
            capo_bedrock_agentcore_control.types.online_evaluation_config_summary_list.deserialize_json(
                data["onlineEvaluationConfigs"]
            )
        )
    else:
        raise DeserializationError(
            "ListOnlineEvaluationConfigsResponse.online_evaluation_configs required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListOnlineEvaluationConfigsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "online_evaluation_configs" in value:
        import capo_bedrock_agentcore_control.types.online_evaluation_config_summary_list

        out["online_evaluation_configs"] = (
            capo_bedrock_agentcore_control.types.online_evaluation_config_summary_list.redact_sensitive(
                value["online_evaluation_configs"]
            )
        )
    return out
