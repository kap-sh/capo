"""Generated from Smithy shape ``com.amazonaws.securityhub#MapFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.map_filter_comparison
    import capo_securityhub.types.non_empty_string


class MapFilter(TypedDict, closed=True):
    key: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The key of the map filter. For example, for <code>ResourceTags</code>, <code>Key</code> identifies the name of the tag. For <code>UserDefinedFields</code>, <code>Key</code> is the name of the field.</p>"""
    value: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The value for the key in the map filter. Filter values are case sensitive. For example, one of the values for a tag called <code>Department</code> might be <code>Security</code>. If you provide <code>security</code> as the filter value, then there's no match.</p>"""
    comparison: NotRequired[
        "capo_securityhub.types.map_filter_comparison.MapFilterComparison"
    ]
    """<p>The condition to apply to the key value when filtering Security Hub CSPM findings with a map filter.</p> <p>To search for values that have the filter value, use one of the following comparison operators:</p> <ul> <li> <p>To search for values that include the filter value, use <code>CONTAINS</code>. For example, for the <code>ResourceTags</code> field, the filter <code>Department CONTAINS Security</code> matches findings that include the value <code>Security</code> for the <code>Department</code> tag. In the same example, a finding with a value of <code>Security team</code> for the <code>Department</code> tag is a match.</p> </li> <li> <p>To search for values that exactly match the filter value, use <code>EQUALS</code>. For example, for the <code>ResourceTags</code> field, the filter <code>Department EQUALS Security</code> matches findings that have the value <code>Security</code> for the <code>Department</code> tag.</p> </li> </ul> <p> <code>CONTAINS</code> and <code>EQUALS</code> filters on the same field are joined by <code>OR</code>. A finding matches if it matches any one of those filters. For example, the filters <code>Department CONTAINS Security OR Department CONTAINS Finance</code> match a finding that includes either <code>Security</code>, <code>Finance</code>, or both values.</p> <p>To search for values that don't have the filter value, use one of the following comparison operators:</p> <ul> <li> <p>To search for values that exclude the filter value, use <code>NOT_CONTAINS</code>. For example, for the <code>ResourceTags</code> field, the filter <code>Department NOT_CONTAINS Finance</code> matches findings that exclude the value <code>Finance</code> for the <code>Department</code> tag.</p> </li> <li> <p>To search for values other than the filter value, use <code>NOT_EQUALS</code>. For example, for the <code>ResourceTags</code> field, the filter <code>Department NOT_EQUALS Finance</code> matches findings that don’t have the value <code>Finance</code> for the <code>Department</code> tag.</p> </li> </ul> <p> <code>NOT_CONTAINS</code> and <code>NOT_EQUALS</code> filters on the same field are joined by <code>AND</code>. A finding matches only if it matches all of those filters. For example, the filters <code>Department NOT_CONTAINS Security AND Department NOT_CONTAINS Finance</code> match a finding that excludes both the <code>Security</code> and <code>Finance</code> values.</p> <p> <code>CONTAINS</code> filters can only be used with other <code>CONTAINS</code> filters. <code>NOT_CONTAINS</code> filters can only be used with other <code>NOT_CONTAINS</code> filters.</p> <p>You can’t have both a <code>CONTAINS</code> filter and a <code>NOT_CONTAINS</code> filter on the same field. Similarly, you can’t have both an <code>EQUALS</code> filter and a <code>NOT_EQUALS</code> filter on the same field. Combining filters in this way returns an error. </p> <p> <code>CONTAINS</code> and <code>NOT_CONTAINS</code> operators can be used only with automation rules. For more information, see <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html">Automation rules</a> in the <i>Security Hub CSPM User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MapFilter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    if "comparison" in value:
        import capo_securityhub.types.map_filter_comparison

        out["Comparison"] = capo_securityhub.types.map_filter_comparison.serialize_json(
            value["comparison"]
        )
    return out


def deserialize_json(data: dict) -> MapFilter:
    out: MapFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("Comparison") is not None:
        import capo_securityhub.types.map_filter_comparison

        out["comparison"] = (
            capo_securityhub.types.map_filter_comparison.deserialize_json(
                data["Comparison"]
            )
        )
    return out
