"""Generated from Smithy shape ``com.amazonaws.lightsail#GetSetupHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.setup_history_page_token


class GetSetupHistoryRequest(TypedDict, closed=True):
    resource_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the resource for which you are requesting information.</p>"""
    page_token: NotRequired[
        "capo_lightsail.types.setup_history_page_token.SetupHistoryPageToken"
    ]
    """<p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetSetupHistory</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSetupHistoryRequest) -> dict:
    out: dict = {}
    out["resourceName"] = value["resource_name"]
    if "page_token" in value:
        out["pageToken"] = value["page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSetupHistoryRequest:
    out: GetSetupHistoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    else:
        out["resource_name"] = ""
    if data.get("pageToken") is not None:
        out["page_token"] = data["pageToken"]
    return out
