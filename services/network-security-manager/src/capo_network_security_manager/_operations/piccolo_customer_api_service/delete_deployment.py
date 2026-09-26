"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#DeleteDeployment``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_network_security_manager._auth._signers
import capo_network_security_manager._auth._sigv4
import capo_network_security_manager._protocol.eventstream
import capo_network_security_manager.errors.access_denied_exception
import capo_network_security_manager.errors.conflict_exception
import capo_network_security_manager.errors.internal_server_exception
import capo_network_security_manager.errors.throttling_exception
import capo_network_security_manager.errors.validation_exception
import capo_network_security_manager.types.delete_deployment_input
from capo_network_security_manager._protocol.errors import parse_error_metadata_json
from capo_network_security_manager._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_network_security_manager._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_network_security_manager.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_network_security_manager.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "ConflictException":
            raise capo_network_security_manager.errors.conflict_exception.ConflictException.from_json(
                data, message
            )
        case "InternalServerException":
            raise capo_network_security_manager.errors.internal_server_exception.InternalServerException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_network_security_manager.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_network_security_manager.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_network_security_manager._auth._signers.Signer | None:
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
            sigv4_config = (
                capo_network_security_manager._auth._sigv4.build_sigv4_auth_scheme(
                    "network-security-manager", options.region, endpoint_scheme
                )
            )
            if sigv4_config is not None:
                return capo_network_security_manager._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_network_security_manager.types.delete_deployment_input.DeleteDeploymentInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/deployments/{deploymentIdentifier}"
    url = url.replace(
        "{deploymentIdentifier}", quote(input_["deployment_identifier"], safe="")
    )
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "DELETE", headers=headers, body=body, context={"signer": signer}
    )


def delete_deployment(
    options: OperationOptions,
    input_: capo_network_security_manager.types.delete_deployment_input.DeleteDeploymentInput,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            handle_error(response)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_delete_deployment(
    options: AsyncOperationOptions,
    input_: capo_network_security_manager.types.delete_deployment_input.DeleteDeploymentInput,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 300:
            await response.aread()
            handle_error(response)
        return None, response
    except BaseException:
        await response.aclose()
        raise
