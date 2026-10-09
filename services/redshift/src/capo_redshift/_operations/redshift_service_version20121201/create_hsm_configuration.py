"""Generated from Smithy shape ``com.amazonaws.redshift#CreateHsmConfiguration``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import capo_redshift._auth._signers
import capo_redshift._auth._sigv4
import capo_redshift._protocol.eventstream
import capo_redshift.errors.hsm_configuration_already_exists_fault
import capo_redshift.errors.hsm_configuration_quota_exceeded_fault
import capo_redshift.errors.invalid_tag_fault
import capo_redshift.errors.tag_limit_exceeded_fault
import capo_redshift.types.create_hsm_configuration_message
import capo_redshift.types.create_hsm_configuration_result
import capo_redshift.types.hsm_configuration
import capo_redshift.types.tag_list
from capo_redshift._protocol.errors import find_error_element, parse_error_metadata
from capo_redshift._protocol.xml import fromstring
from capo_redshift._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_redshift._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_redshift.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    error_el = find_error_element(root)
    match code:
        case "HsmConfigurationAlreadyExistsFault":
            raise capo_redshift.errors.hsm_configuration_already_exists_fault.HsmConfigurationAlreadyExistsFault.from_query(
                error_el, message
            )
        case "HsmConfigurationQuotaExceededFault":
            raise capo_redshift.errors.hsm_configuration_quota_exceeded_fault.HsmConfigurationQuotaExceededFault.from_query(
                error_el, message
            )
        case "InvalidTagFault":
            raise capo_redshift.errors.invalid_tag_fault.InvalidTagFault.from_query(
                error_el, message
            )
        case "TagLimitExceededFault":
            raise capo_redshift.errors.tag_limit_exceeded_fault.TagLimitExceededFault.from_query(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_redshift.types.create_hsm_configuration_result.CreateHsmConfigurationResult:
    root = fromstring(response.read())
    result = root.find("CreateHsmConfigurationResult")
    out: capo_redshift.types.create_hsm_configuration_result.CreateHsmConfigurationResult = capo_redshift.types.create_hsm_configuration_result.deserialize_query(
        result if result is not None else root
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_redshift.types.create_hsm_configuration_result.CreateHsmConfigurationResult:
    root = fromstring(await response.aread())
    result = root.find("CreateHsmConfigurationResult")
    out: capo_redshift.types.create_hsm_configuration_result.CreateHsmConfigurationResult = capo_redshift.types.create_hsm_configuration_result.deserialize_query(
        result if result is not None else root
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_redshift._auth._signers.Signer | None:
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
            sigv4_config = capo_redshift._auth._sigv4.build_sigv4_auth_scheme(
                "redshift", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_redshift._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_redshift.types.create_hsm_configuration_message.CreateHsmConfigurationMessage,
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
    pairs.append(("Action", "CreateHsmConfiguration"))
    pairs.append(("Version", "2012-12-01"))
    capo_redshift.types.create_hsm_configuration_message.serialize_query(
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


def create_hsm_configuration(
    options: OperationOptions,
    input_: capo_redshift.types.create_hsm_configuration_message.CreateHsmConfigurationMessage,
) -> tuple[
    capo_redshift.types.create_hsm_configuration_result.CreateHsmConfigurationResult,
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


async def async_create_hsm_configuration(
    options: AsyncOperationOptions,
    input_: capo_redshift.types.create_hsm_configuration_message.CreateHsmConfigurationMessage,
) -> tuple[
    capo_redshift.types.create_hsm_configuration_result.CreateHsmConfigurationResult,
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
