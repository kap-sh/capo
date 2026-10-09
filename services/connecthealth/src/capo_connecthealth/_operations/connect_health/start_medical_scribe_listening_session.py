"""Generated from Smithy shape ``com.amazonaws.connecthealth#StartMedicalScribeListeningSession``."""

from __future__ import annotations

import json
from typing import Any, cast

import zapros
from typing_extensions import Never

import capo_connecthealth._auth._signers
import capo_connecthealth._auth._sigv4
import capo_connecthealth._iter
import capo_connecthealth._protocol.eventstream
import capo_connecthealth.errors.access_denied_exception
import capo_connecthealth.errors.internal_server_exception
import capo_connecthealth.errors.resource_not_found_exception
import capo_connecthealth.errors.service_quota_exceeded_exception
import capo_connecthealth.errors.throttling_exception
import capo_connecthealth.errors.validation_exception
import capo_connecthealth.types.medical_scribe_input_stream
import capo_connecthealth.types.medical_scribe_language_code
import capo_connecthealth.types.medical_scribe_media_encoding
import capo_connecthealth.types.medical_scribe_output_stream
import capo_connecthealth.types.start_medical_scribe_listening_session_input
import capo_connecthealth.types.start_medical_scribe_listening_session_output
from capo_connecthealth._protocol.errors import parse_error_metadata_json
from capo_connecthealth._protocol.eventstream import (
    MessageDecoder,
    async_raw_stream_to_events,
    raw_stream_to_events,
)
from capo_connecthealth._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_connecthealth._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_connecthealth.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_connecthealth.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "InternalServerException":
            raise capo_connecthealth.errors.internal_server_exception.InternalServerException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_connecthealth.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "ServiceQuotaExceededException":
            raise capo_connecthealth.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_connecthealth.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_connecthealth.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_connecthealth.types.start_medical_scribe_listening_session_output.StartMedicalScribeListeningSessionOutput:
    _message_decoder = MessageDecoder()
    _union_deser = (
        capo_connecthealth.types.medical_scribe_output_stream.deserialize_event_json
    )
    _iter = cast(Any, response.iter_bytes())
    out: capo_connecthealth.types.start_medical_scribe_listening_session_output.StartMedicalScribeListeningSessionOutput = {
        "response_stream": cast(
            Any, raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    if "x-amzn-medscribe-session-id" in response.headers:
        out["session_id"] = response.headers["x-amzn-medscribe-session-id"]
    if "x-amzn-medscribe-domain-id" in response.headers:
        out["domain_id"] = response.headers["x-amzn-medscribe-domain-id"]
    if "x-amzn-medscribe-subscription-id" in response.headers:
        out["subscription_id"] = response.headers["x-amzn-medscribe-subscription-id"]
    if "x-amzn-request-id" in response.headers:
        out["request_id"] = response.headers["x-amzn-request-id"]
    if "x-amzn-medscribe-language-code" in response.headers:
        out["language_code"] = (
            capo_connecthealth.types.medical_scribe_language_code.deserialize_json(
                response.headers["x-amzn-medscribe-language-code"]
            )
        )
    if "x-amzn-medscribe-sample-rate" in response.headers:
        out["media_sample_rate_hertz"] = int(
            response.headers["x-amzn-medscribe-sample-rate"]
        )
    if "x-amzn-medscribe-media-encoding" in response.headers:
        out["media_encoding"] = (
            capo_connecthealth.types.medical_scribe_media_encoding.deserialize_json(
                response.headers["x-amzn-medscribe-media-encoding"]
            )
        )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_connecthealth.types.start_medical_scribe_listening_session_output.StartMedicalScribeListeningSessionOutput:
    _message_decoder = MessageDecoder()
    _union_deser = (
        capo_connecthealth.types.medical_scribe_output_stream.deserialize_event_json
    )
    _iter = cast(Any, response.async_iter_bytes())
    out: capo_connecthealth.types.start_medical_scribe_listening_session_output.StartMedicalScribeListeningSessionOutput = {
        "response_stream": cast(
            Any, async_raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    if "x-amzn-medscribe-session-id" in response.headers:
        out["session_id"] = response.headers["x-amzn-medscribe-session-id"]
    if "x-amzn-medscribe-domain-id" in response.headers:
        out["domain_id"] = response.headers["x-amzn-medscribe-domain-id"]
    if "x-amzn-medscribe-subscription-id" in response.headers:
        out["subscription_id"] = response.headers["x-amzn-medscribe-subscription-id"]
    if "x-amzn-request-id" in response.headers:
        out["request_id"] = response.headers["x-amzn-request-id"]
    if "x-amzn-medscribe-language-code" in response.headers:
        out["language_code"] = (
            capo_connecthealth.types.medical_scribe_language_code.deserialize_json(
                response.headers["x-amzn-medscribe-language-code"]
            )
        )
    if "x-amzn-medscribe-sample-rate" in response.headers:
        out["media_sample_rate_hertz"] = int(
            response.headers["x-amzn-medscribe-sample-rate"]
        )
    if "x-amzn-medscribe-media-encoding" in response.headers:
        out["media_encoding"] = (
            capo_connecthealth.types.medical_scribe_media_encoding.deserialize_json(
                response.headers["x-amzn-medscribe-media-encoding"]
            )
        )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_connecthealth._auth._signers.Signer | None:
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
            sigv4_config = capo_connecthealth._auth._sigv4.build_sigv4_auth_scheme(
                "health-agent", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_connecthealth._auth._signers.SigV4Signer(
                    options.credentials_provider,
                    auth_scheme=sigv4_config,
                    event_stream=True,
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_connecthealth.types.start_medical_scribe_listening_session_input.StartMedicalScribeListeningSessionInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    import capo_connecthealth.types.medical_scribe_language_code
    import capo_connecthealth.types.medical_scribe_media_encoding

    url = endpoint.url.rstrip("/") + "/medical-scribe-stream/"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "session_id" in input_:
        headers["x-amzn-medscribe-session-id"] = input_["session_id"]
    if "domain_id" in input_:
        headers["x-amzn-medscribe-domain-id"] = input_["domain_id"]
    if "subscription_id" in input_:
        headers["x-amzn-medscribe-subscription-id"] = input_["subscription_id"]
    if "language_code" in input_:
        headers["x-amzn-medscribe-language-code"] = (
            capo_connecthealth.types.medical_scribe_language_code.serialize_json(
                input_["language_code"]
            )
        )
    if "media_sample_rate_hertz" in input_:
        headers["x-amzn-medscribe-sample-rate"] = str(input_["media_sample_rate_hertz"])
    if "media_encoding" in input_:
        headers["x-amzn-medscribe-media-encoding"] = (
            capo_connecthealth.types.medical_scribe_media_encoding.serialize_json(
                input_["media_encoding"]
            )
        )

    body = capo_connecthealth._iter.map_sync_iterator(
        input_["input_stream"],
        capo_connecthealth.types.medical_scribe_input_stream.serialize_event_json,
    )

    headers["content-type"] = "application/vnd.amazon-eventstream"
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


def async_build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_connecthealth.types.start_medical_scribe_listening_session_input.StartMedicalScribeListeningSessionInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    import capo_connecthealth.types.medical_scribe_language_code
    import capo_connecthealth.types.medical_scribe_media_encoding

    url = endpoint.url.rstrip("/") + "/medical-scribe-stream/"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "session_id" in input_:
        headers["x-amzn-medscribe-session-id"] = input_["session_id"]
    if "domain_id" in input_:
        headers["x-amzn-medscribe-domain-id"] = input_["domain_id"]
    if "subscription_id" in input_:
        headers["x-amzn-medscribe-subscription-id"] = input_["subscription_id"]
    if "language_code" in input_:
        headers["x-amzn-medscribe-language-code"] = (
            capo_connecthealth.types.medical_scribe_language_code.serialize_json(
                input_["language_code"]
            )
        )
    if "media_sample_rate_hertz" in input_:
        headers["x-amzn-medscribe-sample-rate"] = str(input_["media_sample_rate_hertz"])
    if "media_encoding" in input_:
        headers["x-amzn-medscribe-media-encoding"] = (
            capo_connecthealth.types.medical_scribe_media_encoding.serialize_json(
                input_["media_encoding"]
            )
        )

    body = capo_connecthealth._iter.map_async_iterator(
        input_["input_stream"],
        capo_connecthealth.types.medical_scribe_input_stream.serialize_event_json,
    )

    headers["content-type"] = "application/vnd.amazon-eventstream"
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


def start_medical_scribe_listening_session(
    options: OperationOptions,
    input_: capo_connecthealth.types.start_medical_scribe_listening_session_input.StartMedicalScribeListeningSessionInput,
) -> tuple[
    capo_connecthealth.types.start_medical_scribe_listening_session_output.StartMedicalScribeListeningSessionOutput,
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


async def async_start_medical_scribe_listening_session(
    options: AsyncOperationOptions,
    input_: capo_connecthealth.types.start_medical_scribe_listening_session_input.StartMedicalScribeListeningSessionInput,
) -> tuple[
    capo_connecthealth.types.start_medical_scribe_listening_session_output.StartMedicalScribeListeningSessionOutput,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(
        async_build_request(options, input_)
    )
    try:
        if response.status >= 300:
            await response.aread()
            raise_error(response, handle_error)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
