"""Generated from Smithy shape ``com.amazonaws.eks#DescribeClusterVersions``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_eks._auth._signers
import capo_eks._auth._sigv4
import capo_eks._protocol.eventstream
import capo_eks.errors.invalid_parameter_exception
import capo_eks.errors.invalid_request_exception
import capo_eks.errors.server_exception
import capo_eks.types.cluster_version_list
import capo_eks.types.cluster_version_status
import capo_eks.types.describe_cluster_versions_request
import capo_eks.types.describe_cluster_versions_response
import capo_eks.types.string_list
import capo_eks.types.version_status
from capo_eks._protocol.errors import parse_error_metadata_json
from capo_eks._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_eks._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_eks.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidParameterException":
            raise capo_eks.errors.invalid_parameter_exception.InvalidParameterException.from_json(
                data, message
            )
        case "InvalidRequestException":
            raise capo_eks.errors.invalid_request_exception.InvalidRequestException.from_json(
                data, message
            )
        case "ServerException":
            raise capo_eks.errors.server_exception.ServerException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_eks.types.describe_cluster_versions_response.DescribeClusterVersionsResponse:
    out: capo_eks.types.describe_cluster_versions_response.DescribeClusterVersionsResponse = capo_eks.types.describe_cluster_versions_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_eks.types.describe_cluster_versions_response.DescribeClusterVersionsResponse:
    out: capo_eks.types.describe_cluster_versions_response.DescribeClusterVersionsResponse = capo_eks.types.describe_cluster_versions_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_eks._auth._signers.Signer | None:
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
            sigv4_config = capo_eks._auth._sigv4.build_sigv4_auth_scheme(
                "eks", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_eks._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_eks.types.describe_cluster_versions_request.DescribeClusterVersionsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_eks.types.cluster_version_status
    import capo_eks.types.version_status

    url = endpoint.url.rstrip("/") + "/cluster-versions"
    params: list[tuple[str, str]] = []
    if "cluster_type" in input_:
        params.append(("clusterType", input_["cluster_type"]))
    if "max_results" in input_:
        params.append(("maxResults", str(input_["max_results"])))
    if "next_token" in input_:
        params.append(("nextToken", input_["next_token"]))
    if "default_only" in input_:
        params.append(("defaultOnly", "true" if input_["default_only"] else "false"))
    if "include_all" in input_:
        params.append(("includeAll", "true" if input_["include_all"] else "false"))
    if "cluster_versions" in input_:
        for item in input_["cluster_versions"]:
            params.append(("clusterVersions", item))
    if "status" in input_:
        params.append(
            (
                "status",
                capo_eks.types.cluster_version_status.serialize_json(input_["status"]),
            )
        )
    if "version_status" in input_:
        params.append(
            (
                "versionStatus",
                capo_eks.types.version_status.serialize_json(input_["version_status"]),
            )
        )
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


def describe_cluster_versions(
    options: OperationOptions,
    input_: capo_eks.types.describe_cluster_versions_request.DescribeClusterVersionsRequest,
) -> tuple[
    capo_eks.types.describe_cluster_versions_response.DescribeClusterVersionsResponse,
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


async def async_describe_cluster_versions(
    options: AsyncOperationOptions,
    input_: capo_eks.types.describe_cluster_versions_request.DescribeClusterVersionsRequest,
) -> tuple[
    capo_eks.types.describe_cluster_versions_response.DescribeClusterVersionsResponse,
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
