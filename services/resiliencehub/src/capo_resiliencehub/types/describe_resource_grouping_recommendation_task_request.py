"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DescribeResourceGroupingRecommendationTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.string255


class DescribeResourceGroupingRecommendationTaskRequest(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    grouping_id: NotRequired["capo_resiliencehub.types.string255.String255"]
    """<p>Identifier of the grouping recommendation task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeResourceGroupingRecommendationTaskRequest) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    if "grouping_id" in value:
        out["groupingId"] = value["grouping_id"]
    return out


def deserialize_json(data: dict) -> DescribeResourceGroupingRecommendationTaskRequest:
    out: DescribeResourceGroupingRecommendationTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "DescribeResourceGroupingRecommendationTaskRequest.app_arn required"
        )
    if data.get("groupingId") is not None:
        out["grouping_id"] = data["groupingId"]
    return out
