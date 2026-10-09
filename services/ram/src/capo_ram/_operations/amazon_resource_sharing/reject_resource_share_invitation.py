"""Generated from Smithy shape ``com.amazonaws.ram#RejectResourceShareInvitation``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_ram._auth._signers
import capo_ram._auth._sigv4
import capo_ram._protocol.eventstream
import capo_ram.errors.idempotent_parameter_mismatch_exception
import capo_ram.errors.invalid_client_token_exception
import capo_ram.errors.malformed_arn_exception
import capo_ram.errors.operation_not_permitted_exception
import capo_ram.errors.resource_share_invitation_already_accepted_exception
import capo_ram.errors.resource_share_invitation_already_rejected_exception
import capo_ram.errors.resource_share_invitation_arn_not_found_exception
import capo_ram.errors.resource_share_invitation_expired_exception
import capo_ram.errors.server_internal_exception
import capo_ram.errors.service_unavailable_exception
import capo_ram.types.reject_resource_share_invitation_request
import capo_ram.types.reject_resource_share_invitation_response
import capo_ram.types.resource_share_invitation
from capo_ram._protocol.errors import parse_error_metadata_json
from capo_ram._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_ram._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_ram.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "IdempotentParameterMismatchException":
            raise capo_ram.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException.from_json(
                data, message
            )
        case "InvalidClientTokenException":
            raise capo_ram.errors.invalid_client_token_exception.InvalidClientTokenException.from_json(
                data, message
            )
        case "MalformedArnException":
            raise capo_ram.errors.malformed_arn_exception.MalformedArnException.from_json(
                data, message
            )
        case "OperationNotPermittedException":
            raise capo_ram.errors.operation_not_permitted_exception.OperationNotPermittedException.from_json(
                data, message
            )
        case "ResourceShareInvitationAlreadyAcceptedException":
            raise capo_ram.errors.resource_share_invitation_already_accepted_exception.ResourceShareInvitationAlreadyAcceptedException.from_json(
                data, message
            )
        case "ResourceShareInvitationAlreadyRejectedException":
            raise capo_ram.errors.resource_share_invitation_already_rejected_exception.ResourceShareInvitationAlreadyRejectedException.from_json(
                data, message
            )
        case "ResourceShareInvitationArnNotFoundException":
            raise capo_ram.errors.resource_share_invitation_arn_not_found_exception.ResourceShareInvitationArnNotFoundException.from_json(
                data, message
            )
        case "ResourceShareInvitationExpiredException":
            raise capo_ram.errors.resource_share_invitation_expired_exception.ResourceShareInvitationExpiredException.from_json(
                data, message
            )
        case "ServerInternalException":
            raise capo_ram.errors.server_internal_exception.ServerInternalException.from_json(
                data, message
            )
        case "ServiceUnavailableException":
            raise capo_ram.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_ram.types.reject_resource_share_invitation_response.RejectResourceShareInvitationResponse:
    out: capo_ram.types.reject_resource_share_invitation_response.RejectResourceShareInvitationResponse = capo_ram.types.reject_resource_share_invitation_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_ram.types.reject_resource_share_invitation_response.RejectResourceShareInvitationResponse:
    out: capo_ram.types.reject_resource_share_invitation_response.RejectResourceShareInvitationResponse = capo_ram.types.reject_resource_share_invitation_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_ram._auth._signers.Signer | None:
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
            sigv4_config = capo_ram._auth._sigv4.build_sigv4_auth_scheme(
                "ram", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_ram._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_ram.types.reject_resource_share_invitation_request.RejectResourceShareInvitationRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/rejectresourceshareinvitation"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_ram.types.reject_resource_share_invitation_request.serialize_json(input_),
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


def reject_resource_share_invitation(
    options: OperationOptions,
    input_: capo_ram.types.reject_resource_share_invitation_request.RejectResourceShareInvitationRequest,
) -> tuple[
    capo_ram.types.reject_resource_share_invitation_response.RejectResourceShareInvitationResponse,
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


async def async_reject_resource_share_invitation(
    options: AsyncOperationOptions,
    input_: capo_ram.types.reject_resource_share_invitation_request.RejectResourceShareInvitationRequest,
) -> tuple[
    capo_ram.types.reject_resource_share_invitation_response.RejectResourceShareInvitationResponse,
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
