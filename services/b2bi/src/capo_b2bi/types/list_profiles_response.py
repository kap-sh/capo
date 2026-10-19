"""Generated from Smithy shape ``com.amazonaws.b2bi#ListProfilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.page_token
    import capo_b2bi.types.profile_list


class ListProfilesResponse(TypedDict, closed=True):
    profiles: "capo_b2bi.types.profile_list.ProfileList"
    """<p>Returns an array of <code>ProfileSummary</code> objects.</p>"""
    next_token: NotRequired["capo_b2bi.types.page_token.PageToken"]
    """<p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListProfilesResponse) -> dict:
    out: dict = {}
    import capo_b2bi.types.profile_list

    out["profiles"] = capo_b2bi.types.profile_list.serialize_aws_json_1_0(
        value["profiles"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListProfilesResponse:
    out: ListProfilesResponse = {}  # type: ignore[typeddict-item]
    if data.get("profiles") is not None:
        import capo_b2bi.types.profile_list

        out["profiles"] = capo_b2bi.types.profile_list.deserialize_aws_json_1_0(
            data["profiles"]
        )
    else:
        out["profiles"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
