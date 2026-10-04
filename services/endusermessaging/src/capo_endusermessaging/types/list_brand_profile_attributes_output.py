"""Generated from Smithy shape ``com.amazonaws.endusermessaging#ListBrandProfileAttributesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.brand_profile_attribute_summary_list
    import capo_endusermessaging.types.next_token


class ListBrandProfileAttributesOutput(TypedDict, closed=True):
    brand_profile_attributes: "capo_endusermessaging.types.brand_profile_attribute_summary_list.BrandProfileAttributeSummaryList"
    """<p>The list of brand profile attributes.</p>"""
    next_token: NotRequired["capo_endusermessaging.types.next_token.NextToken"]
    """<p>The token to retrieve the next page of results. This value is returned when more results are available, and is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBrandProfileAttributesOutput) -> dict:
    out: dict = {}
    import capo_endusermessaging.types.brand_profile_attribute_summary_list

    out["brandProfileAttributes"] = (
        capo_endusermessaging.types.brand_profile_attribute_summary_list.serialize_json(
            value["brand_profile_attributes"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBrandProfileAttributesOutput:
    out: ListBrandProfileAttributesOutput = {}  # type: ignore[typeddict-item]
    if data.get("brandProfileAttributes") is not None:
        import capo_endusermessaging.types.brand_profile_attribute_summary_list

        out["brand_profile_attributes"] = (
            capo_endusermessaging.types.brand_profile_attribute_summary_list.deserialize_json(
                data["brandProfileAttributes"]
            )
        )
    else:
        raise DeserializationError(
            "ListBrandProfileAttributesOutput.brand_profile_attributes required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
