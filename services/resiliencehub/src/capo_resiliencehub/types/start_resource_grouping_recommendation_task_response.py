"""Generated from Smithy shape ``com.amazonaws.resiliencehub#StartResourceGroupingRecommendationTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.resources_grouping_rec_gen_status_type
    import capo_resiliencehub.types.string255
    import capo_resiliencehub.types.string500


class StartResourceGroupingRecommendationTaskResponse(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    grouping_id: "capo_resiliencehub.types.string255.String255"
    """<p>Identifier of the grouping recommendation task.</p>"""
    status: "capo_resiliencehub.types.resources_grouping_rec_gen_status_type.ResourcesGroupingRecGenStatusType"
    """<p>Status of the action.</p>"""
    error_message: NotRequired["capo_resiliencehub.types.string500.String500"]
    """<p>Error that occurred while executing a grouping recommendation task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartResourceGroupingRecommendationTaskResponse) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    out["groupingId"] = value["grouping_id"]
    import capo_resiliencehub.types.resources_grouping_rec_gen_status_type

    out["status"] = (
        capo_resiliencehub.types.resources_grouping_rec_gen_status_type.serialize_json(
            value["status"]
        )
    )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> StartResourceGroupingRecommendationTaskResponse:
    out: StartResourceGroupingRecommendationTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "StartResourceGroupingRecommendationTaskResponse.app_arn required"
        )
    if data.get("groupingId") is not None:
        out["grouping_id"] = data["groupingId"]
    else:
        raise DeserializationError(
            "StartResourceGroupingRecommendationTaskResponse.grouping_id required"
        )
    if data.get("status") is not None:
        import capo_resiliencehub.types.resources_grouping_rec_gen_status_type

        out["status"] = (
            capo_resiliencehub.types.resources_grouping_rec_gen_status_type.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "StartResourceGroupingRecommendationTaskResponse.status required"
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out
