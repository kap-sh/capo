"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Lambdas``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.iam_role_arn
    import capo_arc_region_switch.types.lambda_arn


class Lambdas(TypedDict, closed=True):
    cross_account_role: NotRequired[
        "capo_arc_region_switch.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The cross account role for the configuration.</p>"""
    external_id: NotRequired["str"]
    """<p>The external ID (secret key) for the configuration.</p>"""
    arn: NotRequired["capo_arc_region_switch.types.lambda_arn.LambdaArn"]
    """<p>The Amazon Resource Name (ARN) of the Lambda function.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Lambdas) -> dict:
    out: dict = {}
    if "cross_account_role" in value:
        out["crossAccountRole"] = value["cross_account_role"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Lambdas:
    out: Lambdas = {}  # type: ignore[typeddict-item]
    if data.get("crossAccountRole") is not None:
        out["cross_account_role"] = data["crossAccountRole"]
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    return out
