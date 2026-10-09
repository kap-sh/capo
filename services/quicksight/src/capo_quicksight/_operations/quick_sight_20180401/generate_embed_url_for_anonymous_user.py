"""Generated from Smithy shape ``com.amazonaws.quicksight#GenerateEmbedUrlForAnonymousUser``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_quicksight._auth._signers
import capo_quicksight._auth._sigv4
import capo_quicksight._protocol.eventstream
import capo_quicksight.errors.access_denied_exception
import capo_quicksight.errors.internal_failure_exception
import capo_quicksight.errors.invalid_parameter_value_exception
import capo_quicksight.errors.resource_not_found_exception
import capo_quicksight.errors.session_lifetime_in_minutes_invalid_exception
import capo_quicksight.errors.throttling_exception
import capo_quicksight.errors.unsupported_pricing_plan_exception
import capo_quicksight.errors.unsupported_user_edition_exception
import capo_quicksight.types.anonymous_user_embedding_experience_configuration
import capo_quicksight.types.arn_list
import capo_quicksight.types.generate_embed_url_for_anonymous_user_request
import capo_quicksight.types.generate_embed_url_for_anonymous_user_response
import capo_quicksight.types.session_tag_list
import capo_quicksight.types.string_list
from capo_quicksight._protocol.errors import parse_error_metadata_json
from capo_quicksight._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_quicksight._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_quicksight.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_quicksight.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "InternalFailureException":
            raise capo_quicksight.errors.internal_failure_exception.InternalFailureException.from_json(
                data, message
            )
        case "InvalidParameterValueException":
            raise capo_quicksight.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_quicksight.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "SessionLifetimeInMinutesInvalidException":
            raise capo_quicksight.errors.session_lifetime_in_minutes_invalid_exception.SessionLifetimeInMinutesInvalidException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_quicksight.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case "UnsupportedPricingPlanException":
            raise capo_quicksight.errors.unsupported_pricing_plan_exception.UnsupportedPricingPlanException.from_json(
                data, message
            )
        case "UnsupportedUserEditionException":
            raise capo_quicksight.errors.unsupported_user_edition_exception.UnsupportedUserEditionException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_quicksight.types.generate_embed_url_for_anonymous_user_response.GenerateEmbedUrlForAnonymousUserResponse:
    out: capo_quicksight.types.generate_embed_url_for_anonymous_user_response.GenerateEmbedUrlForAnonymousUserResponse = capo_quicksight.types.generate_embed_url_for_anonymous_user_response.deserialize_json(
        json.loads(response.read())
    )
    out["status"] = response.status
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_quicksight.types.generate_embed_url_for_anonymous_user_response.GenerateEmbedUrlForAnonymousUserResponse:
    out: capo_quicksight.types.generate_embed_url_for_anonymous_user_response.GenerateEmbedUrlForAnonymousUserResponse = capo_quicksight.types.generate_embed_url_for_anonymous_user_response.deserialize_json(
        json.loads(await response.aread())
    )
    out["status"] = response.status
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_quicksight._auth._signers.Signer | None:
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
            sigv4_config = capo_quicksight._auth._sigv4.build_sigv4_auth_scheme(
                "quicksight", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_quicksight._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_quicksight.types.generate_embed_url_for_anonymous_user_request.GenerateEmbedUrlForAnonymousUserRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/accounts/{AwsAccountId}/embed-url/anonymous-user"
    url = url.replace("{AwsAccountId}", quote(input_["aws_account_id"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_quicksight.types.generate_embed_url_for_anonymous_user_request.serialize_json(
            input_
        ),
        allow_nan=False,
    ).encode()
    headers["content-type"] = "application/json"
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


def generate_embed_url_for_anonymous_user(
    options: OperationOptions,
    input_: capo_quicksight.types.generate_embed_url_for_anonymous_user_request.GenerateEmbedUrlForAnonymousUserRequest,
) -> tuple[
    capo_quicksight.types.generate_embed_url_for_anonymous_user_response.GenerateEmbedUrlForAnonymousUserResponse,
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


async def async_generate_embed_url_for_anonymous_user(
    options: AsyncOperationOptions,
    input_: capo_quicksight.types.generate_embed_url_for_anonymous_user_request.GenerateEmbedUrlForAnonymousUserRequest,
) -> tuple[
    capo_quicksight.types.generate_embed_url_for_anonymous_user_response.GenerateEmbedUrlForAnonymousUserResponse,
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
