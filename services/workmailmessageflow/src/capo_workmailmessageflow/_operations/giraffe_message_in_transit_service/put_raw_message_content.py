"""Generated from Smithy shape ``com.amazonaws.workmailmessageflow#PutRawMessageContent``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_workmailmessageflow._auth._signers
import capo_workmailmessageflow._auth._sigv4
import capo_workmailmessageflow._protocol.eventstream
import capo_workmailmessageflow.errors.invalid_content_location
import capo_workmailmessageflow.errors.message_frozen
import capo_workmailmessageflow.errors.message_rejected
import capo_workmailmessageflow.errors.resource_not_found_exception
import capo_workmailmessageflow.types.put_raw_message_content_request
import capo_workmailmessageflow.types.put_raw_message_content_response
import capo_workmailmessageflow.types.raw_message_content
from capo_workmailmessageflow._protocol.errors import parse_error_metadata_json
from capo_workmailmessageflow._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_workmailmessageflow._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_workmailmessageflow.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidContentLocation":
            raise capo_workmailmessageflow.errors.invalid_content_location.InvalidContentLocation.from_json(
                data, message
            )
        case "MessageFrozen":
            raise capo_workmailmessageflow.errors.message_frozen.MessageFrozen.from_json(
                data, message
            )
        case "MessageRejected":
            raise capo_workmailmessageflow.errors.message_rejected.MessageRejected.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_workmailmessageflow.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_workmailmessageflow.types.put_raw_message_content_response.PutRawMessageContentResponse:
    out: capo_workmailmessageflow.types.put_raw_message_content_response.PutRawMessageContentResponse = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_workmailmessageflow.types.put_raw_message_content_response.PutRawMessageContentResponse:
    out: capo_workmailmessageflow.types.put_raw_message_content_response.PutRawMessageContentResponse = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_workmailmessageflow._auth._signers.Signer | None:
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
            sigv4_config = (
                capo_workmailmessageflow._auth._sigv4.build_sigv4_auth_scheme(
                    "workmailmessageflow", options.region, endpoint_scheme
                )
            )
            if sigv4_config is not None:
                return capo_workmailmessageflow._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_workmailmessageflow.types.put_raw_message_content_request.PutRawMessageContentRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/messages/{messageId}"
    url = url.replace("{messageId}", quote(input_["message_id"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_workmailmessageflow.types.put_raw_message_content_request.serialize_json(
            input_
        ),
        allow_nan=False,
    ).encode()
    headers["content-type"] = "application/json"
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


def put_raw_message_content(
    options: OperationOptions,
    input_: capo_workmailmessageflow.types.put_raw_message_content_request.PutRawMessageContentRequest,
) -> tuple[
    capo_workmailmessageflow.types.put_raw_message_content_response.PutRawMessageContentResponse,
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


async def async_put_raw_message_content(
    options: AsyncOperationOptions,
    input_: capo_workmailmessageflow.types.put_raw_message_content_request.PutRawMessageContentRequest,
) -> tuple[
    capo_workmailmessageflow.types.put_raw_message_content_response.PutRawMessageContentResponse,
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
