"""Generated from Smithy shape ``com.amazonaws.sts#AssumeRoleWithSAML``."""

from __future__ import annotations

from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import capo_sts._auth._signers
import capo_sts._auth._sigv4
import capo_sts._protocol.eventstream
import capo_sts.errors.expired_token_exception
import capo_sts.errors.idp_rejected_claim_exception
import capo_sts.errors.invalid_identity_token_exception
import capo_sts.errors.malformed_policy_document_exception
import capo_sts.errors.packed_policy_too_large_exception
import capo_sts.errors.region_disabled_exception
import capo_sts.types.assume_role_with_saml_request
import capo_sts.types.assume_role_with_saml_response
import capo_sts.types.assumed_role_user
import capo_sts.types.credentials
import capo_sts.types.policy_descriptor_list_type
from capo_sts._protocol.errors import find_error_element, parse_error_metadata
from capo_sts._protocol.xml import fromstring
from capo_sts._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_sts._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_sts.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    error_el = find_error_element(root)
    match code:
        case "ExpiredTokenException":
            raise capo_sts.errors.expired_token_exception.ExpiredTokenException.from_query(
                error_el, message, response=response
            )
        case "IDPRejectedClaim":
            raise capo_sts.errors.idp_rejected_claim_exception.IDPRejectedClaimException.from_query(
                error_el, message, response=response
            )
        case "InvalidIdentityToken":
            raise capo_sts.errors.invalid_identity_token_exception.InvalidIdentityTokenException.from_query(
                error_el, message, response=response
            )
        case "MalformedPolicyDocument":
            raise capo_sts.errors.malformed_policy_document_exception.MalformedPolicyDocumentException.from_query(
                error_el, message, response=response
            )
        case "PackedPolicyTooLarge":
            raise capo_sts.errors.packed_policy_too_large_exception.PackedPolicyTooLargeException.from_query(
                error_el, message, response=response
            )
        case "RegionDisabledException":
            raise capo_sts.errors.region_disabled_exception.RegionDisabledException.from_query(
                error_el, message, response=response
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_sts.types.assume_role_with_saml_response.AssumeRoleWithSAMLResponse:
    root = fromstring(response.read())
    result = root.find("AssumeRoleWithSAMLResult")
    out: capo_sts.types.assume_role_with_saml_response.AssumeRoleWithSAMLResponse = (
        capo_sts.types.assume_role_with_saml_response.deserialize_query(
            result if result is not None else root
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_sts.types.assume_role_with_saml_response.AssumeRoleWithSAMLResponse:
    root = fromstring(await response.aread())
    result = root.find("AssumeRoleWithSAMLResult")
    out: capo_sts.types.assume_role_with_saml_response.AssumeRoleWithSAMLResponse = (
        capo_sts.types.assume_role_with_saml_response.deserialize_query(
            result if result is not None else root
        )
    )
    return out


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_sts.types.assume_role_with_saml_request.AssumeRoleWithSAMLRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            UseGlobalEndpoint=options.use_global_endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    pairs: list[tuple[str, str]] = []
    pairs.append(("Action", "AssumeRoleWithSAML"))
    pairs.append(("Version", "2011-06-15"))
    capo_sts.types.assume_role_with_saml_request.serialize_query(input_, pairs, "")
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(normalized_url, "POST", headers=headers, body=body)


def assume_role_with_saml(
    options: OperationOptions,
    input_: capo_sts.types.assume_role_with_saml_request.AssumeRoleWithSAMLRequest,
) -> tuple[
    capo_sts.types.assume_role_with_saml_response.AssumeRoleWithSAMLResponse,
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


async def async_assume_role_with_saml(
    options: AsyncOperationOptions,
    input_: capo_sts.types.assume_role_with_saml_request.AssumeRoleWithSAMLRequest,
) -> tuple[
    capo_sts.types.assume_role_with_saml_response.AssumeRoleWithSAMLResponse,
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
