"""Generated from Smithy shape ``com.amazonaws.sqs#ListQueueTags``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_sqs._auth._signers
import capo_sqs._auth._sigv4
import capo_sqs._protocol.eventstream
import capo_sqs.errors.invalid_address
import capo_sqs.errors.invalid_security
import capo_sqs.errors.queue_does_not_exist
import capo_sqs.errors.request_throttled
import capo_sqs.errors.unsupported_operation
import capo_sqs.types.list_queue_tags_request
import capo_sqs.types.list_queue_tags_result
import capo_sqs.types.tag_map
from capo_sqs._protocol.errors import parse_error_metadata_json
from capo_sqs._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_sqs._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_sqs.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidAddress":
            raise capo_sqs.errors.invalid_address.InvalidAddress.from_aws_json_1_0(
                data, message
            )
        case "InvalidSecurity":
            raise capo_sqs.errors.invalid_security.InvalidSecurity.from_aws_json_1_0(
                data, message
            )
        case "QueueDoesNotExist":
            raise capo_sqs.errors.queue_does_not_exist.QueueDoesNotExist.from_aws_json_1_0(
                data, message
            )
        case "RequestThrottled":
            raise capo_sqs.errors.request_throttled.RequestThrottled.from_aws_json_1_0(
                data, message
            )
        case "UnsupportedOperation":
            raise capo_sqs.errors.unsupported_operation.UnsupportedOperation.from_aws_json_1_0(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_sqs.types.list_queue_tags_result.ListQueueTagsResult:
    out: capo_sqs.types.list_queue_tags_result.ListQueueTagsResult = (
        capo_sqs.types.list_queue_tags_result.deserialize_aws_json_1_0(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_sqs.types.list_queue_tags_result.ListQueueTagsResult:
    out: capo_sqs.types.list_queue_tags_result.ListQueueTagsResult = (
        capo_sqs.types.list_queue_tags_result.deserialize_aws_json_1_0(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_sqs._auth._signers.Signer | None:
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
            sigv4_config = capo_sqs._auth._sigv4.build_sigv4_auth_scheme(
                "sqs", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_sqs._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_sqs.types.list_queue_tags_request.ListQueueTagsRequest,
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
    headers["X-Amz-Target"] = "AmazonSQS.ListQueueTags"
    body: bytes | None = json.dumps(
        capo_sqs.types.list_queue_tags_request.serialize_aws_json_1_0(input_),
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
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def list_queue_tags(
    options: OperationOptions,
    input_: capo_sqs.types.list_queue_tags_request.ListQueueTagsRequest,
) -> tuple[capo_sqs.types.list_queue_tags_result.ListQueueTagsResult, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            raise_error(response, handle_error)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_list_queue_tags(
    options: AsyncOperationOptions,
    input_: capo_sqs.types.list_queue_tags_request.ListQueueTagsRequest,
) -> tuple[capo_sqs.types.list_queue_tags_result.ListQueueTagsResult, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 300:
            await response.aread()
            raise_error(response, handle_error)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
