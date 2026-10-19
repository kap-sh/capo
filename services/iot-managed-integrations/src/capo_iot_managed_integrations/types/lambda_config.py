"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#LambdaConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.lambda_arn


class LambdaConfig(TypedDict, closed=True):
    arn: "capo_iot_managed_integrations.types.lambda_arn.LambdaArn"
    """<p>The Amazon Resource Name (ARN) of the Lambda function used as an endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaConfig) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> LambdaConfig:
    out: LambdaConfig = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
