"""Generated from Smithy shape ``com.amazonaws.lambda#DeleteDurableExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.durable_execution_arn


class DeleteDurableExecutionRequest(TypedDict, closed=True):
    durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn"
    """<p>The Amazon Resource Name (ARN) of the durable execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDurableExecutionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDurableExecutionRequest:
    out: DeleteDurableExecutionRequest = {}  # type: ignore[typeddict-item]
    return out
