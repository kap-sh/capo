"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicNullFilter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.boolean
    import capo_quicksight.types.null_filter_type
    import capo_quicksight.types.topic_singular_filter_constant


class TopicNullFilter(TypedDict, closed=True):
    null_filter_type: NotRequired[
        "capo_quicksight.types.null_filter_type.NullFilterType"
    ]
    """<p>The type of the null filter. Valid values for this type are <code>NULLS_ONLY</code>, <code>NON_NULLS_ONLY</code>, and <code>ALL_VALUES</code>.</p>"""
    constant: NotRequired[
        "capo_quicksight.types.topic_singular_filter_constant.TopicSingularFilterConstant"
    ]
    inverse: "capo_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that indicates if the filter is inverse.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicNullFilter) -> dict:
    out: dict = {}
    if "null_filter_type" in value:
        import capo_quicksight.types.null_filter_type

        out["NullFilterType"] = capo_quicksight.types.null_filter_type.serialize_json(
            value["null_filter_type"]
        )
    if "constant" in value:
        import capo_quicksight.types.topic_singular_filter_constant

        out["Constant"] = (
            capo_quicksight.types.topic_singular_filter_constant.serialize_json(
                value["constant"]
            )
        )
    out["Inverse"] = value.get("inverse", False)
    return out


def deserialize_json(data: dict) -> TopicNullFilter:
    out: TopicNullFilter = {}  # type: ignore[typeddict-item]
    if data.get("NullFilterType") is not None:
        import capo_quicksight.types.null_filter_type

        out["null_filter_type"] = (
            capo_quicksight.types.null_filter_type.deserialize_json(
                data["NullFilterType"]
            )
        )
    if data.get("Constant") is not None:
        import capo_quicksight.types.topic_singular_filter_constant

        out["constant"] = (
            capo_quicksight.types.topic_singular_filter_constant.deserialize_json(
                data["Constant"]
            )
        )
    if data.get("Inverse") is not None:
        out["inverse"] = data["Inverse"]
    else:
        out["inverse"] = False
    return out


def redact_sensitive(value: TopicNullFilter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "constant" in value:
        out["constant"] = "*** Sensitive Data Redacted ***"
    return out
