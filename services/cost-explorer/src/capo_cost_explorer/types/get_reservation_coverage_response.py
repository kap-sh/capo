"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetReservationCoverageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.coverage
    import capo_cost_explorer.types.coverages_by_time
    import capo_cost_explorer.types.next_page_token


class GetReservationCoverageResponse(TypedDict, closed=True):
    coverages_by_time: "capo_cost_explorer.types.coverages_by_time.CoveragesByTime"
    """<p>The amount of time that your reservations covered.</p>"""
    total: NotRequired["capo_cost_explorer.types.coverage.Coverage"]
    """<p>The total amount of instance usage that a reservation covered.</p>"""
    next_page_token: NotRequired[
        "capo_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token for the next set of retrievable results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetReservationCoverageResponse) -> dict:
    out: dict = {}
    import capo_cost_explorer.types.coverages_by_time

    out["CoveragesByTime"] = (
        capo_cost_explorer.types.coverages_by_time.serialize_aws_json_1_1(
            value["coverages_by_time"]
        )
    )
    if "total" in value:
        import capo_cost_explorer.types.coverage

        out["Total"] = capo_cost_explorer.types.coverage.serialize_aws_json_1_1(
            value["total"]
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetReservationCoverageResponse:
    out: GetReservationCoverageResponse = {}  # type: ignore[typeddict-item]
    if data.get("CoveragesByTime") is not None:
        import capo_cost_explorer.types.coverages_by_time

        out["coverages_by_time"] = (
            capo_cost_explorer.types.coverages_by_time.deserialize_aws_json_1_1(
                data["CoveragesByTime"]
            )
        )
    else:
        out["coverages_by_time"] = []
    if data.get("Total") is not None:
        import capo_cost_explorer.types.coverage

        out["total"] = capo_cost_explorer.types.coverage.deserialize_aws_json_1_1(
            data["Total"]
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
