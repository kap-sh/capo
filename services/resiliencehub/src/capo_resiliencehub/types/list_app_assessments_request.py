"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListAppAssessmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.assessment_invoker
    import capo_resiliencehub.types.assessment_status_list
    import capo_resiliencehub.types.boolean_optional
    import capo_resiliencehub.types.compliance_status
    import capo_resiliencehub.types.entity_name
    import capo_resiliencehub.types.max_results
    import capo_resiliencehub.types.next_token


class ListAppAssessmentsRequest(TypedDict, closed=True):
    app_arn: NotRequired["capo_resiliencehub.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    assessment_name: NotRequired["capo_resiliencehub.types.entity_name.EntityName"]
    """<p>The name for the assessment.</p>"""
    assessment_status: NotRequired[
        "capo_resiliencehub.types.assessment_status_list.AssessmentStatusList"
    ]
    """<p>The current status of the assessment for the resiliency policy.</p>"""
    compliance_status: NotRequired[
        "capo_resiliencehub.types.compliance_status.ComplianceStatus"
    ]
    """<p>The current status of compliance for the resiliency policy.</p>"""
    invoker: NotRequired[
        "capo_resiliencehub.types.assessment_invoker.AssessmentInvoker"
    ]
    """<p>Specifies the entity that invoked a specific assessment, either a <code>User</code> or the <code>System</code>.</p>"""
    reverse_order: NotRequired[
        "capo_resiliencehub.types.boolean_optional.BooleanOptional"
    ]
    """<p>The default is to sort by ascending <b>startTime</b>. To sort by descending <b>startTime</b>, set reverseOrder to <code>true</code>.</p>"""
    next_token: NotRequired["capo_resiliencehub.types.next_token.NextToken"]
    """<p>Null, or the token from a previous call to get the next set of results.</p>"""
    max_results: NotRequired["capo_resiliencehub.types.max_results.MaxResults"]
    """<p>Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppAssessmentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAppAssessmentsRequest:
    out: ListAppAssessmentsRequest = {}  # type: ignore[typeddict-item]
    return out
