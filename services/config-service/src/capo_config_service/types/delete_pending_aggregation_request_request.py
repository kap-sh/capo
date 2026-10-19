"""Generated from Smithy shape ``com.amazonaws.configservice#DeletePendingAggregationRequestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.account_id
    import capo_config_service.types.aws_region


class DeletePendingAggregationRequestRequest(TypedDict, closed=True):
    requester_account_id: "capo_config_service.types.account_id.AccountId"
    """<p>The 12-digit account ID of the account requesting to aggregate data.</p>"""
    requester_aws_region: "capo_config_service.types.aws_region.AwsRegion"
    """<p>The region requesting to aggregate data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePendingAggregationRequestRequest) -> dict:
    out: dict = {}
    out["RequesterAccountId"] = value["requester_account_id"]
    out["RequesterAwsRegion"] = value["requester_aws_region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePendingAggregationRequestRequest:
    out: DeletePendingAggregationRequestRequest = {}  # type: ignore[typeddict-item]
    if data.get("RequesterAccountId") is not None:
        out["requester_account_id"] = data["RequesterAccountId"]
    else:
        out["requester_account_id"] = ""
    if data.get("RequesterAwsRegion") is not None:
        out["requester_aws_region"] = data["RequesterAwsRegion"]
    else:
        out["requester_aws_region"] = ""
    return out
