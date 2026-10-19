"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteOnlineEvaluationConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.online_evaluation_config_arn
    import capo_bedrock_agentcore_control.types.online_evaluation_config_id
    import capo_bedrock_agentcore_control.types.online_evaluation_config_status


class DeleteOnlineEvaluationConfigResponse(TypedDict, closed=True):
    online_evaluation_config_arn: "capo_bedrock_agentcore_control.types.online_evaluation_config_arn.OnlineEvaluationConfigArn"
    """<p> The Amazon Resource Name (ARN) of the deleted online evaluation configuration. </p>"""
    online_evaluation_config_id: "capo_bedrock_agentcore_control.types.online_evaluation_config_id.OnlineEvaluationConfigId"
    """<p> The unique identifier of the deleted online evaluation configuration. </p>"""
    status: "capo_bedrock_agentcore_control.types.online_evaluation_config_status.OnlineEvaluationConfigStatus"
    """<p> The status of the online evaluation configuration deletion operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteOnlineEvaluationConfigResponse) -> dict:
    out: dict = {}
    out["onlineEvaluationConfigArn"] = value["online_evaluation_config_arn"]
    out["onlineEvaluationConfigId"] = value["online_evaluation_config_id"]
    import capo_bedrock_agentcore_control.types.online_evaluation_config_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.online_evaluation_config_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteOnlineEvaluationConfigResponse:
    out: DeleteOnlineEvaluationConfigResponse = {}  # type: ignore[typeddict-item]
    if data.get("onlineEvaluationConfigArn") is not None:
        out["online_evaluation_config_arn"] = data["onlineEvaluationConfigArn"]
    else:
        out["online_evaluation_config_arn"] = ""
    if data.get("onlineEvaluationConfigId") is not None:
        out["online_evaluation_config_id"] = data["onlineEvaluationConfigId"]
    else:
        out["online_evaluation_config_id"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.online_evaluation_config_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.online_evaluation_config_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.online_evaluation_config_status.OnlineEvaluationConfigStatus",
            "",
        )
    return out
