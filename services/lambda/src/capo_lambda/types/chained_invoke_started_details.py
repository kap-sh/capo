"""Generated from Smithy shape ``com.amazonaws.lambda#ChainedInvokeStartedDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.durable_execution_arn
    import capo_lambda.types.event_input
    import capo_lambda.types.namespaced_function_name
    import capo_lambda.types.tenant_id
    import capo_lambda.types.version_with_latest_published


class ChainedInvokeStartedDetails(TypedDict, closed=True):
    function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName"
    """<p>The name or ARN of the Lambda function being invoked.</p>"""
    tenant_id: NotRequired["capo_lambda.types.tenant_id.TenantId"]
    """<p>The tenant identifier for the chained invocation.</p>"""
    input: NotRequired["capo_lambda.types.event_input.EventInput"]
    """<p>The JSON input payload provided to the chained invocation.</p>"""
    executed_version: NotRequired[
        "capo_lambda.types.version_with_latest_published.VersionWithLatestPublished"
    ]
    """<p>The version of the function that was executed.</p>"""
    durable_execution_arn: NotRequired[
        "capo_lambda.types.durable_execution_arn.DurableExecutionArn"
    ]
    """<p>The Amazon Resource Name (ARN) that identifies the durable execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChainedInvokeStartedDetails) -> dict:
    out: dict = {}
    out["FunctionName"] = value["function_name"]
    if "tenant_id" in value:
        out["TenantId"] = value["tenant_id"]
    if "input" in value:
        import capo_lambda.types.event_input

        out["Input"] = capo_lambda.types.event_input.serialize_json(value["input"])
    if "executed_version" in value:
        out["ExecutedVersion"] = value["executed_version"]
    if "durable_execution_arn" in value:
        out["DurableExecutionArn"] = value["durable_execution_arn"]
    return out


def deserialize_json(data: dict) -> ChainedInvokeStartedDetails:
    out: ChainedInvokeStartedDetails = {}  # type: ignore[typeddict-item]
    if data.get("FunctionName") is not None:
        out["function_name"] = data["FunctionName"]
    else:
        out["function_name"] = ""
    if data.get("TenantId") is not None:
        out["tenant_id"] = data["TenantId"]
    if data.get("Input") is not None:
        import capo_lambda.types.event_input

        out["input"] = capo_lambda.types.event_input.deserialize_json(data["Input"])
    if data.get("ExecutedVersion") is not None:
        out["executed_version"] = data["ExecutedVersion"]
    if data.get("DurableExecutionArn") is not None:
        out["durable_execution_arn"] = data["DurableExecutionArn"]
    return out


def redact_sensitive(value: ChainedInvokeStartedDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input" in value:
        import capo_lambda.types.event_input

        out["input"] = capo_lambda.types.event_input.redact_sensitive(value["input"])
    return out
