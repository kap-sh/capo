"""Generated from Smithy shape ``com.amazonaws.polly#SynthesizeSpeech``."""

from __future__ import annotations

import json
from typing import Any, cast

import zapros
from typing_extensions import Never

import capo_polly._auth._signers
import capo_polly._auth._sigv4
import capo_polly._protocol.eventstream
import capo_polly.errors.engine_not_supported_exception
import capo_polly.errors.invalid_sample_rate_exception
import capo_polly.errors.invalid_ssml_exception
import capo_polly.errors.language_not_supported_exception
import capo_polly.errors.lexicon_not_found_exception
import capo_polly.errors.marks_not_supported_for_format_exception
import capo_polly.errors.service_failure_exception
import capo_polly.errors.ssml_marks_not_supported_for_text_type_exception
import capo_polly.errors.text_length_exceeded_exception
import capo_polly.types.audio_stream
import capo_polly.types.engine
import capo_polly.types.language_code
import capo_polly.types.lexicon_name_list
import capo_polly.types.output_format
import capo_polly.types.speech_mark_type_list
import capo_polly.types.synthesize_speech_input
import capo_polly.types.synthesize_speech_output
import capo_polly.types.text_type
import capo_polly.types.voice_id
from capo_polly._protocol.errors import parse_error_metadata_json
from capo_polly._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_polly._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_polly.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "EngineNotSupportedException":
            raise capo_polly.errors.engine_not_supported_exception.EngineNotSupportedException.from_json(
                data, message
            )
        case "InvalidSampleRateException":
            raise capo_polly.errors.invalid_sample_rate_exception.InvalidSampleRateException.from_json(
                data, message
            )
        case "InvalidSsmlException":
            raise capo_polly.errors.invalid_ssml_exception.InvalidSsmlException.from_json(
                data, message
            )
        case "LanguageNotSupportedException":
            raise capo_polly.errors.language_not_supported_exception.LanguageNotSupportedException.from_json(
                data, message
            )
        case "LexiconNotFoundException":
            raise capo_polly.errors.lexicon_not_found_exception.LexiconNotFoundException.from_json(
                data, message
            )
        case "MarksNotSupportedForFormatException":
            raise capo_polly.errors.marks_not_supported_for_format_exception.MarksNotSupportedForFormatException.from_json(
                data, message
            )
        case "ServiceFailureException":
            raise capo_polly.errors.service_failure_exception.ServiceFailureException.from_json(
                data, message
            )
        case "SsmlMarksNotSupportedForTextTypeException":
            raise capo_polly.errors.ssml_marks_not_supported_for_text_type_exception.SsmlMarksNotSupportedForTextTypeException.from_json(
                data, message
            )
        case "TextLengthExceededException":
            raise capo_polly.errors.text_length_exceeded_exception.TextLengthExceededException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_polly.types.synthesize_speech_output.SynthesizeSpeechOutput:
    _iter = cast(Any, response.iter_raw())
    out: capo_polly.types.synthesize_speech_output.SynthesizeSpeechOutput = {
        "audio_stream": _iter
    }  # type: ignore[reportAssignmentType]
    if "Content-Type" in response.headers:
        out["content_type"] = response.headers["Content-Type"]
    out["request_characters"] = int(response.headers["x-amzn-RequestCharacters"])
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_polly.types.synthesize_speech_output.SynthesizeSpeechOutput:
    _iter = cast(Any, response.async_iter_raw())
    out: capo_polly.types.synthesize_speech_output.SynthesizeSpeechOutput = {
        "audio_stream": _iter
    }  # type: ignore[reportAssignmentType]
    if "Content-Type" in response.headers:
        out["content_type"] = response.headers["Content-Type"]
    out["request_characters"] = int(response.headers["x-amzn-RequestCharacters"])
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_polly._auth._signers.Signer | None:
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
            sigv4_config = capo_polly._auth._sigv4.build_sigv4_auth_scheme(
                "polly", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_polly._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_polly.types.synthesize_speech_input.SynthesizeSpeechInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v1/speech"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_polly.types.synthesize_speech_input.serialize_json(input_), allow_nan=False
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


def synthesize_speech(
    options: OperationOptions,
    input_: capo_polly.types.synthesize_speech_input.SynthesizeSpeechInput,
) -> tuple[
    capo_polly.types.synthesize_speech_output.SynthesizeSpeechOutput, zapros.Response
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


async def async_synthesize_speech(
    options: AsyncOperationOptions,
    input_: capo_polly.types.synthesize_speech_input.SynthesizeSpeechInput,
) -> tuple[
    capo_polly.types.synthesize_speech_output.SynthesizeSpeechOutput, zapros.Response
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
