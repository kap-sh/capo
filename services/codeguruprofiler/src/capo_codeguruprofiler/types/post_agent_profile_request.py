"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#PostAgentProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.agent_profile
    import capo_codeguruprofiler.types.client_token
    import capo_codeguruprofiler.types.profiling_group_name


class PostAgentProfileRequest(TypedDict, closed=True):
    profiling_group_name: (
        "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
    )
    """<p> The name of the profiling group with the aggregated profile that receives the submitted profiling data. </p>"""
    agent_profile: "capo_codeguruprofiler.types.agent_profile.AgentProfile"
    """<p> The submitted profiling data. </p>"""
    profile_token: NotRequired["capo_codeguruprofiler.types.client_token.ClientToken"]
    """<p> Amazon CodeGuru Profiler uses this universally unique identifier (UUID) to prevent the accidental submission of duplicate profiling data if there are failures and retries. </p>"""
    content_type: "str"
    """<p> The format of the submitted profiling data. The format maps to the <code>Accept</code> and <code>Content-Type</code> headers of the HTTP request. You can specify one of the following: or the default . </p> <ul> <li> <p> <code>application/json</code> — standard JSON format </p> </li> <li> <p> <code>application/x-amzn-ion</code> — the Amazon Ion data format. For more information, see <a href="http://amzn.github.io/ion-docs/">Amazon Ion</a>. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostAgentProfileRequest) -> dict:
    out: dict = {}
    import capo_codeguruprofiler.types.agent_profile

    out["agentProfile"] = capo_codeguruprofiler.types.agent_profile.serialize_json(
        value["agent_profile"]
    )
    return out


def deserialize_json(data: dict) -> PostAgentProfileRequest:
    out: PostAgentProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("agentProfile") is not None:
        import capo_codeguruprofiler.types.agent_profile

        out["agent_profile"] = (
            capo_codeguruprofiler.types.agent_profile.deserialize_json(
                data["agentProfile"]
            )
        )
    else:
        raise DeserializationError("PostAgentProfileRequest.agent_profile required")
    return out
