"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchDeleteAutomationRules``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_securityhub._auth._signers
import capo_securityhub._auth._sigv4
import capo_securityhub._protocol.eventstream
import capo_securityhub.errors.internal_exception
import capo_securityhub.errors.invalid_access_exception
import capo_securityhub.errors.invalid_input_exception
import capo_securityhub.errors.limit_exceeded_exception
import capo_securityhub.errors.resource_not_found_exception
import capo_securityhub.types.automation_rules_arns_list
import capo_securityhub.types.batch_delete_automation_rules_request
import capo_securityhub.types.batch_delete_automation_rules_response
import capo_securityhub.types.unprocessed_automation_rules_list
from capo_securityhub._protocol.errors import parse_error_metadata_json
from capo_securityhub._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_securityhub._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_securityhub.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalException":
            raise capo_securityhub.errors.internal_exception.InternalException.from_json(
                data, message
            )
        case "InvalidAccessException":
            raise capo_securityhub.errors.invalid_access_exception.InvalidAccessException.from_json(
                data, message
            )
        case "InvalidInputException":
            raise capo_securityhub.errors.invalid_input_exception.InvalidInputException.from_json(
                data, message
            )
        case "LimitExceededException":
            raise capo_securityhub.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_securityhub.types.batch_delete_automation_rules_response.BatchDeleteAutomationRulesResponse:
    out: capo_securityhub.types.batch_delete_automation_rules_response.BatchDeleteAutomationRulesResponse = capo_securityhub.types.batch_delete_automation_rules_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_securityhub.types.batch_delete_automation_rules_response.BatchDeleteAutomationRulesResponse:
    out: capo_securityhub.types.batch_delete_automation_rules_response.BatchDeleteAutomationRulesResponse = capo_securityhub.types.batch_delete_automation_rules_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_securityhub._auth._signers.Signer | None:
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
            sigv4_config = capo_securityhub._auth._sigv4.build_sigv4_auth_scheme(
                "securityhub", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_securityhub._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_securityhub.types.batch_delete_automation_rules_request.BatchDeleteAutomationRulesRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/automationrules/delete"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_securityhub.types.batch_delete_automation_rules_request.serialize_json(
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


def batch_delete_automation_rules(
    options: OperationOptions,
    input_: capo_securityhub.types.batch_delete_automation_rules_request.BatchDeleteAutomationRulesRequest,
) -> tuple[
    capo_securityhub.types.batch_delete_automation_rules_response.BatchDeleteAutomationRulesResponse,
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


async def async_batch_delete_automation_rules(
    options: AsyncOperationOptions,
    input_: capo_securityhub.types.batch_delete_automation_rules_request.BatchDeleteAutomationRulesRequest,
) -> tuple[
    capo_securityhub.types.batch_delete_automation_rules_response.BatchDeleteAutomationRulesResponse,
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
