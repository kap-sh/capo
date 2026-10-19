"""Generated from Smithy shape ``com.amazonaws.sqs#GetQueueUrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.string


class GetQueueUrlRequest(TypedDict, closed=True):
    queue_name: "capo_sqs.types.string.String"
    """<p>(Required) The name of the queue for which you want to fetch the URL. The name can be up to 80 characters long and can include alphanumeric characters, hyphens (-), and underscores (_). Queue URLs and names are case-sensitive.</p>"""
    queue_owner_aws_account_id: NotRequired["capo_sqs.types.string.String"]
    """<p>(Optional) The Amazon Web Services account ID of the account that created the queue. This is only required when you are attempting to access a queue owned by another Amazon Web Services account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetQueueUrlRequest) -> dict:
    out: dict = {}
    out["QueueName"] = value["queue_name"]
    if "queue_owner_aws_account_id" in value:
        out["QueueOwnerAWSAccountId"] = value["queue_owner_aws_account_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetQueueUrlRequest:
    out: GetQueueUrlRequest = {}  # type: ignore[typeddict-item]
    if data.get("QueueName") is not None:
        out["queue_name"] = data["QueueName"]
    else:
        out["queue_name"] = ""
    if data.get("QueueOwnerAWSAccountId") is not None:
        out["queue_owner_aws_account_id"] = data["QueueOwnerAWSAccountId"]
    return out
