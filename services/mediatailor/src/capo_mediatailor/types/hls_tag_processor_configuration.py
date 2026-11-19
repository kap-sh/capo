"""Generated from Smithy shape ``com.amazonaws.mediatailor#HlsTagProcessorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.runtime_type
    import capo_mediatailor.types.tag_filter_list


class HlsTagProcessorConfiguration(TypedDict, closed=True):
    runtime: "capo_mediatailor.types.runtime_type.RuntimeType"
    """<p>The expression language used to evaluate expressions in the function configuration. The only supported value is <code>JSONATA</code>.</p>"""
    output: NotRequired["capo_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>A map of output bindings that MediaTailor evaluates for each HLS tag that matches <code>TagFilter</code> and, when specified, passes <code>RunCondition</code>. The required <code>tag</code> binding must return exactly one tag action: <code>$updateTag</code>, <code>$removeTag</code>, or <code>$passthroughTag</code>. Optional <code>player_params.&lt;name&gt;</code> bindings write strings, numbers, or booleans that persist for the player session. Optional <code>temp.&lt;name&gt;</code> bindings hold any JSON value for the current invocation and are not persisted. For more information about expression syntax, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-jsonata.html">JSONata expression reference</a> in the <i>MediaTailor User Guide</i>.</p>"""
    tag_filter: "capo_mediatailor.types.tag_filter_list.TagFilterList"
    """<p>A list of HLS tag names that trigger function evaluation. Specify <code>["EXT-X-DATERANGE"]</code>.</p>"""
    run_condition: NotRequired["capo_mediatailor.types.__string.__string"]
    """JSONata expression that must evaluate to true for the processor to run."""


# --- restJson1 ser/de ---
def serialize_json(value: HlsTagProcessorConfiguration) -> dict:
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
    import capo_mediatailor.types.tag_filter_list

    out["TagFilter"] = capo_mediatailor.types.tag_filter_list.serialize_json(
        value["tag_filter"]
    )
    if "run_condition" in value:
        out["RunCondition"] = value["run_condition"]
    return out


def deserialize_json(data: dict) -> HlsTagProcessorConfiguration:
    out: HlsTagProcessorConfiguration = {}  # type: ignore[typeddict-item]
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
    if data.get("TagFilter") is not None:
        import capo_mediatailor.types.tag_filter_list

        out["tag_filter"] = capo_mediatailor.types.tag_filter_list.deserialize_json(
            data["TagFilter"]
        )
    else:
        out["tag_filter"] = []
    if data.get("RunCondition") is not None:
        out["run_condition"] = data["RunCondition"]
    return out
