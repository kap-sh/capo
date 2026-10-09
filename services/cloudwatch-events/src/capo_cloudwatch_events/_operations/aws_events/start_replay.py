"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#StartReplay``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_cloudwatch_events._auth._signers
import capo_cloudwatch_events._auth._sigv4
import capo_cloudwatch_events._protocol.eventstream
import capo_cloudwatch_events.errors.internal_exception
import capo_cloudwatch_events.errors.invalid_event_pattern_exception
import capo_cloudwatch_events.errors.limit_exceeded_exception
import capo_cloudwatch_events.errors.resource_already_exists_exception
import capo_cloudwatch_events.errors.resource_not_found_exception
import capo_cloudwatch_events.types.replay_destination
import capo_cloudwatch_events.types.replay_state
import capo_cloudwatch_events.types.start_replay_request
import capo_cloudwatch_events.types.start_replay_response
import capo_cloudwatch_events.types.timestamp
from capo_cloudwatch_events._protocol.errors import parse_error_metadata_json
from capo_cloudwatch_events._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_cloudwatch_events._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_cloudwatch_events.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalException":
            raise capo_cloudwatch_events.errors.internal_exception.InternalException.from_aws_json_1_1(
                data, message
            )
        case "InvalidEventPatternException":
            raise capo_cloudwatch_events.errors.invalid_event_pattern_exception.InvalidEventPatternException.from_aws_json_1_1(
                data, message
            )
        case "LimitExceededException":
            raise capo_cloudwatch_events.errors.limit_exceeded_exception.LimitExceededException.from_aws_json_1_1(
                data, message
            )
        case "ResourceAlreadyExistsException":
            raise capo_cloudwatch_events.errors.resource_already_exists_exception.ResourceAlreadyExistsException.from_aws_json_1_1(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_cloudwatch_events.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cloudwatch_events.types.start_replay_response.StartReplayResponse:
    out: capo_cloudwatch_events.types.start_replay_response.StartReplayResponse = (
        capo_cloudwatch_events.types.start_replay_response.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_cloudwatch_events.types.start_replay_response.StartReplayResponse:
    out: capo_cloudwatch_events.types.start_replay_response.StartReplayResponse = (
        capo_cloudwatch_events.types.start_replay_response.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_cloudwatch_events._auth._signers.Signer | None:
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
            sigv4_config = capo_cloudwatch_events._auth._sigv4.build_sigv4_auth_scheme(
                "events", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_cloudwatch_events._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_cloudwatch_events.types.start_replay_request.StartReplayRequest,
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
    headers["X-Amz-Target"] = "AWSEvents.StartReplay"
    body: bytes | None = json.dumps(
        capo_cloudwatch_events.types.start_replay_request.serialize_aws_json_1_1(
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


def start_replay(
    options: OperationOptions,
    input_: capo_cloudwatch_events.types.start_replay_request.StartReplayRequest,
) -> tuple[
    capo_cloudwatch_events.types.start_replay_response.StartReplayResponse,
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


async def async_start_replay(
    options: AsyncOperationOptions,
    input_: capo_cloudwatch_events.types.start_replay_request.StartReplayRequest,
) -> tuple[
    capo_cloudwatch_events.types.start_replay_response.StartReplayResponse,
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
