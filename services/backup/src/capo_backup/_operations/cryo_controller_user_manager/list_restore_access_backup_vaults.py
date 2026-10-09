"""Generated from Smithy shape ``com.amazonaws.backup#ListRestoreAccessBackupVaults``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_backup._auth._signers
import capo_backup._auth._sigv4
import capo_backup._protocol.eventstream
import capo_backup.errors.invalid_parameter_value_exception
import capo_backup.errors.missing_parameter_value_exception
import capo_backup.errors.resource_not_found_exception
import capo_backup.errors.service_unavailable_exception
import capo_backup.types.list_restore_access_backup_vaults_input
import capo_backup.types.list_restore_access_backup_vaults_output
import capo_backup.types.restore_access_backup_vault_list
from capo_backup._protocol.errors import parse_error_metadata_json
from capo_backup._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_backup._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_backup.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidParameterValueException":
            raise capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data, message
            )
        case "MissingParameterValueException":
            raise capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_backup.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "ServiceUnavailableException":
            raise capo_backup.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_backup.types.list_restore_access_backup_vaults_output.ListRestoreAccessBackupVaultsOutput:
    out: capo_backup.types.list_restore_access_backup_vaults_output.ListRestoreAccessBackupVaultsOutput = capo_backup.types.list_restore_access_backup_vaults_output.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_backup.types.list_restore_access_backup_vaults_output.ListRestoreAccessBackupVaultsOutput:
    out: capo_backup.types.list_restore_access_backup_vaults_output.ListRestoreAccessBackupVaultsOutput = capo_backup.types.list_restore_access_backup_vaults_output.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_backup._auth._signers.Signer | None:
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
            sigv4_config = capo_backup._auth._sigv4.build_sigv4_auth_scheme(
                "backup", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_backup._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_backup.types.list_restore_access_backup_vaults_input.ListRestoreAccessBackupVaultsInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/logically-air-gapped-backup-vaults/{BackupVaultName}/restore-access-backup-vaults"
    )
    url = url.replace("{BackupVaultName}", quote(input_["backup_vault_name"], safe=""))
    params: list[tuple[str, str]] = []
    if "next_token" in input_:
        params.append(("nextToken", input_["next_token"]))
    if "max_results" in input_:
        params.append(("maxResults", str(input_["max_results"])))
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


def list_restore_access_backup_vaults(
    options: OperationOptions,
    input_: capo_backup.types.list_restore_access_backup_vaults_input.ListRestoreAccessBackupVaultsInput,
) -> tuple[
    capo_backup.types.list_restore_access_backup_vaults_output.ListRestoreAccessBackupVaultsOutput,
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


async def async_list_restore_access_backup_vaults(
    options: AsyncOperationOptions,
    input_: capo_backup.types.list_restore_access_backup_vaults_input.ListRestoreAccessBackupVaultsInput,
) -> tuple[
    capo_backup.types.list_restore_access_backup_vaults_output.ListRestoreAccessBackupVaultsOutput,
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
