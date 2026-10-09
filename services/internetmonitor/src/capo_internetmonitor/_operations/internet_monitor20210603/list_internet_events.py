"""Generated from Smithy shape ``com.amazonaws.internetmonitor#ListInternetEvents``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_internetmonitor._auth._signers
import capo_internetmonitor._auth._sigv4
import capo_internetmonitor._protocol.eventstream
import capo_internetmonitor.errors.access_denied_exception
import capo_internetmonitor.errors.internal_server_exception
import capo_internetmonitor.errors.throttling_exception
import capo_internetmonitor.errors.validation_exception
import capo_internetmonitor.types.internet_events_list
import capo_internetmonitor.types.list_internet_events_input
import capo_internetmonitor.types.list_internet_events_output
from capo_internetmonitor._protocol.errors import parse_error_metadata_json
from capo_internetmonitor._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_internetmonitor._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_internetmonitor.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_internetmonitor.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "InternalServerException":
            raise capo_internetmonitor.errors.internal_server_exception.InternalServerException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_internetmonitor.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_internetmonitor.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_internetmonitor.types.list_internet_events_output.ListInternetEventsOutput:
    out: capo_internetmonitor.types.list_internet_events_output.ListInternetEventsOutput = capo_internetmonitor.types.list_internet_events_output.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_internetmonitor.types.list_internet_events_output.ListInternetEventsOutput:
    out: capo_internetmonitor.types.list_internet_events_output.ListInternetEventsOutput = capo_internetmonitor.types.list_internet_events_output.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_internetmonitor._auth._signers.Signer | None:
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
            sigv4_config = capo_internetmonitor._auth._sigv4.build_sigv4_auth_scheme(
                "internetmonitor", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_internetmonitor._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_internetmonitor.types.list_internet_events_input.ListInternetEventsInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_internetmonitor._protocol.serialize

    url = endpoint.url.rstrip("/") + "/v20210603/InternetEvents"
    params: list[tuple[str, str]] = []
    if "next_token" in input_:
        params.append(("NextToken", input_["next_token"]))
    if "max_results" in input_:
        params.append(("InternetEventMaxResults", str(input_["max_results"])))
    if "start_time" in input_:
        params.append(
            (
                "StartTime",
                capo_internetmonitor._protocol.serialize.fmt_date_time(
                    input_["start_time"]
                ),
            )
        )
    if "end_time" in input_:
        params.append(
            (
                "EndTime",
                capo_internetmonitor._protocol.serialize.fmt_date_time(
                    input_["end_time"]
                ),
            )
        )
    if "event_status" in input_:
        params.append(("EventStatus", input_["event_status"]))
    if "event_type" in input_:
        params.append(("EventType", input_["event_type"]))
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


def list_internet_events(
    options: OperationOptions,
    input_: capo_internetmonitor.types.list_internet_events_input.ListInternetEventsInput,
) -> tuple[
    capo_internetmonitor.types.list_internet_events_output.ListInternetEventsOutput,
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


async def async_list_internet_events(
    options: AsyncOperationOptions,
    input_: capo_internetmonitor.types.list_internet_events_input.ListInternetEventsInput,
) -> tuple[
    capo_internetmonitor.types.list_internet_events_output.ListInternetEventsOutput,
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
