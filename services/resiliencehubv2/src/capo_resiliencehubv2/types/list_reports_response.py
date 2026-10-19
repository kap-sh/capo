"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListReportsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.report_generation_result_list


class ListReportsResponse(TypedDict, closed=True):
    report_generation_results: "capo_resiliencehubv2.types.report_generation_result_list.ReportGenerationResultList"
    """<p>The list of report generation results.</p>"""
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListReportsResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.report_generation_result_list

    out["reportGenerationResults"] = (
        capo_resiliencehubv2.types.report_generation_result_list.serialize_json(
            value["report_generation_results"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListReportsResponse:
    out: ListReportsResponse = {}  # type: ignore[typeddict-item]
    if data.get("reportGenerationResults") is not None:
        import capo_resiliencehubv2.types.report_generation_result_list

        out["report_generation_results"] = (
            capo_resiliencehubv2.types.report_generation_result_list.deserialize_json(
                data["reportGenerationResults"]
            )
        )
    else:
        out["report_generation_results"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
