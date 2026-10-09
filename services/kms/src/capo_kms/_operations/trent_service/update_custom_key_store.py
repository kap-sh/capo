"""Generated from Smithy shape ``com.amazonaws.kms#UpdateCustomKeyStore``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_kms._auth._signers
import capo_kms._auth._sigv4
import capo_kms._protocol.eventstream
import capo_kms.errors.cloud_hsm_cluster_invalid_configuration_exception
import capo_kms.errors.cloud_hsm_cluster_not_active_exception
import capo_kms.errors.cloud_hsm_cluster_not_found_exception
import capo_kms.errors.cloud_hsm_cluster_not_related_exception
import capo_kms.errors.custom_key_store_invalid_state_exception
import capo_kms.errors.custom_key_store_name_in_use_exception
import capo_kms.errors.custom_key_store_not_found_exception
import capo_kms.errors.kms_internal_exception
import capo_kms.errors.xks_proxy_incorrect_authentication_credential_exception
import capo_kms.errors.xks_proxy_invalid_configuration_exception
import capo_kms.errors.xks_proxy_invalid_response_exception
import capo_kms.errors.xks_proxy_uri_endpoint_in_use_exception
import capo_kms.errors.xks_proxy_uri_in_use_exception
import capo_kms.errors.xks_proxy_uri_unreachable_exception
import capo_kms.errors.xks_proxy_vpc_endpoint_service_in_use_exception
import capo_kms.errors.xks_proxy_vpc_endpoint_service_invalid_configuration_exception
import capo_kms.errors.xks_proxy_vpc_endpoint_service_not_found_exception
import capo_kms.types.update_custom_key_store_request
import capo_kms.types.update_custom_key_store_response
import capo_kms.types.xks_proxy_authentication_credential_type
import capo_kms.types.xks_proxy_connectivity_type
from capo_kms._protocol.errors import parse_error_metadata_json
from capo_kms._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_kms._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_kms.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "CloudHsmClusterInvalidConfigurationException":
            raise capo_kms.errors.cloud_hsm_cluster_invalid_configuration_exception.CloudHsmClusterInvalidConfigurationException.from_aws_json_1_1(
                data, message
            )
        case "CloudHsmClusterNotActiveException":
            raise capo_kms.errors.cloud_hsm_cluster_not_active_exception.CloudHsmClusterNotActiveException.from_aws_json_1_1(
                data, message
            )
        case "CloudHsmClusterNotFoundException":
            raise capo_kms.errors.cloud_hsm_cluster_not_found_exception.CloudHsmClusterNotFoundException.from_aws_json_1_1(
                data, message
            )
        case "CloudHsmClusterNotRelatedException":
            raise capo_kms.errors.cloud_hsm_cluster_not_related_exception.CloudHsmClusterNotRelatedException.from_aws_json_1_1(
                data, message
            )
        case "CustomKeyStoreInvalidStateException":
            raise capo_kms.errors.custom_key_store_invalid_state_exception.CustomKeyStoreInvalidStateException.from_aws_json_1_1(
                data, message
            )
        case "CustomKeyStoreNameInUseException":
            raise capo_kms.errors.custom_key_store_name_in_use_exception.CustomKeyStoreNameInUseException.from_aws_json_1_1(
                data, message
            )
        case "CustomKeyStoreNotFoundException":
            raise capo_kms.errors.custom_key_store_not_found_exception.CustomKeyStoreNotFoundException.from_aws_json_1_1(
                data, message
            )
        case "KMSInternalException":
            raise capo_kms.errors.kms_internal_exception.KMSInternalException.from_aws_json_1_1(
                data, message
            )
        case "XksProxyIncorrectAuthenticationCredentialException":
            raise capo_kms.errors.xks_proxy_incorrect_authentication_credential_exception.XksProxyIncorrectAuthenticationCredentialException.from_aws_json_1_1(
                data, message
            )
        case "XksProxyInvalidConfigurationException":
            raise capo_kms.errors.xks_proxy_invalid_configuration_exception.XksProxyInvalidConfigurationException.from_aws_json_1_1(
                data, message
            )
        case "XksProxyInvalidResponseException":
            raise capo_kms.errors.xks_proxy_invalid_response_exception.XksProxyInvalidResponseException.from_aws_json_1_1(
                data, message
            )
        case "XksProxyUriEndpointInUseException":
            raise capo_kms.errors.xks_proxy_uri_endpoint_in_use_exception.XksProxyUriEndpointInUseException.from_aws_json_1_1(
                data, message
            )
        case "XksProxyUriInUseException":
            raise capo_kms.errors.xks_proxy_uri_in_use_exception.XksProxyUriInUseException.from_aws_json_1_1(
                data, message
            )
        case "XksProxyUriUnreachableException":
            raise capo_kms.errors.xks_proxy_uri_unreachable_exception.XksProxyUriUnreachableException.from_aws_json_1_1(
                data, message
            )
        case "XksProxyVpcEndpointServiceInUseException":
            raise capo_kms.errors.xks_proxy_vpc_endpoint_service_in_use_exception.XksProxyVpcEndpointServiceInUseException.from_aws_json_1_1(
                data, message
            )
        case "XksProxyVpcEndpointServiceInvalidConfigurationException":
            raise capo_kms.errors.xks_proxy_vpc_endpoint_service_invalid_configuration_exception.XksProxyVpcEndpointServiceInvalidConfigurationException.from_aws_json_1_1(
                data, message
            )
        case "XksProxyVpcEndpointServiceNotFoundException":
            raise capo_kms.errors.xks_proxy_vpc_endpoint_service_not_found_exception.XksProxyVpcEndpointServiceNotFoundException.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_kms.types.update_custom_key_store_response.UpdateCustomKeyStoreResponse:
    out: capo_kms.types.update_custom_key_store_response.UpdateCustomKeyStoreResponse = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_kms.types.update_custom_key_store_response.UpdateCustomKeyStoreResponse:
    out: capo_kms.types.update_custom_key_store_response.UpdateCustomKeyStoreResponse = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_kms._auth._signers.Signer | None:
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
            sigv4_config = capo_kms._auth._sigv4.build_sigv4_auth_scheme(
                "kms", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_kms._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_kms.types.update_custom_key_store_request.UpdateCustomKeyStoreRequest,
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
    headers["X-Amz-Target"] = "TrentService.UpdateCustomKeyStore"
    body: bytes | None = json.dumps(
        capo_kms.types.update_custom_key_store_request.serialize_aws_json_1_1(input_),
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


def update_custom_key_store(
    options: OperationOptions,
    input_: capo_kms.types.update_custom_key_store_request.UpdateCustomKeyStoreRequest,
) -> tuple[
    capo_kms.types.update_custom_key_store_response.UpdateCustomKeyStoreResponse,
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


async def async_update_custom_key_store(
    options: AsyncOperationOptions,
    input_: capo_kms.types.update_custom_key_store_request.UpdateCustomKeyStoreRequest,
) -> tuple[
    capo_kms.types.update_custom_key_store_response.UpdateCustomKeyStoreResponse,
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
