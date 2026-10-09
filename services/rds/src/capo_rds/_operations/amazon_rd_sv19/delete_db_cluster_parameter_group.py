"""Generated from Smithy shape ``com.amazonaws.rds#DeleteDBClusterParameterGroup``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import capo_rds._auth._signers
import capo_rds._auth._sigv4
import capo_rds._protocol.eventstream
import capo_rds.errors.db_parameter_group_not_found_fault
import capo_rds.errors.invalid_db_parameter_group_state_fault
import capo_rds.types.delete_db_cluster_parameter_group_message
from capo_rds._protocol.errors import find_error_element, parse_error_metadata
from capo_rds._protocol.xml import fromstring
from capo_rds._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_rds._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_rds.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    error_el = find_error_element(root)
    match code:
        case "DBParameterGroupNotFound":
            raise capo_rds.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault.from_query(
                error_el, message
            )
        case "InvalidDBParameterGroupState":
            raise capo_rds.errors.invalid_db_parameter_group_state_fault.InvalidDBParameterGroupStateFault.from_query(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_rds._auth._signers.Signer | None:
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
            sigv4_config = capo_rds._auth._sigv4.build_sigv4_auth_scheme(
                "rds", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_rds._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_rds.types.delete_db_cluster_parameter_group_message.DeleteDBClusterParameterGroupMessage,
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
    pairs: list[tuple[str, str]] = []
    pairs.append(("Action", "DeleteDBClusterParameterGroup"))
    pairs.append(("Version", "2014-10-31"))
    capo_rds.types.delete_db_cluster_parameter_group_message.serialize_query(
        input_, pairs, ""
    )
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
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


def delete_db_cluster_parameter_group(
    options: OperationOptions,
    input_: capo_rds.types.delete_db_cluster_parameter_group_message.DeleteDBClusterParameterGroupMessage,
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


async def async_delete_db_cluster_parameter_group(
    options: AsyncOperationOptions,
    input_: capo_rds.types.delete_db_cluster_parameter_group_message.DeleteDBClusterParameterGroupMessage,
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
