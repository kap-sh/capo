"""Generated from Smithy shape ``com.amazonaws.ebs#StartSnapshot``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_ebs._auth._signers
import capo_ebs._auth._sigv4
import capo_ebs._protocol.eventstream
import capo_ebs.errors.access_denied_exception
import capo_ebs.errors.concurrent_limit_exceeded_exception
import capo_ebs.errors.conflict_exception
import capo_ebs.errors.internal_server_exception
import capo_ebs.errors.request_throttled_exception
import capo_ebs.errors.resource_not_found_exception
import capo_ebs.errors.service_quota_exceeded_exception
import capo_ebs.errors.validation_exception
import capo_ebs.types.sse_type
import capo_ebs.types.start_snapshot_request
import capo_ebs.types.start_snapshot_response
import capo_ebs.types.status
import capo_ebs.types.tags
import capo_ebs.types.time_stamp
from capo_ebs._protocol.errors import parse_error_metadata_json
from capo_ebs._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_ebs._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_ebs.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_ebs.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "ConcurrentLimitExceededException":
            raise capo_ebs.errors.concurrent_limit_exceeded_exception.ConcurrentLimitExceededException.from_json(
                data, message
            )
        case "ConflictException":
            raise capo_ebs.errors.conflict_exception.ConflictException.from_json(
                data, message
            )
        case "InternalServerException":
            raise capo_ebs.errors.internal_server_exception.InternalServerException.from_json(
                data, message
            )
        case "RequestThrottledException":
            raise capo_ebs.errors.request_throttled_exception.RequestThrottledException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_ebs.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "ServiceQuotaExceededException":
            raise capo_ebs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_ebs.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_ebs.types.start_snapshot_response.StartSnapshotResponse:
    out: capo_ebs.types.start_snapshot_response.StartSnapshotResponse = (
        capo_ebs.types.start_snapshot_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_ebs.types.start_snapshot_response.StartSnapshotResponse:
    out: capo_ebs.types.start_snapshot_response.StartSnapshotResponse = (
        capo_ebs.types.start_snapshot_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_ebs._auth._signers.Signer | None:
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
            sigv4_config = capo_ebs._auth._sigv4.build_sigv4_auth_scheme(
                "ebs", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_ebs._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_ebs.types.start_snapshot_request.StartSnapshotRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/snapshots"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_ebs.types.start_snapshot_request.serialize_json(input_), allow_nan=False
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


def start_snapshot(
    options: OperationOptions,
    input_: capo_ebs.types.start_snapshot_request.StartSnapshotRequest,
) -> tuple[
    capo_ebs.types.start_snapshot_response.StartSnapshotResponse, zapros.Response
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


async def async_start_snapshot(
    options: AsyncOperationOptions,
    input_: capo_ebs.types.start_snapshot_request.StartSnapshotRequest,
) -> tuple[
    capo_ebs.types.start_snapshot_response.StartSnapshotResponse, zapros.Response
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
