"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#CodeHook``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.lambda_arn
    import capo_lex_model_building_service.types.message_version


class CodeHook(TypedDict, closed=True):
    uri: "capo_lex_model_building_service.types.lambda_arn.LambdaARN"
    """<p>The Amazon Resource Name (ARN) of the Lambda function.</p>"""
    message_version: (
        "capo_lex_model_building_service.types.message_version.MessageVersion"
    )
    """<p>The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see <a>using-lambda</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeHook) -> dict:
    out: dict = {}
    out["uri"] = value["uri"]
    out["messageVersion"] = value["message_version"]
    return out


def deserialize_json(data: dict) -> CodeHook:
    out: CodeHook = {}  # type: ignore[typeddict-item]
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    else:
        out["uri"] = ""
    if data.get("messageVersion") is not None:
        out["message_version"] = data["messageVersion"]
    else:
        out["message_version"] = ""
    return out
