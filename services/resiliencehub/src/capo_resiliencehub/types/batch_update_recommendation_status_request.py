"""Generated from Smithy shape ``com.amazonaws.resiliencehub#BatchUpdateRecommendationStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.update_recommendation_status_request_entries


class BatchUpdateRecommendationStatusRequest(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    request_entries: "capo_resiliencehub.types.update_recommendation_status_request_entries.UpdateRecommendationStatusRequestEntries"
    """<p>Defines the list of operational recommendations that need to be included or excluded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateRecommendationStatusRequest) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    import capo_resiliencehub.types.update_recommendation_status_request_entries

    out["requestEntries"] = (
        capo_resiliencehub.types.update_recommendation_status_request_entries.serialize_json(
            value["request_entries"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateRecommendationStatusRequest:
    out: BatchUpdateRecommendationStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "BatchUpdateRecommendationStatusRequest.app_arn required"
        )
    if data.get("requestEntries") is not None:
        import capo_resiliencehub.types.update_recommendation_status_request_entries

        out["request_entries"] = (
            capo_resiliencehub.types.update_recommendation_status_request_entries.deserialize_json(
                data["requestEntries"]
            )
        )
    else:
        raise DeserializationError(
            "BatchUpdateRecommendationStatusRequest.request_entries required"
        )
    return out
