"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#RunMicrovm``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_lambda_microvms._auth._signers
import capo_lambda_microvms._auth._sigv4
import capo_lambda_microvms._protocol.eventstream
import capo_lambda_microvms.errors.access_denied_exception
import capo_lambda_microvms.errors.conflict_exception
import capo_lambda_microvms.errors.insufficient_capacity_exception
import capo_lambda_microvms.errors.internal_server_exception
import capo_lambda_microvms.errors.resource_not_found_exception
import capo_lambda_microvms.errors.service_quota_exceeded_exception
import capo_lambda_microvms.errors.throttling_exception
import capo_lambda_microvms.errors.validation_exception
import capo_lambda_microvms.types.idle_policy
import capo_lambda_microvms.types.logging
import capo_lambda_microvms.types.microvm_state
import capo_lambda_microvms.types.network_connector_list
import capo_lambda_microvms.types.run_microvm_request
import capo_lambda_microvms.types.run_microvm_response
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
        case "InsufficientCapacityException":
            raise capo_lambda_microvms.errors.insufficient_capacity_exception.InsufficientCapacityException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "ServiceQuotaExceededException":
            raise capo_lambda_microvms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_lambda_microvms.types.run_microvm_response.RunMicrovmResponse:
    out: capo_lambda_microvms.types.run_microvm_response.RunMicrovmResponse = (
        capo_lambda_microvms.types.run_microvm_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_lambda_microvms.types.run_microvm_response.RunMicrovmResponse:
    out: capo_lambda_microvms.types.run_microvm_response.RunMicrovmResponse = (
        capo_lambda_microvms.types.run_microvm_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
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
    input_: capo_lambda_microvms.types.run_microvm_request.RunMicrovmRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2025-09-09/microvms"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_lambda_microvms.types.run_microvm_request.serialize_json(input_),
        allow_nan=False,
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def run_microvm(
    options: OperationOptions,
    input_: capo_lambda_microvms.types.run_microvm_request.RunMicrovmRequest,
) -> tuple[
    capo_lambda_microvms.types.run_microvm_response.RunMicrovmResponse, zapros.Response
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


async def async_run_microvm(
    options: AsyncOperationOptions,
    input_: capo_lambda_microvms.types.run_microvm_request.RunMicrovmRequest,
) -> tuple[
    capo_lambda_microvms.types.run_microvm_response.RunMicrovmResponse, zapros.Response
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
