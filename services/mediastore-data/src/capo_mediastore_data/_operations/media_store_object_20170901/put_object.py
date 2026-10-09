"""Generated from Smithy shape ``com.amazonaws.mediastoredata#PutObject``."""

from __future__ import annotations

import json
from collections.abc import AsyncIterator, Iterator
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_mediastore_data._auth._signers
import capo_mediastore_data._auth._sigv4
import capo_mediastore_data._body
import capo_mediastore_data._protocol.eventstream
import capo_mediastore_data.errors.container_not_found_exception
import capo_mediastore_data.errors.internal_server_error
import capo_mediastore_data.types.payload_blob
import capo_mediastore_data.types.put_object_request
import capo_mediastore_data.types.put_object_response
import capo_mediastore_data.types.storage_class
import capo_mediastore_data.types.upload_availability
from capo_mediastore_data._protocol.errors import parse_error_metadata_json
from capo_mediastore_data._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_mediastore_data._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_mediastore_data.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ContainerNotFoundException":
            raise capo_mediastore_data.errors.container_not_found_exception.ContainerNotFoundException.from_json(
                data, message
            )
        case "InternalServerError":
            raise capo_mediastore_data.errors.internal_server_error.InternalServerError.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_mediastore_data.types.put_object_response.PutObjectResponse:
    out: capo_mediastore_data.types.put_object_response.PutObjectResponse = (
        capo_mediastore_data.types.put_object_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_mediastore_data.types.put_object_response.PutObjectResponse:
    out: capo_mediastore_data.types.put_object_response.PutObjectResponse = (
        capo_mediastore_data.types.put_object_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_mediastore_data._auth._signers.Signer | None:
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
            sigv4_config = capo_mediastore_data._auth._sigv4.build_sigv4_auth_scheme(
                "mediastore", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_mediastore_data._auth._signers.SigV4Signer(
                    options.credentials_provider,
                    auth_scheme=sigv4_config,
                    unsigned_payload=True,
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_mediastore_data.types.put_object_request.PutObjectRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_mediastore_data.types.storage_class
    import capo_mediastore_data.types.upload_availability

    url = endpoint.url.rstrip("/") + "/{Path+}"
    url = url.replace("{Path+}", quote(input_["path"], safe="/"))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "content_type" in input_:
        headers["Content-Type"] = input_["content_type"]
    if "cache_control" in input_:
        headers["Cache-Control"] = input_["cache_control"]
    if "storage_class" in input_:
        headers["x-amz-storage-class"] = (
            capo_mediastore_data.types.storage_class.serialize_json(
                input_["storage_class"]
            )
        )
    if "upload_availability" in input_:
        headers["x-amz-upload-availability"] = (
            capo_mediastore_data.types.upload_availability.serialize_json(
                input_["upload_availability"]
            )
        )
    body = input_["body"]
    if isinstance(body, capo_mediastore_data._body.Body):
        body = cast(capo_mediastore_data._body.Body[Iterator[bytes]], body)
        stream = body.stream
        if stream is None:
            rebuilt = body.rebuild()
            if rebuilt is None:
                raise RuntimeError("streaming body could not be rebuilt")
            stream, _ = rebuilt
        if "content-length" not in [header.lower() for header in headers]:
            headers["Content-Length"] = str(body.length)
        body = stream
    if isinstance(body, capo_mediastore_data._iter.StaticAnyIterator):
        body = cast(bytes, body.content)
    if not isinstance(body, bytes) and "content-length" not in [
        header.lower() for header in headers
    ]:
        raise ValueError("Content-Length is required for streaming input")
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


async def async_build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_mediastore_data.types.put_object_request.PutObjectRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_mediastore_data.types.storage_class
    import capo_mediastore_data.types.upload_availability

    url = endpoint.url.rstrip("/") + "/{Path+}"
    url = url.replace("{Path+}", quote(input_["path"], safe="/"))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "content_type" in input_:
        headers["Content-Type"] = input_["content_type"]
    if "cache_control" in input_:
        headers["Cache-Control"] = input_["cache_control"]
    if "storage_class" in input_:
        headers["x-amz-storage-class"] = (
            capo_mediastore_data.types.storage_class.serialize_json(
                input_["storage_class"]
            )
        )
    if "upload_availability" in input_:
        headers["x-amz-upload-availability"] = (
            capo_mediastore_data.types.upload_availability.serialize_json(
                input_["upload_availability"]
            )
        )
    body = input_["body"]
    if isinstance(body, capo_mediastore_data._body.Body):
        body = cast(capo_mediastore_data._body.Body[AsyncIterator[bytes]], body)
        stream = body.stream
        if stream is None:
            rebuilt = await body.arebuild()
            if rebuilt is None:
                raise RuntimeError("streaming body could not be rebuilt")
            stream, _ = rebuilt
        if "content-length" not in [header.lower() for header in headers]:
            headers["Content-Length"] = str(body.length)
        body = stream
    if isinstance(body, capo_mediastore_data._iter.StaticAnyIterator):
        body = cast(bytes, body.content)
    if not isinstance(body, bytes) and "content-length" not in [
        header.lower() for header in headers
    ]:
        raise ValueError("Content-Length is required for streaming input")
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


def put_object(
    options: OperationOptions,
    input_: capo_mediastore_data.types.put_object_request.PutObjectRequest,
) -> tuple[
    capo_mediastore_data.types.put_object_response.PutObjectResponse, zapros.Response
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


async def async_put_object(
    options: AsyncOperationOptions,
    input_: capo_mediastore_data.types.put_object_request.PutObjectRequest,
) -> tuple[
    capo_mediastore_data.types.put_object_response.PutObjectResponse, zapros.Response
]:
    response = await options.client.handler.ahandle(
        await async_build_request(options, input_)
    )
    try:
        if response.status >= 300:
            await response.aread()
            raise_error(response, handle_error)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
