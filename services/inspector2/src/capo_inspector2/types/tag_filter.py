"""Generated from Smithy shape ``com.amazonaws.inspector2#TagFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.tag_comparison


class TagFilter(TypedDict, closed=True):
    comparison: "capo_inspector2.types.tag_comparison.TagComparison"
    """<p>The tag filter comparison value.</p>"""
    key: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The tag filter key.</p>"""
    value: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The tag filter value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagFilter) -> dict:
    out: dict = {}
    import capo_inspector2.types.tag_comparison

    out["comparison"] = capo_inspector2.types.tag_comparison.serialize_json(
        value["comparison"]
    )
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> TagFilter:
    out: TagFilter = {}  # type: ignore[typeddict-item]
    if data.get("comparison") is not None:
        import capo_inspector2.types.tag_comparison

        out["comparison"] = capo_inspector2.types.tag_comparison.deserialize_json(
            data["comparison"]
        )
    else:
        import typing

        out["comparison"] = typing.cast(
            "capo_inspector2.types.tag_comparison.TagComparison", ""
        )
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
