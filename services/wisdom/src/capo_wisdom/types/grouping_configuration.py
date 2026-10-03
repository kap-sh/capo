"""Generated from Smithy shape ``com.amazonaws.wisdom#GroupingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wisdom.types.grouping_criteria
    import capo_wisdom.types.grouping_values


class GroupingConfiguration(TypedDict, closed=True):
    criteria: NotRequired["capo_wisdom.types.grouping_criteria.GroupingCriteria"]
    """<p>The criteria used for grouping Wisdom users.</p> <p>The following is the list of supported criteria values.</p> <ul> <li> <p> <code>RoutingProfileArn</code>: Grouping the users by their <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfile.html">Amazon Connect routing profile ARN</a>. User should have <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchRoutingProfiles.html">SearchRoutingProfile</a> and <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeRoutingProfile.html">DescribeRoutingProfile</a> permissions when setting criteria to this value.</p> </li> </ul>"""
    values: NotRequired["capo_wisdom.types.grouping_values.GroupingValues"]
    """<p>The list of values that define different groups of Wisdom users.</p> <ul> <li> <p>When setting <code>criteria</code> to <code>RoutingProfileArn</code>, you need to provide a list of ARNs of <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfile.html">Amazon Connect routing profiles</a> as values of this parameter.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupingConfiguration) -> dict:
    out: dict = {}
    if "criteria" in value:
        out["criteria"] = value["criteria"]
    if "values" in value:
        import capo_wisdom.types.grouping_values

        out["values"] = capo_wisdom.types.grouping_values.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> GroupingConfiguration:
    out: GroupingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("criteria") is not None:
        out["criteria"] = data["criteria"]
    if data.get("values") is not None:
        import capo_wisdom.types.grouping_values

        out["values"] = capo_wisdom.types.grouping_values.deserialize_json(
            data["values"]
        )
    return out
