"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeApplicationFleetAssociations``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import capo_appstream._auth._signers
import capo_appstream._auth._sigv4
import capo_appstream._protocol.eventstream
import capo_appstream.errors.invalid_parameter_combination_exception
import capo_appstream.errors.operation_not_permitted_exception
import capo_appstream.types.application_fleet_association_list
import capo_appstream.types.describe_application_fleet_associations_request
import capo_appstream.types.describe_application_fleet_associations_result
from capo_appstream._protocol import cbor
from capo_appstream._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_appstream._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_appstream.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data, code, message = cbor.parse_error(response)
    match code:
        case "InvalidParameterCombinationException":
            raise capo_appstream.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException.from_cbor(
                data, message, response=response
            )
        case "OperationNotPermittedException":
            raise capo_appstream.errors.operation_not_permitted_exception.OperationNotPermittedException.from_cbor(
                data, message, response=response
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_appstream.types.describe_application_fleet_associations_result.DescribeApplicationFleetAssociationsResult:
    out: capo_appstream.types.describe_application_fleet_associations_result.DescribeApplicationFleetAssociationsResult = capo_appstream.types.describe_application_fleet_associations_result.deserialize_cbor(
        cbor.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_appstream.types.describe_application_fleet_associations_result.DescribeApplicationFleetAssociationsResult:
    out: capo_appstream.types.describe_application_fleet_associations_result.DescribeApplicationFleetAssociationsResult = capo_appstream.types.describe_application_fleet_associations_result.deserialize_cbor(
        cbor.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_appstream._auth._signers.Signer | None:
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
            sigv4_config = capo_appstream._auth._sigv4.build_sigv4_auth_scheme(
                "appstream", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_appstream._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_appstream.types.describe_application_fleet_associations_request.DescribeApplicationFleetAssociationsRequest,
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
        + "/service/PhotonAdminProxyService/operation/DescribeApplicationFleetAssociations"
    )
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["smithy-protocol"] = "rpc-v2-cbor"
    headers["accept"] = "application/cbor"
    body: bytes | None = cbor.dumps(
        capo_appstream.types.describe_application_fleet_associations_request.serialize_cbor(
            input_
        )
    )
    headers["content-type"] = "application/cbor"
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


def describe_application_fleet_associations(
    options: OperationOptions,
    input_: capo_appstream.types.describe_application_fleet_associations_request.DescribeApplicationFleetAssociationsRequest,
) -> tuple[
    capo_appstream.types.describe_application_fleet_associations_result.DescribeApplicationFleetAssociationsResult,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if (
            response.status != 200
            or response.headers.get("smithy-protocol") != "rpc-v2-cbor"
        ):
            response.read()
            raise_error(response, handle_error)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_describe_application_fleet_associations(
    options: AsyncOperationOptions,
    input_: capo_appstream.types.describe_application_fleet_associations_request.DescribeApplicationFleetAssociationsRequest,
) -> tuple[
    capo_appstream.types.describe_application_fleet_associations_result.DescribeApplicationFleetAssociationsResult,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if (
            response.status != 200
            or response.headers.get("smithy-protocol") != "rpc-v2-cbor"
        ):
            await response.aread()
            raise_error(response, handle_error)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
