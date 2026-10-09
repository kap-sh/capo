"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateOriginRequestPolicy``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import capo_cloudfront._auth._signers
import capo_cloudfront._auth._sigv4
import capo_cloudfront._protocol.eventstream
import capo_cloudfront.errors.access_denied
import capo_cloudfront.errors.inconsistent_quantities
import capo_cloudfront.errors.invalid_argument
import capo_cloudfront.errors.origin_request_policy_already_exists
import capo_cloudfront.errors.too_many_cookies_in_origin_request_policy
import capo_cloudfront.errors.too_many_headers_in_origin_request_policy
import capo_cloudfront.errors.too_many_origin_request_policies
import capo_cloudfront.errors.too_many_query_strings_in_origin_request_policy
import capo_cloudfront.types.create_origin_request_policy_request
import capo_cloudfront.types.create_origin_request_policy_result
import capo_cloudfront.types.origin_request_policy
import capo_cloudfront.types.origin_request_policy_config
from capo_cloudfront._protocol.errors import find_error_element, parse_error_metadata
from capo_cloudfront._protocol.xml import Element, fromstring, tostring
from capo_cloudfront._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_cloudfront._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_cloudfront.errors import UnknownServiceError

STATUS_CODE_TO_CODE = {403: "AccessDenied", 409: "OriginRequestPolicyAlreadyExists"}


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
        case "InconsistentQuantities":
            raise capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities.from_xml(
                error_el, message
            )
        case "InvalidArgument":
            raise capo_cloudfront.errors.invalid_argument.InvalidArgument.from_xml(
                error_el, message
            )
        case "OriginRequestPolicyAlreadyExists":
            raise capo_cloudfront.errors.origin_request_policy_already_exists.OriginRequestPolicyAlreadyExists.from_xml(
                error_el, message
            )
        case "TooManyCookiesInOriginRequestPolicy":
            raise capo_cloudfront.errors.too_many_cookies_in_origin_request_policy.TooManyCookiesInOriginRequestPolicy.from_xml(
                error_el, message
            )
        case "TooManyHeadersInOriginRequestPolicy":
            raise capo_cloudfront.errors.too_many_headers_in_origin_request_policy.TooManyHeadersInOriginRequestPolicy.from_xml(
                error_el, message
            )
        case "TooManyOriginRequestPolicies":
            raise capo_cloudfront.errors.too_many_origin_request_policies.TooManyOriginRequestPolicies.from_xml(
                error_el, message
            )
        case "TooManyQueryStringsInOriginRequestPolicy":
            raise capo_cloudfront.errors.too_many_query_strings_in_origin_request_policy.TooManyQueryStringsInOriginRequestPolicy.from_xml(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cloudfront.types.create_origin_request_policy_result.CreateOriginRequestPolicyResult:
    out: capo_cloudfront.types.create_origin_request_policy_result.CreateOriginRequestPolicyResult = {
        "origin_request_policy": capo_cloudfront.types.origin_request_policy.deserialize_xml(
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
) -> capo_cloudfront.types.create_origin_request_policy_result.CreateOriginRequestPolicyResult:
    out: capo_cloudfront.types.create_origin_request_policy_result.CreateOriginRequestPolicyResult = {
        "origin_request_policy": capo_cloudfront.types.origin_request_policy.deserialize_xml(
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
    input_: capo_cloudfront.types.create_origin_request_policy_request.CreateOriginRequestPolicyRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2020-05-31/origin-request-policy"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    payload_root = Element("_")
    capo_cloudfront.types.origin_request_policy_config.serialize_xml(
        input_["origin_request_policy_config"],
        payload_root,
        "OriginRequestPolicyConfig",
    )
    body: bytes | None = tostring(payload_root[0])
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


def create_origin_request_policy(
    options: OperationOptions,
    input_: capo_cloudfront.types.create_origin_request_policy_request.CreateOriginRequestPolicyRequest,
) -> tuple[
    capo_cloudfront.types.create_origin_request_policy_result.CreateOriginRequestPolicyResult,
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


async def async_create_origin_request_policy(
    options: AsyncOperationOptions,
    input_: capo_cloudfront.types.create_origin_request_policy_request.CreateOriginRequestPolicyRequest,
) -> tuple[
    capo_cloudfront.types.create_origin_request_policy_result.CreateOriginRequestPolicyResult,
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
