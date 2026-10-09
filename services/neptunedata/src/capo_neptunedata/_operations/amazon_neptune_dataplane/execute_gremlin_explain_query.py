"""Generated from Smithy shape ``com.amazonaws.neptunedata#ExecuteGremlinExplainQuery``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_neptunedata._auth._signers
import capo_neptunedata._auth._sigv4
import capo_neptunedata._protocol.eventstream
import capo_neptunedata.errors.bad_request_exception
import capo_neptunedata.errors.cancelled_by_user_exception
import capo_neptunedata.errors.client_timeout_exception
import capo_neptunedata.errors.concurrent_modification_exception
import capo_neptunedata.errors.constraint_violation_exception
import capo_neptunedata.errors.failure_by_query_exception
import capo_neptunedata.errors.illegal_argument_exception
import capo_neptunedata.errors.invalid_argument_exception
import capo_neptunedata.errors.invalid_parameter_exception
import capo_neptunedata.errors.malformed_query_exception
import capo_neptunedata.errors.memory_limit_exceeded_exception
import capo_neptunedata.errors.missing_parameter_exception
import capo_neptunedata.errors.parsing_exception
import capo_neptunedata.errors.preconditions_failed_exception
import capo_neptunedata.errors.query_limit_exceeded_exception
import capo_neptunedata.errors.query_limit_exception
import capo_neptunedata.errors.query_too_large_exception
import capo_neptunedata.errors.time_limit_exceeded_exception
import capo_neptunedata.errors.too_many_requests_exception
import capo_neptunedata.errors.unsupported_operation_exception
import capo_neptunedata.types.execute_gremlin_explain_query_input
import capo_neptunedata.types.execute_gremlin_explain_query_output
import capo_neptunedata.types.report_as_text
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
        case "BadRequestException":
            raise capo_neptunedata.errors.bad_request_exception.BadRequestException.from_json(
                data, message
            )
        case "CancelledByUserException":
            raise capo_neptunedata.errors.cancelled_by_user_exception.CancelledByUserException.from_json(
                data, message
            )
        case "ClientTimeoutException":
            raise capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException.from_json(
                data, message
            )
        case "ConcurrentModificationException":
            raise capo_neptunedata.errors.concurrent_modification_exception.ConcurrentModificationException.from_json(
                data, message
            )
        case "ConstraintViolationException":
            raise capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException.from_json(
                data, message
            )
        case "FailureByQueryException":
            raise capo_neptunedata.errors.failure_by_query_exception.FailureByQueryException.from_json(
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
        case "MalformedQueryException":
            raise capo_neptunedata.errors.malformed_query_exception.MalformedQueryException.from_json(
                data, message
            )
        case "MemoryLimitExceededException":
            raise capo_neptunedata.errors.memory_limit_exceeded_exception.MemoryLimitExceededException.from_json(
                data, message
            )
        case "MissingParameterException":
            raise capo_neptunedata.errors.missing_parameter_exception.MissingParameterException.from_json(
                data, message
            )
        case "ParsingException":
            raise capo_neptunedata.errors.parsing_exception.ParsingException.from_json(
                data, message
            )
        case "PreconditionsFailedException":
            raise capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException.from_json(
                data, message
            )
        case "QueryLimitExceededException":
            raise capo_neptunedata.errors.query_limit_exceeded_exception.QueryLimitExceededException.from_json(
                data, message
            )
        case "QueryLimitException":
            raise capo_neptunedata.errors.query_limit_exception.QueryLimitException.from_json(
                data, message
            )
        case "QueryTooLargeException":
            raise capo_neptunedata.errors.query_too_large_exception.QueryTooLargeException.from_json(
                data, message
            )
        case "TimeLimitExceededException":
            raise capo_neptunedata.errors.time_limit_exceeded_exception.TimeLimitExceededException.from_json(
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
) -> capo_neptunedata.types.execute_gremlin_explain_query_output.ExecuteGremlinExplainQueryOutput:
    out: capo_neptunedata.types.execute_gremlin_explain_query_output.ExecuteGremlinExplainQueryOutput = {
        "output": b"".join(response.iter_raw())
    }  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_neptunedata.types.execute_gremlin_explain_query_output.ExecuteGremlinExplainQueryOutput:
    out: capo_neptunedata.types.execute_gremlin_explain_query_output.ExecuteGremlinExplainQueryOutput = {
        "output": b"".join([chunk async for chunk in response.async_iter_raw()])
    }  # type: ignore[typeddict-item]
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
    input_: capo_neptunedata.types.execute_gremlin_explain_query_input.ExecuteGremlinExplainQueryInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/gremlin/explain"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_neptunedata.types.execute_gremlin_explain_query_input.serialize_json(
            input_
        ),
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


def execute_gremlin_explain_query(
    options: OperationOptions,
    input_: capo_neptunedata.types.execute_gremlin_explain_query_input.ExecuteGremlinExplainQueryInput,
) -> tuple[
    capo_neptunedata.types.execute_gremlin_explain_query_output.ExecuteGremlinExplainQueryOutput,
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


async def async_execute_gremlin_explain_query(
    options: AsyncOperationOptions,
    input_: capo_neptunedata.types.execute_gremlin_explain_query_input.ExecuteGremlinExplainQueryInput,
) -> tuple[
    capo_neptunedata.types.execute_gremlin_explain_query_output.ExecuteGremlinExplainQueryOutput,
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
