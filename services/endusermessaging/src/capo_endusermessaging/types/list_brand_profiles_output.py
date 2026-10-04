"""Generated from Smithy shape ``com.amazonaws.endusermessaging#ListBrandProfilesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.brand_profile_info_list
    import capo_endusermessaging.types.next_token


class ListBrandProfilesOutput(TypedDict, closed=True):
    brand_profiles: (
        "capo_endusermessaging.types.brand_profile_info_list.BrandProfileInfoList"
    )
    """<p>The list of brand profiles.</p>"""
    next_token: NotRequired["capo_endusermessaging.types.next_token.NextToken"]
    """<p>The token to retrieve the next page of results. This value is returned when more results are available, and is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBrandProfilesOutput) -> dict:
    out: dict = {}
    import capo_endusermessaging.types.brand_profile_info_list

    out["brandProfiles"] = (
        capo_endusermessaging.types.brand_profile_info_list.serialize_json(
            value["brand_profiles"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBrandProfilesOutput:
    out: ListBrandProfilesOutput = {}  # type: ignore[typeddict-item]
    if data.get("brandProfiles") is not None:
        import capo_endusermessaging.types.brand_profile_info_list

        out["brand_profiles"] = (
            capo_endusermessaging.types.brand_profile_info_list.deserialize_json(
                data["brandProfiles"]
            )
        )
    else:
        raise DeserializationError("ListBrandProfilesOutput.brand_profiles required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
