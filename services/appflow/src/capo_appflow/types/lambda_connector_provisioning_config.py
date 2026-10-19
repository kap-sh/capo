"""Generated from Smithy shape ``com.amazonaws.appflow#LambdaConnectorProvisioningConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.arn


class LambdaConnectorProvisioningConfig(TypedDict, closed=True):
    lambda_arn: "capo_appflow.types.arn.ARN"
    """<p>Lambda ARN of the connector being registered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaConnectorProvisioningConfig) -> dict:
    out: dict = {}
    out["lambdaArn"] = value["lambda_arn"]
    return out


def deserialize_json(data: dict) -> LambdaConnectorProvisioningConfig:
    out: LambdaConnectorProvisioningConfig = {}  # type: ignore[typeddict-item]
    if data.get("lambdaArn") is not None:
        out["lambda_arn"] = data["lambdaArn"]
    else:
        out["lambda_arn"] = ""
    return out
