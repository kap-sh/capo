"""Generated from Smithy shape ``com.amazonaws.rdsdata#ExecuteStatement``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_rds_data._auth._signers
import capo_rds_data._auth._sigv4
import capo_rds_data._protocol.eventstream
import capo_rds_data.errors.access_denied_exception
import capo_rds_data.errors.bad_request_exception
import capo_rds_data.errors.database_error_exception
import capo_rds_data.errors.database_not_found_exception
import capo_rds_data.errors.database_resuming_exception
import capo_rds_data.errors.database_unavailable_exception
import capo_rds_data.errors.forbidden_exception
import capo_rds_data.errors.http_endpoint_not_enabled_exception
import capo_rds_data.errors.internal_server_error_exception
import capo_rds_data.errors.invalid_resource_state_exception
import capo_rds_data.errors.invalid_secret_exception
import capo_rds_data.errors.secrets_error_exception
import capo_rds_data.errors.service_unavailable_error
import capo_rds_data.errors.statement_timeout_exception
import capo_rds_data.errors.transaction_not_found_exception
import capo_rds_data.errors.unsupported_result_exception
import capo_rds_data.types.execute_statement_request
import capo_rds_data.types.execute_statement_response
import capo_rds_data.types.field_list
import capo_rds_data.types.metadata
import capo_rds_data.types.records_format_type
import capo_rds_data.types.result_set_options
import capo_rds_data.types.sql_parameters_list
import capo_rds_data.types.sql_records
from capo_rds_data._protocol.errors import parse_error_metadata_json
from capo_rds_data._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_rds_data._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_rds_data.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_rds_data.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "BadRequestException":
            raise capo_rds_data.errors.bad_request_exception.BadRequestException.from_json(
                data, message
            )
        case "DatabaseErrorException":
            raise capo_rds_data.errors.database_error_exception.DatabaseErrorException.from_json(
                data, message
            )
        case "DatabaseNotFoundException":
            raise capo_rds_data.errors.database_not_found_exception.DatabaseNotFoundException.from_json(
                data, message
            )
        case "DatabaseResumingException":
            raise capo_rds_data.errors.database_resuming_exception.DatabaseResumingException.from_json(
                data, message
            )
        case "DatabaseUnavailableException":
            raise capo_rds_data.errors.database_unavailable_exception.DatabaseUnavailableException.from_json(
                data, message
            )
        case "ForbiddenException":
            raise capo_rds_data.errors.forbidden_exception.ForbiddenException.from_json(
                data, message
            )
        case "HttpEndpointNotEnabledException":
            raise capo_rds_data.errors.http_endpoint_not_enabled_exception.HttpEndpointNotEnabledException.from_json(
                data, message
            )
        case "InternalServerErrorException":
            raise capo_rds_data.errors.internal_server_error_exception.InternalServerErrorException.from_json(
                data, message
            )
        case "InvalidResourceStateException":
            raise capo_rds_data.errors.invalid_resource_state_exception.InvalidResourceStateException.from_json(
                data, message
            )
        case "InvalidSecretException":
            raise capo_rds_data.errors.invalid_secret_exception.InvalidSecretException.from_json(
                data, message
            )
        case "SecretsErrorException":
            raise capo_rds_data.errors.secrets_error_exception.SecretsErrorException.from_json(
                data, message
            )
        case "ServiceUnavailableError":
            raise capo_rds_data.errors.service_unavailable_error.ServiceUnavailableError.from_json(
                data, message
            )
        case "StatementTimeoutException":
            raise capo_rds_data.errors.statement_timeout_exception.StatementTimeoutException.from_json(
                data, message
            )
        case "TransactionNotFoundException":
            raise capo_rds_data.errors.transaction_not_found_exception.TransactionNotFoundException.from_json(
                data, message
            )
        case "UnsupportedResultException":
            raise capo_rds_data.errors.unsupported_result_exception.UnsupportedResultException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_rds_data.types.execute_statement_response.ExecuteStatementResponse:
    out: capo_rds_data.types.execute_statement_response.ExecuteStatementResponse = (
        capo_rds_data.types.execute_statement_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_rds_data.types.execute_statement_response.ExecuteStatementResponse:
    out: capo_rds_data.types.execute_statement_response.ExecuteStatementResponse = (
        capo_rds_data.types.execute_statement_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_rds_data._auth._signers.Signer | None:
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
            sigv4_config = capo_rds_data._auth._sigv4.build_sigv4_auth_scheme(
                "rds-data", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_rds_data._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_rds_data.types.execute_statement_request.ExecuteStatementRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/Execute"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_rds_data.types.execute_statement_request.serialize_json(input_),
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


def execute_statement(
    options: OperationOptions,
    input_: capo_rds_data.types.execute_statement_request.ExecuteStatementRequest,
) -> tuple[
    capo_rds_data.types.execute_statement_response.ExecuteStatementResponse,
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


async def async_execute_statement(
    options: AsyncOperationOptions,
    input_: capo_rds_data.types.execute_statement_request.ExecuteStatementRequest,
) -> tuple[
    capo_rds_data.types.execute_statement_response.ExecuteStatementResponse,
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
