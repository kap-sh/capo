"""Generated from Smithy shape ``com.amazonaws.detective#CreateMembers``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_detective._auth._signers
import capo_detective._auth._sigv4
import capo_detective._protocol.eventstream
import capo_detective.errors.access_denied_exception
import capo_detective.errors.internal_server_exception
import capo_detective.errors.resource_not_found_exception
import capo_detective.errors.service_quota_exceeded_exception
import capo_detective.errors.validation_exception
import capo_detective.types.account_list
import capo_detective.types.create_members_request
import capo_detective.types.create_members_response
import capo_detective.types.member_detail_list
import capo_detective.types.unprocessed_account_list
from capo_detective._protocol.errors import parse_error_metadata_json
from capo_detective._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_detective._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_detective.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_detective.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "InternalServerException":
            raise capo_detective.errors.internal_server_exception.InternalServerException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_detective.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "ServiceQuotaExceededException":
            raise capo_detective.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_detective.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_detective.types.create_members_response.CreateMembersResponse:
    out: capo_detective.types.create_members_response.CreateMembersResponse = (
        capo_detective.types.create_members_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_detective.types.create_members_response.CreateMembersResponse:
    out: capo_detective.types.create_members_response.CreateMembersResponse = (
        capo_detective.types.create_members_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_detective._auth._signers.Signer | None:
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
            sigv4_config = capo_detective._auth._sigv4.build_sigv4_auth_scheme(
                "detective", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_detective._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_detective.types.create_members_request.CreateMembersRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/graph/members"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_detective.types.create_members_request.serialize_json(input_),
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


def create_members(
    options: OperationOptions,
    input_: capo_detective.types.create_members_request.CreateMembersRequest,
) -> tuple[
    capo_detective.types.create_members_response.CreateMembersResponse, zapros.Response
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


async def async_create_members(
    options: AsyncOperationOptions,
    input_: capo_detective.types.create_members_request.CreateMembersRequest,
) -> tuple[
    capo_detective.types.create_members_response.CreateMembersResponse, zapros.Response
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
