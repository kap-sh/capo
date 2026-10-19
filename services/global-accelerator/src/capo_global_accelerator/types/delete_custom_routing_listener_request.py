"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#DeleteCustomRoutingListenerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.generic_string


class DeleteCustomRoutingListenerRequest(TypedDict, closed=True):
    listener_arn: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the listener to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCustomRoutingListenerRequest) -> dict:
    out: dict = {}
    out["ListenerArn"] = value["listener_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCustomRoutingListenerRequest:
    out: DeleteCustomRoutingListenerRequest = {}  # type: ignore[typeddict-item]
    if data.get("ListenerArn") is not None:
        out["listener_arn"] = data["ListenerArn"]
    else:
        out["listener_arn"] = ""
    return out
