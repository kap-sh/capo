"""Generated from Smithy shape ``com.amazonaws.comprehend#DetectSyntax``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_comprehend._auth._signers
import capo_comprehend._auth._sigv4
import capo_comprehend._protocol.eventstream
import capo_comprehend.errors.internal_server_exception
import capo_comprehend.errors.invalid_request_exception
import capo_comprehend.errors.text_size_limit_exceeded_exception
import capo_comprehend.errors.unsupported_language_exception
import capo_comprehend.types.detect_syntax_request
import capo_comprehend.types.detect_syntax_response
import capo_comprehend.types.list_of_syntax_tokens
import capo_comprehend.types.syntax_language_code
from capo_comprehend._protocol.errors import parse_error_metadata_json
from capo_comprehend._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_comprehend._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_comprehend.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServerException":
            raise capo_comprehend.errors.internal_server_exception.InternalServerException.from_aws_json_1_1(
                data, message
            )
        case "InvalidRequestException":
            raise capo_comprehend.errors.invalid_request_exception.InvalidRequestException.from_aws_json_1_1(
                data, message
            )
        case "TextSizeLimitExceededException":
            raise capo_comprehend.errors.text_size_limit_exceeded_exception.TextSizeLimitExceededException.from_aws_json_1_1(
                data, message
            )
        case "UnsupportedLanguageException":
            raise capo_comprehend.errors.unsupported_language_exception.UnsupportedLanguageException.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_comprehend.types.detect_syntax_response.DetectSyntaxResponse:
    out: capo_comprehend.types.detect_syntax_response.DetectSyntaxResponse = (
        capo_comprehend.types.detect_syntax_response.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_comprehend.types.detect_syntax_response.DetectSyntaxResponse:
    out: capo_comprehend.types.detect_syntax_response.DetectSyntaxResponse = (
        capo_comprehend.types.detect_syntax_response.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_comprehend._auth._signers.Signer | None:
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
            sigv4_config = capo_comprehend._auth._sigv4.build_sigv4_auth_scheme(
                "comprehend", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_comprehend._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_comprehend.types.detect_syntax_request.DetectSyntaxRequest,
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
    headers["X-Amz-Target"] = "Comprehend_20171127.DetectSyntax"
    body: bytes | None = json.dumps(
        capo_comprehend.types.detect_syntax_request.serialize_aws_json_1_1(input_),
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


def detect_syntax(
    options: OperationOptions,
    input_: capo_comprehend.types.detect_syntax_request.DetectSyntaxRequest,
) -> tuple[
    capo_comprehend.types.detect_syntax_response.DetectSyntaxResponse, zapros.Response
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


async def async_detect_syntax(
    options: AsyncOperationOptions,
    input_: capo_comprehend.types.detect_syntax_request.DetectSyntaxRequest,
) -> tuple[
    capo_comprehend.types.detect_syntax_response.DetectSyntaxResponse, zapros.Response
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
