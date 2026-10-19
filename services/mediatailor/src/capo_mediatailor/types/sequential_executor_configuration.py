"""Generated from Smithy shape ``com.amazonaws.mediatailor#SequentialExecutorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__integer
    import capo_mediatailor.types.__list_of_functions_ref
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.runtime_type


class SequentialExecutorConfiguration(TypedDict, closed=True):
    runtime: "capo_mediatailor.types.runtime_type.RuntimeType"
    """<p>The expression language used to evaluate expressions in the function configuration. Set this to <code>JSONata</code>.</p>"""
    output: NotRequired["capo_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>An optional map of output bindings that controls which bindings the sequence commits to the session state after all steps complete. If omitted, MediaTailor commits all accumulated output bindings from all child steps.</p>"""
    function_list: "capo_mediatailor.types.__list_of_functions_ref.__listOfFunctionsRef"
    """<p>An ordered list of 1 to 10 steps. Each step specifies a child function to execute and an optional run condition expression that controls whether the step runs. MediaTailor executes steps in order, passing data between steps through temporary data.</p>"""
    timeout_milliseconds: "capo_mediatailor.types.__integer.__integer"
    """<p>The maximum time, in milliseconds, for the entire sequence to complete. This timeout covers all steps, including any HTTP calls made by child functions. If the sequence exceeds this timeout, MediaTailor discards all output from the sequence and proceeds with default behavior.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SequentialExecutorConfiguration) -> dict:
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
    import capo_mediatailor.types.__list_of_functions_ref

    out["FunctionList"] = capo_mediatailor.types.__list_of_functions_ref.serialize_json(
        value["function_list"]
    )
    out["TimeoutMilliseconds"] = value["timeout_milliseconds"]
    return out


def deserialize_json(data: dict) -> SequentialExecutorConfiguration:
    out: SequentialExecutorConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Runtime") is not None:
        import capo_mediatailor.types.runtime_type

        out["runtime"] = capo_mediatailor.types.runtime_type.deserialize_json(
            data["Runtime"]
        )
    else:
        import typing

        out["runtime"] = typing.cast(
            "capo_mediatailor.types.runtime_type.RuntimeType", ""
        )
    if data.get("Output") is not None:
        import capo_mediatailor.types.__map_of__string

        out["output"] = capo_mediatailor.types.__map_of__string.deserialize_json(
            data["Output"]
        )
    if data.get("FunctionList") is not None:
        import capo_mediatailor.types.__list_of_functions_ref

        out["function_list"] = (
            capo_mediatailor.types.__list_of_functions_ref.deserialize_json(
                data["FunctionList"]
            )
        )
    else:
        out["function_list"] = []
    if data.get("TimeoutMilliseconds") is not None:
        out["timeout_milliseconds"] = data["TimeoutMilliseconds"]
    else:
        out["timeout_milliseconds"] = 0
    return out
