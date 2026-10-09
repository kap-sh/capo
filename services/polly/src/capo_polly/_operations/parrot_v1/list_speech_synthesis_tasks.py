"""Generated from Smithy shape ``com.amazonaws.polly#ListSpeechSynthesisTasks``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_polly._auth._signers
import capo_polly._auth._sigv4
import capo_polly._protocol.eventstream
import capo_polly.errors.invalid_next_token_exception
import capo_polly.errors.service_failure_exception
import capo_polly.types.list_speech_synthesis_tasks_input
import capo_polly.types.list_speech_synthesis_tasks_output
import capo_polly.types.synthesis_tasks
import capo_polly.types.task_status
from capo_polly._protocol.errors import parse_error_metadata_json
from capo_polly._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_polly._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_polly.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidNextTokenException":
            raise capo_polly.errors.invalid_next_token_exception.InvalidNextTokenException.from_json(
                data, message
            )
        case "ServiceFailureException":
            raise capo_polly.errors.service_failure_exception.ServiceFailureException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_polly.types.list_speech_synthesis_tasks_output.ListSpeechSynthesisTasksOutput:
    out: capo_polly.types.list_speech_synthesis_tasks_output.ListSpeechSynthesisTasksOutput = capo_polly.types.list_speech_synthesis_tasks_output.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_polly.types.list_speech_synthesis_tasks_output.ListSpeechSynthesisTasksOutput:
    out: capo_polly.types.list_speech_synthesis_tasks_output.ListSpeechSynthesisTasksOutput = capo_polly.types.list_speech_synthesis_tasks_output.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_polly._auth._signers.Signer | None:
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
            sigv4_config = capo_polly._auth._sigv4.build_sigv4_auth_scheme(
                "polly", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_polly._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_polly.types.list_speech_synthesis_tasks_input.ListSpeechSynthesisTasksInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_polly.types.task_status

    url = endpoint.url.rstrip("/") + "/v1/synthesisTasks"
    params: list[tuple[str, str]] = []
    if "max_results" in input_:
        params.append(("MaxResults", str(input_["max_results"])))
    if "next_token" in input_:
        params.append(("NextToken", input_["next_token"]))
    if "status" in input_:
        params.append(
            ("Status", capo_polly.types.task_status.serialize_json(input_["status"]))
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


def list_speech_synthesis_tasks(
    options: OperationOptions,
    input_: capo_polly.types.list_speech_synthesis_tasks_input.ListSpeechSynthesisTasksInput,
) -> tuple[
    capo_polly.types.list_speech_synthesis_tasks_output.ListSpeechSynthesisTasksOutput,
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


async def async_list_speech_synthesis_tasks(
    options: AsyncOperationOptions,
    input_: capo_polly.types.list_speech_synthesis_tasks_input.ListSpeechSynthesisTasksInput,
) -> tuple[
    capo_polly.types.list_speech_synthesis_tasks_output.ListSpeechSynthesisTasksOutput,
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
