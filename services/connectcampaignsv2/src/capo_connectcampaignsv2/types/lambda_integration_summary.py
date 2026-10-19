"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#LambdaIntegrationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.lambda_arn


class LambdaIntegrationSummary(TypedDict, closed=True):
    function_arn: "capo_connectcampaignsv2.types.lambda_arn.LambdaArn"


# --- restJson1 ser/de ---
def serialize_json(value: LambdaIntegrationSummary) -> dict:
    out: dict = {}
    out["functionArn"] = value["function_arn"]
    return out


def deserialize_json(data: dict) -> LambdaIntegrationSummary:
    out: LambdaIntegrationSummary = {}  # type: ignore[typeddict-item]
    if data.get("functionArn") is not None:
        out["function_arn"] = data["functionArn"]
    else:
        out["function_arn"] = ""
    return out
