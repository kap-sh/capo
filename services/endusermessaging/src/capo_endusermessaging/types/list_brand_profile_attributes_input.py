"""Generated from Smithy shape ``com.amazonaws.endusermessaging#ListBrandProfileAttributesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.brand_profile_id_or_arn
    import capo_endusermessaging.types.max_results
    import capo_endusermessaging.types.next_token


class ListBrandProfileAttributesInput(TypedDict, closed=True):
    brand_profile_id: (
        "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn"
    )
    """<p>The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>"""
    next_token: NotRequired["capo_endusermessaging.types.next_token.NextToken"]
    """<p>The token to retrieve the next page of results. This value is returned when more results are available, and is null when there are no more results to return.</p>"""
    max_results: NotRequired["capo_endusermessaging.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBrandProfileAttributesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBrandProfileAttributesInput:
    out: ListBrandProfileAttributesInput = {}  # type: ignore[typeddict-item]
    return out
