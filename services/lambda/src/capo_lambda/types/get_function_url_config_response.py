"""Generated from Smithy shape ``com.amazonaws.lambda#GetFunctionUrlConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.cors
    import capo_lambda.types.function_arn
    import capo_lambda.types.function_url
    import capo_lambda.types.function_url_auth_type
    import capo_lambda.types.invoke_mode
    import capo_lambda.types.timestamp


class GetFunctionUrlConfigResponse(TypedDict, closed=True):
    function_url: "capo_lambda.types.function_url.FunctionUrl"
    """<p>The HTTP URL endpoint for your function.</p>"""
    function_arn: "capo_lambda.types.function_arn.FunctionArn"
    """<p>The Amazon Resource Name (ARN) of your function.</p>"""
    auth_type: "capo_lambda.types.function_url_auth_type.FunctionUrlAuthType"
    """<p>The type of authentication that your function URL uses. Set to <code>AWS_IAM</code> if you want to restrict access to authenticated users only. Set to <code>NONE</code> if you want to bypass IAM authentication to create a public endpoint. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html">Control access to Lambda function URLs</a>.</p>"""
    cors: NotRequired["capo_lambda.types.cors.Cors"]
    """<p>The <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS">cross-origin resource sharing (CORS)</a> settings for your function URL.</p>"""
    creation_time: "capo_lambda.types.timestamp.Timestamp"
    """<p>When the function URL was created, in <a href="https://www.w3.org/TR/NOTE-datetime">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    last_modified_time: "capo_lambda.types.timestamp.Timestamp"
    """<p>When the function URL configuration was last updated, in <a href="https://www.w3.org/TR/NOTE-datetime">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    invoke_mode: NotRequired["capo_lambda.types.invoke_mode.InvokeMode"]
    """<p>Use one of the following options:</p> <ul> <li> <p> <code>BUFFERED</code> – This is the default option. Lambda invokes your function using the <code>Invoke</code> API operation. Invocation results are available when the payload is complete. The maximum payload size is 6 MB.</p> </li> <li> <p> <code>RESPONSE_STREAM</code> – Your function streams payload results as they become available. Lambda invokes your function using the <code>InvokeWithResponseStream</code> API operation. The maximum response payload size is 200 MB.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFunctionUrlConfigResponse) -> dict:
    out: dict = {}
    out["FunctionUrl"] = value["function_url"]
    out["FunctionArn"] = value["function_arn"]
    import capo_lambda.types.function_url_auth_type

    out["AuthType"] = capo_lambda.types.function_url_auth_type.serialize_json(
        value["auth_type"]
    )
    if "cors" in value:
        import capo_lambda.types.cors

        out["Cors"] = capo_lambda.types.cors.serialize_json(value["cors"])
    out["CreationTime"] = value["creation_time"]
    out["LastModifiedTime"] = value["last_modified_time"]
    if "invoke_mode" in value:
        import capo_lambda.types.invoke_mode

        out["InvokeMode"] = capo_lambda.types.invoke_mode.serialize_json(
            value["invoke_mode"]
        )
    return out


def deserialize_json(data: dict) -> GetFunctionUrlConfigResponse:
    out: GetFunctionUrlConfigResponse = {}  # type: ignore[typeddict-item]
    if data.get("FunctionUrl") is not None:
        out["function_url"] = data["FunctionUrl"]
    else:
        raise DeserializationError("GetFunctionUrlConfigResponse.function_url required")
    if data.get("FunctionArn") is not None:
        out["function_arn"] = data["FunctionArn"]
    else:
        raise DeserializationError("GetFunctionUrlConfigResponse.function_arn required")
    if data.get("AuthType") is not None:
        import capo_lambda.types.function_url_auth_type

        out["auth_type"] = capo_lambda.types.function_url_auth_type.deserialize_json(
            data["AuthType"]
        )
    else:
        raise DeserializationError("GetFunctionUrlConfigResponse.auth_type required")
    if data.get("Cors") is not None:
        import capo_lambda.types.cors

        out["cors"] = capo_lambda.types.cors.deserialize_json(data["Cors"])
    if data.get("CreationTime") is not None:
        out["creation_time"] = data["CreationTime"]
    else:
        raise DeserializationError(
            "GetFunctionUrlConfigResponse.creation_time required"
        )
    if data.get("LastModifiedTime") is not None:
        out["last_modified_time"] = data["LastModifiedTime"]
    else:
        raise DeserializationError(
            "GetFunctionUrlConfigResponse.last_modified_time required"
        )
    if data.get("InvokeMode") is not None:
        import capo_lambda.types.invoke_mode

        out["invoke_mode"] = capo_lambda.types.invoke_mode.deserialize_json(
            data["InvokeMode"]
        )
    return out
