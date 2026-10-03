"""Generated from Smithy shape ``com.amazonaws.connect#DescribePromptRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.prompt_id


class DescribePromptRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    prompt_id: "capo_connect.types.prompt_id.PromptId"
    """<p>A unique identifier for the prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePromptRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribePromptRequest:
    out: DescribePromptRequest = {}  # type: ignore[typeddict-item]
    return out
