"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeWebAppRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.web_app_id


class DescribeWebAppRequest(TypedDict, closed=True):
    web_app_id: "capo_transfer.types.web_app_id.WebAppId"
    """<p>Provide the unique identifier for the web app.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWebAppRequest) -> dict:
    out: dict = {}
    out["WebAppId"] = value["web_app_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWebAppRequest:
    out: DescribeWebAppRequest = {}  # type: ignore[typeddict-item]
    if data.get("WebAppId") is not None:
        out["web_app_id"] = data["WebAppId"]
    else:
        out["web_app_id"] = ""
    return out
