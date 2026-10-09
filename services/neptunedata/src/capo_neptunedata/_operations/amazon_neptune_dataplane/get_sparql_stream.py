"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetSparqlStream``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_neptunedata._auth._signers
import capo_neptunedata._auth._sigv4
import capo_neptunedata._protocol.eventstream
import capo_neptunedata.errors.client_timeout_exception
import capo_neptunedata.errors.constraint_violation_exception
import capo_neptunedata.errors.expired_stream_exception
import capo_neptunedata.errors.illegal_argument_exception
import capo_neptunedata.errors.invalid_argument_exception
import capo_neptunedata.errors.invalid_parameter_exception
import capo_neptunedata.errors.memory_limit_exceeded_exception
import capo_neptunedata.errors.preconditions_failed_exception
import capo_neptunedata.errors.stream_records_not_found_exception
import capo_neptunedata.errors.throttling_exception
import capo_neptunedata.errors.too_many_requests_exception
import capo_neptunedata.errors.unsupported_operation_exception
import capo_neptunedata.types.encoding
import capo_neptunedata.types.get_sparql_stream_input
import capo_neptunedata.types.get_sparql_stream_output
import capo_neptunedata.types.iterator_type
import capo_neptunedata.types.sparql_records_list
import capo_neptunedata.types.string_valued_map
from capo_neptunedata._protocol.errors import parse_error_metadata_json
from capo_neptunedata._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_neptunedata._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_neptunedata.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ClientTimeoutException":
            raise capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException.from_json(
                data, message
            )
        case "ConstraintViolationException":
            raise capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException.from_json(
                data, message
            )
        case "ExpiredStreamException":
            raise capo_neptunedata.errors.expired_stream_exception.ExpiredStreamException.from_json(
                data, message
            )
        case "IllegalArgumentException":
            raise capo_neptunedata.errors.illegal_argument_exception.IllegalArgumentException.from_json(
                data, message
            )
        case "InvalidArgumentException":
            raise capo_neptunedata.errors.invalid_argument_exception.InvalidArgumentException.from_json(
                data, message
            )
        case "InvalidParameterException":
            raise capo_neptunedata.errors.invalid_parameter_exception.InvalidParameterException.from_json(
                data, message
            )
        case "MemoryLimitExceededException":
            raise capo_neptunedata.errors.memory_limit_exceeded_exception.MemoryLimitExceededException.from_json(
                data, message
            )
        case "PreconditionsFailedException":
            raise capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException.from_json(
                data, message
            )
        case "StreamRecordsNotFoundException":
            raise capo_neptunedata.errors.stream_records_not_found_exception.StreamRecordsNotFoundException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_neptunedata.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case "TooManyRequestsException":
            raise capo_neptunedata.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data, message
            )
        case "UnsupportedOperationException":
            raise capo_neptunedata.errors.unsupported_operation_exception.UnsupportedOperationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_neptunedata.types.get_sparql_stream_output.GetSparqlStreamOutput:
    out: capo_neptunedata.types.get_sparql_stream_output.GetSparqlStreamOutput = (
        capo_neptunedata.types.get_sparql_stream_output.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_neptunedata.types.get_sparql_stream_output.GetSparqlStreamOutput:
    out: capo_neptunedata.types.get_sparql_stream_output.GetSparqlStreamOutput = (
        capo_neptunedata.types.get_sparql_stream_output.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_neptunedata._auth._signers.Signer | None:
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
            sigv4_config = capo_neptunedata._auth._sigv4.build_sigv4_auth_scheme(
                "neptune-db", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_neptunedata._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_neptunedata.types.get_sparql_stream_input.GetSparqlStreamInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_neptunedata.types.encoding
    import capo_neptunedata.types.iterator_type

    url = endpoint.url.rstrip("/") + "/sparql/stream"
    params: list[tuple[str, str]] = []
    if "limit" in input_:
        params.append(("limit", str(input_["limit"])))
    if "iterator_type" in input_:
        params.append(
            (
                "iteratorType",
                capo_neptunedata.types.iterator_type.serialize_json(
                    input_["iterator_type"]
                ),
            )
        )
    if "commit_num" in input_:
        params.append(("commitNum", str(input_["commit_num"])))
    if "op_num" in input_:
        params.append(("opNum", str(input_["op_num"])))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "encoding" in input_:
        headers["Accept-Encoding"] = capo_neptunedata.types.encoding.serialize_json(
            input_["encoding"]
        )
    body: bytes | None = b""
    signer = (
        None
        if options.anonymous
        else get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    )
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_sparql_stream(
    options: OperationOptions,
    input_: capo_neptunedata.types.get_sparql_stream_input.GetSparqlStreamInput,
) -> tuple[
    capo_neptunedata.types.get_sparql_stream_output.GetSparqlStreamOutput,
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


async def async_get_sparql_stream(
    options: AsyncOperationOptions,
    input_: capo_neptunedata.types.get_sparql_stream_input.GetSparqlStreamInput,
) -> tuple[
    capo_neptunedata.types.get_sparql_stream_output.GetSparqlStreamOutput,
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
