"""Generated from Smithy shape ``com.amazonaws.medialive#CreateChannel``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_medialive._auth._signers
import capo_medialive._auth._sigv4
import capo_medialive._protocol.eventstream
import capo_medialive.errors.bad_gateway_exception
import capo_medialive.errors.bad_request_exception
import capo_medialive.errors.conflict_exception
import capo_medialive.errors.forbidden_exception
import capo_medialive.errors.gateway_timeout_exception
import capo_medialive.errors.internal_server_error_exception
import capo_medialive.errors.too_many_requests_exception
import capo_medialive.errors.unprocessable_entity_exception
import capo_medialive.types.__list_of__string
import capo_medialive.types.__list_of_input_attachment
import capo_medialive.types.__list_of_output_destination
import capo_medialive.types.anywhere_settings
import capo_medialive.types.cdi_input_specification
import capo_medialive.types.channel
import capo_medialive.types.channel_class
import capo_medialive.types.channel_engine_version_request
import capo_medialive.types.create_channel_request
import capo_medialive.types.create_channel_response
import capo_medialive.types.encoder_settings
import capo_medialive.types.inference_settings
import capo_medialive.types.input_specification
import capo_medialive.types.linked_channel_settings
import capo_medialive.types.log_level
import capo_medialive.types.maintenance_create_settings
import capo_medialive.types.tags
import capo_medialive.types.vpc_output_settings
from capo_medialive._protocol.errors import parse_error_metadata_json
from capo_medialive._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_medialive._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_medialive.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadGatewayException":
            raise capo_medialive.errors.bad_gateway_exception.BadGatewayException.from_json(
                data, message
            )
        case "BadRequestException":
            raise capo_medialive.errors.bad_request_exception.BadRequestException.from_json(
                data, message
            )
        case "ConflictException":
            raise capo_medialive.errors.conflict_exception.ConflictException.from_json(
                data, message
            )
        case "ForbiddenException":
            raise capo_medialive.errors.forbidden_exception.ForbiddenException.from_json(
                data, message
            )
        case "GatewayTimeoutException":
            raise capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException.from_json(
                data, message
            )
        case "InternalServerErrorException":
            raise capo_medialive.errors.internal_server_error_exception.InternalServerErrorException.from_json(
                data, message
            )
        case "TooManyRequestsException":
            raise capo_medialive.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data, message
            )
        case "UnprocessableEntityException":
            raise capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_medialive.types.create_channel_response.CreateChannelResponse:
    out: capo_medialive.types.create_channel_response.CreateChannelResponse = (
        capo_medialive.types.create_channel_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_medialive.types.create_channel_response.CreateChannelResponse:
    out: capo_medialive.types.create_channel_response.CreateChannelResponse = (
        capo_medialive.types.create_channel_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_medialive._auth._signers.Signer | None:
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
            sigv4_config = capo_medialive._auth._sigv4.build_sigv4_auth_scheme(
                "medialive", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_medialive._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_medialive.types.create_channel_request.CreateChannelRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/prod/channels"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_medialive.types.create_channel_request.serialize_json(input_),
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


def create_channel(
    options: OperationOptions,
    input_: capo_medialive.types.create_channel_request.CreateChannelRequest,
) -> tuple[
    capo_medialive.types.create_channel_response.CreateChannelResponse, zapros.Response
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


async def async_create_channel(
    options: AsyncOperationOptions,
    input_: capo_medialive.types.create_channel_request.CreateChannelRequest,
) -> tuple[
    capo_medialive.types.create_channel_response.CreateChannelResponse, zapros.Response
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
