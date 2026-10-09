"""Generated from Smithy shape ``com.amazonaws.mediastoredata#DescribeObject``."""

from __future__ import annotations

import json
from email.utils import parsedate_to_datetime as _parse_http_date
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_mediastore_data._auth._signers
import capo_mediastore_data._auth._sigv4
import capo_mediastore_data._protocol.eventstream
import capo_mediastore_data.errors.container_not_found_exception
import capo_mediastore_data.errors.internal_server_error
import capo_mediastore_data.errors.object_not_found_exception
import capo_mediastore_data.types.describe_object_request
import capo_mediastore_data.types.describe_object_response
import capo_mediastore_data.types.time_stamp
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
        case "ObjectNotFoundException":
            raise capo_mediastore_data.errors.object_not_found_exception.ObjectNotFoundException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_mediastore_data.types.describe_object_response.DescribeObjectResponse:
    out: capo_mediastore_data.types.describe_object_response.DescribeObjectResponse = {}  # type: ignore[typeddict-item]
    if "ETag" in response.headers:
        out["e_tag"] = response.headers["ETag"]
    if "Content-Type" in response.headers:
        out["content_type"] = response.headers["Content-Type"]
    if "Content-Length" in response.headers:
        out["content_length"] = int(response.headers["Content-Length"])
    if "Cache-Control" in response.headers:
        out["cache_control"] = response.headers["Cache-Control"]
    if "Last-Modified" in response.headers:
        out["last_modified"] = _parse_http_date(response.headers["Last-Modified"])
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_mediastore_data.types.describe_object_response.DescribeObjectResponse:
    out: capo_mediastore_data.types.describe_object_response.DescribeObjectResponse = {}  # type: ignore[typeddict-item]
    if "ETag" in response.headers:
        out["e_tag"] = response.headers["ETag"]
    if "Content-Type" in response.headers:
        out["content_type"] = response.headers["Content-Type"]
    if "Content-Length" in response.headers:
        out["content_length"] = int(response.headers["Content-Length"])
    if "Cache-Control" in response.headers:
        out["cache_control"] = response.headers["Cache-Control"]
    if "Last-Modified" in response.headers:
        out["last_modified"] = _parse_http_date(response.headers["Last-Modified"])
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
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_mediastore_data.types.describe_object_request.DescribeObjectRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/{Path+}"
    url = url.replace("{Path+}", quote(input_["path"], safe="/"))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
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
        normalized_url, "HEAD", headers=headers, body=body, context={"signer": signer}
    )


def describe_object(
    options: OperationOptions,
    input_: capo_mediastore_data.types.describe_object_request.DescribeObjectRequest,
) -> tuple[
    capo_mediastore_data.types.describe_object_response.DescribeObjectResponse,
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


async def async_describe_object(
    options: AsyncOperationOptions,
    input_: capo_mediastore_data.types.describe_object_request.DescribeObjectRequest,
) -> tuple[
    capo_mediastore_data.types.describe_object_response.DescribeObjectResponse,
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
