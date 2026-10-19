"""Generated from Smithy shape ``com.amazonaws.route53profiles#CreateProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53profiles.types.creator_request_id
    import capo_route53profiles.types.name
    import capo_route53profiles.types.tag_list


class CreateProfileRequest(TypedDict, closed=True):
    name: "capo_route53profiles.types.name.Name"
    """<p> A name for the Profile. </p>"""
    client_token: "capo_route53profiles.types.creator_request_id.CreatorRequestId"
    """<p> <code>ClientToken</code> is an idempotency token that ensures a call to <code>CreateProfile</code> completes only once. You choose the value to pass. For example, an issue might prevent you from getting a response from <code>CreateProfile</code>. In this case, safely retry your call to <code>CreateProfile</code> by using the same <code>CreateProfile</code> parameter value. </p>"""
    tags: NotRequired["capo_route53profiles.types.tag_list.TagList"]
    """<p> A list of the tag keys and values that you want to associate with the Route 53 Profile. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProfileRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_route53profiles.types.tag_list

        out["Tags"] = capo_route53profiles.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateProfileRequest:
    out: CreateProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    if data.get("Tags") is not None:
        import capo_route53profiles.types.tag_list

        out["tags"] = capo_route53profiles.types.tag_list.deserialize_json(data["Tags"])
    return out
