"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AcceptResourceGroupingRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.accept_grouping_recommendation_entries
    import capo_resiliencehub.types.arn


class AcceptResourceGroupingRecommendationsRequest(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    entries: "capo_resiliencehub.types.accept_grouping_recommendation_entries.AcceptGroupingRecommendationEntries"
    """<p>List of resource grouping recommendations you want to include in your application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptResourceGroupingRecommendationsRequest) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    import capo_resiliencehub.types.accept_grouping_recommendation_entries

    out["entries"] = (
        capo_resiliencehub.types.accept_grouping_recommendation_entries.serialize_json(
            value["entries"]
        )
    )
    return out


def deserialize_json(data: dict) -> AcceptResourceGroupingRecommendationsRequest:
    out: AcceptResourceGroupingRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "AcceptResourceGroupingRecommendationsRequest.app_arn required"
        )
    if data.get("entries") is not None:
        import capo_resiliencehub.types.accept_grouping_recommendation_entries

        out["entries"] = (
            capo_resiliencehub.types.accept_grouping_recommendation_entries.deserialize_json(
                data["entries"]
            )
        )
    else:
        raise DeserializationError(
            "AcceptResourceGroupingRecommendationsRequest.entries required"
        )
    return out
