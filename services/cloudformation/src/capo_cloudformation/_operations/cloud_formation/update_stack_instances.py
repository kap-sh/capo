"""Generated from Smithy shape ``com.amazonaws.cloudformation#UpdateStackInstances``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import capo_cloudformation._auth._signers
import capo_cloudformation._auth._sigv4
import capo_cloudformation._protocol.eventstream
import capo_cloudformation.errors.invalid_operation_exception
import capo_cloudformation.errors.operation_id_already_exists_exception
import capo_cloudformation.errors.operation_in_progress_exception
import capo_cloudformation.errors.stack_instance_not_found_exception
import capo_cloudformation.errors.stack_set_not_found_exception
import capo_cloudformation.errors.stale_request_exception
import capo_cloudformation.types.account_list
import capo_cloudformation.types.call_as
import capo_cloudformation.types.deployment_targets
import capo_cloudformation.types.parameters
import capo_cloudformation.types.region_list
import capo_cloudformation.types.stack_set_operation_preferences
import capo_cloudformation.types.update_stack_instances_input
import capo_cloudformation.types.update_stack_instances_output
from capo_cloudformation._protocol.errors import (
    find_error_element,
    parse_error_metadata,
)
from capo_cloudformation._protocol.xml import fromstring
from capo_cloudformation._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_cloudformation._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_cloudformation.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    error_el = find_error_element(root)
    match code:
        case "InvalidOperationException":
            raise capo_cloudformation.errors.invalid_operation_exception.InvalidOperationException.from_query(
                error_el, message
            )
        case "OperationIdAlreadyExistsException":
            raise capo_cloudformation.errors.operation_id_already_exists_exception.OperationIdAlreadyExistsException.from_query(
                error_el, message
            )
        case "OperationInProgressException":
            raise capo_cloudformation.errors.operation_in_progress_exception.OperationInProgressException.from_query(
                error_el, message
            )
        case "StackInstanceNotFoundException":
            raise capo_cloudformation.errors.stack_instance_not_found_exception.StackInstanceNotFoundException.from_query(
                error_el, message
            )
        case "StackSetNotFoundException":
            raise capo_cloudformation.errors.stack_set_not_found_exception.StackSetNotFoundException.from_query(
                error_el, message
            )
        case "StaleRequestException":
            raise capo_cloudformation.errors.stale_request_exception.StaleRequestException.from_query(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cloudformation.types.update_stack_instances_output.UpdateStackInstancesOutput:
    root = fromstring(response.read())
    result = root.find("UpdateStackInstancesResult")
    out: capo_cloudformation.types.update_stack_instances_output.UpdateStackInstancesOutput = capo_cloudformation.types.update_stack_instances_output.deserialize_query(
        result if result is not None else root
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_cloudformation.types.update_stack_instances_output.UpdateStackInstancesOutput:
    root = fromstring(await response.aread())
    result = root.find("UpdateStackInstancesResult")
    out: capo_cloudformation.types.update_stack_instances_output.UpdateStackInstancesOutput = capo_cloudformation.types.update_stack_instances_output.deserialize_query(
        result if result is not None else root
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_cloudformation._auth._signers.Signer | None:
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
            sigv4_config = capo_cloudformation._auth._sigv4.build_sigv4_auth_scheme(
                "cloudformation", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_cloudformation._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_cloudformation.types.update_stack_instances_input.UpdateStackInstancesInput,
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
    pairs: list[tuple[str, str]] = []
    pairs.append(("Action", "UpdateStackInstances"))
    pairs.append(("Version", "2010-05-15"))
    capo_cloudformation.types.update_stack_instances_input.serialize_query(
        input_, pairs, ""
    )
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
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


def update_stack_instances(
    options: OperationOptions,
    input_: capo_cloudformation.types.update_stack_instances_input.UpdateStackInstancesInput,
) -> tuple[
    capo_cloudformation.types.update_stack_instances_output.UpdateStackInstancesOutput,
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


async def async_update_stack_instances(
    options: AsyncOperationOptions,
    input_: capo_cloudformation.types.update_stack_instances_input.UpdateStackInstancesInput,
) -> tuple[
    capo_cloudformation.types.update_stack_instances_output.UpdateStackInstancesOutput,
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
