"""Generated from Smithy shape ``com.amazonaws.athena#GetResourceDashboardResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_athena.types.string


class GetResourceDashboardResponse(TypedDict, closed=True):
    url: "capo_athena.types.string.String"
    """<p>The Live UI/Persistence UI url for a session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourceDashboardResponse) -> dict:
    out: dict = {}
    out["Url"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourceDashboardResponse:
    out: GetResourceDashboardResponse = {}  # type: ignore[typeddict-item]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    else:
        out["url"] = ""
    return out
