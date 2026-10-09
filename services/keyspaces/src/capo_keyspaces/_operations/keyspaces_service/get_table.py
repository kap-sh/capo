"""Generated from Smithy shape ``com.amazonaws.keyspaces#GetTable``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_keyspaces._auth._signers
import capo_keyspaces._auth._sigv4
import capo_keyspaces._protocol.eventstream
import capo_keyspaces.errors.access_denied_exception
import capo_keyspaces.errors.internal_server_exception
import capo_keyspaces.errors.resource_not_found_exception
import capo_keyspaces.errors.service_quota_exceeded_exception
import capo_keyspaces.errors.validation_exception
import capo_keyspaces.types.capacity_specification_summary
import capo_keyspaces.types.cdc_specification_summary
import capo_keyspaces.types.client_side_timestamps
import capo_keyspaces.types.comment
import capo_keyspaces.types.encryption_specification
import capo_keyspaces.types.get_table_request
import capo_keyspaces.types.get_table_response
import capo_keyspaces.types.point_in_time_recovery_summary
import capo_keyspaces.types.replica_specification_summary_list
import capo_keyspaces.types.schema_definition
import capo_keyspaces.types.time_to_live
import capo_keyspaces.types.timestamp
import capo_keyspaces.types.warm_throughput_specification_summary
from capo_keyspaces._protocol.errors import parse_error_metadata_json
from capo_keyspaces._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_keyspaces._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_keyspaces.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_keyspaces.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_0(
                data, message
            )
        case "InternalServerException":
            raise capo_keyspaces.errors.internal_server_exception.InternalServerException.from_aws_json_1_0(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_keyspaces.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_0(
                data, message
            )
        case "ServiceQuotaExceededException":
            raise capo_keyspaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_aws_json_1_0(
                data, message
            )
        case "ValidationException":
            raise capo_keyspaces.errors.validation_exception.ValidationException.from_aws_json_1_0(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_keyspaces.types.get_table_response.GetTableResponse:
    out: capo_keyspaces.types.get_table_response.GetTableResponse = (
        capo_keyspaces.types.get_table_response.deserialize_aws_json_1_0(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_keyspaces.types.get_table_response.GetTableResponse:
    out: capo_keyspaces.types.get_table_response.GetTableResponse = (
        capo_keyspaces.types.get_table_response.deserialize_aws_json_1_0(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_keyspaces._auth._signers.Signer | None:
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
            sigv4_config = capo_keyspaces._auth._sigv4.build_sigv4_auth_scheme(
                "cassandra", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_keyspaces._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_keyspaces.types.get_table_request.GetTableRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "KeyspacesService.GetTable"
    body: bytes | None = json.dumps(
        capo_keyspaces.types.get_table_request.serialize_aws_json_1_0(input_),
        allow_nan=False,
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.0"
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


def get_table(
    options: OperationOptions,
    input_: capo_keyspaces.types.get_table_request.GetTableRequest,
) -> tuple[capo_keyspaces.types.get_table_response.GetTableResponse, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            raise_error(response, handle_error)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_get_table(
    options: AsyncOperationOptions,
    input_: capo_keyspaces.types.get_table_request.GetTableRequest,
) -> tuple[capo_keyspaces.types.get_table_response.GetTableResponse, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 300:
            await response.aread()
            raise_error(response, handle_error)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
