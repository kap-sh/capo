"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#ModifyCluster``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_cloudhsm_v2._auth._signers
import capo_cloudhsm_v2._auth._sigv4
import capo_cloudhsm_v2._protocol.eventstream
import capo_cloudhsm_v2.errors.cloud_hsm_access_denied_exception
import capo_cloudhsm_v2.errors.cloud_hsm_internal_failure_exception
import capo_cloudhsm_v2.errors.cloud_hsm_invalid_request_exception
import capo_cloudhsm_v2.errors.cloud_hsm_resource_not_found_exception
import capo_cloudhsm_v2.errors.cloud_hsm_service_exception
import capo_cloudhsm_v2.types.backup_retention_policy
import capo_cloudhsm_v2.types.cluster
import capo_cloudhsm_v2.types.modify_cluster_request
import capo_cloudhsm_v2.types.modify_cluster_response
from capo_cloudhsm_v2._protocol.errors import parse_error_metadata_json
from capo_cloudhsm_v2._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_cloudhsm_v2._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_cloudhsm_v2.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "CloudHsmAccessDeniedException":
            raise capo_cloudhsm_v2.errors.cloud_hsm_access_denied_exception.CloudHsmAccessDeniedException.from_aws_json_1_1(
                data, message
            )
        case "CloudHsmInternalFailureException":
            raise capo_cloudhsm_v2.errors.cloud_hsm_internal_failure_exception.CloudHsmInternalFailureException.from_aws_json_1_1(
                data, message
            )
        case "CloudHsmInvalidRequestException":
            raise capo_cloudhsm_v2.errors.cloud_hsm_invalid_request_exception.CloudHsmInvalidRequestException.from_aws_json_1_1(
                data, message
            )
        case "CloudHsmResourceNotFoundException":
            raise capo_cloudhsm_v2.errors.cloud_hsm_resource_not_found_exception.CloudHsmResourceNotFoundException.from_aws_json_1_1(
                data, message
            )
        case "CloudHsmServiceException":
            raise capo_cloudhsm_v2.errors.cloud_hsm_service_exception.CloudHsmServiceException.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cloudhsm_v2.types.modify_cluster_response.ModifyClusterResponse:
    out: capo_cloudhsm_v2.types.modify_cluster_response.ModifyClusterResponse = (
        capo_cloudhsm_v2.types.modify_cluster_response.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_cloudhsm_v2.types.modify_cluster_response.ModifyClusterResponse:
    out: capo_cloudhsm_v2.types.modify_cluster_response.ModifyClusterResponse = (
        capo_cloudhsm_v2.types.modify_cluster_response.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_cloudhsm_v2._auth._signers.Signer | None:
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
            sigv4_config = capo_cloudhsm_v2._auth._sigv4.build_sigv4_auth_scheme(
                "cloudhsm", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_cloudhsm_v2._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_cloudhsm_v2.types.modify_cluster_request.ModifyClusterRequest,
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
    headers["X-Amz-Target"] = "BaldrApiService.ModifyCluster"
    body: bytes | None = json.dumps(
        capo_cloudhsm_v2.types.modify_cluster_request.serialize_aws_json_1_1(input_),
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


def modify_cluster(
    options: OperationOptions,
    input_: capo_cloudhsm_v2.types.modify_cluster_request.ModifyClusterRequest,
) -> tuple[
    capo_cloudhsm_v2.types.modify_cluster_response.ModifyClusterResponse,
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


async def async_modify_cluster(
    options: AsyncOperationOptions,
    input_: capo_cloudhsm_v2.types.modify_cluster_request.ModifyClusterRequest,
) -> tuple[
    capo_cloudhsm_v2.types.modify_cluster_response.ModifyClusterResponse,
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
