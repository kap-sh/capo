"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeMetricCategoriesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.metric_category_list
    import capo_ec2.types.string


class DescribeMetricCategoriesResult(TypedDict, closed=True):
    metric_categories: NotRequired[
        "capo_ec2.types.metric_category_list.MetricCategoryList"
    ]
    """<p>Information about the metric categories.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeMetricCategoriesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "metric_categories" in value:
        import capo_ec2.types.metric_category_list

        capo_ec2.types.metric_category_list.serialize_ec2_query(
            value["metric_categories"], pairs, f"{key_prefix}MetricCategorySet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeMetricCategoriesResult:
    out: DescribeMetricCategoriesResult = {}  # type: ignore[typeddict-item]
    child_metric_categories = el.find("metricCategorySet")
    if child_metric_categories is not None:
        import capo_ec2.types.metric_category_list

        out["metric_categories"] = (
            capo_ec2.types.metric_category_list.deserialize_ec2_query(
                child_metric_categories
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
