"""Generated from Smithy shape ``com.amazonaws.securityhub#StringFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.string_filter_comparison


class StringFilter(TypedDict, closed=True):
    value: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is <code>Security Hub CSPM</code>. If you provide <code>security hub</code> as the filter value, there's no match.</p>"""
    comparison: NotRequired[
        "capo_securityhub.types.string_filter_comparison.StringFilterComparison"
    ]
    """<p>The condition to apply to a string value when filtering Security Hub CSPM findings.</p> <p>To search for values that have the filter value, use one of the following comparison operators:</p> <ul> <li> <p>To search for values that include the filter value, use <code>CONTAINS</code>. For example, the filter <code>Title CONTAINS CloudFront</code> matches findings that have a <code>Title</code> that includes the string CloudFront.</p> </li> <li> <p>To search for values that exactly match the filter value, use <code>EQUALS</code>. For example, the filter <code>AwsAccountId EQUALS 123456789012</code> only matches findings that have an account ID of <code>123456789012</code>.</p> </li> <li> <p>To search for values that start with the filter value, use <code>PREFIX</code>. For example, the filter <code>ResourceRegion PREFIX us</code> matches findings that have a <code>ResourceRegion</code> that starts with <code>us</code>. A <code>ResourceRegion</code> that starts with a different value, such as <code>af</code>, <code>ap</code>, or <code>ca</code>, doesn't match.</p> </li> </ul> <p> <code>CONTAINS</code>, <code>EQUALS</code>, and <code>PREFIX</code> filters on the same field are joined by <code>OR</code>. A finding matches if it matches any one of those filters. For example, the filters <code>Title CONTAINS CloudFront OR Title CONTAINS CloudWatch</code> match a finding that includes either <code>CloudFront</code>, <code>CloudWatch</code>, or both strings in the title.</p> <p>To search for values that don’t have the filter value, use one of the following comparison operators:</p> <ul> <li> <p>To search for values that exclude the filter value, use <code>NOT_CONTAINS</code>. For example, the filter <code>Title NOT_CONTAINS CloudFront</code> matches findings that have a <code>Title</code> that excludes the string CloudFront.</p> </li> <li> <p>To search for values other than the filter value, use <code>NOT_EQUALS</code>. For example, the filter <code>AwsAccountId NOT_EQUALS 123456789012</code> only matches findings that have an account ID other than <code>123456789012</code>.</p> </li> <li> <p>To search for values that don't start with the filter value, use <code>PREFIX_NOT_EQUALS</code>. For example, the filter <code>ResourceRegion PREFIX_NOT_EQUALS us</code> matches findings with a <code>ResourceRegion</code> that starts with a value other than <code>us</code>.</p> </li> </ul> <p> <code>NOT_CONTAINS</code>, <code>NOT_EQUALS</code>, and <code>PREFIX_NOT_EQUALS</code> filters on the same field are joined by <code>AND</code>. A finding matches only if it matches all of those filters. For example, the filters <code>Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch</code> match a finding that excludes both <code>CloudFront</code> and <code>CloudWatch</code> in the title.</p> <p>You can’t have both a <code>CONTAINS</code> filter and a <code>NOT_CONTAINS</code> filter on the same field. Similarly, you can't provide both an <code>EQUALS</code> filter and a <code>NOT_EQUALS</code> or <code>PREFIX_NOT_EQUALS</code> filter on the same field. Combining filters in this way returns an error. <code>CONTAINS</code> filters can only be used with other <code>CONTAINS</code> filters. <code>NOT_CONTAINS</code> filters can only be used with other <code>NOT_CONTAINS</code> filters. </p> <p>You can combine <code>PREFIX</code> filters with <code>NOT_EQUALS</code> or <code>PREFIX_NOT_EQUALS</code> filters for the same field. Security Hub CSPM first processes the <code>PREFIX</code> filters, and then the <code>NOT_EQUALS</code> or <code>PREFIX_NOT_EQUALS</code> filters.</p> <p>For example, for the following filters, Security Hub CSPM first identifies findings that have resource types that start with either <code>AwsIam</code> or <code>AwsEc2</code>. It then excludes findings that have a resource type of <code>AwsIamPolicy</code> and findings that have a resource type of <code>AwsEc2NetworkInterface</code>.</p> <ul> <li> <p> <code>ResourceType PREFIX AwsIam</code> </p> </li> <li> <p> <code>ResourceType PREFIX AwsEc2</code> </p> </li> <li> <p> <code>ResourceType NOT_EQUALS AwsIamPolicy</code> </p> </li> <li> <p> <code>ResourceType NOT_EQUALS AwsEc2NetworkInterface</code> </p> </li> </ul> <p>The <code>CONTAINS</code> operator works with automation rules V1 and V2. The <code>NOT_CONTAINS</code> operator works only with automation rules V1. The <code>CONTAINS_WORD</code> operator works only in the <code>GetFindingsV2</code>, <code>GetFindingStatisticsV2</code>, <code>GetResourcesV2</code>, and <code>GetResourcesStatisticsV2</code> APIs. For more information, see <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html">Automation rules</a> in the <i>Security Hub CSPM User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StringFilter) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "comparison" in value:
        import capo_securityhub.types.string_filter_comparison

        out["Comparison"] = (
            capo_securityhub.types.string_filter_comparison.serialize_json(
                value["comparison"]
            )
        )
    return out


def deserialize_json(data: dict) -> StringFilter:
    out: StringFilter = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("Comparison") is not None:
        import capo_securityhub.types.string_filter_comparison

        out["comparison"] = (
            capo_securityhub.types.string_filter_comparison.deserialize_json(
                data["Comparison"]
            )
        )
    return out
