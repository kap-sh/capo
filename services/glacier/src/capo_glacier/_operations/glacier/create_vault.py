"""Generated from Smithy shape ``com.amazonaws.glacier#CreateVault``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_glacier._auth._signers
import capo_glacier._auth._sigv4
import capo_glacier._protocol.eventstream
import capo_glacier.errors.invalid_parameter_value_exception
import capo_glacier.errors.limit_exceeded_exception
import capo_glacier.errors.missing_parameter_value_exception
import capo_glacier.errors.no_longer_supported_exception
import capo_glacier.errors.service_unavailable_exception
import capo_glacier.types.create_vault_input
import capo_glacier.types.create_vault_output
from capo_glacier._protocol.errors import parse_error_metadata_json
from capo_glacier._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_glacier._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_glacier.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidParameterValueException":
            raise capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data, message
            )
        case "LimitExceededException":
            raise capo_glacier.errors.limit_exceeded_exception.LimitExceededException.from_json(
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
        case "ServiceUnavailableException":
            raise capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_glacier.types.create_vault_output.CreateVaultOutput:
    out: capo_glacier.types.create_vault_output.CreateVaultOutput = {}  # type: ignore[typeddict-item]
    if "Location" in response.headers:
        out["location"] = response.headers["Location"]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_glacier.types.create_vault_output.CreateVaultOutput:
    out: capo_glacier.types.create_vault_output.CreateVaultOutput = {}  # type: ignore[typeddict-item]
    if "Location" in response.headers:
        out["location"] = response.headers["Location"]
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
    input_: capo_glacier.types.create_vault_input.CreateVaultInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/{accountId}/vaults/{vaultName}"
    url = url.replace("{accountId}", quote(input_["account_id"], safe=""))
    url = url.replace("{vaultName}", quote(input_["vault_name"], safe=""))
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
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def create_vault(
    options: OperationOptions,
    input_: capo_glacier.types.create_vault_input.CreateVaultInput,
) -> tuple[capo_glacier.types.create_vault_output.CreateVaultOutput, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            raise_error(response, handle_error)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_create_vault(
    options: AsyncOperationOptions,
    input_: capo_glacier.types.create_vault_input.CreateVaultInput,
) -> tuple[capo_glacier.types.create_vault_output.CreateVaultOutput, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 300:
            await response.aread()
            raise_error(response, handle_error)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
