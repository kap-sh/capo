"""Generated from Smithy shape ``com.amazonaws.transfer#ListProfilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.listed_profiles
    import capo_transfer.types.next_token


class ListProfilesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_transfer.types.next_token.NextToken"]
    """<p>Returns a token that you can use to call <code>ListProfiles</code> again and receive additional results, if there are any.</p>"""
    profiles: "capo_transfer.types.listed_profiles.ListedProfiles"
    """<p>Returns an array, where each item contains the details of a profile.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProfilesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_transfer.types.listed_profiles

    out["Profiles"] = capo_transfer.types.listed_profiles.serialize_aws_json_1_1(
        value["profiles"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProfilesResponse:
    out: ListProfilesResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Profiles") is not None:
        import capo_transfer.types.listed_profiles

        out["profiles"] = capo_transfer.types.listed_profiles.deserialize_aws_json_1_1(
            data["Profiles"]
        )
    else:
        out["profiles"] = []
    return out
