"""Generated from Smithy shape ``com.amazonaws.iot#LambdaAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.function_arn


class LambdaAction(TypedDict, closed=True):
    function_arn: "capo_iot.types.function_arn.FunctionArn"
    """<p>The ARN of the Lambda function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaAction) -> dict:
    out: dict = {}
    out["functionArn"] = value["function_arn"]
    return out


def deserialize_json(data: dict) -> LambdaAction:
    out: LambdaAction = {}  # type: ignore[typeddict-item]
    if data.get("functionArn") is not None:
        out["function_arn"] = data["functionArn"]
    else:
        out["function_arn"] = ""
    return out
