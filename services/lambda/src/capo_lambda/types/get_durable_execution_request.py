"""Generated from Smithy shape ``com.amazonaws.lambda#GetDurableExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.durable_execution_arn
    import capo_lambda.types.include_execution_data


class GetDurableExecutionRequest(TypedDict, closed=True):
    durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn"
    """<p>The Amazon Resource Name (ARN) of the durable execution.</p>"""
    include_execution_data: NotRequired[
        "capo_lambda.types.include_execution_data.IncludeExecutionData"
    ]
    """<p>Specifies whether to include execution data such as input payload, result, and error information in the response. Set to <code>false</code> for a more compact response that includes only execution metadata. The default value is set to <code>true</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDurableExecutionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDurableExecutionRequest:
    out: GetDurableExecutionRequest = {}  # type: ignore[typeddict-item]
    return out
