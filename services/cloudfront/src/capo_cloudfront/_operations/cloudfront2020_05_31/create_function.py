"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateFunction``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import capo_cloudfront._auth._signers
import capo_cloudfront._auth._sigv4
import capo_cloudfront._protocol.eventstream
import capo_cloudfront.errors.function_already_exists
import capo_cloudfront.errors.function_size_limit_exceeded
import capo_cloudfront.errors.invalid_argument
import capo_cloudfront.errors.too_many_functions
import capo_cloudfront.errors.unsupported_operation
import capo_cloudfront.types.create_function_request
import capo_cloudfront.types.create_function_result
import capo_cloudfront.types.function_blob
import capo_cloudfront.types.function_config
import capo_cloudfront.types.function_summary
import capo_cloudfront.types.tags
from capo_cloudfront._protocol.errors import find_error_element, parse_error_metadata
from capo_cloudfront._protocol.xml import Element, SubElement, fromstring, tostring
from capo_cloudfront._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_cloudfront._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_cloudfront.errors import UnknownServiceError

STATUS_CODE_TO_CODE = {409: "FunctionAlreadyExists", 413: "FunctionSizeLimitExceeded"}


def handle_error(response: zapros.Response) -> Never:
    body = response.read()
    if body:
        root = fromstring(body)
        code, message = parse_error_metadata(root)
        error_el = find_error_element(root)
    else:
        code = STATUS_CODE_TO_CODE.get(response.status)
        message = None
        error_el = Element("Error")
    match code:
        case "FunctionAlreadyExists":
            raise capo_cloudfront.errors.function_already_exists.FunctionAlreadyExists.from_xml(
                error_el, message
            )
        case "FunctionSizeLimitExceeded":
            raise capo_cloudfront.errors.function_size_limit_exceeded.FunctionSizeLimitExceeded.from_xml(
                error_el, message
            )
        case "InvalidArgument":
            raise capo_cloudfront.errors.invalid_argument.InvalidArgument.from_xml(
                error_el, message
            )
        case "TooManyFunctions":
            raise capo_cloudfront.errors.too_many_functions.TooManyFunctions.from_xml(
                error_el, message
            )
        case "UnsupportedOperation":
            raise capo_cloudfront.errors.unsupported_operation.UnsupportedOperation.from_xml(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cloudfront.types.create_function_result.CreateFunctionResult:
    out: capo_cloudfront.types.create_function_result.CreateFunctionResult = {
        "function_summary": capo_cloudfront.types.function_summary.deserialize_xml(
            fromstring(response.read())
        )
    }  # type: ignore[typeddict-item]
    if "Location" in response.headers:
        out["location"] = response.headers["Location"]
    if "ETag" in response.headers:
        out["e_tag"] = response.headers["ETag"]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_cloudfront.types.create_function_result.CreateFunctionResult:
    out: capo_cloudfront.types.create_function_result.CreateFunctionResult = {
        "function_summary": capo_cloudfront.types.function_summary.deserialize_xml(
            fromstring(await response.aread())
        )
    }  # type: ignore[typeddict-item]
    if "Location" in response.headers:
        out["location"] = response.headers["Location"]
    if "ETag" in response.headers:
        out["e_tag"] = response.headers["ETag"]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_cloudfront._auth._signers.Signer | None:
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
            sigv4_config = capo_cloudfront._auth._sigv4.build_sigv4_auth_scheme(
                "cloudfront", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_cloudfront._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_cloudfront.types.create_function_request.CreateFunctionRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2020-05-31/function"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import capo_cloudfront.types.function_blob
    import capo_cloudfront.types.function_config
    import capo_cloudfront.types.tags

    root = Element("CreateFunctionRequest")
    if "name" in input_:
        SubElement(root, "Name").text = input_["name"]
    if "function_config" in input_:
        capo_cloudfront.types.function_config.serialize_xml(
            input_["function_config"], root, "FunctionConfig"
        )
    if "function_code" in input_:
        capo_cloudfront.types.function_blob.serialize_xml(
            input_["function_code"], root, "FunctionCode"
        )
    if "tags" in input_:
        capo_cloudfront.types.tags.serialize_xml(input_["tags"], root, "Tags")
    body: bytes | None = tostring(root)
    headers["content-type"] = "application/xml"
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


def create_function(
    options: OperationOptions,
    input_: capo_cloudfront.types.create_function_request.CreateFunctionRequest,
) -> tuple[
    capo_cloudfront.types.create_function_result.CreateFunctionResult, zapros.Response
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


async def async_create_function(
    options: AsyncOperationOptions,
    input_: capo_cloudfront.types.create_function_request.CreateFunctionRequest,
) -> tuple[
    capo_cloudfront.types.create_function_result.CreateFunctionResult, zapros.Response
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
