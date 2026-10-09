"""Generated from Smithy shape ``com.amazonaws.polly#PutLexicon``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_polly._auth._signers
import capo_polly._auth._sigv4
import capo_polly._protocol.eventstream
import capo_polly.errors.invalid_lexicon_exception
import capo_polly.errors.lexicon_size_exceeded_exception
import capo_polly.errors.max_lexeme_length_exceeded_exception
import capo_polly.errors.max_lexicons_number_exceeded_exception
import capo_polly.errors.service_failure_exception
import capo_polly.errors.unsupported_pls_alphabet_exception
import capo_polly.errors.unsupported_pls_language_exception
import capo_polly.types.put_lexicon_input
import capo_polly.types.put_lexicon_output
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
        case "InvalidLexiconException":
            raise capo_polly.errors.invalid_lexicon_exception.InvalidLexiconException.from_json(
                data, message
            )
        case "LexiconSizeExceededException":
            raise capo_polly.errors.lexicon_size_exceeded_exception.LexiconSizeExceededException.from_json(
                data, message
            )
        case "MaxLexemeLengthExceededException":
            raise capo_polly.errors.max_lexeme_length_exceeded_exception.MaxLexemeLengthExceededException.from_json(
                data, message
            )
        case "MaxLexiconsNumberExceededException":
            raise capo_polly.errors.max_lexicons_number_exceeded_exception.MaxLexiconsNumberExceededException.from_json(
                data, message
            )
        case "ServiceFailureException":
            raise capo_polly.errors.service_failure_exception.ServiceFailureException.from_json(
                data, message
            )
        case "UnsupportedPlsAlphabetException":
            raise capo_polly.errors.unsupported_pls_alphabet_exception.UnsupportedPlsAlphabetException.from_json(
                data, message
            )
        case "UnsupportedPlsLanguageException":
            raise capo_polly.errors.unsupported_pls_language_exception.UnsupportedPlsLanguageException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_polly.types.put_lexicon_output.PutLexiconOutput:
    out: capo_polly.types.put_lexicon_output.PutLexiconOutput = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_polly.types.put_lexicon_output.PutLexiconOutput:
    out: capo_polly.types.put_lexicon_output.PutLexiconOutput = {}  # type: ignore[typeddict-item]
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
    input_: capo_polly.types.put_lexicon_input.PutLexiconInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v1/lexicons/{Name}"
    url = url.replace("{Name}", quote(input_["name"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_polly.types.put_lexicon_input.serialize_json(input_), allow_nan=False
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
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def put_lexicon(
    options: OperationOptions,
    input_: capo_polly.types.put_lexicon_input.PutLexiconInput,
) -> tuple[capo_polly.types.put_lexicon_output.PutLexiconOutput, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            raise_error(response, handle_error)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_put_lexicon(
    options: AsyncOperationOptions,
    input_: capo_polly.types.put_lexicon_input.PutLexiconInput,
) -> tuple[capo_polly.types.put_lexicon_output.PutLexiconOutput, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 300:
            await response.aread()
            raise_error(response, handle_error)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
