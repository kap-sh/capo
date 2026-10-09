"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#PutSession``."""

from __future__ import annotations

import json
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_lex_runtime_service._auth._signers
import capo_lex_runtime_service._auth._sigv4
import capo_lex_runtime_service._protocol.eventstream
import capo_lex_runtime_service.errors.bad_gateway_exception
import capo_lex_runtime_service.errors.bad_request_exception
import capo_lex_runtime_service.errors.conflict_exception
import capo_lex_runtime_service.errors.dependency_failed_exception
import capo_lex_runtime_service.errors.internal_failure_exception
import capo_lex_runtime_service.errors.limit_exceeded_exception
import capo_lex_runtime_service.errors.not_acceptable_exception
import capo_lex_runtime_service.errors.not_found_exception
import capo_lex_runtime_service.types.active_contexts_list
import capo_lex_runtime_service.types.blob_stream
import capo_lex_runtime_service.types.dialog_action
import capo_lex_runtime_service.types.dialog_state
import capo_lex_runtime_service.types.intent_summary_list
import capo_lex_runtime_service.types.message_format_type
import capo_lex_runtime_service.types.put_session_request
import capo_lex_runtime_service.types.put_session_response
import capo_lex_runtime_service.types.string_map
from capo_lex_runtime_service._protocol.errors import parse_error_metadata_json
from capo_lex_runtime_service._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_lex_runtime_service._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_lex_runtime_service.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadGatewayException":
            raise capo_lex_runtime_service.errors.bad_gateway_exception.BadGatewayException.from_json(
                data, message
            )
        case "BadRequestException":
            raise capo_lex_runtime_service.errors.bad_request_exception.BadRequestException.from_json(
                data, message
            )
        case "ConflictException":
            raise capo_lex_runtime_service.errors.conflict_exception.ConflictException.from_json(
                data, message
            )
        case "DependencyFailedException":
            raise capo_lex_runtime_service.errors.dependency_failed_exception.DependencyFailedException.from_json(
                data, message
            )
        case "InternalFailureException":
            raise capo_lex_runtime_service.errors.internal_failure_exception.InternalFailureException.from_json(
                data, message
            )
        case "LimitExceededException":
            raise capo_lex_runtime_service.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data, message
            )
        case "NotAcceptableException":
            raise capo_lex_runtime_service.errors.not_acceptable_exception.NotAcceptableException.from_json(
                data, message
            )
        case "NotFoundException":
            raise capo_lex_runtime_service.errors.not_found_exception.NotFoundException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_lex_runtime_service.types.put_session_response.PutSessionResponse:
    _iter = cast(Any, response.iter_raw())
    out: capo_lex_runtime_service.types.put_session_response.PutSessionResponse = {
        "audio_stream": _iter
    }  # type: ignore[reportAssignmentType]
    if "Content-Type" in response.headers:
        out["content_type"] = response.headers["Content-Type"]
    if "x-amz-lex-intent-name" in response.headers:
        out["intent_name"] = response.headers["x-amz-lex-intent-name"]
    if "x-amz-lex-slots" in response.headers:
        out["slots"] = response.headers["x-amz-lex-slots"]
    if "x-amz-lex-session-attributes" in response.headers:
        out["session_attributes"] = response.headers["x-amz-lex-session-attributes"]
    if "x-amz-lex-message" in response.headers:
        out["message"] = response.headers["x-amz-lex-message"]
    if "x-amz-lex-encoded-message" in response.headers:
        out["encoded_message"] = response.headers["x-amz-lex-encoded-message"]
    if "x-amz-lex-message-format" in response.headers:
        out["message_format"] = (
            capo_lex_runtime_service.types.message_format_type.deserialize_json(
                response.headers["x-amz-lex-message-format"]
            )
        )
    if "x-amz-lex-dialog-state" in response.headers:
        out["dialog_state"] = (
            capo_lex_runtime_service.types.dialog_state.deserialize_json(
                response.headers["x-amz-lex-dialog-state"]
            )
        )
    if "x-amz-lex-slot-to-elicit" in response.headers:
        out["slot_to_elicit"] = response.headers["x-amz-lex-slot-to-elicit"]
    if "x-amz-lex-session-id" in response.headers:
        out["session_id"] = response.headers["x-amz-lex-session-id"]
    if "x-amz-lex-active-contexts" in response.headers:
        out["active_contexts"] = response.headers["x-amz-lex-active-contexts"]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_lex_runtime_service.types.put_session_response.PutSessionResponse:
    _iter = cast(Any, response.async_iter_raw())
    out: capo_lex_runtime_service.types.put_session_response.PutSessionResponse = {
        "audio_stream": _iter
    }  # type: ignore[reportAssignmentType]
    if "Content-Type" in response.headers:
        out["content_type"] = response.headers["Content-Type"]
    if "x-amz-lex-intent-name" in response.headers:
        out["intent_name"] = response.headers["x-amz-lex-intent-name"]
    if "x-amz-lex-slots" in response.headers:
        out["slots"] = response.headers["x-amz-lex-slots"]
    if "x-amz-lex-session-attributes" in response.headers:
        out["session_attributes"] = response.headers["x-amz-lex-session-attributes"]
    if "x-amz-lex-message" in response.headers:
        out["message"] = response.headers["x-amz-lex-message"]
    if "x-amz-lex-encoded-message" in response.headers:
        out["encoded_message"] = response.headers["x-amz-lex-encoded-message"]
    if "x-amz-lex-message-format" in response.headers:
        out["message_format"] = (
            capo_lex_runtime_service.types.message_format_type.deserialize_json(
                response.headers["x-amz-lex-message-format"]
            )
        )
    if "x-amz-lex-dialog-state" in response.headers:
        out["dialog_state"] = (
            capo_lex_runtime_service.types.dialog_state.deserialize_json(
                response.headers["x-amz-lex-dialog-state"]
            )
        )
    if "x-amz-lex-slot-to-elicit" in response.headers:
        out["slot_to_elicit"] = response.headers["x-amz-lex-slot-to-elicit"]
    if "x-amz-lex-session-id" in response.headers:
        out["session_id"] = response.headers["x-amz-lex-session-id"]
    if "x-amz-lex-active-contexts" in response.headers:
        out["active_contexts"] = response.headers["x-amz-lex-active-contexts"]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_lex_runtime_service._auth._signers.Signer | None:
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
            sigv4_config = (
                capo_lex_runtime_service._auth._sigv4.build_sigv4_auth_scheme(
                    "lex", options.region, endpoint_scheme
                )
            )
            if sigv4_config is not None:
                return capo_lex_runtime_service._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_lex_runtime_service.types.put_session_request.PutSessionRequest,
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
        + "/bot/{botName}/alias/{botAlias}/user/{userId}/session"
    )
    url = url.replace("{botName}", quote(input_["bot_name"], safe=""))
    url = url.replace("{botAlias}", quote(input_["bot_alias"], safe=""))
    url = url.replace("{userId}", quote(input_["user_id"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "accept" in input_:
        headers["Accept"] = input_["accept"]
    body: bytes | None = json.dumps(
        capo_lex_runtime_service.types.put_session_request.serialize_json(input_),
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


def put_session(
    options: OperationOptions,
    input_: capo_lex_runtime_service.types.put_session_request.PutSessionRequest,
) -> tuple[
    capo_lex_runtime_service.types.put_session_response.PutSessionResponse,
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


async def async_put_session(
    options: AsyncOperationOptions,
    input_: capo_lex_runtime_service.types.put_session_request.PutSessionRequest,
) -> tuple[
    capo_lex_runtime_service.types.put_session_response.PutSessionResponse,
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
