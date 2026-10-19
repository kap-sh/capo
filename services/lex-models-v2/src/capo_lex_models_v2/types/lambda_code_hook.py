"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#LambdaCodeHook``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.code_hook_interface_version
    import capo_lex_models_v2.types.lambda_arn


class LambdaCodeHook(TypedDict, closed=True):
    lambda_arn: "capo_lex_models_v2.types.lambda_arn.LambdaARN"
    """<p>The Amazon Resource Name (ARN) of the Lambda function.</p>"""
    code_hook_interface_version: (
        "capo_lex_models_v2.types.code_hook_interface_version.CodeHookInterfaceVersion"
    )
    """<p>The version of the request-response that you want Amazon Lex to use to invoke your Lambda function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaCodeHook) -> dict:
    out: dict = {}
    out["lambdaARN"] = value["lambda_arn"]
    out["codeHookInterfaceVersion"] = value["code_hook_interface_version"]
    return out


def deserialize_json(data: dict) -> LambdaCodeHook:
    out: LambdaCodeHook = {}  # type: ignore[typeddict-item]
    if data.get("lambdaARN") is not None:
        out["lambda_arn"] = data["lambdaARN"]
    else:
        out["lambda_arn"] = ""
    if data.get("codeHookInterfaceVersion") is not None:
        out["code_hook_interface_version"] = data["codeHookInterfaceVersion"]
    else:
        out["code_hook_interface_version"] = ""
    return out
