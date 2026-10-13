"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListOpportunitiesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.opportunity_summaries


class ListOpportunitiesResponse(TypedDict, closed=True):
    opportunity_summaries: (
        "capo_partnercentral_selling.types.opportunity_summaries.OpportunitySummaries"
    )
    """<p>An array that contains minimal details for opportunities that match the request criteria. This summary view provides a quick overview of relevant opportunities.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token used to retrieve the next set of results in subsequent calls. This token is included in the response only if there are additional result pages available.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListOpportunitiesResponse) -> dict:
    out: dict = {}
    import capo_partnercentral_selling.types.opportunity_summaries

    out["OpportunitySummaries"] = (
        capo_partnercentral_selling.types.opportunity_summaries.serialize_aws_json_1_0(
            value["opportunity_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListOpportunitiesResponse:
    out: ListOpportunitiesResponse = {}  # type: ignore[typeddict-item]
    if data.get("OpportunitySummaries") is not None:
        import capo_partnercentral_selling.types.opportunity_summaries

        out["opportunity_summaries"] = (
            capo_partnercentral_selling.types.opportunity_summaries.deserialize_aws_json_1_0(
                data["OpportunitySummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListOpportunitiesResponse.opportunity_summaries required"
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListOpportunitiesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "opportunity_summaries" in value:
        import capo_partnercentral_selling.types.opportunity_summaries

        out["opportunity_summaries"] = (
            capo_partnercentral_selling.types.opportunity_summaries.redact_sensitive(
                value["opportunity_summaries"]
            )
        )
    return out
