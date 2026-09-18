"""Generated from Smithy shape ``com.amazonaws.codeartifact#PublishPackageVersion``."""

from __future__ import annotations

import json
from collections.abc import AsyncIterator, Iterator
from typing import Any, cast

import zapros
from typing_extensions import Never

import capo_codeartifact._auth._signers
import capo_codeartifact._auth._sigv4
import capo_codeartifact._body
import capo_codeartifact._protocol.eventstream
import capo_codeartifact.errors.access_denied_exception
import capo_codeartifact.errors.conflict_exception
import capo_codeartifact.errors.internal_server_exception
import capo_codeartifact.errors.resource_not_found_exception
import capo_codeartifact.errors.service_quota_exceeded_exception
import capo_codeartifact.errors.throttling_exception
import capo_codeartifact.errors.validation_exception
import capo_codeartifact.types.asset
import capo_codeartifact.types.asset_summary
import capo_codeartifact.types.package_format
import capo_codeartifact.types.package_version_status
import capo_codeartifact.types.publish_package_version_request
import capo_codeartifact.types.publish_package_version_result
from capo_codeartifact._protocol.errors import parse_error_metadata_json
from capo_codeartifact._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_codeartifact._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_codeartifact.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_codeartifact.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "ConflictException":
            raise capo_codeartifact.errors.conflict_exception.ConflictException.from_json(
                data, message
            )
        case "InternalServerException":
            raise capo_codeartifact.errors.internal_server_exception.InternalServerException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "ServiceQuotaExceededException":
            raise capo_codeartifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_codeartifact.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_codeartifact.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_codeartifact.types.publish_package_version_result.PublishPackageVersionResult:
    out: capo_codeartifact.types.publish_package_version_result.PublishPackageVersionResult = capo_codeartifact.types.publish_package_version_result.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_codeartifact.types.publish_package_version_result.PublishPackageVersionResult:
    out: capo_codeartifact.types.publish_package_version_result.PublishPackageVersionResult = capo_codeartifact.types.publish_package_version_result.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_codeartifact._auth._signers.Signer | None:
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
            sigv4_config = capo_codeartifact._auth._sigv4.build_sigv4_auth_scheme(
                "codeartifact", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_codeartifact._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_codeartifact.types.publish_package_version_request.PublishPackageVersionRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_codeartifact.types.package_format

    url = endpoint.url.rstrip("/") + "/v1/package/version/publish"
    params: list[tuple[str, str]] = []
    if "domain" in input_:
        params.append(("domain", input_["domain"]))
    if "domain_owner" in input_:
        params.append(("domain-owner", input_["domain_owner"]))
    if "repository" in input_:
        params.append(("repository", input_["repository"]))
    if "format" in input_:
        params.append(
            (
                "format",
                capo_codeartifact.types.package_format.serialize_json(input_["format"]),
            )
        )
    if "namespace" in input_:
        params.append(("namespace", input_["namespace"]))
    if "package" in input_:
        params.append(("package", input_["package"]))
    if "package_version" in input_:
        params.append(("version", input_["package_version"]))
    if "asset_name" in input_:
        params.append(("asset", input_["asset_name"]))
    if "unfinished" in input_:
        params.append(("unfinished", "true" if input_["unfinished"] else "false"))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "asset_sha256" in input_:
        headers["x-amz-content-sha256"] = input_["asset_sha256"]
    body = input_["asset_content"]
    if isinstance(body, capo_codeartifact._body.Body):
        body = cast(capo_codeartifact._body.Body[Iterator[bytes]], body)
        stream = body.stream
        if stream is None:
            rebuilt = body.rebuild()
            if rebuilt is None:
                raise RuntimeError("streaming body could not be rebuilt")
            stream, _ = rebuilt
        if "content-length" not in [header.lower() for header in headers]:
            headers["Content-Length"] = str(body.length)
        body = stream
    if isinstance(body, capo_codeartifact._iter.StaticAnyIterator):
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
    input_: capo_codeartifact.types.publish_package_version_request.PublishPackageVersionRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_codeartifact.types.package_format

    url = endpoint.url.rstrip("/") + "/v1/package/version/publish"
    params: list[tuple[str, str]] = []
    if "domain" in input_:
        params.append(("domain", input_["domain"]))
    if "domain_owner" in input_:
        params.append(("domain-owner", input_["domain_owner"]))
    if "repository" in input_:
        params.append(("repository", input_["repository"]))
    if "format" in input_:
        params.append(
            (
                "format",
                capo_codeartifact.types.package_format.serialize_json(input_["format"]),
            )
        )
    if "namespace" in input_:
        params.append(("namespace", input_["namespace"]))
    if "package" in input_:
        params.append(("package", input_["package"]))
    if "package_version" in input_:
        params.append(("version", input_["package_version"]))
    if "asset_name" in input_:
        params.append(("asset", input_["asset_name"]))
    if "unfinished" in input_:
        params.append(("unfinished", "true" if input_["unfinished"] else "false"))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "asset_sha256" in input_:
        headers["x-amz-content-sha256"] = input_["asset_sha256"]
    body = input_["asset_content"]
    if isinstance(body, capo_codeartifact._body.Body):
        body = cast(capo_codeartifact._body.Body[AsyncIterator[bytes]], body)
        stream = body.stream
        if stream is None:
            rebuilt = await body.arebuild()
            if rebuilt is None:
                raise RuntimeError("streaming body could not be rebuilt")
            stream, _ = rebuilt
        if "content-length" not in [header.lower() for header in headers]:
            headers["Content-Length"] = str(body.length)
        body = stream
    if isinstance(body, capo_codeartifact._iter.StaticAnyIterator):
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


def publish_package_version(
    options: OperationOptions,
    input_: capo_codeartifact.types.publish_package_version_request.PublishPackageVersionRequest,
) -> tuple[
    capo_codeartifact.types.publish_package_version_result.PublishPackageVersionResult,
    zapros.Response,
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


async def async_publish_package_version(
    options: AsyncOperationOptions,
    input_: capo_codeartifact.types.publish_package_version_request.PublishPackageVersionRequest,
) -> tuple[
    capo_codeartifact.types.publish_package_version_result.PublishPackageVersionResult,
    zapros.Response,
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
