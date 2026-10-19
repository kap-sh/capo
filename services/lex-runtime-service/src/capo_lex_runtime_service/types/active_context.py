"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#ActiveContext``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_lex_runtime_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_runtime_service.types.active_context_name
    import capo_lex_runtime_service.types.active_context_parameters_map
    import capo_lex_runtime_service.types.active_context_time_to_live


class ActiveContext(TypedDict, closed=True):
    name: "capo_lex_runtime_service.types.active_context_name.ActiveContextName"
    """<p>The name of the context.</p>"""
    time_to_live: "capo_lex_runtime_service.types.active_context_time_to_live.ActiveContextTimeToLive"
    """<p>The length of time or number of turns that a context remains active.</p>"""
    parameters: "capo_lex_runtime_service.types.active_context_parameters_map.ActiveContextParametersMap"
    """<p>State variables for the current context. You can use these values as default values for slots in subsequent events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActiveContext) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_lex_runtime_service.types.active_context_time_to_live

    out["timeToLive"] = (
        capo_lex_runtime_service.types.active_context_time_to_live.serialize_json(
            value["time_to_live"]
        )
    )
    import capo_lex_runtime_service.types.active_context_parameters_map

    out["parameters"] = (
        capo_lex_runtime_service.types.active_context_parameters_map.serialize_json(
            value["parameters"]
        )
    )
    return out


def deserialize_json(data: dict) -> ActiveContext:
    out: ActiveContext = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("timeToLive") is not None:
        import capo_lex_runtime_service.types.active_context_time_to_live

        out["time_to_live"] = (
            capo_lex_runtime_service.types.active_context_time_to_live.deserialize_json(
                data["timeToLive"]
            )
        )
    else:
        raise DeserializationError("ActiveContext.time_to_live required")
    if data.get("parameters") is not None:
        import capo_lex_runtime_service.types.active_context_parameters_map

        out["parameters"] = (
            capo_lex_runtime_service.types.active_context_parameters_map.deserialize_json(
                data["parameters"]
            )
        )
    else:
        out["parameters"] = {}
    return out


def redact_sensitive(value: ActiveContext) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "parameters" in value:
        import capo_lex_runtime_service.types.active_context_parameters_map

        out["parameters"] = (
            capo_lex_runtime_service.types.active_context_parameters_map.redact_sensitive(
                value["parameters"]
            )
        )
    return out
