"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListTagsForResource``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import capo_cloudfront._auth._signers
import capo_cloudfront._auth._sigv4
import capo_cloudfront._protocol.eventstream
import capo_cloudfront.errors.access_denied
import capo_cloudfront.errors.invalid_argument
import capo_cloudfront.errors.invalid_tagging
import capo_cloudfront.errors.no_such_resource
import capo_cloudfront.types.list_tags_for_resource_request
import capo_cloudfront.types.list_tags_for_resource_result
import capo_cloudfront.types.tags
from capo_cloudfront._protocol.errors import find_error_element, parse_error_metadata
from capo_cloudfront._protocol.xml import Element, fromstring
from capo_cloudfront._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_cloudfront._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_cloudfront.errors import UnknownServiceError

STATUS_CODE_TO_CODE = {403: "AccessDenied", 404: "NoSuchResource"}


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
        case "AccessDenied":
            raise capo_cloudfront.errors.access_denied.AccessDenied.from_xml(
                error_el, message
            )
        case "InvalidArgument":
            raise capo_cloudfront.errors.invalid_argument.InvalidArgument.from_xml(
                error_el, message
            )
        case "InvalidTagging":
            raise capo_cloudfront.errors.invalid_tagging.InvalidTagging.from_xml(
                error_el, message
            )
        case "NoSuchResource":
            raise capo_cloudfront.errors.no_such_resource.NoSuchResource.from_xml(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cloudfront.types.list_tags_for_resource_result.ListTagsForResourceResult:
    out: capo_cloudfront.types.list_tags_for_resource_result.ListTagsForResourceResult = {
        "tags": capo_cloudfront.types.tags.deserialize_xml(fromstring(response.read()))
    }  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_cloudfront.types.list_tags_for_resource_result.ListTagsForResourceResult:
    out: capo_cloudfront.types.list_tags_for_resource_result.ListTagsForResourceResult = {
        "tags": capo_cloudfront.types.tags.deserialize_xml(
            fromstring(await response.aread())
        )
    }  # type: ignore[typeddict-item]
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
    input_: capo_cloudfront.types.list_tags_for_resource_request.ListTagsForResourceRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2020-05-31/tagging"
    params: list[tuple[str, str]] = []
    if "resource" in input_:
        params.append(("Resource", input_["resource"]))
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


def list_tags_for_resource(
    options: OperationOptions,
    input_: capo_cloudfront.types.list_tags_for_resource_request.ListTagsForResourceRequest,
) -> tuple[
    capo_cloudfront.types.list_tags_for_resource_result.ListTagsForResourceResult,
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


async def async_list_tags_for_resource(
    options: AsyncOperationOptions,
    input_: capo_cloudfront.types.list_tags_for_resource_request.ListTagsForResourceRequest,
) -> tuple[
    capo_cloudfront.types.list_tags_for_resource_result.ListTagsForResourceResult,
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
