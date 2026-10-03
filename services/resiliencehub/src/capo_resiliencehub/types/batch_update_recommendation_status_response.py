"""Generated from Smithy shape ``com.amazonaws.resiliencehub#BatchUpdateRecommendationStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.batch_update_recommendation_status_failed_entries
    import capo_resiliencehub.types.batch_update_recommendation_status_successful_entries


class BatchUpdateRecommendationStatusResponse(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    successful_entries: "capo_resiliencehub.types.batch_update_recommendation_status_successful_entries.BatchUpdateRecommendationStatusSuccessfulEntries"
    """<p>A list of items that were included or excluded.</p>"""
    failed_entries: "capo_resiliencehub.types.batch_update_recommendation_status_failed_entries.BatchUpdateRecommendationStatusFailedEntries"
    """<p>A list of items with error details about each item, which could not be included or excluded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateRecommendationStatusResponse) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    import capo_resiliencehub.types.batch_update_recommendation_status_successful_entries

    out["successfulEntries"] = (
        capo_resiliencehub.types.batch_update_recommendation_status_successful_entries.serialize_json(
            value["successful_entries"]
        )
    )
    import capo_resiliencehub.types.batch_update_recommendation_status_failed_entries

    out["failedEntries"] = (
        capo_resiliencehub.types.batch_update_recommendation_status_failed_entries.serialize_json(
            value["failed_entries"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateRecommendationStatusResponse:
    out: BatchUpdateRecommendationStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "BatchUpdateRecommendationStatusResponse.app_arn required"
        )
    if data.get("successfulEntries") is not None:
        import capo_resiliencehub.types.batch_update_recommendation_status_successful_entries

        out["successful_entries"] = (
            capo_resiliencehub.types.batch_update_recommendation_status_successful_entries.deserialize_json(
                data["successfulEntries"]
            )
        )
    else:
        raise DeserializationError(
            "BatchUpdateRecommendationStatusResponse.successful_entries required"
        )
    if data.get("failedEntries") is not None:
        import capo_resiliencehub.types.batch_update_recommendation_status_failed_entries

        out["failed_entries"] = (
            capo_resiliencehub.types.batch_update_recommendation_status_failed_entries.deserialize_json(
                data["failedEntries"]
            )
        )
    else:
        raise DeserializationError(
            "BatchUpdateRecommendationStatusResponse.failed_entries required"
        )
    return out
