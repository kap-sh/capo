"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Lambdas``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.iam_role_arn
    import capo_arc_region_switch.types.lambda_arn
    import capo_arc_region_switch.types.lambda_payload


class Lambdas(TypedDict, closed=True):
    cross_account_role: NotRequired[
        "capo_arc_region_switch.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The cross account role for the configuration.</p>"""
    external_id: NotRequired["str"]
    """<p>The external ID (secret key) for the configuration.</p>"""
    arn: NotRequired["capo_arc_region_switch.types.lambda_arn.LambdaArn"]
    """<p>The Amazon Resource Name (ARN) of the Lambda function.</p>"""
    payload: NotRequired["capo_arc_region_switch.types.lambda_payload.LambdaPayload"]
    """<p>The JSON payload to send to the Lambda function invocation. If you don't specify a payload, Region switch invokes the function with only the execution metadata.</p> <p>If you provide a JSON object, Region switch merges execution metadata keys (<code>InvokedBy</code>, <code>PlanArn</code>, <code>ExecutionId</code>, <code>StepName</code>) into the top level. If one of your keys has the same name as a metadata key, your key takes precedence.</p> <p>If you provide any other JSON type (string, number, boolean, or array), Region switch forwards it to the Lambda function unchanged, without adding metadata.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Lambdas) -> dict:
    out: dict = {}
    if "cross_account_role" in value:
        out["crossAccountRole"] = value["cross_account_role"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "payload" in value:
        out["payload"] = value["payload"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Lambdas:
    out: Lambdas = {}  # type: ignore[typeddict-item]
    if data.get("crossAccountRole") is not None:
        out["cross_account_role"] = data["crossAccountRole"]
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("payload") is not None:
        out["payload"] = data["payload"]
    return out


def redact_sensitive(value: Lambdas) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payload" in value:
        out["payload"] = "*** Sensitive Data Redacted ***"
    return out
