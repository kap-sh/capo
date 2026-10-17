"""Generated from Smithy shape ``com.amazonaws.lambda#ChainedInvokeOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.namespaced_function_name
    import capo_lambda.types.tenant_id
    import capo_lambda.types.x_amzn_trace_id


class ChainedInvokeOptions(TypedDict, closed=True):
    function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName"
    """<p>The name or ARN of the Lambda function to invoke.</p>"""
    tenant_id: NotRequired["capo_lambda.types.tenant_id.TenantId"]
    """<p>The tenant identifier for the chained invocation.</p>"""
    x_amzn_trace_id: NotRequired["capo_lambda.types.x_amzn_trace_id.XAmznTraceId"]
    """<p>The optional X-Ray trace header to use when starting the chained invocation. If you omit this value, the child invocation inherits the parent durable execution's trace header.</p> <p>Specify this value on the <code>START</code> update for the chained invocation operation. For more information about the header format, see <a href="https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-tracingheader">Tracing header</a> in the <i>X-Ray Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChainedInvokeOptions) -> dict:
    out: dict = {}
    out["FunctionName"] = value["function_name"]
    if "tenant_id" in value:
        out["TenantId"] = value["tenant_id"]
    if "x_amzn_trace_id" in value:
        out["XAmznTraceId"] = value["x_amzn_trace_id"]
    return out


def deserialize_json(data: dict) -> ChainedInvokeOptions:
    out: ChainedInvokeOptions = {}  # type: ignore[typeddict-item]
    if data.get("FunctionName") is not None:
        out["function_name"] = data["FunctionName"]
    else:
        raise DeserializationError("ChainedInvokeOptions.function_name required")
    if data.get("TenantId") is not None:
        out["tenant_id"] = data["TenantId"]
    if data.get("XAmznTraceId") is not None:
        out["x_amzn_trace_id"] = data["XAmznTraceId"]
    return out
