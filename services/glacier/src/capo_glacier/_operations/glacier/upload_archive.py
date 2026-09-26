"""Generated from Smithy shape ``com.amazonaws.glacier#UploadArchive``."""

from __future__ import annotations

import json
from collections.abc import AsyncIterator, Iterator
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_glacier._auth._signers
import capo_glacier._auth._sigv4
import capo_glacier._body
import capo_glacier._protocol.eventstream
import capo_glacier.errors.invalid_parameter_value_exception
import capo_glacier.errors.missing_parameter_value_exception
import capo_glacier.errors.no_longer_supported_exception
import capo_glacier.errors.request_timeout_exception
import capo_glacier.errors.resource_not_found_exception
import capo_glacier.errors.service_unavailable_exception
import capo_glacier.types.archive_creation_output
import capo_glacier.types.stream
import capo_glacier.types.upload_archive_input
from capo_glacier._protocol.errors import parse_error_metadata_json
from capo_glacier._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_glacier._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_glacier.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidParameterValueException":
            raise capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data, message
            )
        case "MissingParameterValueException":
            raise capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException.from_json(
                data, message
            )
        case "NoLongerSupportedException":
            raise capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException.from_json(
                data, message
            )
        case "RequestTimeoutException":
            raise capo_glacier.errors.request_timeout_exception.RequestTimeoutException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "ServiceUnavailableException":
            raise capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_glacier.types.archive_creation_output.ArchiveCreationOutput:
    out: capo_glacier.types.archive_creation_output.ArchiveCreationOutput = {}  # type: ignore[typeddict-item]
    if "Location" in response.headers:
        out["location"] = response.headers["Location"]
    if "x-amz-sha256-tree-hash" in response.headers:
        out["checksum"] = response.headers["x-amz-sha256-tree-hash"]
    if "x-amz-archive-id" in response.headers:
        out["archive_id"] = response.headers["x-amz-archive-id"]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_glacier.types.archive_creation_output.ArchiveCreationOutput:
    out: capo_glacier.types.archive_creation_output.ArchiveCreationOutput = {}  # type: ignore[typeddict-item]
    if "Location" in response.headers:
        out["location"] = response.headers["Location"]
    if "x-amz-sha256-tree-hash" in response.headers:
        out["checksum"] = response.headers["x-amz-sha256-tree-hash"]
    if "x-amz-archive-id" in response.headers:
        out["archive_id"] = response.headers["x-amz-archive-id"]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_glacier._auth._signers.Signer | None:
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
            sigv4_config = capo_glacier._auth._sigv4.build_sigv4_auth_scheme(
                "glacier", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_glacier._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_glacier.types.upload_archive_input.UploadArchiveInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/{accountId}/vaults/{vaultName}/archives"
    url = url.replace("{vaultName}", quote(input_["vault_name"], safe=""))
    url = url.replace("{accountId}", quote(input_["account_id"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "archive_description" in input_:
        headers["x-amz-archive-description"] = input_["archive_description"]
    if "checksum" in input_:
        headers["x-amz-sha256-tree-hash"] = input_["checksum"]
    body = input_["body"]
    if isinstance(body, capo_glacier._body.Body):
        body = cast(capo_glacier._body.Body[Iterator[bytes]], body)
        stream = body.stream
        if stream is None:
            rebuilt = body.rebuild()
            if rebuilt is None:
                raise RuntimeError("streaming body could not be rebuilt")
            stream, _ = rebuilt
        if "content-length" not in [header.lower() for header in headers]:
            headers["Content-Length"] = str(body.length)
        body = stream
    if isinstance(body, capo_glacier._iter.StaticAnyIterator):
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
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


async def async_build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_glacier.types.upload_archive_input.UploadArchiveInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/{accountId}/vaults/{vaultName}/archives"
    url = url.replace("{vaultName}", quote(input_["vault_name"], safe=""))
    url = url.replace("{accountId}", quote(input_["account_id"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "archive_description" in input_:
        headers["x-amz-archive-description"] = input_["archive_description"]
    if "checksum" in input_:
        headers["x-amz-sha256-tree-hash"] = input_["checksum"]
    body = input_["body"]
    if isinstance(body, capo_glacier._body.Body):
        body = cast(capo_glacier._body.Body[AsyncIterator[bytes]], body)
        stream = body.stream
        if stream is None:
            rebuilt = await body.arebuild()
            if rebuilt is None:
                raise RuntimeError("streaming body could not be rebuilt")
            stream, _ = rebuilt
        if "content-length" not in [header.lower() for header in headers]:
            headers["Content-Length"] = str(body.length)
        body = stream
    if isinstance(body, capo_glacier._iter.StaticAnyIterator):
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
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def upload_archive(
    options: OperationOptions,
    input_: capo_glacier.types.upload_archive_input.UploadArchiveInput,
) -> tuple[
    capo_glacier.types.archive_creation_output.ArchiveCreationOutput, zapros.Response
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


async def async_upload_archive(
    options: AsyncOperationOptions,
    input_: capo_glacier.types.upload_archive_input.UploadArchiveInput,
) -> tuple[
    capo_glacier.types.archive_creation_output.ArchiveCreationOutput, zapros.Response
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
