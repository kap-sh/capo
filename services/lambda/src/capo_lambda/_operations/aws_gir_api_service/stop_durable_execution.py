"""Generated from Smithy shape ``com.amazonaws.lambda#StopDurableExecution``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_lambda._auth._signers
import capo_lambda._auth._sigv4
import capo_lambda._protocol.eventstream
import capo_lambda.errors.invalid_parameter_value_exception
import capo_lambda.errors.kms_access_denied_exception
import capo_lambda.errors.kms_disabled_exception
import capo_lambda.errors.kms_invalid_state_exception
import capo_lambda.errors.kms_not_found_exception
import capo_lambda.errors.resource_not_found_exception
import capo_lambda.errors.service_exception
import capo_lambda.errors.too_many_requests_exception
import capo_lambda.types.error_object
import capo_lambda.types.execution_timestamp
import capo_lambda.types.stop_durable_execution_request
import capo_lambda.types.stop_durable_execution_response
from capo_lambda._protocol.errors import parse_error_metadata_json
from capo_lambda._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_lambda._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_lambda.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidParameterValueException":
            raise capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data, message
            )
        case "KMSAccessDeniedException":
            raise capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException.from_json(
                data, message
            )
        case "KMSDisabledException":
            raise capo_lambda.errors.kms_disabled_exception.KMSDisabledException.from_json(
                data, message
            )
        case "KMSInvalidStateException":
            raise capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException.from_json(
                data, message
            )
        case "KMSNotFoundException":
            raise capo_lambda.errors.kms_not_found_exception.KMSNotFoundException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "ServiceException":
            raise capo_lambda.errors.service_exception.ServiceException.from_json(
                data, message
            )
        case "TooManyRequestsException":
            raise capo_lambda.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_lambda.types.stop_durable_execution_response.StopDurableExecutionResponse:
    out: capo_lambda.types.stop_durable_execution_response.StopDurableExecutionResponse = capo_lambda.types.stop_durable_execution_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_lambda.types.stop_durable_execution_response.StopDurableExecutionResponse:
    out: capo_lambda.types.stop_durable_execution_response.StopDurableExecutionResponse = capo_lambda.types.stop_durable_execution_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_lambda._auth._signers.Signer | None:
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
            sigv4_config = capo_lambda._auth._sigv4.build_sigv4_auth_scheme(
                "lambda", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_lambda._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_lambda.types.stop_durable_execution_request.StopDurableExecutionRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/2025-12-01/durable-executions/{DurableExecutionArn}/stop"
    )
    url = url.replace(
        "{DurableExecutionArn}", quote(input_["durable_execution_arn"], safe="")
    )
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "error" in input_:
        body: bytes | None = json.dumps(
            capo_lambda.types.error_object.serialize_json(input_["error"]),
            allow_nan=False,
        ).encode()
        headers["content-type"] = "application/json"
    else:
        body = b""
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


def stop_durable_execution(
    options: OperationOptions,
    input_: capo_lambda.types.stop_durable_execution_request.StopDurableExecutionRequest,
) -> tuple[
    capo_lambda.types.stop_durable_execution_response.StopDurableExecutionResponse,
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


async def async_stop_durable_execution(
    options: AsyncOperationOptions,
    input_: capo_lambda.types.stop_durable_execution_request.StopDurableExecutionRequest,
) -> tuple[
    capo_lambda.types.stop_durable_execution_response.StopDurableExecutionResponse,
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
