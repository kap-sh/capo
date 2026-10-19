"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#GetDependencyInsightsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.dependency_insights_error_code
    import capo_resiliencehubv2.types.dependency_insights_list
    import capo_resiliencehubv2.types.dependency_insights_status


class GetDependencyInsightsResponse(TypedDict, closed=True):
    overview: NotRequired["str"]
    """<p>A summary of the dependency insights for the service. This field is not returned until the status is COMPLETED.</p>"""
    insights: NotRequired[
        "capo_resiliencehubv2.types.dependency_insights_list.DependencyInsightsList"
    ]
    """<p>The list of dependency insights generated for the service. This field is not returned until the status is COMPLETED.</p>"""
    status: (
        "capo_resiliencehubv2.types.dependency_insights_status.DependencyInsightsStatus"
    )
    """<p>The status of the dependency insights generation. Valid values:</p> <ul> <li> <p>IN_PROGRESS - Insights generation is in progress.</p> </li> <li> <p>COMPLETED - Insights generation completed successfully.</p> </li> <li> <p>FAILED - Insights generation failed. See errorCode and errorMessage for details.</p> </li> </ul>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the dependency insights were generated.</p>"""
    error_code: NotRequired[
        "capo_resiliencehubv2.types.dependency_insights_error_code.DependencyInsightsErrorCode"
    ]
    """<p>The error code returned when insights generation failed. Valid values:</p> <ul> <li> <p>INSUFFICIENT_DATA - There was not enough dependency data to generate insights.</p> </li> <li> <p>LLM_GENERATION_FAILED - The insights could not be generated.</p> </li> <li> <p>INTERNAL_ERROR - An internal error occurred while generating insights.</p> </li> </ul>"""
    error_message: NotRequired["str"]
    """<p>A message describing why insights generation failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDependencyInsightsResponse) -> dict:
    out: dict = {}
    if "overview" in value:
        out["overview"] = value["overview"]
    if "insights" in value:
        import capo_resiliencehubv2.types.dependency_insights_list

        out["insights"] = (
            capo_resiliencehubv2.types.dependency_insights_list.serialize_json(
                value["insights"]
            )
        )
    import capo_resiliencehubv2.types.dependency_insights_status

    out["status"] = (
        capo_resiliencehubv2.types.dependency_insights_status.serialize_json(
            value["status"]
        )
    )
    if "created_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["createdAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "error_code" in value:
        import capo_resiliencehubv2.types.dependency_insights_error_code

        out["errorCode"] = (
            capo_resiliencehubv2.types.dependency_insights_error_code.serialize_json(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> GetDependencyInsightsResponse:
    out: GetDependencyInsightsResponse = {}  # type: ignore[typeddict-item]
    if data.get("overview") is not None:
        out["overview"] = data["overview"]
    if data.get("insights") is not None:
        import capo_resiliencehubv2.types.dependency_insights_list

        out["insights"] = (
            capo_resiliencehubv2.types.dependency_insights_list.deserialize_json(
                data["insights"]
            )
        )
    if data.get("status") is not None:
        import capo_resiliencehubv2.types.dependency_insights_status

        out["status"] = (
            capo_resiliencehubv2.types.dependency_insights_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_resiliencehubv2.types.dependency_insights_status.DependencyInsightsStatus",
            "",
        )
    if data.get("createdAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["created_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if data.get("errorCode") is not None:
        import capo_resiliencehubv2.types.dependency_insights_error_code

        out["error_code"] = (
            capo_resiliencehubv2.types.dependency_insights_error_code.deserialize_json(
                data["errorCode"]
            )
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out
