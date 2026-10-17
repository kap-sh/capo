"""Generated from Smithy shape ``com.amazonaws.lambda#ChainedInvokeOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.namespaced_function_name
    import capo_lambda.types.tenant_id


class ChainedInvokeOptions(TypedDict, closed=True):
    function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName"
    """<p>The name or ARN of the Lambda function to invoke.</p>"""
    tenant_id: NotRequired["capo_lambda.types.tenant_id.TenantId"]
    """<p>The tenant identifier for the chained invocation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChainedInvokeOptions) -> dict:
    out: dict = {}
    out["FunctionName"] = value["function_name"]
    if "tenant_id" in value:
        out["TenantId"] = value["tenant_id"]
    return out


def deserialize_json(data: dict) -> ChainedInvokeOptions:
    out: ChainedInvokeOptions = {}  # type: ignore[typeddict-item]
    if data.get("FunctionName") is not None:
        out["function_name"] = data["FunctionName"]
    else:
        raise DeserializationError("ChainedInvokeOptions.function_name required")
    if data.get("TenantId") is not None:
        out["tenant_id"] = data["TenantId"]
    return out
