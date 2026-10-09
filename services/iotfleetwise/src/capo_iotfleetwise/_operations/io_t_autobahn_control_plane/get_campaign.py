"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetCampaign``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_iotfleetwise._auth._signers
import capo_iotfleetwise._auth._sigv4
import capo_iotfleetwise._protocol.eventstream
import capo_iotfleetwise.errors.access_denied_exception
import capo_iotfleetwise.errors.internal_server_exception
import capo_iotfleetwise.errors.resource_not_found_exception
import capo_iotfleetwise.errors.throttling_exception
import capo_iotfleetwise.errors.validation_exception
import capo_iotfleetwise.types.campaign_status
import capo_iotfleetwise.types.collection_scheme
import capo_iotfleetwise.types.compression
import capo_iotfleetwise.types.data_destination_configs
import capo_iotfleetwise.types.data_extra_dimension_node_path_list
import capo_iotfleetwise.types.data_partitions
import capo_iotfleetwise.types.diagnostics_mode
import capo_iotfleetwise.types.get_campaign_request
import capo_iotfleetwise.types.get_campaign_response
import capo_iotfleetwise.types.signal_fetch_information_list
import capo_iotfleetwise.types.signal_information_list
import capo_iotfleetwise.types.spooling_mode
import capo_iotfleetwise.types.timestamp
from capo_iotfleetwise._protocol.errors import parse_error_metadata_json
from capo_iotfleetwise._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_iotfleetwise._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_iotfleetwise.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServerException":
            raise capo_iotfleetwise.errors.internal_server_exception.InternalServerException.from_aws_json_1_0(
                data, message
            )
        case "AccessDeniedException":
            raise capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_0(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_0(
                data, message
            )
        case "ThrottlingException":
            raise capo_iotfleetwise.errors.throttling_exception.ThrottlingException.from_aws_json_1_0(
                data, message
            )
        case "ValidationException":
            raise capo_iotfleetwise.errors.validation_exception.ValidationException.from_aws_json_1_0(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_iotfleetwise.types.get_campaign_response.GetCampaignResponse:
    out: capo_iotfleetwise.types.get_campaign_response.GetCampaignResponse = (
        capo_iotfleetwise.types.get_campaign_response.deserialize_aws_json_1_0(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_iotfleetwise.types.get_campaign_response.GetCampaignResponse:
    out: capo_iotfleetwise.types.get_campaign_response.GetCampaignResponse = (
        capo_iotfleetwise.types.get_campaign_response.deserialize_aws_json_1_0(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_iotfleetwise._auth._signers.Signer | None:
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
            sigv4_config = capo_iotfleetwise._auth._sigv4.build_sigv4_auth_scheme(
                "iotfleetwise", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_iotfleetwise._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_iotfleetwise.types.get_campaign_request.GetCampaignRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/campaigns/{name}"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "IoTAutobahnControlPlane.GetCampaign"
    body: bytes | None = json.dumps(
        capo_iotfleetwise.types.get_campaign_request.serialize_aws_json_1_0(input_),
        allow_nan=False,
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.0"
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


def get_campaign(
    options: OperationOptions,
    input_: capo_iotfleetwise.types.get_campaign_request.GetCampaignRequest,
) -> tuple[
    capo_iotfleetwise.types.get_campaign_response.GetCampaignResponse, zapros.Response
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


async def async_get_campaign(
    options: AsyncOperationOptions,
    input_: capo_iotfleetwise.types.get_campaign_request.GetCampaignRequest,
) -> tuple[
    capo_iotfleetwise.types.get_campaign_response.GetCampaignResponse, zapros.Response
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
