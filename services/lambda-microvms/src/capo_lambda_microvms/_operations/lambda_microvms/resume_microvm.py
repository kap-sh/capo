"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#ResumeMicrovm``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_lambda_microvms._auth._signers
import capo_lambda_microvms._auth._sigv4
import capo_lambda_microvms._protocol.eventstream
import capo_lambda_microvms.errors.access_denied_exception
import capo_lambda_microvms.errors.conflict_exception
import capo_lambda_microvms.errors.internal_server_exception
import capo_lambda_microvms.errors.resource_not_found_exception
import capo_lambda_microvms.errors.throttling_exception
import capo_lambda_microvms.errors.validation_exception
import capo_lambda_microvms.types.resume_microvm_request
import capo_lambda_microvms.types.resume_microvm_response
from capo_lambda_microvms._protocol.errors import parse_error_metadata_json
from capo_lambda_microvms._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_lambda_microvms._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_lambda_microvms.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "InternalServerException":
            raise capo_lambda_microvms.errors.internal_server_exception.InternalServerException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_lambda_microvms.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_lambda_microvms.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case "ConflictException":
            raise capo_lambda_microvms.errors.conflict_exception.ConflictException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_lambda_microvms.types.resume_microvm_response.ResumeMicrovmResponse:
    out: capo_lambda_microvms.types.resume_microvm_response.ResumeMicrovmResponse = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_lambda_microvms.types.resume_microvm_response.ResumeMicrovmResponse:
    out: capo_lambda_microvms.types.resume_microvm_response.ResumeMicrovmResponse = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_lambda_microvms._auth._signers.Signer | None:
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
            sigv4_config = capo_lambda_microvms._auth._sigv4.build_sigv4_auth_scheme(
                "lambda", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_lambda_microvms._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_lambda_microvms.types.resume_microvm_request.ResumeMicrovmRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2025-09-09/microvms/{microvmIdentifier}/resume"
    url = url.replace(
        "{microvmIdentifier}", quote(input_["microvm_identifier"], safe="")
    )
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def resume_microvm(
    options: OperationOptions,
    input_: capo_lambda_microvms.types.resume_microvm_request.ResumeMicrovmRequest,
) -> tuple[
    capo_lambda_microvms.types.resume_microvm_response.ResumeMicrovmResponse,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_resume_microvm(
    options: AsyncOperationOptions,
    input_: capo_lambda_microvms.types.resume_microvm_request.ResumeMicrovmRequest,
) -> tuple[
    capo_lambda_microvms.types.resume_microvm_response.ResumeMicrovmResponse,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 300:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
