"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TagFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.tag_filter_key
    import capo_cloudwatch_logs.types.tag_filter_values


class TagFilter(TypedDict, closed=True):
    key: "capo_cloudwatch_logs.types.tag_filter_key.TagFilterKey"
    """<p>The tag key to filter on.</p>"""
    values: NotRequired["capo_cloudwatch_logs.types.tag_filter_values.TagFilterValues"]
    """<p>An optional list of tag values to filter on.</p> <ul> <li> <p>If you specify a filter that contains more than one value for a key, the response returns log groups that match any of the specified values for that key.</p> </li> <li> <p>If you don't specify values, the response returns all log groups that are tagged with that key, with any or no value.</p> </li> <li> <p>Use <code>*</code> for wildcard matching. For example, <code>prod*</code> matches values that start with <code>prod</code>.</p> </li> <li> <p>Use <code>!</code> as a prefix for negation. For example, <code>!prod</code> matches values that are not <code>prod</code>.</p> </li> <li> <p>Exact matching and negation are case-sensitive. Wildcard matching is case-insensitive.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagFilter) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "values" in value:
        import capo_cloudwatch_logs.types.tag_filter_values

        out["values"] = (
            capo_cloudwatch_logs.types.tag_filter_values.serialize_aws_json_1_1(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagFilter:
    out: TagFilter = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("values") is not None:
        import capo_cloudwatch_logs.types.tag_filter_values

        out["values"] = (
            capo_cloudwatch_logs.types.tag_filter_values.deserialize_aws_json_1_1(
                data["values"]
            )
        )
    return out
