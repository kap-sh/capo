"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#UpdatePackagingGroup``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_mediapackage_vod._auth._signers
import capo_mediapackage_vod._auth._sigv4
import capo_mediapackage_vod._protocol.eventstream
import capo_mediapackage_vod.errors.forbidden_exception
import capo_mediapackage_vod.errors.internal_server_error_exception
import capo_mediapackage_vod.errors.not_found_exception
import capo_mediapackage_vod.errors.service_unavailable_exception
import capo_mediapackage_vod.errors.too_many_requests_exception
import capo_mediapackage_vod.errors.unprocessable_entity_exception
import capo_mediapackage_vod.types.authorization
import capo_mediapackage_vod.types.egress_access_logs
import capo_mediapackage_vod.types.tags
import capo_mediapackage_vod.types.update_packaging_group_request
import capo_mediapackage_vod.types.update_packaging_group_response
from capo_mediapackage_vod._protocol.errors import parse_error_metadata_json
from capo_mediapackage_vod._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_mediapackage_vod._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_mediapackage_vod.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ForbiddenException":
            raise capo_mediapackage_vod.errors.forbidden_exception.ForbiddenException.from_json(
                data, message
            )
        case "InternalServerErrorException":
            raise capo_mediapackage_vod.errors.internal_server_error_exception.InternalServerErrorException.from_json(
                data, message
            )
        case "NotFoundException":
            raise capo_mediapackage_vod.errors.not_found_exception.NotFoundException.from_json(
                data, message
            )
        case "ServiceUnavailableException":
            raise capo_mediapackage_vod.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data, message
            )
        case "TooManyRequestsException":
            raise capo_mediapackage_vod.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data, message
            )
        case "UnprocessableEntityException":
            raise capo_mediapackage_vod.errors.unprocessable_entity_exception.UnprocessableEntityException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_mediapackage_vod.types.update_packaging_group_response.UpdatePackagingGroupResponse:
    out: capo_mediapackage_vod.types.update_packaging_group_response.UpdatePackagingGroupResponse = capo_mediapackage_vod.types.update_packaging_group_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_mediapackage_vod.types.update_packaging_group_response.UpdatePackagingGroupResponse:
    out: capo_mediapackage_vod.types.update_packaging_group_response.UpdatePackagingGroupResponse = capo_mediapackage_vod.types.update_packaging_group_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_mediapackage_vod._auth._signers.Signer | None:
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
            sigv4_config = capo_mediapackage_vod._auth._sigv4.build_sigv4_auth_scheme(
                "mediapackage-vod", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_mediapackage_vod._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_mediapackage_vod.types.update_packaging_group_request.UpdatePackagingGroupRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/packaging_groups/{Id}"
    url = url.replace("{Id}", quote(input_["id"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_mediapackage_vod.types.update_packaging_group_request.serialize_json(
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
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def update_packaging_group(
    options: OperationOptions,
    input_: capo_mediapackage_vod.types.update_packaging_group_request.UpdatePackagingGroupRequest,
) -> tuple[
    capo_mediapackage_vod.types.update_packaging_group_response.UpdatePackagingGroupResponse,
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


async def async_update_packaging_group(
    options: AsyncOperationOptions,
    input_: capo_mediapackage_vod.types.update_packaging_group_request.UpdatePackagingGroupRequest,
) -> tuple[
    capo_mediapackage_vod.types.update_packaging_group_response.UpdatePackagingGroupResponse,
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
