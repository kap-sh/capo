"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#StartMedicalStreamTranscription``."""

from __future__ import annotations

import json
from typing import Any, cast

import zapros
from typing_extensions import Never

import capo_transcribe_streaming._auth._signers
import capo_transcribe_streaming._auth._sigv4
import capo_transcribe_streaming._iter
import capo_transcribe_streaming._protocol.eventstream
import capo_transcribe_streaming.errors.bad_request_exception
import capo_transcribe_streaming.errors.conflict_exception
import capo_transcribe_streaming.errors.internal_failure_exception
import capo_transcribe_streaming.errors.limit_exceeded_exception
import capo_transcribe_streaming.errors.service_unavailable_exception
import capo_transcribe_streaming.types.audio_stream
import capo_transcribe_streaming.types.language_code
import capo_transcribe_streaming.types.media_encoding
import capo_transcribe_streaming.types.medical_content_identification_type
import capo_transcribe_streaming.types.medical_transcript_result_stream
import capo_transcribe_streaming.types.specialty
import capo_transcribe_streaming.types.start_medical_stream_transcription_request
import capo_transcribe_streaming.types.start_medical_stream_transcription_response
import capo_transcribe_streaming.types.type
from capo_transcribe_streaming._protocol.errors import parse_error_metadata_json
from capo_transcribe_streaming._protocol.eventstream import (
    MessageDecoder,
    async_raw_stream_to_events,
    raw_stream_to_events,
)
from capo_transcribe_streaming._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_transcribe_streaming._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_transcribe_streaming.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            raise capo_transcribe_streaming.errors.bad_request_exception.BadRequestException.from_json(
                data, message
            )
        case "ConflictException":
            raise capo_transcribe_streaming.errors.conflict_exception.ConflictException.from_json(
                data, message
            )
        case "InternalFailureException":
            raise capo_transcribe_streaming.errors.internal_failure_exception.InternalFailureException.from_json(
                data, message
            )
        case "LimitExceededException":
            raise capo_transcribe_streaming.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data, message
            )
        case "ServiceUnavailableException":
            raise capo_transcribe_streaming.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_transcribe_streaming.types.start_medical_stream_transcription_response.StartMedicalStreamTranscriptionResponse:
    _message_decoder = MessageDecoder()
    _union_deser = capo_transcribe_streaming.types.medical_transcript_result_stream.deserialize_event_json
    _iter = cast(Any, response.iter_bytes())
    out: capo_transcribe_streaming.types.start_medical_stream_transcription_response.StartMedicalStreamTranscriptionResponse = {
        "transcript_result_stream": cast(
            Any, raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    if "x-amzn-request-id" in response.headers:
        out["request_id"] = response.headers["x-amzn-request-id"]
    if "x-amzn-transcribe-language-code" in response.headers:
        out["language_code"] = (
            capo_transcribe_streaming.types.language_code.deserialize_json(
                response.headers["x-amzn-transcribe-language-code"]
            )
        )
    if "x-amzn-transcribe-sample-rate" in response.headers:
        out["media_sample_rate_hertz"] = int(
            response.headers["x-amzn-transcribe-sample-rate"]
        )
    if "x-amzn-transcribe-media-encoding" in response.headers:
        out["media_encoding"] = (
            capo_transcribe_streaming.types.media_encoding.deserialize_json(
                response.headers["x-amzn-transcribe-media-encoding"]
            )
        )
    if "x-amzn-transcribe-vocabulary-name" in response.headers:
        out["vocabulary_name"] = response.headers["x-amzn-transcribe-vocabulary-name"]
    if "x-amzn-transcribe-specialty" in response.headers:
        out["specialty"] = capo_transcribe_streaming.types.specialty.deserialize_json(
            response.headers["x-amzn-transcribe-specialty"]
        )
    if "x-amzn-transcribe-type" in response.headers:
        out["type"] = capo_transcribe_streaming.types.type.deserialize_json(
            response.headers["x-amzn-transcribe-type"]
        )
    out["show_speaker_label"] = (
        response.headers["x-amzn-transcribe-show-speaker-label"].lower() == "true"
    )
    if "x-amzn-transcribe-session-id" in response.headers:
        out["session_id"] = response.headers["x-amzn-transcribe-session-id"]
    out["enable_channel_identification"] = (
        response.headers["x-amzn-transcribe-enable-channel-identification"].lower()
        == "true"
    )
    if "x-amzn-transcribe-number-of-channels" in response.headers:
        out["number_of_channels"] = int(
            response.headers["x-amzn-transcribe-number-of-channels"]
        )
    if "x-amzn-transcribe-content-identification-type" in response.headers:
        out["content_identification_type"] = (
            capo_transcribe_streaming.types.medical_content_identification_type.deserialize_json(
                response.headers["x-amzn-transcribe-content-identification-type"]
            )
        )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_transcribe_streaming.types.start_medical_stream_transcription_response.StartMedicalStreamTranscriptionResponse:
    _message_decoder = MessageDecoder()
    _union_deser = capo_transcribe_streaming.types.medical_transcript_result_stream.deserialize_event_json
    _iter = cast(Any, response.async_iter_bytes())
    out: capo_transcribe_streaming.types.start_medical_stream_transcription_response.StartMedicalStreamTranscriptionResponse = {
        "transcript_result_stream": cast(
            Any, async_raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    if "x-amzn-request-id" in response.headers:
        out["request_id"] = response.headers["x-amzn-request-id"]
    if "x-amzn-transcribe-language-code" in response.headers:
        out["language_code"] = (
            capo_transcribe_streaming.types.language_code.deserialize_json(
                response.headers["x-amzn-transcribe-language-code"]
            )
        )
    if "x-amzn-transcribe-sample-rate" in response.headers:
        out["media_sample_rate_hertz"] = int(
            response.headers["x-amzn-transcribe-sample-rate"]
        )
    if "x-amzn-transcribe-media-encoding" in response.headers:
        out["media_encoding"] = (
            capo_transcribe_streaming.types.media_encoding.deserialize_json(
                response.headers["x-amzn-transcribe-media-encoding"]
            )
        )
    if "x-amzn-transcribe-vocabulary-name" in response.headers:
        out["vocabulary_name"] = response.headers["x-amzn-transcribe-vocabulary-name"]
    if "x-amzn-transcribe-specialty" in response.headers:
        out["specialty"] = capo_transcribe_streaming.types.specialty.deserialize_json(
            response.headers["x-amzn-transcribe-specialty"]
        )
    if "x-amzn-transcribe-type" in response.headers:
        out["type"] = capo_transcribe_streaming.types.type.deserialize_json(
            response.headers["x-amzn-transcribe-type"]
        )
    out["show_speaker_label"] = (
        response.headers["x-amzn-transcribe-show-speaker-label"].lower() == "true"
    )
    if "x-amzn-transcribe-session-id" in response.headers:
        out["session_id"] = response.headers["x-amzn-transcribe-session-id"]
    out["enable_channel_identification"] = (
        response.headers["x-amzn-transcribe-enable-channel-identification"].lower()
        == "true"
    )
    if "x-amzn-transcribe-number-of-channels" in response.headers:
        out["number_of_channels"] = int(
            response.headers["x-amzn-transcribe-number-of-channels"]
        )
    if "x-amzn-transcribe-content-identification-type" in response.headers:
        out["content_identification_type"] = (
            capo_transcribe_streaming.types.medical_content_identification_type.deserialize_json(
                response.headers["x-amzn-transcribe-content-identification-type"]
            )
        )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_transcribe_streaming._auth._signers.Signer | None:
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
                capo_transcribe_streaming._auth._sigv4.build_sigv4_auth_scheme(
                    "transcribe", options.region, endpoint_scheme
                )
            )
            if sigv4_config is not None:
                return capo_transcribe_streaming._auth._signers.SigV4Signer(
                    options.credentials_provider,
                    auth_scheme=sigv4_config,
                    event_stream=True,
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_transcribe_streaming.types.start_medical_stream_transcription_request.StartMedicalStreamTranscriptionRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_transcribe_streaming.types.language_code
    import capo_transcribe_streaming.types.media_encoding
    import capo_transcribe_streaming.types.medical_content_identification_type
    import capo_transcribe_streaming.types.specialty
    import capo_transcribe_streaming.types.type

    url = endpoint.url.rstrip("/") + "/medical-stream-transcription"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "language_code" in input_:
        headers["x-amzn-transcribe-language-code"] = (
            capo_transcribe_streaming.types.language_code.serialize_json(
                input_["language_code"]
            )
        )
    if "media_sample_rate_hertz" in input_:
        headers["x-amzn-transcribe-sample-rate"] = str(
            input_["media_sample_rate_hertz"]
        )
    if "media_encoding" in input_:
        headers["x-amzn-transcribe-media-encoding"] = (
            capo_transcribe_streaming.types.media_encoding.serialize_json(
                input_["media_encoding"]
            )
        )
    if "vocabulary_name" in input_:
        headers["x-amzn-transcribe-vocabulary-name"] = input_["vocabulary_name"]
    if "specialty" in input_:
        headers["x-amzn-transcribe-specialty"] = (
            capo_transcribe_streaming.types.specialty.serialize_json(
                input_["specialty"]
            )
        )
    if "type" in input_:
        headers["x-amzn-transcribe-type"] = (
            capo_transcribe_streaming.types.type.serialize_json(input_["type"])
        )
    headers["x-amzn-transcribe-show-speaker-label"] = (
        "true" if input_.get("show_speaker_label", False) else "false"
    )
    if "session_id" in input_:
        headers["x-amzn-transcribe-session-id"] = input_["session_id"]
    headers["x-amzn-transcribe-enable-channel-identification"] = (
        "true" if input_.get("enable_channel_identification", False) else "false"
    )
    if "number_of_channels" in input_:
        headers["x-amzn-transcribe-number-of-channels"] = str(
            input_["number_of_channels"]
        )
    if "content_identification_type" in input_:
        headers["x-amzn-transcribe-content-identification-type"] = (
            capo_transcribe_streaming.types.medical_content_identification_type.serialize_json(
                input_["content_identification_type"]
            )
        )

    body = capo_transcribe_streaming._iter.map_sync_iterator(
        input_["audio_stream"],
        capo_transcribe_streaming.types.audio_stream.serialize_event_json,
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
    input_: capo_transcribe_streaming.types.start_medical_stream_transcription_request.StartMedicalStreamTranscriptionRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_transcribe_streaming.types.language_code
    import capo_transcribe_streaming.types.media_encoding
    import capo_transcribe_streaming.types.medical_content_identification_type
    import capo_transcribe_streaming.types.specialty
    import capo_transcribe_streaming.types.type

    url = endpoint.url.rstrip("/") + "/medical-stream-transcription"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "language_code" in input_:
        headers["x-amzn-transcribe-language-code"] = (
            capo_transcribe_streaming.types.language_code.serialize_json(
                input_["language_code"]
            )
        )
    if "media_sample_rate_hertz" in input_:
        headers["x-amzn-transcribe-sample-rate"] = str(
            input_["media_sample_rate_hertz"]
        )
    if "media_encoding" in input_:
        headers["x-amzn-transcribe-media-encoding"] = (
            capo_transcribe_streaming.types.media_encoding.serialize_json(
                input_["media_encoding"]
            )
        )
    if "vocabulary_name" in input_:
        headers["x-amzn-transcribe-vocabulary-name"] = input_["vocabulary_name"]
    if "specialty" in input_:
        headers["x-amzn-transcribe-specialty"] = (
            capo_transcribe_streaming.types.specialty.serialize_json(
                input_["specialty"]
            )
        )
    if "type" in input_:
        headers["x-amzn-transcribe-type"] = (
            capo_transcribe_streaming.types.type.serialize_json(input_["type"])
        )
    headers["x-amzn-transcribe-show-speaker-label"] = (
        "true" if input_.get("show_speaker_label", False) else "false"
    )
    if "session_id" in input_:
        headers["x-amzn-transcribe-session-id"] = input_["session_id"]
    headers["x-amzn-transcribe-enable-channel-identification"] = (
        "true" if input_.get("enable_channel_identification", False) else "false"
    )
    if "number_of_channels" in input_:
        headers["x-amzn-transcribe-number-of-channels"] = str(
            input_["number_of_channels"]
        )
    if "content_identification_type" in input_:
        headers["x-amzn-transcribe-content-identification-type"] = (
            capo_transcribe_streaming.types.medical_content_identification_type.serialize_json(
                input_["content_identification_type"]
            )
        )

    body = capo_transcribe_streaming._iter.map_async_iterator(
        input_["audio_stream"],
        capo_transcribe_streaming.types.audio_stream.serialize_event_json,
    )

    headers["content-type"] = "application/vnd.amazon-eventstream"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def start_medical_stream_transcription(
    options: OperationOptions,
    input_: capo_transcribe_streaming.types.start_medical_stream_transcription_request.StartMedicalStreamTranscriptionRequest,
) -> tuple[
    capo_transcribe_streaming.types.start_medical_stream_transcription_response.StartMedicalStreamTranscriptionResponse,
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


async def async_start_medical_stream_transcription(
    options: AsyncOperationOptions,
    input_: capo_transcribe_streaming.types.start_medical_stream_transcription_request.StartMedicalStreamTranscriptionRequest,
) -> tuple[
    capo_transcribe_streaming.types.start_medical_stream_transcription_response.StartMedicalStreamTranscriptionResponse,
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
