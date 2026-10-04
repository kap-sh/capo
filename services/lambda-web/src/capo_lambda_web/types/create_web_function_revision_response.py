"""Generated from Smithy shape ``com.amazonaws.lambdaweb#CreateWebFunctionRevisionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_web.types.build_config
    import capo_lambda_web.types.date_time
    import capo_lambda_web.types.description
    import capo_lambda_web.types.function_arn
    import capo_lambda_web.types.kms_key_arn
    import capo_lambda_web.types.revision_arn
    import capo_lambda_web.types.revision_errors
    import capo_lambda_web.types.revision_id
    import capo_lambda_web.types.revision_state
    import capo_lambda_web.types.service_config


class CreateWebFunctionRevisionResponse(TypedDict, closed=True):
    function_arn: "capo_lambda_web.types.function_arn.FunctionArn"
    """<p>The Amazon Resource Name (ARN) of the web function.</p>"""
    revision_arn: "capo_lambda_web.types.revision_arn.RevisionArn"
    """<p>The Amazon Resource Name (ARN) of the revision.</p>"""
    revision_id: "capo_lambda_web.types.revision_id.RevisionId"
    """<p>The identifier of the revision.</p>"""
    description: NotRequired["capo_lambda_web.types.description.Description"]
    """<p>The description of the revision.</p>"""
    kms_key_arn: NotRequired["capo_lambda_web.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt the revision's code and environment variables.</p>"""
    build_config: "capo_lambda_web.types.build_config.BuildConfig"
    service_config: "capo_lambda_web.types.service_config.ServiceConfig"
    state: "capo_lambda_web.types.revision_state.RevisionState"
    """<p>The current state of the revision.</p>"""
    state_reason: "str"
    """<p>The reason for the current state of the revision.</p>"""
    errors: NotRequired["capo_lambda_web.types.revision_errors.RevisionErrors"]
    """<p>A list of errors encountered during revision creation. This field is absent when the revision has no errors.</p>"""
    created_at: "capo_lambda_web.types.date_time.DateTime"
    """<p>The date and time the revision was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWebFunctionRevisionResponse) -> dict:
    out: dict = {}
    out["functionArn"] = value["function_arn"]
    out["revisionArn"] = value["revision_arn"]
    out["revisionId"] = value["revision_id"]
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
    import capo_lambda_web.types.revision_state

    out["state"] = capo_lambda_web.types.revision_state.serialize_json(value["state"])
    out["stateReason"] = value["state_reason"]
    if "errors" in value:
        import capo_lambda_web.types.revision_errors

        out["errors"] = capo_lambda_web.types.revision_errors.serialize_json(
            value["errors"]
        )
    import capo_lambda_web.types.date_time

    out["createdAt"] = capo_lambda_web.types.date_time.serialize_json(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> CreateWebFunctionRevisionResponse:
    out: CreateWebFunctionRevisionResponse = {}  # type: ignore[typeddict-item]
    if data.get("functionArn") is not None:
        out["function_arn"] = data["functionArn"]
    else:
        raise DeserializationError(
            "CreateWebFunctionRevisionResponse.function_arn required"
        )
    if data.get("revisionArn") is not None:
        out["revision_arn"] = data["revisionArn"]
    else:
        raise DeserializationError(
            "CreateWebFunctionRevisionResponse.revision_arn required"
        )
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    else:
        raise DeserializationError(
            "CreateWebFunctionRevisionResponse.revision_id required"
        )
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
            "CreateWebFunctionRevisionResponse.build_config required"
        )
    if data.get("serviceConfig") is not None:
        import capo_lambda_web.types.service_config

        out["service_config"] = capo_lambda_web.types.service_config.deserialize_json(
            data["serviceConfig"]
        )
    else:
        raise DeserializationError(
            "CreateWebFunctionRevisionResponse.service_config required"
        )
    if data.get("state") is not None:
        import capo_lambda_web.types.revision_state

        out["state"] = capo_lambda_web.types.revision_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("CreateWebFunctionRevisionResponse.state required")
    if data.get("stateReason") is not None:
        out["state_reason"] = data["stateReason"]
    else:
        raise DeserializationError(
            "CreateWebFunctionRevisionResponse.state_reason required"
        )
    if data.get("errors") is not None:
        import capo_lambda_web.types.revision_errors

        out["errors"] = capo_lambda_web.types.revision_errors.deserialize_json(
            data["errors"]
        )
    if data.get("createdAt") is not None:
        import capo_lambda_web.types.date_time

        out["created_at"] = capo_lambda_web.types.date_time.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError(
            "CreateWebFunctionRevisionResponse.created_at required"
        )
    return out
