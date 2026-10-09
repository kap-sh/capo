"""Generated from Smithy shape ``com.amazonaws.appsync#ListTypesByAssociation``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_appsync._auth._signers
import capo_appsync._auth._sigv4
import capo_appsync._protocol.eventstream
import capo_appsync.errors.bad_request_exception
import capo_appsync.errors.concurrent_modification_exception
import capo_appsync.errors.internal_failure_exception
import capo_appsync.errors.not_found_exception
import capo_appsync.errors.unauthorized_exception
import capo_appsync.types.list_types_by_association_request
import capo_appsync.types.list_types_by_association_response
import capo_appsync.types.type_definition_format
import capo_appsync.types.type_list
from capo_appsync._protocol.errors import parse_error_metadata_json
from capo_appsync._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_appsync._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_appsync.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            raise capo_appsync.errors.bad_request_exception.BadRequestException.from_json(
                data, message
            )
        case "ConcurrentModificationException":
            raise capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException.from_json(
                data, message
            )
        case "InternalFailureException":
            raise capo_appsync.errors.internal_failure_exception.InternalFailureException.from_json(
                data, message
            )
        case "NotFoundException":
            raise capo_appsync.errors.not_found_exception.NotFoundException.from_json(
                data, message
            )
        case "UnauthorizedException":
            raise capo_appsync.errors.unauthorized_exception.UnauthorizedException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> (
    capo_appsync.types.list_types_by_association_response.ListTypesByAssociationResponse
):
    out: capo_appsync.types.list_types_by_association_response.ListTypesByAssociationResponse = capo_appsync.types.list_types_by_association_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> (
    capo_appsync.types.list_types_by_association_response.ListTypesByAssociationResponse
):
    out: capo_appsync.types.list_types_by_association_response.ListTypesByAssociationResponse = capo_appsync.types.list_types_by_association_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_appsync._auth._signers.Signer | None:
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
            sigv4_config = capo_appsync._auth._sigv4.build_sigv4_auth_scheme(
                "appsync", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_appsync._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_appsync.types.list_types_by_association_request.ListTypesByAssociationRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_appsync.types.type_definition_format

    url = (
        endpoint.url.rstrip("/")
        + "/v1/mergedApis/{mergedApiIdentifier}/sourceApiAssociations/{associationId}/types"
    )
    url = url.replace(
        "{mergedApiIdentifier}", quote(input_["merged_api_identifier"], safe="")
    )
    url = url.replace("{associationId}", quote(input_["association_id"], safe=""))
    params: list[tuple[str, str]] = []
    if "format" in input_:
        params.append(
            (
                "format",
                capo_appsync.types.type_definition_format.serialize_json(
                    input_["format"]
                ),
            )
        )
    if "next_token" in input_:
        params.append(("nextToken", input_["next_token"]))
    params.append(("maxResults", str(input_.get("max_results", 0))))
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
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_types_by_association(
    options: OperationOptions,
    input_: capo_appsync.types.list_types_by_association_request.ListTypesByAssociationRequest,
) -> tuple[
    capo_appsync.types.list_types_by_association_response.ListTypesByAssociationResponse,
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


async def async_list_types_by_association(
    options: AsyncOperationOptions,
    input_: capo_appsync.types.list_types_by_association_request.ListTypesByAssociationRequest,
) -> tuple[
    capo_appsync.types.list_types_by_association_response.ListTypesByAssociationResponse,
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
