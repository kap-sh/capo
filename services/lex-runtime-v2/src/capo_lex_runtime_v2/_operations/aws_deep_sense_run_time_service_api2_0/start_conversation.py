"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#StartConversation``."""

from __future__ import annotations

import json
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_lex_runtime_v2._auth._signers
import capo_lex_runtime_v2._auth._sigv4
import capo_lex_runtime_v2._iter
import capo_lex_runtime_v2._protocol.eventstream
import capo_lex_runtime_v2.errors.access_denied_exception
import capo_lex_runtime_v2.errors.internal_server_exception
import capo_lex_runtime_v2.errors.throttling_exception
import capo_lex_runtime_v2.errors.validation_exception
import capo_lex_runtime_v2.types.conversation_mode
import capo_lex_runtime_v2.types.start_conversation_request
import capo_lex_runtime_v2.types.start_conversation_request_event_stream
import capo_lex_runtime_v2.types.start_conversation_response
import capo_lex_runtime_v2.types.start_conversation_response_event_stream
from capo_lex_runtime_v2._protocol.errors import parse_error_metadata_json
from capo_lex_runtime_v2._protocol.eventstream import (
    MessageDecoder,
    async_raw_stream_to_events,
    raw_stream_to_events,
)
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
        case "InternalServerException":
            raise capo_lex_runtime_v2.errors.internal_server_exception.InternalServerException.from_json(
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
) -> capo_lex_runtime_v2.types.start_conversation_response.StartConversationResponse:
    _message_decoder = MessageDecoder()
    _union_deser = capo_lex_runtime_v2.types.start_conversation_response_event_stream.deserialize_event_json
    _iter = cast(Any, response.iter_bytes())
    out: capo_lex_runtime_v2.types.start_conversation_response.StartConversationResponse = {
        "response_event_stream": cast(
            Any, raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_lex_runtime_v2.types.start_conversation_response.StartConversationResponse:
    _message_decoder = MessageDecoder()
    _union_deser = capo_lex_runtime_v2.types.start_conversation_response_event_stream.deserialize_event_json
    _iter = cast(Any, response.async_iter_bytes())
    out: capo_lex_runtime_v2.types.start_conversation_response.StartConversationResponse = {
        "response_event_stream": cast(
            Any, async_raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
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
                    event_stream=True,
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_lex_runtime_v2.types.start_conversation_request.StartConversationRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_lex_runtime_v2.types.conversation_mode

    url = (
        endpoint.url.rstrip("/")
        + "/bots/{botId}/botAliases/{botAliasId}/botLocales/{localeId}/sessions/{sessionId}/conversation"
    )
    url = url.replace("{botId}", quote(input_["bot_id"], safe=""))
    url = url.replace("{botAliasId}", quote(input_["bot_alias_id"], safe=""))
    url = url.replace("{localeId}", quote(input_["locale_id"], safe=""))
    url = url.replace("{sessionId}", quote(input_["session_id"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "conversation_mode" in input_:
        headers["x-amz-lex-conversation-mode"] = (
            capo_lex_runtime_v2.types.conversation_mode.serialize_json(
                input_["conversation_mode"]
            )
        )

    body = capo_lex_runtime_v2._iter.map_sync_iterator(
        input_["request_event_stream"],
        capo_lex_runtime_v2.types.start_conversation_request_event_stream.serialize_event_json,
    )

    headers["content-type"] = "application/vnd.amazon-eventstream"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def async_build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_lex_runtime_v2.types.start_conversation_request.StartConversationRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_lex_runtime_v2.types.conversation_mode

    url = (
        endpoint.url.rstrip("/")
        + "/bots/{botId}/botAliases/{botAliasId}/botLocales/{localeId}/sessions/{sessionId}/conversation"
    )
    url = url.replace("{botId}", quote(input_["bot_id"], safe=""))
    url = url.replace("{botAliasId}", quote(input_["bot_alias_id"], safe=""))
    url = url.replace("{localeId}", quote(input_["locale_id"], safe=""))
    url = url.replace("{sessionId}", quote(input_["session_id"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "conversation_mode" in input_:
        headers["x-amz-lex-conversation-mode"] = (
            capo_lex_runtime_v2.types.conversation_mode.serialize_json(
                input_["conversation_mode"]
            )
        )

    body = capo_lex_runtime_v2._iter.map_async_iterator(
        input_["request_event_stream"],
        capo_lex_runtime_v2.types.start_conversation_request_event_stream.serialize_event_json,
    )

    headers["content-type"] = "application/vnd.amazon-eventstream"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def start_conversation(
    options: OperationOptions,
    input_: capo_lex_runtime_v2.types.start_conversation_request.StartConversationRequest,
) -> tuple[
    capo_lex_runtime_v2.types.start_conversation_response.StartConversationResponse,
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


async def async_start_conversation(
    options: AsyncOperationOptions,
    input_: capo_lex_runtime_v2.types.start_conversation_request.StartConversationRequest,
) -> tuple[
    capo_lex_runtime_v2.types.start_conversation_response.StartConversationResponse,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(
        async_build_request(options, input_)
    )
    try:
        if response.status >= 300:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
