"""Generated from Smithy shape ``com.amazonaws.mediatailor#CustomOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.runtime_type


class CustomOutputConfiguration(TypedDict, closed=True):
    runtime: "capo_mediatailor.types.runtime_type.RuntimeType"
    """<p>The expression language used to evaluate expressions in the function configuration. Set this to <code>JSONata</code>.</p>"""
    output: NotRequired["capo_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>A map of output bindings. Each key is a namespaced output path (such as <code>player_params.device_type</code> or <code>temp.variant</code>), and each value is an expression that MediaTailor evaluates at runtime against the current session state. For more information about expression syntax, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-jsonata.html">JSONata expression reference</a> in the <i>MediaTailor User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomOutputConfiguration) -> dict:
    out: dict = {}
    import capo_mediatailor.types.runtime_type

    out["Runtime"] = capo_mediatailor.types.runtime_type.serialize_json(
        value["runtime"]
    )
    if "output" in value:
        import capo_mediatailor.types.__map_of__string

        out["Output"] = capo_mediatailor.types.__map_of__string.serialize_json(
            value["output"]
        )
    return out


def deserialize_json(data: dict) -> CustomOutputConfiguration:
    out: CustomOutputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Runtime") is not None:
        import capo_mediatailor.types.runtime_type

        out["runtime"] = capo_mediatailor.types.runtime_type.deserialize_json(
            data["Runtime"]
        )
    else:
        raise DeserializationError("CustomOutputConfiguration.runtime required")
    if data.get("Output") is not None:
        import capo_mediatailor.types.__map_of__string

        out["output"] = capo_mediatailor.types.__map_of__string.deserialize_json(
            data["Output"]
        )
    return out
