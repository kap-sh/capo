"""Generated from Smithy shape ``com.amazonaws.applicationsignals#CreateServiceLevelObjective``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_application_signals._auth._signers
import capo_application_signals._auth._sigv4
import capo_application_signals._protocol.eventstream
import capo_application_signals.errors.access_denied_exception
import capo_application_signals.errors.conflict_exception
import capo_application_signals.errors.service_quota_exceeded_exception
import capo_application_signals.errors.throttling_exception
import capo_application_signals.errors.validation_exception
import capo_application_signals.types.burn_rate_configurations
import capo_application_signals.types.create_service_level_objective_input
import capo_application_signals.types.create_service_level_objective_output
import capo_application_signals.types.goal
import capo_application_signals.types.request_based_service_level_indicator_config
import capo_application_signals.types.service_level_indicator_config
import capo_application_signals.types.service_level_objective
import capo_application_signals.types.tag_list
from capo_application_signals._protocol.errors import parse_error_metadata_json
from capo_application_signals._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_application_signals._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_application_signals.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_application_signals.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "ConflictException":
            raise capo_application_signals.errors.conflict_exception.ConflictException.from_json(
                data, message
            )
        case "ServiceQuotaExceededException":
            raise capo_application_signals.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_application_signals.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_application_signals.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_application_signals.types.create_service_level_objective_output.CreateServiceLevelObjectiveOutput:
    out: capo_application_signals.types.create_service_level_objective_output.CreateServiceLevelObjectiveOutput = capo_application_signals.types.create_service_level_objective_output.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_application_signals.types.create_service_level_objective_output.CreateServiceLevelObjectiveOutput:
    out: capo_application_signals.types.create_service_level_objective_output.CreateServiceLevelObjectiveOutput = capo_application_signals.types.create_service_level_objective_output.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_application_signals._auth._signers.Signer | None:
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
                capo_application_signals._auth._sigv4.build_sigv4_auth_scheme(
                    "application-signals", options.region, endpoint_scheme
                )
            )
            if sigv4_config is not None:
                return capo_application_signals._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_application_signals.types.create_service_level_objective_input.CreateServiceLevelObjectiveInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/slo"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_application_signals.types.create_service_level_objective_input.serialize_json(
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


def create_service_level_objective(
    options: OperationOptions,
    input_: capo_application_signals.types.create_service_level_objective_input.CreateServiceLevelObjectiveInput,
) -> tuple[
    capo_application_signals.types.create_service_level_objective_output.CreateServiceLevelObjectiveOutput,
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


async def async_create_service_level_objective(
    options: AsyncOperationOptions,
    input_: capo_application_signals.types.create_service_level_objective_input.CreateServiceLevelObjectiveInput,
) -> tuple[
    capo_application_signals.types.create_service_level_objective_output.CreateServiceLevelObjectiveOutput,
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
