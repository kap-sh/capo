"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#BatchDeleteAgentError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.agent_id
    import capo_application_discovery_service.types.delete_agent_error_code
    import capo_application_discovery_service.types.string


class BatchDeleteAgentError(TypedDict, closed=True):
    agent_id: "capo_application_discovery_service.types.agent_id.AgentId"
    """<p> The ID of the agent or data collector to delete. </p>"""
    error_message: "capo_application_discovery_service.types.string.String"
    """<p> The description of the error that occurred for the delete failed agent. </p>"""
    error_code: "capo_application_discovery_service.types.delete_agent_error_code.DeleteAgentErrorCode"
    """<p> The type of error that occurred for the delete failed agent. Valid status are: AGENT_IN_USE | NOT_FOUND | INTERNAL_SERVER_ERROR. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteAgentError) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    out["errorMessage"] = value["error_message"]
    import capo_application_discovery_service.types.delete_agent_error_code

    out["errorCode"] = (
        capo_application_discovery_service.types.delete_agent_error_code.serialize_aws_json_1_1(
            value["error_code"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteAgentError:
    out: BatchDeleteAgentError = {}  # type: ignore[typeddict-item]
    if data.get("agentId") is not None:
        out["agent_id"] = data["agentId"]
    else:
        out["agent_id"] = ""
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        out["error_message"] = ""
    if data.get("errorCode") is not None:
        import capo_application_discovery_service.types.delete_agent_error_code

        out["error_code"] = (
            capo_application_discovery_service.types.delete_agent_error_code.deserialize_aws_json_1_1(
                data["errorCode"]
            )
        )
    else:
        import typing

        out["error_code"] = typing.cast(
            "capo_application_discovery_service.types.delete_agent_error_code.DeleteAgentErrorCode",
            "",
        )
    return out
