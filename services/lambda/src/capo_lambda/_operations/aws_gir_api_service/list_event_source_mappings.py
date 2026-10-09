"""Generated from Smithy shape ``com.amazonaws.lambda#ListEventSourceMappings``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_lambda._auth._signers
import capo_lambda._auth._sigv4
import capo_lambda._protocol.eventstream
import capo_lambda.errors.invalid_parameter_value_exception
import capo_lambda.errors.resource_not_found_exception
import capo_lambda.errors.service_exception
import capo_lambda.errors.too_many_requests_exception
import capo_lambda.types.event_source_mappings_list
import capo_lambda.types.list_event_source_mappings_request
import capo_lambda.types.list_event_source_mappings_response
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
) -> capo_lambda.types.list_event_source_mappings_response.ListEventSourceMappingsResponse:
    out: capo_lambda.types.list_event_source_mappings_response.ListEventSourceMappingsResponse = capo_lambda.types.list_event_source_mappings_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_lambda.types.list_event_source_mappings_response.ListEventSourceMappingsResponse:
    out: capo_lambda.types.list_event_source_mappings_response.ListEventSourceMappingsResponse = capo_lambda.types.list_event_source_mappings_response.deserialize_json(
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
    input_: capo_lambda.types.list_event_source_mappings_request.ListEventSourceMappingsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2015-03-31/event-source-mappings"
    params: list[tuple[str, str]] = []
    if "event_source_arn" in input_:
        params.append(("EventSourceArn", input_["event_source_arn"]))
    if "function_name" in input_:
        params.append(("FunctionName", input_["function_name"]))
    if "marker" in input_:
        params.append(("Marker", input_["marker"]))
    if "max_items" in input_:
        params.append(("MaxItems", str(input_["max_items"])))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = (
        None
        if options.anonymous
        else get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    )
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_event_source_mappings(
    options: OperationOptions,
    input_: capo_lambda.types.list_event_source_mappings_request.ListEventSourceMappingsRequest,
) -> tuple[
    capo_lambda.types.list_event_source_mappings_response.ListEventSourceMappingsResponse,
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


async def async_list_event_source_mappings(
    options: AsyncOperationOptions,
    input_: capo_lambda.types.list_event_source_mappings_request.ListEventSourceMappingsRequest,
) -> tuple[
    capo_lambda.types.list_event_source_mappings_response.ListEventSourceMappingsResponse,
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
