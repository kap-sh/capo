"""Generated from Smithy shape ``com.amazonaws.lambda#CreateFunctionUrlConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.cors
    import capo_lambda.types.function_url_auth_type
    import capo_lambda.types.function_url_function_name
    import capo_lambda.types.function_url_qualifier
    import capo_lambda.types.invoke_mode


class CreateFunctionUrlConfigRequest(TypedDict, closed=True):
    function_name: (
        "capo_lambda.types.function_url_function_name.FunctionUrlFunctionName"
    )
    """<p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    qualifier: NotRequired[
        "capo_lambda.types.function_url_qualifier.FunctionUrlQualifier"
    ]
    """<p>The alias name.</p>"""
    auth_type: "capo_lambda.types.function_url_auth_type.FunctionUrlAuthType"
    """<p>The type of authentication that your function URL uses. Set to <code>AWS_IAM</code> if you want to restrict access to authenticated users only. Set to <code>NONE</code> if you want to bypass IAM authentication to create a public endpoint. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html">Control access to Lambda function URLs</a>.</p>"""
    cors: NotRequired["capo_lambda.types.cors.Cors"]
    """<p>The <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS">cross-origin resource sharing (CORS)</a> settings for your function URL.</p>"""
    invoke_mode: NotRequired["capo_lambda.types.invoke_mode.InvokeMode"]
    """<p>Use one of the following options:</p> <ul> <li> <p> <code>BUFFERED</code> – This is the default option. Lambda invokes your function using the <code>Invoke</code> API operation. Invocation results are available when the payload is complete. The maximum payload size is 6 MB.</p> </li> <li> <p> <code>RESPONSE_STREAM</code> – Your function streams payload results as they become available. Lambda invokes your function using the <code>InvokeWithResponseStream</code> API operation. The maximum response payload size is 200 MB.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFunctionUrlConfigRequest) -> dict:
    out: dict = {}
    import capo_lambda.types.function_url_auth_type

    out["AuthType"] = capo_lambda.types.function_url_auth_type.serialize_json(
        value["auth_type"]
    )
    if "cors" in value:
        import capo_lambda.types.cors

        out["Cors"] = capo_lambda.types.cors.serialize_json(value["cors"])
    if "invoke_mode" in value:
        import capo_lambda.types.invoke_mode

        out["InvokeMode"] = capo_lambda.types.invoke_mode.serialize_json(
            value["invoke_mode"]
        )
    return out


def deserialize_json(data: dict) -> CreateFunctionUrlConfigRequest:
    out: CreateFunctionUrlConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("AuthType") is not None:
        import capo_lambda.types.function_url_auth_type

        out["auth_type"] = capo_lambda.types.function_url_auth_type.deserialize_json(
            data["AuthType"]
        )
    else:
        raise DeserializationError("CreateFunctionUrlConfigRequest.auth_type required")
    if data.get("Cors") is not None:
        import capo_lambda.types.cors

        out["cors"] = capo_lambda.types.cors.deserialize_json(data["Cors"])
    if data.get("InvokeMode") is not None:
        import capo_lambda.types.invoke_mode

        out["invoke_mode"] = capo_lambda.types.invoke_mode.deserialize_json(
            data["InvokeMode"]
        )
    return out
