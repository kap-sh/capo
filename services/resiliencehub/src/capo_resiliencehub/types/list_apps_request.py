"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListAppsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.boolean_optional
    import capo_resiliencehub.types.entity_name
    import capo_resiliencehub.types.max_results
    import capo_resiliencehub.types.next_token
    import capo_resiliencehub.types.time_stamp


class ListAppsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_resiliencehub.types.next_token.NextToken"]
    """<p>Null, or the token from a previous call to get the next set of results.</p>"""
    max_results: NotRequired["capo_resiliencehub.types.max_results.MaxResults"]
    """<p>Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>"""
    name: NotRequired["capo_resiliencehub.types.entity_name.EntityName"]
    """<p>The name for the one of the listed applications.</p>"""
    app_arn: NotRequired["capo_resiliencehub.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    from_last_assessment_time: NotRequired[
        "capo_resiliencehub.types.time_stamp.TimeStamp"
    ]
    """<p>Lower limit of the range that is used to filter applications based on their last assessment times.</p>"""
    to_last_assessment_time: NotRequired[
        "capo_resiliencehub.types.time_stamp.TimeStamp"
    ]
    """<p>Upper limit of the range that is used to filter the applications based on their last assessment times.</p>"""
    reverse_order: NotRequired[
        "capo_resiliencehub.types.boolean_optional.BooleanOptional"
    ]
    """<p>The application list is sorted based on the values of <code>lastAppComplianceEvaluationTime</code> field. By default, application list is sorted in ascending order. To sort the application list in descending order, set this field to <code>True</code>.</p>"""
    aws_application_arn: NotRequired["capo_resiliencehub.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of Resource Groups group that is integrated with an AppRegistry application. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAppsRequest:
    out: ListAppsRequest = {}  # type: ignore[typeddict-item]
    return out
