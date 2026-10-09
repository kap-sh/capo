"""Generated from Smithy shape ``com.amazonaws.support#AddAttachmentsToSet``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_support._auth._signers
import capo_support._auth._sigv4
import capo_support._protocol.eventstream
import capo_support.errors.attachment_limit_exceeded
import capo_support.errors.attachment_set_expired
import capo_support.errors.attachment_set_id_not_found
import capo_support.errors.attachment_set_size_limit_exceeded
import capo_support.errors.dry_run_operation_exception
import capo_support.errors.internal_server_error
import capo_support.types.add_attachments_to_set_request
import capo_support.types.add_attachments_to_set_response
import capo_support.types.attachments
from capo_support._protocol.errors import parse_error_metadata_json
from capo_support._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_support._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_support.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AttachmentLimitExceeded":
            raise capo_support.errors.attachment_limit_exceeded.AttachmentLimitExceeded.from_aws_json_1_1(
                data, message
            )
        case "AttachmentSetExpired":
            raise capo_support.errors.attachment_set_expired.AttachmentSetExpired.from_aws_json_1_1(
                data, message
            )
        case "AttachmentSetIdNotFound":
            raise capo_support.errors.attachment_set_id_not_found.AttachmentSetIdNotFound.from_aws_json_1_1(
                data, message
            )
        case "AttachmentSetSizeLimitExceeded":
            raise capo_support.errors.attachment_set_size_limit_exceeded.AttachmentSetSizeLimitExceeded.from_aws_json_1_1(
                data, message
            )
        case "DryRunOperationException":
            raise capo_support.errors.dry_run_operation_exception.DryRunOperationException.from_aws_json_1_1(
                data, message
            )
        case "InternalServerError":
            raise capo_support.errors.internal_server_error.InternalServerError.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_support.types.add_attachments_to_set_response.AddAttachmentsToSetResponse:
    out: capo_support.types.add_attachments_to_set_response.AddAttachmentsToSetResponse = capo_support.types.add_attachments_to_set_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_support.types.add_attachments_to_set_response.AddAttachmentsToSetResponse:
    out: capo_support.types.add_attachments_to_set_response.AddAttachmentsToSetResponse = capo_support.types.add_attachments_to_set_response.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_support._auth._signers.Signer | None:
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
            sigv4_config = capo_support._auth._sigv4.build_sigv4_auth_scheme(
                "support", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_support._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_support.types.add_attachments_to_set_request.AddAttachmentsToSetRequest,
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
    headers["X-Amz-Target"] = "AWSSupport_20130415.AddAttachmentsToSet"
    body: bytes | None = json.dumps(
        capo_support.types.add_attachments_to_set_request.serialize_aws_json_1_1(
            input_
        ),
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


def add_attachments_to_set(
    options: OperationOptions,
    input_: capo_support.types.add_attachments_to_set_request.AddAttachmentsToSetRequest,
) -> tuple[
    capo_support.types.add_attachments_to_set_response.AddAttachmentsToSetResponse,
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


async def async_add_attachments_to_set(
    options: AsyncOperationOptions,
    input_: capo_support.types.add_attachments_to_set_request.AddAttachmentsToSetRequest,
) -> tuple[
    capo_support.types.add_attachments_to_set_response.AddAttachmentsToSetResponse,
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
