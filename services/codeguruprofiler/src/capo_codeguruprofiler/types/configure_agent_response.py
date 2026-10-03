"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#ConfigureAgentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.agent_configuration


class ConfigureAgentResponse(TypedDict, closed=True):
    configuration: "capo_codeguruprofiler.types.agent_configuration.AgentConfiguration"
    """<p> An <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AgentConfiguration.html"> <code>AgentConfiguration</code> </a> object that specifies if an agent profiles or not and for how long to return profiling data. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigureAgentResponse) -> dict:
    out: dict = {}
    import capo_codeguruprofiler.types.agent_configuration

    out["configuration"] = (
        capo_codeguruprofiler.types.agent_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConfigureAgentResponse:
    out: ConfigureAgentResponse = {}  # type: ignore[typeddict-item]
    if data.get("configuration") is not None:
        import capo_codeguruprofiler.types.agent_configuration

        out["configuration"] = (
            capo_codeguruprofiler.types.agent_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("ConfigureAgentResponse.configuration required")
    return out
