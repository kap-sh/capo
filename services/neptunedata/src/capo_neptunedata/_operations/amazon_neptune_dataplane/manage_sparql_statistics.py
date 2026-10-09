"""Generated from Smithy shape ``com.amazonaws.neptunedata#ManageSparqlStatistics``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_neptunedata._auth._signers
import capo_neptunedata._auth._sigv4
import capo_neptunedata._protocol.eventstream
import capo_neptunedata.errors.access_denied_exception
import capo_neptunedata.errors.bad_request_exception
import capo_neptunedata.errors.client_timeout_exception
import capo_neptunedata.errors.constraint_violation_exception
import capo_neptunedata.errors.illegal_argument_exception
import capo_neptunedata.errors.invalid_argument_exception
import capo_neptunedata.errors.invalid_parameter_exception
import capo_neptunedata.errors.missing_parameter_exception
import capo_neptunedata.errors.preconditions_failed_exception
import capo_neptunedata.errors.read_only_violation_exception
import capo_neptunedata.errors.statistics_not_available_exception
import capo_neptunedata.errors.too_many_requests_exception
import capo_neptunedata.errors.unsupported_operation_exception
import capo_neptunedata.types.manage_sparql_statistics_input
import capo_neptunedata.types.manage_sparql_statistics_output
import capo_neptunedata.types.refresh_statistics_id_map
import capo_neptunedata.types.statistics_auto_generation_mode
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
        case "AccessDeniedException":
            raise capo_neptunedata.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "BadRequestException":
            raise capo_neptunedata.errors.bad_request_exception.BadRequestException.from_json(
                data, message
            )
        case "ClientTimeoutException":
            raise capo_neptunedata.errors.client_timeout_exception.ClientTimeoutException.from_json(
                data, message
            )
        case "ConstraintViolationException":
            raise capo_neptunedata.errors.constraint_violation_exception.ConstraintViolationException.from_json(
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
        case "MissingParameterException":
            raise capo_neptunedata.errors.missing_parameter_exception.MissingParameterException.from_json(
                data, message
            )
        case "PreconditionsFailedException":
            raise capo_neptunedata.errors.preconditions_failed_exception.PreconditionsFailedException.from_json(
                data, message
            )
        case "ReadOnlyViolationException":
            raise capo_neptunedata.errors.read_only_violation_exception.ReadOnlyViolationException.from_json(
                data, message
            )
        case "StatisticsNotAvailableException":
            raise capo_neptunedata.errors.statistics_not_available_exception.StatisticsNotAvailableException.from_json(
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
) -> (
    capo_neptunedata.types.manage_sparql_statistics_output.ManageSparqlStatisticsOutput
):
    out: capo_neptunedata.types.manage_sparql_statistics_output.ManageSparqlStatisticsOutput = capo_neptunedata.types.manage_sparql_statistics_output.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> (
    capo_neptunedata.types.manage_sparql_statistics_output.ManageSparqlStatisticsOutput
):
    out: capo_neptunedata.types.manage_sparql_statistics_output.ManageSparqlStatisticsOutput = capo_neptunedata.types.manage_sparql_statistics_output.deserialize_json(
        json.loads(await response.aread())
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
    input_: capo_neptunedata.types.manage_sparql_statistics_input.ManageSparqlStatisticsInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/sparql/statistics"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_neptunedata.types.manage_sparql_statistics_input.serialize_json(input_),
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


def manage_sparql_statistics(
    options: OperationOptions,
    input_: capo_neptunedata.types.manage_sparql_statistics_input.ManageSparqlStatisticsInput,
) -> tuple[
    capo_neptunedata.types.manage_sparql_statistics_output.ManageSparqlStatisticsOutput,
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


async def async_manage_sparql_statistics(
    options: AsyncOperationOptions,
    input_: capo_neptunedata.types.manage_sparql_statistics_input.ManageSparqlStatisticsInput,
) -> tuple[
    capo_neptunedata.types.manage_sparql_statistics_output.ManageSparqlStatisticsOutput,
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
