"""Generated from Smithy shape ``com.amazonaws.lambdaweb#CreateWebFunctionRevisionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_web.types.build_config
    import capo_lambda_web.types.description
    import capo_lambda_web.types.function_name
    import capo_lambda_web.types.kms_key_arn
    import capo_lambda_web.types.service_config


class CreateWebFunctionRevisionRequest(TypedDict, closed=True):
    function_name: "capo_lambda_web.types.function_name.FunctionName"
    """<p>The name of the web function. You can specify the function name or the function ARN. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    description: NotRequired["capo_lambda_web.types.description.Description"]
    """<p>A description of the revision.</p>"""
    kms_key_arn: NotRequired["capo_lambda_web.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the AWS Key Management Service (AWS KMS) key used to encrypt the revision's code and environment variables.</p>"""
    build_config: "capo_lambda_web.types.build_config.BuildConfig"
    """<p>The build configuration for the revision, including code location and runtime settings.</p>"""
    service_config: "capo_lambda_web.types.service_config.ServiceConfig"
    """<p>The service configuration for the revision, including execution role, timeout, and concurrency settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWebFunctionRevisionRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    import capo_lambda_web.types.build_config

    out["buildConfig"] = capo_lambda_web.types.build_config.serialize_json(
        value["build_config"]
    )
    import capo_lambda_web.types.service_config

    out["serviceConfig"] = capo_lambda_web.types.service_config.serialize_json(
        value["service_config"]
    )
    return out


def deserialize_json(data: dict) -> CreateWebFunctionRevisionRequest:
    out: CreateWebFunctionRevisionRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("buildConfig") is not None:
        import capo_lambda_web.types.build_config

        out["build_config"] = capo_lambda_web.types.build_config.deserialize_json(
            data["buildConfig"]
        )
    else:
        raise DeserializationError(
            "CreateWebFunctionRevisionRequest.build_config required"
        )
    if data.get("serviceConfig") is not None:
        import capo_lambda_web.types.service_config

        out["service_config"] = capo_lambda_web.types.service_config.deserialize_json(
            data["serviceConfig"]
        )
    else:
        raise DeserializationError(
            "CreateWebFunctionRevisionRequest.service_config required"
        )
    return out
