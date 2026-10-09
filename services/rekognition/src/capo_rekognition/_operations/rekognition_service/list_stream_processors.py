"""Generated from Smithy shape ``com.amazonaws.rekognition#ListStreamProcessors``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_rekognition._auth._signers
import capo_rekognition._auth._sigv4
import capo_rekognition._protocol.eventstream
import capo_rekognition.errors.access_denied_exception
import capo_rekognition.errors.internal_server_error
import capo_rekognition.errors.invalid_pagination_token_exception
import capo_rekognition.errors.invalid_parameter_exception
import capo_rekognition.errors.provisioned_throughput_exceeded_exception
import capo_rekognition.errors.throttling_exception
import capo_rekognition.types.list_stream_processors_request
import capo_rekognition.types.list_stream_processors_response
import capo_rekognition.types.stream_processor_list
from capo_rekognition._protocol.errors import parse_error_metadata_json
from capo_rekognition._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_rekognition._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_rekognition.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_rekognition.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data, message
            )
        case "InternalServerError":
            raise capo_rekognition.errors.internal_server_error.InternalServerError.from_aws_json_1_1(
                data, message
            )
        case "InvalidPaginationTokenException":
            raise capo_rekognition.errors.invalid_pagination_token_exception.InvalidPaginationTokenException.from_aws_json_1_1(
                data, message
            )
        case "InvalidParameterException":
            raise capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data, message
            )
        case "ProvisionedThroughputExceededException":
            raise capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException.from_aws_json_1_1(
                data, message
            )
        case "ThrottlingException":
            raise capo_rekognition.errors.throttling_exception.ThrottlingException.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> (
    capo_rekognition.types.list_stream_processors_response.ListStreamProcessorsResponse
):
    out: capo_rekognition.types.list_stream_processors_response.ListStreamProcessorsResponse = capo_rekognition.types.list_stream_processors_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> (
    capo_rekognition.types.list_stream_processors_response.ListStreamProcessorsResponse
):
    out: capo_rekognition.types.list_stream_processors_response.ListStreamProcessorsResponse = capo_rekognition.types.list_stream_processors_response.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_rekognition._auth._signers.Signer | None:
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
            sigv4_config = capo_rekognition._auth._sigv4.build_sigv4_auth_scheme(
                "rekognition", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_rekognition._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_rekognition.types.list_stream_processors_request.ListStreamProcessorsRequest,
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
    headers["X-Amz-Target"] = "RekognitionService.ListStreamProcessors"
    body: bytes | None = json.dumps(
        capo_rekognition.types.list_stream_processors_request.serialize_aws_json_1_1(
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


def list_stream_processors(
    options: OperationOptions,
    input_: capo_rekognition.types.list_stream_processors_request.ListStreamProcessorsRequest,
) -> tuple[
    capo_rekognition.types.list_stream_processors_response.ListStreamProcessorsResponse,
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


async def async_list_stream_processors(
    options: AsyncOperationOptions,
    input_: capo_rekognition.types.list_stream_processors_request.ListStreamProcessorsRequest,
) -> tuple[
    capo_rekognition.types.list_stream_processors_response.ListStreamProcessorsResponse,
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
