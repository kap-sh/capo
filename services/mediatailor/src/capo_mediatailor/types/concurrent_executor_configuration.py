"""Generated from Smithy shape ``com.amazonaws.mediatailor#ConcurrentExecutorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__integer
    import capo_mediatailor.types.__list_of_functions_ref
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.runtime_type


class ConcurrentExecutorConfiguration(TypedDict, closed=True):
    runtime: "capo_mediatailor.types.runtime_type.RuntimeType"
    """<p>The expression language used to evaluate expressions in the function configuration. Set this to <code>JSONata</code>.</p>"""
    output: "capo_mediatailor.types.__map_of__string.__mapOf__string"
    """<p>A map of output bindings that controls which bindings the executor commits to the session state after all child functions complete. Each key is a namespaced output path, and each value is an expression that MediaTailor evaluates against the combined results of the child functions.</p>"""
    function_list: "capo_mediatailor.types.__list_of_functions_ref.__listOfFunctionsRef"
    """<p>The list of child functions that MediaTailor runs in parallel. Each entry specifies a child function to execute and an optional run condition expression that controls whether the function runs.</p>"""
    timeout_milliseconds: "capo_mediatailor.types.__integer.__integer"
    """<p>The maximum time, in milliseconds, for all child functions to complete. This timeout covers every function in the list, including any HTTP calls the child functions make. If the executor exceeds this timeout, MediaTailor discards all output from the executor and proceeds with default behavior.</p>"""
    max_concurrency: "capo_mediatailor.types.__integer.__integer"
    """<p>The maximum number of child functions that MediaTailor runs simultaneously. When the list contains more functions than <code>MaxConcurrency</code>, MediaTailor starts additional functions as running ones complete, so that no more than <code>MaxConcurrency</code> functions run at the same time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConcurrentExecutorConfiguration) -> dict:
    out: dict = {}
    import capo_mediatailor.types.runtime_type

    out["Runtime"] = capo_mediatailor.types.runtime_type.serialize_json(
        value["runtime"]
    )
    import capo_mediatailor.types.__map_of__string

    out["Output"] = capo_mediatailor.types.__map_of__string.serialize_json(
        value["output"]
    )
    import capo_mediatailor.types.__list_of_functions_ref

    out["FunctionList"] = capo_mediatailor.types.__list_of_functions_ref.serialize_json(
        value["function_list"]
    )
    out["TimeoutMilliseconds"] = value["timeout_milliseconds"]
    out["MaxConcurrency"] = value["max_concurrency"]
    return out


def deserialize_json(data: dict) -> ConcurrentExecutorConfiguration:
    out: ConcurrentExecutorConfiguration = {}  # type: ignore[typeddict-item]
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
    else:
        out["output"] = {}
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
    if data.get("MaxConcurrency") is not None:
        out["max_concurrency"] = data["MaxConcurrency"]
    else:
        out["max_concurrency"] = 0
    return out
