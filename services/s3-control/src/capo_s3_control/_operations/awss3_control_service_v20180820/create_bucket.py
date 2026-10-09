"""Generated from Smithy shape ``com.amazonaws.s3control#CreateBucket``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import capo_s3_control._auth._signers
import capo_s3_control._auth._sigv4
import capo_s3_control._protocol.eventstream
import capo_s3_control.errors.bucket_already_exists
import capo_s3_control.errors.bucket_already_owned_by_you
import capo_s3_control.types.bucket_canned_acl
import capo_s3_control.types.create_bucket_configuration
import capo_s3_control.types.create_bucket_request
import capo_s3_control.types.create_bucket_result
from capo_s3_control._protocol.errors import find_error_element, parse_error_metadata
from capo_s3_control._protocol.xml import Element, fromstring, tostring
from capo_s3_control._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_s3_control._rule_engine._endpoint_runtime import apply_label
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
        case "BucketAlreadyExists":
            raise capo_s3_control.errors.bucket_already_exists.BucketAlreadyExists.from_xml(
                error_el, message
            )
        case "BucketAlreadyOwnedByYou":
            raise capo_s3_control.errors.bucket_already_owned_by_you.BucketAlreadyOwnedByYou.from_xml(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_s3_control.types.create_bucket_result.CreateBucketResult:
    out: capo_s3_control.types.create_bucket_result.CreateBucketResult = (
        capo_s3_control.types.create_bucket_result.deserialize_xml(
            fromstring(response.read())
        )
    )
    if "Location" in response.headers:
        out["location"] = response.headers["Location"]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_s3_control.types.create_bucket_result.CreateBucketResult:
    out: capo_s3_control.types.create_bucket_result.CreateBucketResult = (
        capo_s3_control.types.create_bucket_result.deserialize_xml(
            fromstring(await response.aread())
        )
    )
    if "Location" in response.headers:
        out["location"] = response.headers["Location"]
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
    input_: capo_s3_control.types.create_bucket_request.CreateBucketRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseFIPS=options.use_fips,
            UseDualStack=options.use_dual_stack,
            Endpoint=options.endpoint,
            AccountId=options.account_id,
            RequiresAccountId=options.requires_account_id,
            OutpostId=input_.get("outpost_id"),
            Bucket=input_.get("bucket"),
            AccessPointName=options.access_point_name,
            UseArnRegion=options.use_arn_region,
            ResourceArn=options.resource_arn,
            UseS3ExpressControlEndpoint=options.use_s3_express_control_endpoint,
        )
    )  # noqa: F841
    import capo_s3_control.types.bucket_canned_acl

    url = endpoint.url.rstrip("/") + "/v20180820/bucket/{Bucket}"
    url = apply_label(url, "{Bucket}", input_["bucket"])
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "acl" in input_:
        headers["x-amz-acl"] = capo_s3_control.types.bucket_canned_acl.to_xml_text(
            input_["acl"]
        )
    if "grant_full_control" in input_:
        headers["x-amz-grant-full-control"] = input_["grant_full_control"]
    if "grant_read" in input_:
        headers["x-amz-grant-read"] = input_["grant_read"]
    if "grant_read_acp" in input_:
        headers["x-amz-grant-read-acp"] = input_["grant_read_acp"]
    if "grant_write" in input_:
        headers["x-amz-grant-write"] = input_["grant_write"]
    if "grant_write_acp" in input_:
        headers["x-amz-grant-write-acp"] = input_["grant_write_acp"]
    headers["x-amz-bucket-object-lock-enabled"] = (
        "true" if input_.get("object_lock_enabled_for_bucket", False) else "false"
    )
    if "outpost_id" in input_:
        headers["x-amz-outpost-id"] = input_["outpost_id"]
    if "create_bucket_configuration" in input_:
        payload_root = Element("_")
        capo_s3_control.types.create_bucket_configuration.serialize_xml(
            input_["create_bucket_configuration"],
            payload_root,
            "CreateBucketConfiguration",
        )
        body: bytes | None = tostring(payload_root[0])
        headers["content-type"] = "application/xml"
    else:
        body = b""
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


def create_bucket(
    options: OperationOptions,
    input_: capo_s3_control.types.create_bucket_request.CreateBucketRequest,
) -> tuple[
    capo_s3_control.types.create_bucket_result.CreateBucketResult, zapros.Response
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


async def async_create_bucket(
    options: AsyncOperationOptions,
    input_: capo_s3_control.types.create_bucket_request.CreateBucketRequest,
) -> tuple[
    capo_s3_control.types.create_bucket_result.CreateBucketResult, zapros.Response
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
