"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListRecommendationTemplatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.boolean_optional
    import capo_resiliencehub.types.entity_name
    import capo_resiliencehub.types.max_results
    import capo_resiliencehub.types.next_token
    import capo_resiliencehub.types.recommendation_template_status_list


class ListRecommendationTemplatesRequest(TypedDict, closed=True):
    assessment_arn: NotRequired["capo_resiliencehub.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    reverse_order: NotRequired[
        "capo_resiliencehub.types.boolean_optional.BooleanOptional"
    ]
    """<p>The default is to sort by ascending <b>startTime</b>. To sort by descending <b>startTime</b>, set reverseOrder to <code>true</code>.</p>"""
    status: NotRequired[
        "capo_resiliencehub.types.recommendation_template_status_list.RecommendationTemplateStatusList"
    ]
    """<p>Status of the action.</p>"""
    recommendation_template_arn: NotRequired["capo_resiliencehub.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for a recommendation template.</p>"""
    name: NotRequired["capo_resiliencehub.types.entity_name.EntityName"]
    """<p>The name for one of the listed recommendation templates.</p>"""
    next_token: NotRequired["capo_resiliencehub.types.next_token.NextToken"]
    """<p>Null, or the token from a previous call to get the next set of results.</p>"""
    max_results: NotRequired["capo_resiliencehub.types.max_results.MaxResults"]
    """<p>Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationTemplatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRecommendationTemplatesRequest:
    out: ListRecommendationTemplatesRequest = {}  # type: ignore[typeddict-item]
    return out
