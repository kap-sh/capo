"""Generated from Smithy shape ``com.amazonaws.lambda#PutFunctionCodeSigningConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.code_signing_config_arn
    import capo_lambda.types.function_name


class PutFunctionCodeSigningConfigResponse(TypedDict, closed=True):
    code_signing_config_arn: (
        "capo_lambda.types.code_signing_config_arn.CodeSigningConfigArn"
    )
    """<p>The The Amazon Resource Name (ARN) of the code signing configuration.</p>"""
    function_name: "capo_lambda.types.function_name.FunctionName"
    """<p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutFunctionCodeSigningConfigResponse) -> dict:
    out: dict = {}
    out["CodeSigningConfigArn"] = value["code_signing_config_arn"]
    out["FunctionName"] = value["function_name"]
    return out


def deserialize_json(data: dict) -> PutFunctionCodeSigningConfigResponse:
    out: PutFunctionCodeSigningConfigResponse = {}  # type: ignore[typeddict-item]
    if data.get("CodeSigningConfigArn") is not None:
        out["code_signing_config_arn"] = data["CodeSigningConfigArn"]
    else:
        raise DeserializationError(
            "PutFunctionCodeSigningConfigResponse.code_signing_config_arn required"
        )
    if data.get("FunctionName") is not None:
        out["function_name"] = data["FunctionName"]
    else:
        raise DeserializationError(
            "PutFunctionCodeSigningConfigResponse.function_name required"
        )
    return out
