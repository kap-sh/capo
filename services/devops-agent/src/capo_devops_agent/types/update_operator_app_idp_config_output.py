"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateOperatorAppIdpConfigOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.idp_auth_configuration


class UpdateOperatorAppIdpConfigOutput(TypedDict, closed=True):
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""
    idp: "capo_devops_agent.types.idp_auth_configuration.IdpAuthConfiguration"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOperatorAppIdpConfigOutput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    import capo_devops_agent.types.idp_auth_configuration

    out["idp"] = capo_devops_agent.types.idp_auth_configuration.serialize_json(
        value["idp"]
    )
    return out


def deserialize_json(data: dict) -> UpdateOperatorAppIdpConfigOutput:
    out: UpdateOperatorAppIdpConfigOutput = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("idp") is not None:
        import capo_devops_agent.types.idp_auth_configuration

        out["idp"] = capo_devops_agent.types.idp_auth_configuration.deserialize_json(
            data["idp"]
        )
    else:
        raise DeserializationError("UpdateOperatorAppIdpConfigOutput.idp required")
    return out
