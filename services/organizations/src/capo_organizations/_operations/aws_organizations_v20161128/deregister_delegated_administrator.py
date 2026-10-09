"""Generated from Smithy shape ``com.amazonaws.organizations#DeregisterDelegatedAdministrator``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_organizations._auth._signers
import capo_organizations._auth._sigv4
import capo_organizations._protocol.eventstream
import capo_organizations.errors.access_denied_exception
import capo_organizations.errors.account_not_found_exception
import capo_organizations.errors.account_not_registered_exception
import capo_organizations.errors.aws_organizations_not_in_use_exception
import capo_organizations.errors.concurrent_modification_exception
import capo_organizations.errors.constraint_violation_exception
import capo_organizations.errors.invalid_input_exception
import capo_organizations.errors.service_exception
import capo_organizations.errors.too_many_requests_exception
import capo_organizations.errors.unsupported_api_endpoint_exception
import capo_organizations.types.deregister_delegated_administrator_request
from capo_organizations._protocol.errors import parse_error_metadata_json
from capo_organizations._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_organizations._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_organizations.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_organizations.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data, message
            )
        case "AccountNotFoundException":
            raise capo_organizations.errors.account_not_found_exception.AccountNotFoundException.from_aws_json_1_1(
                data, message
            )
        case "AccountNotRegisteredException":
            raise capo_organizations.errors.account_not_registered_exception.AccountNotRegisteredException.from_aws_json_1_1(
                data, message
            )
        case "AWSOrganizationsNotInUseException":
            raise capo_organizations.errors.aws_organizations_not_in_use_exception.AWSOrganizationsNotInUseException.from_aws_json_1_1(
                data, message
            )
        case "ConcurrentModificationException":
            raise capo_organizations.errors.concurrent_modification_exception.ConcurrentModificationException.from_aws_json_1_1(
                data, message
            )
        case "ConstraintViolationException":
            raise capo_organizations.errors.constraint_violation_exception.ConstraintViolationException.from_aws_json_1_1(
                data, message
            )
        case "InvalidInputException":
            raise capo_organizations.errors.invalid_input_exception.InvalidInputException.from_aws_json_1_1(
                data, message
            )
        case "ServiceException":
            raise capo_organizations.errors.service_exception.ServiceException.from_aws_json_1_1(
                data, message
            )
        case "TooManyRequestsException":
            raise capo_organizations.errors.too_many_requests_exception.TooManyRequestsException.from_aws_json_1_1(
                data, message
            )
        case "UnsupportedAPIEndpointException":
            raise capo_organizations.errors.unsupported_api_endpoint_exception.UnsupportedAPIEndpointException.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_organizations._auth._signers.Signer | None:
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
            sigv4_config = capo_organizations._auth._sigv4.build_sigv4_auth_scheme(
                "organizations", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_organizations._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_organizations.types.deregister_delegated_administrator_request.DeregisterDelegatedAdministratorRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = (
        "AWSOrganizationsV20161128.DeregisterDelegatedAdministrator"
    )
    body: bytes | None = json.dumps(
        capo_organizations.types.deregister_delegated_administrator_request.serialize_aws_json_1_1(
            input_
        ),
        allow_nan=False,
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
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


def deregister_delegated_administrator(
    options: OperationOptions,
    input_: capo_organizations.types.deregister_delegated_administrator_request.DeregisterDelegatedAdministratorRequest,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            raise_error(response, handle_error)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_deregister_delegated_administrator(
    options: AsyncOperationOptions,
    input_: capo_organizations.types.deregister_delegated_administrator_request.DeregisterDelegatedAdministratorRequest,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 300:
            await response.aread()
            raise_error(response, handle_error)
        return None, response
    except BaseException:
        await response.aclose()
        raise
