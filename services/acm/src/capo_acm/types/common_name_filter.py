"""Generated from Smithy shape ``com.amazonaws.acm#CommonNameFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_acm.types.comparison_operator
    import capo_acm.types.filter_string


class CommonNameFilter(TypedDict, closed=True):
    value: "capo_acm.types.filter_string.FilterString"
    """<p>The value to match against.</p>"""
    comparison_operator: "capo_acm.types.comparison_operator.ComparisonOperator"
    """<p>The comparison operator to use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommonNameFilter) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    import capo_acm.types.comparison_operator

    out["ComparisonOperator"] = (
        capo_acm.types.comparison_operator.serialize_aws_json_1_1(
            value["comparison_operator"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CommonNameFilter:
    out: CommonNameFilter = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    if data.get("ComparisonOperator") is not None:
        import capo_acm.types.comparison_operator

        out["comparison_operator"] = (
            capo_acm.types.comparison_operator.deserialize_aws_json_1_1(
                data["ComparisonOperator"]
            )
        )
    else:
        import typing

        out["comparison_operator"] = typing.cast(
            "capo_acm.types.comparison_operator.ComparisonOperator", ""
        )
    return out
