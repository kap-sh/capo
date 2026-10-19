"""Generated from Smithy shape ``com.amazonaws.devopsagent#EnableOperatorAppOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.iam_auth_configuration
    import capo_devops_agent.types.idc_auth_configuration
    import capo_devops_agent.types.idp_auth_configuration
    import capo_devops_agent.types.operator_app_url


class EnableOperatorAppOutput(TypedDict, closed=True):
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""
    operator_app_url: NotRequired[
        "capo_devops_agent.types.operator_app_url.OperatorAppUrl"
    ]
    """<p>The URL for operators to access the Operator App</p>"""
    iam: NotRequired[
        "capo_devops_agent.types.iam_auth_configuration.IamAuthConfiguration"
    ]
    idc: NotRequired[
        "capo_devops_agent.types.idc_auth_configuration.IdcAuthConfiguration"
    ]
    idp: NotRequired[
        "capo_devops_agent.types.idp_auth_configuration.IdpAuthConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: EnableOperatorAppOutput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    if "operator_app_url" in value:
        out["operatorAppUrl"] = value["operator_app_url"]
    if "iam" in value:
        import capo_devops_agent.types.iam_auth_configuration

        out["iam"] = capo_devops_agent.types.iam_auth_configuration.serialize_json(
            value["iam"]
        )
    if "idc" in value:
        import capo_devops_agent.types.idc_auth_configuration

        out["idc"] = capo_devops_agent.types.idc_auth_configuration.serialize_json(
            value["idc"]
        )
    if "idp" in value:
        import capo_devops_agent.types.idp_auth_configuration

        out["idp"] = capo_devops_agent.types.idp_auth_configuration.serialize_json(
            value["idp"]
        )
    return out


def deserialize_json(data: dict) -> EnableOperatorAppOutput:
    out: EnableOperatorAppOutput = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("operatorAppUrl") is not None:
        out["operator_app_url"] = data["operatorAppUrl"]
    if data.get("iam") is not None:
        import capo_devops_agent.types.iam_auth_configuration

        out["iam"] = capo_devops_agent.types.iam_auth_configuration.deserialize_json(
            data["iam"]
        )
    if data.get("idc") is not None:
        import capo_devops_agent.types.idc_auth_configuration

        out["idc"] = capo_devops_agent.types.idc_auth_configuration.deserialize_json(
            data["idc"]
        )
    if data.get("idp") is not None:
        import capo_devops_agent.types.idp_auth_configuration

        out["idp"] = capo_devops_agent.types.idp_auth_configuration.deserialize_json(
            data["idp"]
        )
    return out
