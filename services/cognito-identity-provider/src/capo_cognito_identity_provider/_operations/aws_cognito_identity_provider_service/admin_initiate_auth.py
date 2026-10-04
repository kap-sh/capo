"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminInitiateAuth``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_cognito_identity_provider._auth._signers
import capo_cognito_identity_provider._auth._sigv4
import capo_cognito_identity_provider._protocol.eventstream
import capo_cognito_identity_provider.errors.feature_unavailable_in_tier_exception
import capo_cognito_identity_provider.errors.internal_error_exception
import capo_cognito_identity_provider.errors.invalid_email_role_access_policy_exception
import capo_cognito_identity_provider.errors.invalid_lambda_response_exception
import capo_cognito_identity_provider.errors.invalid_parameter_exception
import capo_cognito_identity_provider.errors.invalid_sms_role_access_policy_exception
import capo_cognito_identity_provider.errors.invalid_sms_role_trust_relationship_exception
import capo_cognito_identity_provider.errors.invalid_user_pool_configuration_exception
import capo_cognito_identity_provider.errors.mfa_method_not_found_exception
import capo_cognito_identity_provider.errors.not_authorized_exception
import capo_cognito_identity_provider.errors.operation_not_enabled_exception
import capo_cognito_identity_provider.errors.password_reset_required_exception
import capo_cognito_identity_provider.errors.resource_not_found_exception
import capo_cognito_identity_provider.errors.too_many_requests_exception
import capo_cognito_identity_provider.errors.unexpected_lambda_exception
import capo_cognito_identity_provider.errors.unsupported_operation_exception
import capo_cognito_identity_provider.errors.user_lambda_validation_exception
import capo_cognito_identity_provider.errors.user_not_confirmed_exception
import capo_cognito_identity_provider.errors.user_not_found_exception
import capo_cognito_identity_provider.types.admin_initiate_auth_request
import capo_cognito_identity_provider.types.admin_initiate_auth_response
import capo_cognito_identity_provider.types.analytics_metadata_type
import capo_cognito_identity_provider.types.auth_flow_type
import capo_cognito_identity_provider.types.auth_parameters_type
import capo_cognito_identity_provider.types.authentication_result_type
import capo_cognito_identity_provider.types.available_challenge_list_type
import capo_cognito_identity_provider.types.challenge_name_type
import capo_cognito_identity_provider.types.challenge_parameters_type
import capo_cognito_identity_provider.types.client_metadata_type
import capo_cognito_identity_provider.types.context_data_type
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
        case "FeatureUnavailableInTierException":
            raise capo_cognito_identity_provider.errors.feature_unavailable_in_tier_exception.FeatureUnavailableInTierException.from_aws_json_1_1(
                data, message
            )
        case "InternalErrorException":
            raise capo_cognito_identity_provider.errors.internal_error_exception.InternalErrorException.from_aws_json_1_1(
                data, message
            )
        case "InvalidEmailRoleAccessPolicyException":
            raise capo_cognito_identity_provider.errors.invalid_email_role_access_policy_exception.InvalidEmailRoleAccessPolicyException.from_aws_json_1_1(
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
        case "InvalidSmsRoleAccessPolicyException":
            raise capo_cognito_identity_provider.errors.invalid_sms_role_access_policy_exception.InvalidSmsRoleAccessPolicyException.from_aws_json_1_1(
                data, message
            )
        case "InvalidSmsRoleTrustRelationshipException":
            raise capo_cognito_identity_provider.errors.invalid_sms_role_trust_relationship_exception.InvalidSmsRoleTrustRelationshipException.from_aws_json_1_1(
                data, message
            )
        case "InvalidUserPoolConfigurationException":
            raise capo_cognito_identity_provider.errors.invalid_user_pool_configuration_exception.InvalidUserPoolConfigurationException.from_aws_json_1_1(
                data, message
            )
        case "MFAMethodNotFoundException":
            raise capo_cognito_identity_provider.errors.mfa_method_not_found_exception.MFAMethodNotFoundException.from_aws_json_1_1(
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
        case "PasswordResetRequiredException":
            raise capo_cognito_identity_provider.errors.password_reset_required_exception.PasswordResetRequiredException.from_aws_json_1_1(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_cognito_identity_provider.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_1(
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
        case "UnsupportedOperationException":
            raise capo_cognito_identity_provider.errors.unsupported_operation_exception.UnsupportedOperationException.from_aws_json_1_1(
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
) -> capo_cognito_identity_provider.types.admin_initiate_auth_response.AdminInitiateAuthResponse:
    out: capo_cognito_identity_provider.types.admin_initiate_auth_response.AdminInitiateAuthResponse = capo_cognito_identity_provider.types.admin_initiate_auth_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_cognito_identity_provider.types.admin_initiate_auth_response.AdminInitiateAuthResponse:
    out: capo_cognito_identity_provider.types.admin_initiate_auth_response.AdminInitiateAuthResponse = capo_cognito_identity_provider.types.admin_initiate_auth_response.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
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
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_cognito_identity_provider.types.admin_initiate_auth_request.AdminInitiateAuthRequest,
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
    headers["X-Amz-Target"] = "AWSCognitoIdentityProviderService.AdminInitiateAuth"
    body: bytes | None = json.dumps(
        capo_cognito_identity_provider.types.admin_initiate_auth_request.serialize_aws_json_1_1(
            input_
        ),
        allow_nan=False,
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def admin_initiate_auth(
    options: OperationOptions,
    input_: capo_cognito_identity_provider.types.admin_initiate_auth_request.AdminInitiateAuthRequest,
) -> tuple[
    capo_cognito_identity_provider.types.admin_initiate_auth_response.AdminInitiateAuthResponse,
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


async def async_admin_initiate_auth(
    options: AsyncOperationOptions,
    input_: capo_cognito_identity_provider.types.admin_initiate_auth_request.AdminInitiateAuthRequest,
) -> tuple[
    capo_cognito_identity_provider.types.admin_initiate_auth_response.AdminInitiateAuthResponse,
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
