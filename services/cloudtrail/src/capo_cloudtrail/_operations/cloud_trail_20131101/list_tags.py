"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListTags``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_cloudtrail._auth._signers
import capo_cloudtrail._auth._sigv4
import capo_cloudtrail._protocol.eventstream
import capo_cloudtrail.errors.channel_arn_invalid_exception
import capo_cloudtrail.errors.cloud_trail_arn_invalid_exception
import capo_cloudtrail.errors.event_data_store_arn_invalid_exception
import capo_cloudtrail.errors.event_data_store_not_found_exception
import capo_cloudtrail.errors.inactive_event_data_store_exception
import capo_cloudtrail.errors.invalid_token_exception
import capo_cloudtrail.errors.invalid_trail_name_exception
import capo_cloudtrail.errors.no_management_account_slr_exists_exception
import capo_cloudtrail.errors.operation_not_permitted_exception
import capo_cloudtrail.errors.resource_not_found_exception
import capo_cloudtrail.errors.resource_type_not_supported_exception
import capo_cloudtrail.errors.unsupported_operation_exception
import capo_cloudtrail.types.list_tags_request
import capo_cloudtrail.types.list_tags_response
import capo_cloudtrail.types.resource_id_list
import capo_cloudtrail.types.resource_tag_list
from capo_cloudtrail._protocol.errors import parse_error_metadata_json
from capo_cloudtrail._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_cloudtrail._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_cloudtrail.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ChannelARNInvalidException":
            raise capo_cloudtrail.errors.channel_arn_invalid_exception.ChannelARNInvalidException.from_aws_json_1_1(
                data, message
            )
        case "CloudTrailARNInvalidException":
            raise capo_cloudtrail.errors.cloud_trail_arn_invalid_exception.CloudTrailARNInvalidException.from_aws_json_1_1(
                data, message
            )
        case "EventDataStoreARNInvalidException":
            raise capo_cloudtrail.errors.event_data_store_arn_invalid_exception.EventDataStoreARNInvalidException.from_aws_json_1_1(
                data, message
            )
        case "EventDataStoreNotFoundException":
            raise capo_cloudtrail.errors.event_data_store_not_found_exception.EventDataStoreNotFoundException.from_aws_json_1_1(
                data, message
            )
        case "InactiveEventDataStoreException":
            raise capo_cloudtrail.errors.inactive_event_data_store_exception.InactiveEventDataStoreException.from_aws_json_1_1(
                data, message
            )
        case "InvalidTokenException":
            raise capo_cloudtrail.errors.invalid_token_exception.InvalidTokenException.from_aws_json_1_1(
                data, message
            )
        case "InvalidTrailNameException":
            raise capo_cloudtrail.errors.invalid_trail_name_exception.InvalidTrailNameException.from_aws_json_1_1(
                data, message
            )
        case "NoManagementAccountSLRExistsException":
            raise capo_cloudtrail.errors.no_management_account_slr_exists_exception.NoManagementAccountSLRExistsException.from_aws_json_1_1(
                data, message
            )
        case "OperationNotPermittedException":
            raise capo_cloudtrail.errors.operation_not_permitted_exception.OperationNotPermittedException.from_aws_json_1_1(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_cloudtrail.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_1(
                data, message
            )
        case "ResourceTypeNotSupportedException":
            raise capo_cloudtrail.errors.resource_type_not_supported_exception.ResourceTypeNotSupportedException.from_aws_json_1_1(
                data, message
            )
        case "UnsupportedOperationException":
            raise capo_cloudtrail.errors.unsupported_operation_exception.UnsupportedOperationException.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cloudtrail.types.list_tags_response.ListTagsResponse:
    out: capo_cloudtrail.types.list_tags_response.ListTagsResponse = (
        capo_cloudtrail.types.list_tags_response.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_cloudtrail.types.list_tags_response.ListTagsResponse:
    out: capo_cloudtrail.types.list_tags_response.ListTagsResponse = (
        capo_cloudtrail.types.list_tags_response.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_cloudtrail._auth._signers.Signer | None:
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
            sigv4_config = capo_cloudtrail._auth._sigv4.build_sigv4_auth_scheme(
                "cloudtrail", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_cloudtrail._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_cloudtrail.types.list_tags_request.ListTagsRequest,
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
    headers["X-Amz-Target"] = "CloudTrail_20131101.ListTags"
    body: bytes | None = json.dumps(
        capo_cloudtrail.types.list_tags_request.serialize_aws_json_1_1(input_),
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


def list_tags(
    options: OperationOptions,
    input_: capo_cloudtrail.types.list_tags_request.ListTagsRequest,
) -> tuple[capo_cloudtrail.types.list_tags_response.ListTagsResponse, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            raise_error(response, handle_error)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_list_tags(
    options: AsyncOperationOptions,
    input_: capo_cloudtrail.types.list_tags_request.ListTagsRequest,
) -> tuple[capo_cloudtrail.types.list_tags_response.ListTagsResponse, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 300:
            await response.aread()
            raise_error(response, handle_error)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
