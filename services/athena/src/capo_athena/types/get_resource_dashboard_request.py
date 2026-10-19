"""Generated from Smithy shape ``com.amazonaws.athena#GetResourceDashboardRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_athena.types.amazon_resource_name


class GetResourceDashboardRequest(TypedDict, closed=True):
    resource_arn: "capo_athena.types.amazon_resource_name.AmazonResourceName"
    """<p>The The Amazon Resource Name (ARN) for a session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourceDashboardRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourceDashboardRequest:
    out: GetResourceDashboardRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    return out
