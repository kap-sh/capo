"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#StartDependencyInsightsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.dependency_insights_status


class StartDependencyInsightsResponse(TypedDict, closed=True):
    status: (
        "capo_resiliencehubv2.types.dependency_insights_status.DependencyInsightsStatus"
    )
    """<p>The status of the dependency insights generation. Valid values:</p> <ul> <li> <p>IN_PROGRESS - Insights generation is in progress.</p> </li> <li> <p>COMPLETED - Insights generation completed successfully.</p> </li> <li> <p>FAILED - Insights generation failed. Call GetDependencyInsights for the error code and message.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDependencyInsightsResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.dependency_insights_status

    out["status"] = (
        capo_resiliencehubv2.types.dependency_insights_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartDependencyInsightsResponse:
    out: StartDependencyInsightsResponse = {}  # type: ignore[typeddict-item]
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
    return out
