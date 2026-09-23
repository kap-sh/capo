"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#RecognizeUtterance``."""

from __future__ import annotations

import json
from collections.abc import AsyncIterator, Iterator
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_lex_runtime_v2._auth._signers
import capo_lex_runtime_v2._auth._sigv4
import capo_lex_runtime_v2._body
import capo_lex_runtime_v2._protocol.eventstream
import capo_lex_runtime_v2.errors.access_denied_exception
import capo_lex_runtime_v2.errors.bad_gateway_exception
import capo_lex_runtime_v2.errors.conflict_exception
import capo_lex_runtime_v2.errors.dependency_failed_exception
import capo_lex_runtime_v2.errors.internal_server_exception
import capo_lex_runtime_v2.errors.resource_not_found_exception
import capo_lex_runtime_v2.errors.throttling_exception
import capo_lex_runtime_v2.errors.validation_exception
import capo_lex_runtime_v2.types.blob_stream
import capo_lex_runtime_v2.types.recognize_utterance_request
import capo_lex_runtime_v2.types.recognize_utterance_response
from capo_lex_runtime_v2._protocol.errors import parse_error_metadata_json
from capo_lex_runtime_v2._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_lex_runtime_v2._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_lex_runtime_v2.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_lex_runtime_v2.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "BadGatewayException":
            raise capo_lex_runtime_v2.errors.bad_gateway_exception.BadGatewayException.from_json(
                data, message
            )
        case "ConflictException":
            raise capo_lex_runtime_v2.errors.conflict_exception.ConflictException.from_json(
                data, message
            )
        case "DependencyFailedException":
            raise capo_lex_runtime_v2.errors.dependency_failed_exception.DependencyFailedException.from_json(
                data, message
            )
        case "InternalServerException":
            raise capo_lex_runtime_v2.errors.internal_server_exception.InternalServerException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_lex_runtime_v2.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_lex_runtime_v2.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_lex_runtime_v2.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_lex_runtime_v2.types.recognize_utterance_response.RecognizeUtteranceResponse:
    _iter = cast(Any, response.iter_raw())
    out: capo_lex_runtime_v2.types.recognize_utterance_response.RecognizeUtteranceResponse = {
        "audio_stream": _iter
    }  # type: ignore[reportAssignmentType]
    if "x-amz-lex-input-mode" in response.headers:
        out["input_mode"] = response.headers["x-amz-lex-input-mode"]
    if "Content-Type" in response.headers:
        out["content_type"] = response.headers["Content-Type"]
    if "x-amz-lex-messages" in response.headers:
        out["messages"] = response.headers["x-amz-lex-messages"]
    if "x-amz-lex-interpretations" in response.headers:
        out["interpretations"] = response.headers["x-amz-lex-interpretations"]
    if "x-amz-lex-session-state" in response.headers:
        out["session_state"] = response.headers["x-amz-lex-session-state"]
    if "x-amz-lex-request-attributes" in response.headers:
        out["request_attributes"] = response.headers["x-amz-lex-request-attributes"]
    if "x-amz-lex-session-id" in response.headers:
        out["session_id"] = response.headers["x-amz-lex-session-id"]
    if "x-amz-lex-input-transcript" in response.headers:
        out["input_transcript"] = response.headers["x-amz-lex-input-transcript"]
    if "x-amz-lex-recognized-bot-member" in response.headers:
        out["recognized_bot_member"] = response.headers[
            "x-amz-lex-recognized-bot-member"
        ]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_lex_runtime_v2.types.recognize_utterance_response.RecognizeUtteranceResponse:
    _iter = cast(Any, response.async_iter_raw())
    out: capo_lex_runtime_v2.types.recognize_utterance_response.RecognizeUtteranceResponse = {
        "audio_stream": _iter
    }  # type: ignore[reportAssignmentType]
    if "x-amz-lex-input-mode" in response.headers:
        out["input_mode"] = response.headers["x-amz-lex-input-mode"]
    if "Content-Type" in response.headers:
        out["content_type"] = response.headers["Content-Type"]
    if "x-amz-lex-messages" in response.headers:
        out["messages"] = response.headers["x-amz-lex-messages"]
    if "x-amz-lex-interpretations" in response.headers:
        out["interpretations"] = response.headers["x-amz-lex-interpretations"]
    if "x-amz-lex-session-state" in response.headers:
        out["session_state"] = response.headers["x-amz-lex-session-state"]
    if "x-amz-lex-request-attributes" in response.headers:
        out["request_attributes"] = response.headers["x-amz-lex-request-attributes"]
    if "x-amz-lex-session-id" in response.headers:
        out["session_id"] = response.headers["x-amz-lex-session-id"]
    if "x-amz-lex-input-transcript" in response.headers:
        out["input_transcript"] = response.headers["x-amz-lex-input-transcript"]
    if "x-amz-lex-recognized-bot-member" in response.headers:
        out["recognized_bot_member"] = response.headers[
            "x-amz-lex-recognized-bot-member"
        ]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_lex_runtime_v2._auth._signers.Signer | None:
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
            sigv4_config = capo_lex_runtime_v2._auth._sigv4.build_sigv4_auth_scheme(
                "lex", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_lex_runtime_v2._auth._signers.SigV4Signer(
                    options.credentials_provider,
                    auth_scheme=sigv4_config,
                    unsigned_payload=True,
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_lex_runtime_v2.types.recognize_utterance_request.RecognizeUtteranceRequest,
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
        + "/bots/{botId}/botAliases/{botAliasId}/botLocales/{localeId}/sessions/{sessionId}/utterance"
    )
    url = url.replace("{botId}", quote(input_["bot_id"], safe=""))
    url = url.replace("{botAliasId}", quote(input_["bot_alias_id"], safe=""))
    url = url.replace("{localeId}", quote(input_["locale_id"], safe=""))
    url = url.replace("{sessionId}", quote(input_["session_id"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "session_state" in input_:
        headers["x-amz-lex-session-state"] = input_["session_state"]
    if "request_attributes" in input_:
        headers["x-amz-lex-request-attributes"] = input_["request_attributes"]
    if "request_content_type" in input_:
        headers["Content-Type"] = input_["request_content_type"]
    if "response_content_type" in input_:
        headers["Response-Content-Type"] = input_["response_content_type"]
    body = input_["input_stream"]
    if isinstance(body, capo_lex_runtime_v2._body.Body):
        body = cast(capo_lex_runtime_v2._body.Body[Iterator[bytes]], body)
        stream = body.stream
        if stream is None:
            rebuilt = body.rebuild()
            if rebuilt is None:
                raise RuntimeError("streaming body could not be rebuilt")
            stream, _ = rebuilt
        if "content-length" not in [header.lower() for header in headers]:
            headers["Content-Length"] = str(body.length)
        body = stream
    if isinstance(body, capo_lex_runtime_v2._iter.StaticAnyIterator):
        body = cast(bytes, body.content)
    if not isinstance(body, bytes) and "content-length" not in [
        header.lower() for header in headers
    ]:
        raise ValueError("Content-Length is required for streaming input")
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


async def async_build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_lex_runtime_v2.types.recognize_utterance_request.RecognizeUtteranceRequest,
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
        + "/bots/{botId}/botAliases/{botAliasId}/botLocales/{localeId}/sessions/{sessionId}/utterance"
    )
    url = url.replace("{botId}", quote(input_["bot_id"], safe=""))
    url = url.replace("{botAliasId}", quote(input_["bot_alias_id"], safe=""))
    url = url.replace("{localeId}", quote(input_["locale_id"], safe=""))
    url = url.replace("{sessionId}", quote(input_["session_id"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "session_state" in input_:
        headers["x-amz-lex-session-state"] = input_["session_state"]
    if "request_attributes" in input_:
        headers["x-amz-lex-request-attributes"] = input_["request_attributes"]
    if "request_content_type" in input_:
        headers["Content-Type"] = input_["request_content_type"]
    if "response_content_type" in input_:
        headers["Response-Content-Type"] = input_["response_content_type"]
    body = input_["input_stream"]
    if isinstance(body, capo_lex_runtime_v2._body.Body):
        body = cast(capo_lex_runtime_v2._body.Body[AsyncIterator[bytes]], body)
        stream = body.stream
        if stream is None:
            rebuilt = await body.arebuild()
            if rebuilt is None:
                raise RuntimeError("streaming body could not be rebuilt")
            stream, _ = rebuilt
        if "content-length" not in [header.lower() for header in headers]:
            headers["Content-Length"] = str(body.length)
        body = stream
    if isinstance(body, capo_lex_runtime_v2._iter.StaticAnyIterator):
        body = cast(bytes, body.content)
    if not isinstance(body, bytes) and "content-length" not in [
        header.lower() for header in headers
    ]:
        raise ValueError("Content-Length is required for streaming input")
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def recognize_utterance(
    options: OperationOptions,
    input_: capo_lex_runtime_v2.types.recognize_utterance_request.RecognizeUtteranceRequest,
) -> tuple[
    capo_lex_runtime_v2.types.recognize_utterance_response.RecognizeUtteranceResponse,
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


async def async_recognize_utterance(
    options: AsyncOperationOptions,
    input_: capo_lex_runtime_v2.types.recognize_utterance_request.RecognizeUtteranceRequest,
) -> tuple[
    capo_lex_runtime_v2.types.recognize_utterance_response.RecognizeUtteranceResponse,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(
        await async_build_request(options, input_)
    )
    try:
        if response.status >= 300:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
