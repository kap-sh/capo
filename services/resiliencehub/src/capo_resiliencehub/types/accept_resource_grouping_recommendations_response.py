"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AcceptResourceGroupingRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.failed_grouping_recommendation_entries


class AcceptResourceGroupingRecommendationsResponse(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    failed_entries: "capo_resiliencehub.types.failed_grouping_recommendation_entries.FailedGroupingRecommendationEntries"
    """<p>List of resource grouping recommendations that could not be included in your application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptResourceGroupingRecommendationsResponse) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    import capo_resiliencehub.types.failed_grouping_recommendation_entries

    out["failedEntries"] = (
        capo_resiliencehub.types.failed_grouping_recommendation_entries.serialize_json(
            value["failed_entries"]
        )
    )
    return out


def deserialize_json(data: dict) -> AcceptResourceGroupingRecommendationsResponse:
    out: AcceptResourceGroupingRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "AcceptResourceGroupingRecommendationsResponse.app_arn required"
        )
    if data.get("failedEntries") is not None:
        import capo_resiliencehub.types.failed_grouping_recommendation_entries

        out["failed_entries"] = (
            capo_resiliencehub.types.failed_grouping_recommendation_entries.deserialize_json(
                data["failedEntries"]
            )
        )
    else:
        raise DeserializationError(
            "AcceptResourceGroupingRecommendationsResponse.failed_entries required"
        )
    return out
