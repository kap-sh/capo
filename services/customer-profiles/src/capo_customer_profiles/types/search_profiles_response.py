"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SearchProfilesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.profile_list
    import capo_customer_profiles.types.token


class SearchProfilesResponse(TypedDict, closed=True):
    items: NotRequired["capo_customer_profiles.types.profile_list.ProfileList"]
    """<p>The list of Profiles matching the search criteria.</p>"""
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous SearchProfiles API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchProfilesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_customer_profiles.types.profile_list

        out["Items"] = capo_customer_profiles.types.profile_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchProfilesResponse:
    out: SearchProfilesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_customer_profiles.types.profile_list

        out["items"] = capo_customer_profiles.types.profile_list.deserialize_json(
            data["Items"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: SearchProfilesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_customer_profiles.types.profile_list

        out["items"] = capo_customer_profiles.types.profile_list.redact_sensitive(
            value["items"]
        )
    return out
