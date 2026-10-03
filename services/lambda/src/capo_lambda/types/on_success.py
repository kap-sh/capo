"""Generated from Smithy shape ``com.amazonaws.lambda#OnSuccess``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.destination_arn


class OnSuccess(TypedDict, closed=True):
    destination: NotRequired["capo_lambda.types.destination_arn.DestinationArn"]
    """<p>The Amazon Resource Name (ARN) of the destination resource.</p> <note> <p>Amazon SNS destinations have a message size limit of 256 KB. If the combined size of the function request and response payload exceeds the limit, Lambda will drop the payload when sending <code>OnFailure</code> event to the destination. For details on this behavior, refer to <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html">Retaining records of asynchronous invocations</a>.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: OnSuccess) -> dict:
    out: dict = {}
    if "destination" in value:
        out["Destination"] = value["destination"]
    return out


def deserialize_json(data: dict) -> OnSuccess:
    out: OnSuccess = {}  # type: ignore[typeddict-item]
    if data.get("Destination") is not None:
        out["destination"] = data["Destination"]
    return out
