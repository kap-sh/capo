"""Generated from Smithy shape ``com.amazonaws.ebs#PutSnapshotBlock``."""

from __future__ import annotations

import json
from collections.abc import AsyncIterator, Iterator
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_ebs._auth._signers
import capo_ebs._auth._sigv4
import capo_ebs._body
import capo_ebs._protocol.eventstream
import capo_ebs.errors.access_denied_exception
import capo_ebs.errors.internal_server_exception
import capo_ebs.errors.request_throttled_exception
import capo_ebs.errors.resource_not_found_exception
import capo_ebs.errors.service_quota_exceeded_exception
import capo_ebs.errors.validation_exception
import capo_ebs.types.block_data
import capo_ebs.types.checksum_algorithm
import capo_ebs.types.put_snapshot_block_request
import capo_ebs.types.put_snapshot_block_response
from capo_ebs._protocol.errors import parse_error_metadata_json
from capo_ebs._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_ebs._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_ebs.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_ebs.errors.access_denied_exception.AccessDeniedException.from_json(
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
) -> capo_ebs.types.put_snapshot_block_response.PutSnapshotBlockResponse:
    out: capo_ebs.types.put_snapshot_block_response.PutSnapshotBlockResponse = {}  # type: ignore[typeddict-item]
    if "x-amz-Checksum" in response.headers:
        out["checksum"] = response.headers["x-amz-Checksum"]
    if "x-amz-Checksum-Algorithm" in response.headers:
        out["checksum_algorithm"] = capo_ebs.types.checksum_algorithm.deserialize_json(
            response.headers["x-amz-Checksum-Algorithm"]
        )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_ebs.types.put_snapshot_block_response.PutSnapshotBlockResponse:
    out: capo_ebs.types.put_snapshot_block_response.PutSnapshotBlockResponse = {}  # type: ignore[typeddict-item]
    if "x-amz-Checksum" in response.headers:
        out["checksum"] = response.headers["x-amz-Checksum"]
    if "x-amz-Checksum-Algorithm" in response.headers:
        out["checksum_algorithm"] = capo_ebs.types.checksum_algorithm.deserialize_json(
            response.headers["x-amz-Checksum-Algorithm"]
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
                    options.credentials_provider,
                    auth_scheme=sigv4_config,
                    unsigned_payload=True,
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_ebs.types.put_snapshot_block_request.PutSnapshotBlockRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_ebs.types.checksum_algorithm

    url = endpoint.url.rstrip("/") + "/snapshots/{SnapshotId}/blocks/{BlockIndex}"
    url = url.replace("{SnapshotId}", quote(input_["snapshot_id"], safe=""))
    url = url.replace("{BlockIndex}", quote(str(input_["block_index"]), safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "data_length" in input_:
        headers["x-amz-Data-Length"] = str(input_["data_length"])
    if "progress" in input_:
        headers["x-amz-Progress"] = str(input_["progress"])
    if "checksum" in input_:
        headers["x-amz-Checksum"] = input_["checksum"]
    if "checksum_algorithm" in input_:
        headers["x-amz-Checksum-Algorithm"] = (
            capo_ebs.types.checksum_algorithm.serialize_json(
                input_["checksum_algorithm"]
            )
        )
    body = input_["block_data"]
    if isinstance(body, capo_ebs._body.Body):
        body = cast(capo_ebs._body.Body[Iterator[bytes]], body)
        stream = body.stream
        if stream is None:
            rebuilt = body.rebuild()
            if rebuilt is None:
                raise RuntimeError("streaming body could not be rebuilt")
            stream, _ = rebuilt
        if "content-length" not in [header.lower() for header in headers]:
            headers["Content-Length"] = str(body.length)
        body = stream
    if isinstance(body, capo_ebs._iter.StaticAnyIterator):
        body = cast(bytes, body.content)
    if not isinstance(body, bytes) and "content-length" not in [
        header.lower() for header in headers
    ]:
        raise ValueError("Content-Length is required for streaming input")
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


async def async_build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_ebs.types.put_snapshot_block_request.PutSnapshotBlockRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_ebs.types.checksum_algorithm

    url = endpoint.url.rstrip("/") + "/snapshots/{SnapshotId}/blocks/{BlockIndex}"
    url = url.replace("{SnapshotId}", quote(input_["snapshot_id"], safe=""))
    url = url.replace("{BlockIndex}", quote(str(input_["block_index"]), safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "data_length" in input_:
        headers["x-amz-Data-Length"] = str(input_["data_length"])
    if "progress" in input_:
        headers["x-amz-Progress"] = str(input_["progress"])
    if "checksum" in input_:
        headers["x-amz-Checksum"] = input_["checksum"]
    if "checksum_algorithm" in input_:
        headers["x-amz-Checksum-Algorithm"] = (
            capo_ebs.types.checksum_algorithm.serialize_json(
                input_["checksum_algorithm"]
            )
        )
    body = input_["block_data"]
    if isinstance(body, capo_ebs._body.Body):
        body = cast(capo_ebs._body.Body[AsyncIterator[bytes]], body)
        stream = body.stream
        if stream is None:
            rebuilt = await body.arebuild()
            if rebuilt is None:
                raise RuntimeError("streaming body could not be rebuilt")
            stream, _ = rebuilt
        if "content-length" not in [header.lower() for header in headers]:
            headers["Content-Length"] = str(body.length)
        body = stream
    if isinstance(body, capo_ebs._iter.StaticAnyIterator):
        body = cast(bytes, body.content)
    if not isinstance(body, bytes) and "content-length" not in [
        header.lower() for header in headers
    ]:
        raise ValueError("Content-Length is required for streaming input")
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def put_snapshot_block(
    options: OperationOptions,
    input_: capo_ebs.types.put_snapshot_block_request.PutSnapshotBlockRequest,
) -> tuple[
    capo_ebs.types.put_snapshot_block_response.PutSnapshotBlockResponse, zapros.Response
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


async def async_put_snapshot_block(
    options: AsyncOperationOptions,
    input_: capo_ebs.types.put_snapshot_block_request.PutSnapshotBlockRequest,
) -> tuple[
    capo_ebs.types.put_snapshot_block_response.PutSnapshotBlockResponse, zapros.Response
]:
    response = await options.client.handler.ahandle(
        await async_build_request(options, input_)
    )
    try:
        if response.status >= 300:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
