"""Generated from Smithy shape ``com.amazonaws.freetier#GetFreeTierUsageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_freetier.types.free_tier_usages
    import capo_freetier.types.next_page_token


class GetFreeTierUsageResponse(TypedDict, closed=True):
    free_tier_usages: "capo_freetier.types.free_tier_usages.FreeTierUsages"
    """<p>The list of Free Tier usage objects that meet your filter expression.</p>"""
    next_token: NotRequired["capo_freetier.types.next_page_token.NextPageToken"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetFreeTierUsageResponse) -> dict:
    out: dict = {}
    import capo_freetier.types.free_tier_usages

    out["freeTierUsages"] = capo_freetier.types.free_tier_usages.serialize_aws_json_1_0(
        value["free_tier_usages"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetFreeTierUsageResponse:
    out: GetFreeTierUsageResponse = {}  # type: ignore[typeddict-item]
    if data.get("freeTierUsages") is not None:
        import capo_freetier.types.free_tier_usages

        out["free_tier_usages"] = (
            capo_freetier.types.free_tier_usages.deserialize_aws_json_1_0(
                data["freeTierUsages"]
            )
        )
    else:
        out["free_tier_usages"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
