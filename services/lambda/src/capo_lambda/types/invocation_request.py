"""Generated from Smithy shape ``com.amazonaws.lambda#InvocationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.blob
    import capo_lambda.types.durable_execution_name
    import capo_lambda.types.invocation_type
    import capo_lambda.types.log_type
    import capo_lambda.types.namespaced_function_name
    import capo_lambda.types.numeric_latest_published_or_alias_qualifier
    import capo_lambda.types.string
    import capo_lambda.types.tenant_id


class InvocationRequest(TypedDict, closed=True):
    function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName"
    """<p>The name or ARN of the Lambda function, version, or alias.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    invocation_type: NotRequired["capo_lambda.types.invocation_type.InvocationType"]
    """<p>Choose from the following options.</p> <ul> <li> <p> <code>RequestResponse</code> (default) – Invoke the function synchronously. Keep the connection open until the function returns a response or times out. The API response includes the function response and additional data.</p> </li> <li> <p> <code>Event</code> – Invoke the function asynchronously. Send events that fail multiple times to the function's dead-letter queue (if one is configured). The API response only includes a status code.</p> </li> <li> <p> <code>DryRun</code> – Validate parameter values and verify that the user or role has permission to invoke the function.</p> </li> </ul>"""
    log_type: NotRequired["capo_lambda.types.log_type.LogType"]
    """<p>Set to <code>Tail</code> to include the execution log in the response. Applies to synchronously invoked functions only.</p>"""
    client_context: NotRequired["capo_lambda.types.string.String"]
    """<p>Up to 3,583 bytes of base64-encoded data about the invoking client to pass to the function in the context object. Lambda passes the <code>ClientContext</code> object to your function for synchronous invocations only.</p>"""
    durable_execution_name: NotRequired[
        "capo_lambda.types.durable_execution_name.DurableExecutionName"
    ]
    """<p>A unique name for the durable execution. If you invoke a durable function using a name that already exists with the same payload, Lambda returns the existing execution instead of creating a duplicate. If the payload differs, Lambda returns a <code>DurableExecutionAlreadyStartedException</code> error.</p> <p>If not specified, Lambda generates a unique identifier automatically. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/durable-execution-idempotency.html#durable-idempotency-execution-names">Execution names</a>.</p>"""
    payload: NotRequired["capo_lambda.types.blob.Blob"]
    """<p>The JSON that you want to provide to your Lambda function as input. The maximum payload size is 6 MB for synchronous invocations and 1 MB for asynchronous invocations.</p> <p>You can enter the JSON directly. For example, <code>--payload '{ "key": "value" }'</code>. You can also specify a file path. For example, <code>--payload file://payload.json</code>.</p>"""
    qualifier: NotRequired[
        "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
    ]
    """<p>Specify a version or alias to invoke a published version of the function.</p>"""
    tenant_id: NotRequired["capo_lambda.types.tenant_id.TenantId"]
    """<p>The identifier of the tenant in a multi-tenant Lambda function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvocationRequest) -> dict:
    out: dict = {}
    if "payload" in value:
        import capo_lambda.types.blob

        out["Payload"] = capo_lambda.types.blob.serialize_json(value["payload"])
    return out


def deserialize_json(data: dict) -> InvocationRequest:
    out: InvocationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Payload") is not None:
        import capo_lambda.types.blob

        out["payload"] = capo_lambda.types.blob.deserialize_json(data["Payload"])
    return out
