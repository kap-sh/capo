"""Generated from Smithy shape ``com.amazonaws.s3control#PutJobTagging``."""

from __future__ import annotations

from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_s3_control._auth._signers
import capo_s3_control._auth._sigv4
import capo_s3_control._protocol.eventstream
import capo_s3_control.errors.internal_service_exception
import capo_s3_control.errors.not_found_exception
import capo_s3_control.errors.too_many_requests_exception
import capo_s3_control.errors.too_many_tags_exception
import capo_s3_control.types.put_job_tagging_request
import capo_s3_control.types.put_job_tagging_result
import capo_s3_control.types.s3_tag_set
from capo_s3_control._protocol.errors import find_error_element, parse_error_metadata
from capo_s3_control._protocol.xml import Element, fromstring, tostring
from capo_s3_control._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_s3_control._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_s3_control.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    body = response.read()
    if not body:
        raise UnknownServiceError(code=None, message=None, response=response)
    root = fromstring(body)
    code, message = parse_error_metadata(root)
    error_el = find_error_element(root)
    match code:
        case "InternalServiceException":
            raise capo_s3_control.errors.internal_service_exception.InternalServiceException.from_xml(
                error_el, message
            )
        case "NotFoundException":
            raise capo_s3_control.errors.not_found_exception.NotFoundException.from_xml(
                error_el, message
            )
        case "TooManyRequestsException":
            raise capo_s3_control.errors.too_many_requests_exception.TooManyRequestsException.from_xml(
                error_el, message
            )
        case "TooManyTagsException":
            raise capo_s3_control.errors.too_many_tags_exception.TooManyTagsException.from_xml(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_s3_control.types.put_job_tagging_result.PutJobTaggingResult:
    out: capo_s3_control.types.put_job_tagging_result.PutJobTaggingResult = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_s3_control.types.put_job_tagging_result.PutJobTaggingResult:
    out: capo_s3_control.types.put_job_tagging_result.PutJobTaggingResult = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_s3_control._auth._signers.Signer | None:
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
            sigv4_config = capo_s3_control._auth._sigv4.build_sigv4_auth_scheme(
                "s3", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_s3_control._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_s3_control.types.put_job_tagging_request.PutJobTaggingRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseFIPS=options.use_fips,
            UseDualStack=options.use_dual_stack,
            Endpoint=options.endpoint,
            AccountId=input_.get("account_id"),
            RequiresAccountId=True,
            OutpostId=options.outpost_id,
            Bucket=options.bucket,
            AccessPointName=options.access_point_name,
            UseArnRegion=options.use_arn_region,
            ResourceArn=options.resource_arn,
            UseS3ExpressControlEndpoint=options.use_s3_express_control_endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v20180820/jobs/{JobId}/tagging"
    url = url.replace("{JobId}", quote(input_["job_id"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "account_id" in input_:
        headers["x-amz-account-id"] = input_["account_id"]
    import capo_s3_control.types.s3_tag_set

    root = Element("PutJobTaggingRequest")
    if "tags" in input_:
        capo_s3_control.types.s3_tag_set.serialize_xml(input_["tags"], root, "Tags")
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
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def put_job_tagging(
    options: OperationOptions,
    input_: capo_s3_control.types.put_job_tagging_request.PutJobTaggingRequest,
) -> tuple[
    capo_s3_control.types.put_job_tagging_result.PutJobTaggingResult, zapros.Response
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


async def async_put_job_tagging(
    options: AsyncOperationOptions,
    input_: capo_s3_control.types.put_job_tagging_request.PutJobTaggingRequest,
) -> tuple[
    capo_s3_control.types.put_job_tagging_result.PutJobTaggingResult, zapros.Response
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
