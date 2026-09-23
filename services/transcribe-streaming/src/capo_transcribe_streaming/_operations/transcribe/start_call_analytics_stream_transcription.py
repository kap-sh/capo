"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#StartCallAnalyticsStreamTranscription``."""

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
import capo_transcribe_streaming.types.call_analytics_language_code
import capo_transcribe_streaming.types.call_analytics_transcript_result_stream
import capo_transcribe_streaming.types.content_identification_type
import capo_transcribe_streaming.types.content_redaction_type
import capo_transcribe_streaming.types.media_encoding
import capo_transcribe_streaming.types.partial_results_stability
import capo_transcribe_streaming.types.start_call_analytics_stream_transcription_request
import capo_transcribe_streaming.types.start_call_analytics_stream_transcription_response
import capo_transcribe_streaming.types.vocabulary_filter_method
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
) -> capo_transcribe_streaming.types.start_call_analytics_stream_transcription_response.StartCallAnalyticsStreamTranscriptionResponse:
    _message_decoder = MessageDecoder()
    _union_deser = capo_transcribe_streaming.types.call_analytics_transcript_result_stream.deserialize_event_json
    _iter = cast(Any, response.iter_bytes())
    out: capo_transcribe_streaming.types.start_call_analytics_stream_transcription_response.StartCallAnalyticsStreamTranscriptionResponse = {
        "call_analytics_transcript_result_stream": cast(
            Any, raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    if "x-amzn-request-id" in response.headers:
        out["request_id"] = response.headers["x-amzn-request-id"]
    if "x-amzn-transcribe-language-code" in response.headers:
        out["language_code"] = (
            capo_transcribe_streaming.types.call_analytics_language_code.deserialize_json(
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
    if "x-amzn-transcribe-session-id" in response.headers:
        out["session_id"] = response.headers["x-amzn-transcribe-session-id"]
    if "x-amzn-transcribe-vocabulary-filter-name" in response.headers:
        out["vocabulary_filter_name"] = response.headers[
            "x-amzn-transcribe-vocabulary-filter-name"
        ]
    if "x-amzn-transcribe-vocabulary-filter-method" in response.headers:
        out["vocabulary_filter_method"] = (
            capo_transcribe_streaming.types.vocabulary_filter_method.deserialize_json(
                response.headers["x-amzn-transcribe-vocabulary-filter-method"]
            )
        )
    if "x-amzn-transcribe-language-model-name" in response.headers:
        out["language_model_name"] = response.headers[
            "x-amzn-transcribe-language-model-name"
        ]
    out["identify_language"] = (
        response.headers["x-amzn-transcribe-identify-language"].lower() == "true"
    )
    if "x-amzn-transcribe-language-options" in response.headers:
        out["language_options"] = response.headers["x-amzn-transcribe-language-options"]
    if "x-amzn-transcribe-preferred-language" in response.headers:
        out["preferred_language"] = (
            capo_transcribe_streaming.types.call_analytics_language_code.deserialize_json(
                response.headers["x-amzn-transcribe-preferred-language"]
            )
        )
    if "x-amzn-transcribe-vocabulary-names" in response.headers:
        out["vocabulary_names"] = response.headers["x-amzn-transcribe-vocabulary-names"]
    if "x-amzn-transcribe-vocabulary-filter-names" in response.headers:
        out["vocabulary_filter_names"] = response.headers[
            "x-amzn-transcribe-vocabulary-filter-names"
        ]
    out["enable_partial_results_stabilization"] = (
        response.headers[
            "x-amzn-transcribe-enable-partial-results-stabilization"
        ].lower()
        == "true"
    )
    if "x-amzn-transcribe-partial-results-stability" in response.headers:
        out["partial_results_stability"] = (
            capo_transcribe_streaming.types.partial_results_stability.deserialize_json(
                response.headers["x-amzn-transcribe-partial-results-stability"]
            )
        )
    if "x-amzn-transcribe-content-identification-type" in response.headers:
        out["content_identification_type"] = (
            capo_transcribe_streaming.types.content_identification_type.deserialize_json(
                response.headers["x-amzn-transcribe-content-identification-type"]
            )
        )
    if "x-amzn-transcribe-content-redaction-type" in response.headers:
        out["content_redaction_type"] = (
            capo_transcribe_streaming.types.content_redaction_type.deserialize_json(
                response.headers["x-amzn-transcribe-content-redaction-type"]
            )
        )
    if "x-amzn-transcribe-pii-entity-types" in response.headers:
        out["pii_entity_types"] = response.headers["x-amzn-transcribe-pii-entity-types"]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_transcribe_streaming.types.start_call_analytics_stream_transcription_response.StartCallAnalyticsStreamTranscriptionResponse:
    _message_decoder = MessageDecoder()
    _union_deser = capo_transcribe_streaming.types.call_analytics_transcript_result_stream.deserialize_event_json
    _iter = cast(Any, response.async_iter_bytes())
    out: capo_transcribe_streaming.types.start_call_analytics_stream_transcription_response.StartCallAnalyticsStreamTranscriptionResponse = {
        "call_analytics_transcript_result_stream": cast(
            Any, async_raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    if "x-amzn-request-id" in response.headers:
        out["request_id"] = response.headers["x-amzn-request-id"]
    if "x-amzn-transcribe-language-code" in response.headers:
        out["language_code"] = (
            capo_transcribe_streaming.types.call_analytics_language_code.deserialize_json(
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
    if "x-amzn-transcribe-session-id" in response.headers:
        out["session_id"] = response.headers["x-amzn-transcribe-session-id"]
    if "x-amzn-transcribe-vocabulary-filter-name" in response.headers:
        out["vocabulary_filter_name"] = response.headers[
            "x-amzn-transcribe-vocabulary-filter-name"
        ]
    if "x-amzn-transcribe-vocabulary-filter-method" in response.headers:
        out["vocabulary_filter_method"] = (
            capo_transcribe_streaming.types.vocabulary_filter_method.deserialize_json(
                response.headers["x-amzn-transcribe-vocabulary-filter-method"]
            )
        )
    if "x-amzn-transcribe-language-model-name" in response.headers:
        out["language_model_name"] = response.headers[
            "x-amzn-transcribe-language-model-name"
        ]
    out["identify_language"] = (
        response.headers["x-amzn-transcribe-identify-language"].lower() == "true"
    )
    if "x-amzn-transcribe-language-options" in response.headers:
        out["language_options"] = response.headers["x-amzn-transcribe-language-options"]
    if "x-amzn-transcribe-preferred-language" in response.headers:
        out["preferred_language"] = (
            capo_transcribe_streaming.types.call_analytics_language_code.deserialize_json(
                response.headers["x-amzn-transcribe-preferred-language"]
            )
        )
    if "x-amzn-transcribe-vocabulary-names" in response.headers:
        out["vocabulary_names"] = response.headers["x-amzn-transcribe-vocabulary-names"]
    if "x-amzn-transcribe-vocabulary-filter-names" in response.headers:
        out["vocabulary_filter_names"] = response.headers[
            "x-amzn-transcribe-vocabulary-filter-names"
        ]
    out["enable_partial_results_stabilization"] = (
        response.headers[
            "x-amzn-transcribe-enable-partial-results-stabilization"
        ].lower()
        == "true"
    )
    if "x-amzn-transcribe-partial-results-stability" in response.headers:
        out["partial_results_stability"] = (
            capo_transcribe_streaming.types.partial_results_stability.deserialize_json(
                response.headers["x-amzn-transcribe-partial-results-stability"]
            )
        )
    if "x-amzn-transcribe-content-identification-type" in response.headers:
        out["content_identification_type"] = (
            capo_transcribe_streaming.types.content_identification_type.deserialize_json(
                response.headers["x-amzn-transcribe-content-identification-type"]
            )
        )
    if "x-amzn-transcribe-content-redaction-type" in response.headers:
        out["content_redaction_type"] = (
            capo_transcribe_streaming.types.content_redaction_type.deserialize_json(
                response.headers["x-amzn-transcribe-content-redaction-type"]
            )
        )
    if "x-amzn-transcribe-pii-entity-types" in response.headers:
        out["pii_entity_types"] = response.headers["x-amzn-transcribe-pii-entity-types"]
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
    input_: capo_transcribe_streaming.types.start_call_analytics_stream_transcription_request.StartCallAnalyticsStreamTranscriptionRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_transcribe_streaming.types.call_analytics_language_code
    import capo_transcribe_streaming.types.content_identification_type
    import capo_transcribe_streaming.types.content_redaction_type
    import capo_transcribe_streaming.types.media_encoding
    import capo_transcribe_streaming.types.partial_results_stability
    import capo_transcribe_streaming.types.vocabulary_filter_method

    url = endpoint.url.rstrip("/") + "/call-analytics-stream-transcription"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "language_code" in input_:
        headers["x-amzn-transcribe-language-code"] = (
            capo_transcribe_streaming.types.call_analytics_language_code.serialize_json(
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
    if "session_id" in input_:
        headers["x-amzn-transcribe-session-id"] = input_["session_id"]
    if "vocabulary_filter_name" in input_:
        headers["x-amzn-transcribe-vocabulary-filter-name"] = input_[
            "vocabulary_filter_name"
        ]
    if "vocabulary_filter_method" in input_:
        headers["x-amzn-transcribe-vocabulary-filter-method"] = (
            capo_transcribe_streaming.types.vocabulary_filter_method.serialize_json(
                input_["vocabulary_filter_method"]
            )
        )
    if "language_model_name" in input_:
        headers["x-amzn-transcribe-language-model-name"] = input_["language_model_name"]
    headers["x-amzn-transcribe-identify-language"] = (
        "true" if input_.get("identify_language", False) else "false"
    )
    if "language_options" in input_:
        headers["x-amzn-transcribe-language-options"] = input_["language_options"]
    if "preferred_language" in input_:
        headers["x-amzn-transcribe-preferred-language"] = (
            capo_transcribe_streaming.types.call_analytics_language_code.serialize_json(
                input_["preferred_language"]
            )
        )
    if "vocabulary_names" in input_:
        headers["x-amzn-transcribe-vocabulary-names"] = input_["vocabulary_names"]
    if "vocabulary_filter_names" in input_:
        headers["x-amzn-transcribe-vocabulary-filter-names"] = input_[
            "vocabulary_filter_names"
        ]
    headers["x-amzn-transcribe-enable-partial-results-stabilization"] = (
        "true" if input_.get("enable_partial_results_stabilization", False) else "false"
    )
    if "partial_results_stability" in input_:
        headers["x-amzn-transcribe-partial-results-stability"] = (
            capo_transcribe_streaming.types.partial_results_stability.serialize_json(
                input_["partial_results_stability"]
            )
        )
    if "content_identification_type" in input_:
        headers["x-amzn-transcribe-content-identification-type"] = (
            capo_transcribe_streaming.types.content_identification_type.serialize_json(
                input_["content_identification_type"]
            )
        )
    if "content_redaction_type" in input_:
        headers["x-amzn-transcribe-content-redaction-type"] = (
            capo_transcribe_streaming.types.content_redaction_type.serialize_json(
                input_["content_redaction_type"]
            )
        )
    if "pii_entity_types" in input_:
        headers["x-amzn-transcribe-pii-entity-types"] = input_["pii_entity_types"]

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
    input_: capo_transcribe_streaming.types.start_call_analytics_stream_transcription_request.StartCallAnalyticsStreamTranscriptionRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_transcribe_streaming.types.call_analytics_language_code
    import capo_transcribe_streaming.types.content_identification_type
    import capo_transcribe_streaming.types.content_redaction_type
    import capo_transcribe_streaming.types.media_encoding
    import capo_transcribe_streaming.types.partial_results_stability
    import capo_transcribe_streaming.types.vocabulary_filter_method

    url = endpoint.url.rstrip("/") + "/call-analytics-stream-transcription"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "language_code" in input_:
        headers["x-amzn-transcribe-language-code"] = (
            capo_transcribe_streaming.types.call_analytics_language_code.serialize_json(
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
    if "session_id" in input_:
        headers["x-amzn-transcribe-session-id"] = input_["session_id"]
    if "vocabulary_filter_name" in input_:
        headers["x-amzn-transcribe-vocabulary-filter-name"] = input_[
            "vocabulary_filter_name"
        ]
    if "vocabulary_filter_method" in input_:
        headers["x-amzn-transcribe-vocabulary-filter-method"] = (
            capo_transcribe_streaming.types.vocabulary_filter_method.serialize_json(
                input_["vocabulary_filter_method"]
            )
        )
    if "language_model_name" in input_:
        headers["x-amzn-transcribe-language-model-name"] = input_["language_model_name"]
    headers["x-amzn-transcribe-identify-language"] = (
        "true" if input_.get("identify_language", False) else "false"
    )
    if "language_options" in input_:
        headers["x-amzn-transcribe-language-options"] = input_["language_options"]
    if "preferred_language" in input_:
        headers["x-amzn-transcribe-preferred-language"] = (
            capo_transcribe_streaming.types.call_analytics_language_code.serialize_json(
                input_["preferred_language"]
            )
        )
    if "vocabulary_names" in input_:
        headers["x-amzn-transcribe-vocabulary-names"] = input_["vocabulary_names"]
    if "vocabulary_filter_names" in input_:
        headers["x-amzn-transcribe-vocabulary-filter-names"] = input_[
            "vocabulary_filter_names"
        ]
    headers["x-amzn-transcribe-enable-partial-results-stabilization"] = (
        "true" if input_.get("enable_partial_results_stabilization", False) else "false"
    )
    if "partial_results_stability" in input_:
        headers["x-amzn-transcribe-partial-results-stability"] = (
            capo_transcribe_streaming.types.partial_results_stability.serialize_json(
                input_["partial_results_stability"]
            )
        )
    if "content_identification_type" in input_:
        headers["x-amzn-transcribe-content-identification-type"] = (
            capo_transcribe_streaming.types.content_identification_type.serialize_json(
                input_["content_identification_type"]
            )
        )
    if "content_redaction_type" in input_:
        headers["x-amzn-transcribe-content-redaction-type"] = (
            capo_transcribe_streaming.types.content_redaction_type.serialize_json(
                input_["content_redaction_type"]
            )
        )
    if "pii_entity_types" in input_:
        headers["x-amzn-transcribe-pii-entity-types"] = input_["pii_entity_types"]

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


def start_call_analytics_stream_transcription(
    options: OperationOptions,
    input_: capo_transcribe_streaming.types.start_call_analytics_stream_transcription_request.StartCallAnalyticsStreamTranscriptionRequest,
) -> tuple[
    capo_transcribe_streaming.types.start_call_analytics_stream_transcription_response.StartCallAnalyticsStreamTranscriptionResponse,
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


async def async_start_call_analytics_stream_transcription(
    options: AsyncOperationOptions,
    input_: capo_transcribe_streaming.types.start_call_analytics_stream_transcription_request.StartCallAnalyticsStreamTranscriptionRequest,
) -> tuple[
    capo_transcribe_streaming.types.start_call_analytics_stream_transcription_response.StartCallAnalyticsStreamTranscriptionResponse,
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
