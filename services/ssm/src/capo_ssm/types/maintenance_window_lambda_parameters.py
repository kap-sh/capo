"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowLambdaParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_lambda_client_context
    import capo_ssm.types.maintenance_window_lambda_payload
    import capo_ssm.types.maintenance_window_lambda_qualifier


class MaintenanceWindowLambdaParameters(TypedDict, closed=True):
    client_context: NotRequired[
        "capo_ssm.types.maintenance_window_lambda_client_context.MaintenanceWindowLambdaClientContext"
    ]
    """<p>Pass client-specific information to the Lambda function that you are invoking. You can then process the client information in your Lambda function as you choose through the context variable.</p>"""
    qualifier: NotRequired[
        "capo_ssm.types.maintenance_window_lambda_qualifier.MaintenanceWindowLambdaQualifier"
    ]
    """<p>(Optional) Specify an Lambda function version or alias name. If you specify a function version, the operation uses the qualified function Amazon Resource Name (ARN) to invoke a specific Lambda function. If you specify an alias name, the operation uses the alias ARN to invoke the Lambda function version to which the alias points.</p>"""
    payload: NotRequired[
        "capo_ssm.types.maintenance_window_lambda_payload.MaintenanceWindowLambdaPayload"
    ]
    """<p>JSON to provide to your Lambda function as input.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowLambdaParameters) -> dict:
    out: dict = {}
    if "client_context" in value:
        out["ClientContext"] = value["client_context"]
    if "qualifier" in value:
        out["Qualifier"] = value["qualifier"]
    if "payload" in value:
        import capo_ssm.types.maintenance_window_lambda_payload

        out["Payload"] = (
            capo_ssm.types.maintenance_window_lambda_payload.serialize_aws_json_1_1(
                value["payload"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MaintenanceWindowLambdaParameters:
    out: MaintenanceWindowLambdaParameters = {}  # type: ignore[typeddict-item]
    if data.get("ClientContext") is not None:
        out["client_context"] = data["ClientContext"]
    if data.get("Qualifier") is not None:
        out["qualifier"] = data["Qualifier"]
    if data.get("Payload") is not None:
        import capo_ssm.types.maintenance_window_lambda_payload

        out["payload"] = (
            capo_ssm.types.maintenance_window_lambda_payload.deserialize_aws_json_1_1(
                data["Payload"]
            )
        )
    return out


def redact_sensitive(value: MaintenanceWindowLambdaParameters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payload" in value:
        out["payload"] = "*** Sensitive Data Redacted ***"
    return out
