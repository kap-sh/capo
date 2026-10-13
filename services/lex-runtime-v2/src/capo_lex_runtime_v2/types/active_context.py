"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#ActiveContext``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_lex_runtime_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.active_context_name
    import capo_lex_runtime_v2.types.active_context_parameters_map
    import capo_lex_runtime_v2.types.active_context_time_to_live


class ActiveContext(TypedDict, closed=True):
    name: "capo_lex_runtime_v2.types.active_context_name.ActiveContextName"
    """<p>The name of the context.</p>"""
    time_to_live: (
        "capo_lex_runtime_v2.types.active_context_time_to_live.ActiveContextTimeToLive"
    )
    """<p>Indicates the number of turns or seconds that the context is active. Once the time to live expires, the context is no longer returned in a response.</p>"""
    context_attributes: "capo_lex_runtime_v2.types.active_context_parameters_map.ActiveContextParametersMap"
    """<p>A list of contexts active for the request. A context can be activated when a previous intent is fulfilled, or by including the context in the request.</p> <p>If you don't specify a list of contexts, Amazon Lex V2 will use the current list of contexts for the session. If you specify an empty list, all contexts for the session are cleared. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActiveContext) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_lex_runtime_v2.types.active_context_time_to_live

    out["timeToLive"] = (
        capo_lex_runtime_v2.types.active_context_time_to_live.serialize_json(
            value["time_to_live"]
        )
    )
    import capo_lex_runtime_v2.types.active_context_parameters_map

    out["contextAttributes"] = (
        capo_lex_runtime_v2.types.active_context_parameters_map.serialize_json(
            value["context_attributes"]
        )
    )
    return out


def deserialize_json(data: dict) -> ActiveContext:
    out: ActiveContext = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ActiveContext.name required")
    if data.get("timeToLive") is not None:
        import capo_lex_runtime_v2.types.active_context_time_to_live

        out["time_to_live"] = (
            capo_lex_runtime_v2.types.active_context_time_to_live.deserialize_json(
                data["timeToLive"]
            )
        )
    else:
        raise DeserializationError("ActiveContext.time_to_live required")
    if data.get("contextAttributes") is not None:
        import capo_lex_runtime_v2.types.active_context_parameters_map

        out["context_attributes"] = (
            capo_lex_runtime_v2.types.active_context_parameters_map.deserialize_json(
                data["contextAttributes"]
            )
        )
    else:
        raise DeserializationError("ActiveContext.context_attributes required")
    return out


def redact_sensitive(value: ActiveContext) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "context_attributes" in value:
        import capo_lex_runtime_v2.types.active_context_parameters_map

        out["context_attributes"] = (
            capo_lex_runtime_v2.types.active_context_parameters_map.redact_sensitive(
                value["context_attributes"]
            )
        )
    return out
