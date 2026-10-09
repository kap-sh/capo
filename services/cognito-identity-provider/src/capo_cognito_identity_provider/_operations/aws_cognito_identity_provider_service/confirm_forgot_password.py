"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ConfirmForgotPassword``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_cognito_identity_provider._auth._signers
import capo_cognito_identity_provider._auth._sigv4
import capo_cognito_identity_provider._protocol.eventstream
import capo_cognito_identity_provider.errors.code_mismatch_exception
import capo_cognito_identity_provider.errors.expired_code_exception
import capo_cognito_identity_provider.errors.forbidden_exception
import capo_cognito_identity_provider.errors.internal_error_exception
import capo_cognito_identity_provider.errors.invalid_lambda_response_exception
import capo_cognito_identity_provider.errors.invalid_parameter_exception
import capo_cognito_identity_provider.errors.invalid_password_exception
import capo_cognito_identity_provider.errors.limit_exceeded_exception
import capo_cognito_identity_provider.errors.not_authorized_exception
import capo_cognito_identity_provider.errors.operation_not_enabled_exception
import capo_cognito_identity_provider.errors.password_history_policy_violation_exception
import capo_cognito_identity_provider.errors.resource_not_found_exception
import capo_cognito_identity_provider.errors.too_many_failed_attempts_exception
import capo_cognito_identity_provider.errors.too_many_requests_exception
import capo_cognito_identity_provider.errors.unexpected_lambda_exception
import capo_cognito_identity_provider.errors.user_lambda_validation_exception
import capo_cognito_identity_provider.errors.user_not_confirmed_exception
import capo_cognito_identity_provider.errors.user_not_found_exception
import capo_cognito_identity_provider.types.analytics_metadata_type
import capo_cognito_identity_provider.types.client_metadata_type
import capo_cognito_identity_provider.types.confirm_forgot_password_request
import capo_cognito_identity_provider.types.confirm_forgot_password_response
import capo_cognito_identity_provider.types.user_context_data_type
from capo_cognito_identity_provider._protocol.errors import parse_error_metadata_json
from capo_cognito_identity_provider._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_cognito_identity_provider._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_cognito_identity_provider.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "CodeMismatchException":
            raise capo_cognito_identity_provider.errors.code_mismatch_exception.CodeMismatchException.from_aws_json_1_1(
                data, message
            )
        case "ExpiredCodeException":
            raise capo_cognito_identity_provider.errors.expired_code_exception.ExpiredCodeException.from_aws_json_1_1(
                data, message
            )
        case "ForbiddenException":
            raise capo_cognito_identity_provider.errors.forbidden_exception.ForbiddenException.from_aws_json_1_1(
                data, message
            )
        case "InternalErrorException":
            raise capo_cognito_identity_provider.errors.internal_error_exception.InternalErrorException.from_aws_json_1_1(
                data, message
            )
        case "InvalidLambdaResponseException":
            raise capo_cognito_identity_provider.errors.invalid_lambda_response_exception.InvalidLambdaResponseException.from_aws_json_1_1(
                data, message
            )
        case "InvalidParameterException":
            raise capo_cognito_identity_provider.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data, message
            )
        case "InvalidPasswordException":
            raise capo_cognito_identity_provider.errors.invalid_password_exception.InvalidPasswordException.from_aws_json_1_1(
                data, message
            )
        case "LimitExceededException":
            raise capo_cognito_identity_provider.errors.limit_exceeded_exception.LimitExceededException.from_aws_json_1_1(
                data, message
            )
        case "NotAuthorizedException":
            raise capo_cognito_identity_provider.errors.not_authorized_exception.NotAuthorizedException.from_aws_json_1_1(
                data, message
            )
        case "OperationNotEnabledException":
            raise capo_cognito_identity_provider.errors.operation_not_enabled_exception.OperationNotEnabledException.from_aws_json_1_1(
                data, message
            )
        case "PasswordHistoryPolicyViolationException":
            raise capo_cognito_identity_provider.errors.password_history_policy_violation_exception.PasswordHistoryPolicyViolationException.from_aws_json_1_1(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_cognito_identity_provider.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_1(
                data, message
            )
        case "TooManyFailedAttemptsException":
            raise capo_cognito_identity_provider.errors.too_many_failed_attempts_exception.TooManyFailedAttemptsException.from_aws_json_1_1(
                data, message
            )
        case "TooManyRequestsException":
            raise capo_cognito_identity_provider.errors.too_many_requests_exception.TooManyRequestsException.from_aws_json_1_1(
                data, message
            )
        case "UnexpectedLambdaException":
            raise capo_cognito_identity_provider.errors.unexpected_lambda_exception.UnexpectedLambdaException.from_aws_json_1_1(
                data, message
            )
        case "UserLambdaValidationException":
            raise capo_cognito_identity_provider.errors.user_lambda_validation_exception.UserLambdaValidationException.from_aws_json_1_1(
                data, message
            )
        case "UserNotConfirmedException":
            raise capo_cognito_identity_provider.errors.user_not_confirmed_exception.UserNotConfirmedException.from_aws_json_1_1(
                data, message
            )
        case "UserNotFoundException":
            raise capo_cognito_identity_provider.errors.user_not_found_exception.UserNotFoundException.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cognito_identity_provider.types.confirm_forgot_password_response.ConfirmForgotPasswordResponse:
    out: capo_cognito_identity_provider.types.confirm_forgot_password_response.ConfirmForgotPasswordResponse = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_cognito_identity_provider.types.confirm_forgot_password_response.ConfirmForgotPasswordResponse:
    out: capo_cognito_identity_provider.types.confirm_forgot_password_response.ConfirmForgotPasswordResponse = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_cognito_identity_provider._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if (
        options.credentials_provider is not None
        and name_to_schema
        and not name_to_schema.keys() & {"sigv4", "sigv4-s3express"}
    ):
        raise RuntimeError(
            "Endpoint requires an unsupported auth scheme: " + ", ".join(name_to_schema)
        )
    if options.credentials_provider is not None:
        endpoint_scheme = name_to_schema.get("sigv4") or name_to_schema.get(
            "sigv4-s3express"
        )
        if endpoint_scheme is not None or not name_to_schema:
            sigv4_config = (
                capo_cognito_identity_provider._auth._sigv4.build_sigv4_auth_scheme(
                    "cognito-idp", options.region, endpoint_scheme
                )
            )
            if sigv4_config is not None:
                return capo_cognito_identity_provider._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    return None


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_cognito_identity_provider.types.confirm_forgot_password_request.ConfirmForgotPasswordRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "AWSCognitoIdentityProviderService.ConfirmForgotPassword"
    body: bytes | None = json.dumps(
        capo_cognito_identity_provider.types.confirm_forgot_password_request.serialize_aws_json_1_1(
            input_
        ),
        allow_nan=False,
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = (
        None
        if options.anonymous
        else get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    )
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def confirm_forgot_password(
    options: OperationOptions,
    input_: capo_cognito_identity_provider.types.confirm_forgot_password_request.ConfirmForgotPasswordRequest,
) -> tuple[
    capo_cognito_identity_provider.types.confirm_forgot_password_response.ConfirmForgotPasswordResponse,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            raise_error(response, handle_error)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_confirm_forgot_password(
    options: AsyncOperationOptions,
    input_: capo_cognito_identity_provider.types.confirm_forgot_password_request.ConfirmForgotPasswordRequest,
) -> tuple[
    capo_cognito_identity_provider.types.confirm_forgot_password_response.ConfirmForgotPasswordResponse,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 300:
            await response.aread()
            raise_error(response, handle_error)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
