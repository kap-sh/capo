"""Generated from Smithy shape ``com.amazonaws.devopsagent#RemoteAgentSigV4AuthorizationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.role_arn
    import capo_devops_agent.types.sig_v4_region


class RemoteAgentSigV4AuthorizationConfig(TypedDict, closed=True):
    region: "capo_devops_agent.types.sig_v4_region.SigV4Region"
    service: "str"
    """<p>The AWS service name for SigV4 signing.</p>"""
    role_arn: NotRequired["capo_devops_agent.types.role_arn.RoleArn"]


# --- restJson1 ser/de ---
def serialize_json(value: RemoteAgentSigV4AuthorizationConfig) -> dict:
    out: dict = {}
    out["region"] = value["region"]
    out["service"] = value["service"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> RemoteAgentSigV4AuthorizationConfig:
    out: RemoteAgentSigV4AuthorizationConfig = {}  # type: ignore[typeddict-item]
    if data.get("region") is not None:
        out["region"] = data["region"]
    else:
        out["region"] = ""
    if data.get("service") is not None:
        out["service"] = data["service"]
    else:
        out["service"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    return out
