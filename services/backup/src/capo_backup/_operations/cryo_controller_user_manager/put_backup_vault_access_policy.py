"""Generated from Smithy shape ``com.amazonaws.backup#PutBackupVaultAccessPolicy``."""

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
import capo_backup.types.put_backup_vault_access_policy_input
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
    input_: capo_backup.types.put_backup_vault_access_policy_input.PutBackupVaultAccessPolicyInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/backup-vaults/{BackupVaultName}/access-policy"
    url = url.replace("{BackupVaultName}", quote(input_["backup_vault_name"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_backup.types.put_backup_vault_access_policy_input.serialize_json(input_),
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


def put_backup_vault_access_policy(
    options: OperationOptions,
    input_: capo_backup.types.put_backup_vault_access_policy_input.PutBackupVaultAccessPolicyInput,
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


async def async_put_backup_vault_access_policy(
    options: AsyncOperationOptions,
    input_: capo_backup.types.put_backup_vault_access_policy_input.PutBackupVaultAccessPolicyInput,
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
