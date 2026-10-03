"""Generated from Smithy shape ``com.amazonaws.datasync#FilterRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.filter_type
    import capo_datasync.types.filter_value


class FilterRule(TypedDict, closed=True):
    filter_type: NotRequired["capo_datasync.types.filter_type.FilterType"]
    """<p>The type of filter rule to apply. DataSync only supports the SIMPLE_PATTERN rule type.</p>"""
    value: NotRequired["capo_datasync.types.filter_value.FilterValue"]
    """<p>A single filter string that consists of the patterns to include or exclude. The patterns are delimited by "|" (that is, a pipe), for example: <code>/folder1|/folder2</code> </p> <p> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterRule) -> dict:
    out: dict = {}
    if "filter_type" in value:
        import capo_datasync.types.filter_type

        out["FilterType"] = capo_datasync.types.filter_type.serialize_aws_json_1_1(
            value["filter_type"]
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FilterRule:
    out: FilterRule = {}  # type: ignore[typeddict-item]
    if data.get("FilterType") is not None:
        import capo_datasync.types.filter_type

        out["filter_type"] = capo_datasync.types.filter_type.deserialize_aws_json_1_1(
            data["FilterType"]
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
