"""Generated from Smithy shape ``com.amazonaws.ssm#ValidateCloudConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.cloud_connector_id
    import capo_ssm.types.next_token
    import capo_ssm.types.validate_cloud_connector_max_results


class ValidateCloudConnectorRequest(TypedDict, closed=True):
    cloud_connector_id: "capo_ssm.types.cloud_connector_id.CloudConnectorId"
    """<p>The ID of the cloud connector to validate.</p>"""
    max_results: NotRequired[
        "capo_ssm.types.validate_cloud_connector_max_results.ValidateCloudConnectorMaxResults"
    ]
    """<p>The maximum number of validation findings to return.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidateCloudConnectorRequest) -> dict:
    out: dict = {}
    out["CloudConnectorId"] = value["cloud_connector_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidateCloudConnectorRequest:
    out: ValidateCloudConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("CloudConnectorId") is not None:
        out["cloud_connector_id"] = data["CloudConnectorId"]
    else:
        out["cloud_connector_id"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
