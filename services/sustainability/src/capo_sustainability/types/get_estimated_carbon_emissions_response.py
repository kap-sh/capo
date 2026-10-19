"""Generated from Smithy shape ``com.amazonaws.sustainability#GetEstimatedCarbonEmissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sustainability.types.estimated_carbon_emissions_list
    import capo_sustainability.types.next_token


class GetEstimatedCarbonEmissionsResponse(TypedDict, closed=True):
    results: "capo_sustainability.types.estimated_carbon_emissions_list.EstimatedCarbonEmissionsList"
    """<p>The result of the requested inputs.</p>"""
    next_token: NotRequired["capo_sustainability.types.next_token.NextToken"]
    """<p>The pagination token indicating there are additional pages available. You can use the token in a following request to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEstimatedCarbonEmissionsResponse) -> dict:
    out: dict = {}
    import capo_sustainability.types.estimated_carbon_emissions_list

    out["Results"] = (
        capo_sustainability.types.estimated_carbon_emissions_list.serialize_json(
            value["results"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetEstimatedCarbonEmissionsResponse:
    out: GetEstimatedCarbonEmissionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Results") is not None:
        import capo_sustainability.types.estimated_carbon_emissions_list

        out["results"] = (
            capo_sustainability.types.estimated_carbon_emissions_list.deserialize_json(
                data["Results"]
            )
        )
    else:
        out["results"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
