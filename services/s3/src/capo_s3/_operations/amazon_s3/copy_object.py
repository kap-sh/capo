"""Generated from Smithy shape ``com.amazonaws.s3#CopyObject``."""

from __future__ import annotations

from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_s3._auth._signers
import capo_s3._auth._sigv4
import capo_s3._protocol.eventstream
import capo_s3.errors.object_not_in_active_tier_error
import capo_s3.types.annotation_directive
import capo_s3.types.checksum_algorithm
import capo_s3.types.copy_object_output
import capo_s3.types.copy_object_request
import capo_s3.types.copy_object_result
import capo_s3.types.copy_source_if_modified_since
import capo_s3.types.copy_source_if_unmodified_since
import capo_s3.types.metadata
import capo_s3.types.metadata_directive
import capo_s3.types.object_canned_acl
import capo_s3.types.object_lock_legal_hold_status
import capo_s3.types.object_lock_mode
import capo_s3.types.object_lock_retain_until_date
import capo_s3.types.request_charged
import capo_s3.types.request_payer
import capo_s3.types.server_side_encryption
import capo_s3.types.storage_class
import capo_s3.types.tagging_directive
from capo_s3._protocol.errors import (
    find_error_element,
    is_xml_error_body,
    parse_error_metadata,
)
from capo_s3._protocol.xml import Element, fromstring
from capo_s3._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_s3._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_s3.errors import UnknownServiceError

STATUS_CODE_TO_CODE = {403: "ObjectNotInActiveTierError"}


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
        case "ObjectNotInActiveTierError":
            raise capo_s3.errors.object_not_in_active_tier_error.ObjectNotInActiveTierError.from_xml(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_s3.types.copy_object_output.CopyObjectOutput:
    out: capo_s3.types.copy_object_output.CopyObjectOutput = {
        "copy_object_result": capo_s3.types.copy_object_result.deserialize_xml(
            fromstring(response.read())
        )
    }  # type: ignore[typeddict-item]
    if "x-amz-expiration" in response.headers:
        out["expiration"] = response.headers["x-amz-expiration"]
    if "x-amz-copy-source-version-id" in response.headers:
        out["copy_source_version_id"] = response.headers["x-amz-copy-source-version-id"]
    if "x-amz-version-id" in response.headers:
        out["version_id"] = response.headers["x-amz-version-id"]
    if "x-amz-server-side-encryption" in response.headers:
        out["server_side_encryption"] = (
            capo_s3.types.server_side_encryption.from_xml_text(
                response.headers["x-amz-server-side-encryption"]
            )
        )
    if "x-amz-server-side-encryption-customer-algorithm" in response.headers:
        out["sse_customer_algorithm"] = response.headers[
            "x-amz-server-side-encryption-customer-algorithm"
        ]
    if "x-amz-server-side-encryption-customer-key-MD5" in response.headers:
        out["sse_customer_key_md5"] = response.headers[
            "x-amz-server-side-encryption-customer-key-MD5"
        ]
    if "x-amz-server-side-encryption-aws-kms-key-id" in response.headers:
        out["ssekms_key_id"] = response.headers[
            "x-amz-server-side-encryption-aws-kms-key-id"
        ]
    if "x-amz-server-side-encryption-context" in response.headers:
        out["ssekms_encryption_context"] = response.headers[
            "x-amz-server-side-encryption-context"
        ]
    if "x-amz-server-side-encryption-bucket-key-enabled" in response.headers:
        out["bucket_key_enabled"] = (
            response.headers["x-amz-server-side-encryption-bucket-key-enabled"].lower()
            == "true"
        )
    if "x-amz-request-charged" in response.headers:
        out["request_charged"] = capo_s3.types.request_charged.from_xml_text(
            response.headers["x-amz-request-charged"]
        )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_s3.types.copy_object_output.CopyObjectOutput:
    out: capo_s3.types.copy_object_output.CopyObjectOutput = {
        "copy_object_result": capo_s3.types.copy_object_result.deserialize_xml(
            fromstring(await response.aread())
        )
    }  # type: ignore[typeddict-item]
    if "x-amz-expiration" in response.headers:
        out["expiration"] = response.headers["x-amz-expiration"]
    if "x-amz-copy-source-version-id" in response.headers:
        out["copy_source_version_id"] = response.headers["x-amz-copy-source-version-id"]
    if "x-amz-version-id" in response.headers:
        out["version_id"] = response.headers["x-amz-version-id"]
    if "x-amz-server-side-encryption" in response.headers:
        out["server_side_encryption"] = (
            capo_s3.types.server_side_encryption.from_xml_text(
                response.headers["x-amz-server-side-encryption"]
            )
        )
    if "x-amz-server-side-encryption-customer-algorithm" in response.headers:
        out["sse_customer_algorithm"] = response.headers[
            "x-amz-server-side-encryption-customer-algorithm"
        ]
    if "x-amz-server-side-encryption-customer-key-MD5" in response.headers:
        out["sse_customer_key_md5"] = response.headers[
            "x-amz-server-side-encryption-customer-key-MD5"
        ]
    if "x-amz-server-side-encryption-aws-kms-key-id" in response.headers:
        out["ssekms_key_id"] = response.headers[
            "x-amz-server-side-encryption-aws-kms-key-id"
        ]
    if "x-amz-server-side-encryption-context" in response.headers:
        out["ssekms_encryption_context"] = response.headers[
            "x-amz-server-side-encryption-context"
        ]
    if "x-amz-server-side-encryption-bucket-key-enabled" in response.headers:
        out["bucket_key_enabled"] = (
            response.headers["x-amz-server-side-encryption-bucket-key-enabled"].lower()
            == "true"
        )
    if "x-amz-request-charged" in response.headers:
        out["request_charged"] = capo_s3.types.request_charged.from_xml_text(
            response.headers["x-amz-request-charged"]
        )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_s3._auth._signers.Signer | None:
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
            sigv4_config = capo_s3._auth._sigv4.build_sigv4_auth_scheme(
                "s3", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_s3._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_s3.types.copy_object_request.CopyObjectRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Bucket=input_.get("bucket"),
            Region=options.region,
            UseFIPS=options.use_fips,
            UseDualStack=options.use_dual_stack,
            Endpoint=options.endpoint,
            ForcePathStyle=options.force_path_style,
            Accelerate=options.accelerate,
            UseGlobalEndpoint=options.use_global_endpoint,
            UseObjectLambdaEndpoint=options.use_object_lambda_endpoint,
            Key=input_.get("key"),
            Prefix=options.prefix,
            CopySource=input_.get("copy_source"),
            DisableAccessPoints=options.disable_access_points,
            DisableMultiRegionAccessPoints=options.disable_multi_region_access_points,
            UseArnRegion=options.use_arn_region,
            UseS3ExpressControlEndpoint=options.use_s3_express_control_endpoint,
            DisableS3ExpressSessionAuth=True,
        )
    )  # noqa: F841
    import capo_s3._protocol.serialize
    import capo_s3.types.annotation_directive
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.metadata_directive
    import capo_s3.types.object_canned_acl
    import capo_s3.types.object_lock_legal_hold_status
    import capo_s3.types.object_lock_mode
    import capo_s3.types.request_payer
    import capo_s3.types.server_side_encryption
    import capo_s3.types.storage_class
    import capo_s3.types.tagging_directive

    url = endpoint.url.rstrip("/") + "/{Key+}?x-id=CopyObject"
    url = url.replace("{Key+}", quote(input_["key"], safe="/"))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "acl" in input_:
        headers["x-amz-acl"] = capo_s3.types.object_canned_acl.to_xml_text(
            input_["acl"]
        )
    if "cache_control" in input_:
        headers["Cache-Control"] = input_["cache_control"]
    if "checksum_algorithm" in input_:
        headers["x-amz-checksum-algorithm"] = (
            capo_s3.types.checksum_algorithm.to_xml_text(input_["checksum_algorithm"])
        )
    if "content_disposition" in input_:
        headers["Content-Disposition"] = input_["content_disposition"]
    if "content_encoding" in input_:
        headers["Content-Encoding"] = input_["content_encoding"]
    if "content_language" in input_:
        headers["Content-Language"] = input_["content_language"]
    if "content_type" in input_:
        headers["Content-Type"] = input_["content_type"]
    if "copy_source" in input_:
        headers["x-amz-copy-source"] = input_["copy_source"]
    if "copy_source_if_match" in input_:
        headers["x-amz-copy-source-if-match"] = input_["copy_source_if_match"]
    if "copy_source_if_modified_since" in input_:
        headers["x-amz-copy-source-if-modified-since"] = (
            capo_s3._protocol.serialize.fmt_http_date(
                input_["copy_source_if_modified_since"]
            )
        )
    if "copy_source_if_none_match" in input_:
        headers["x-amz-copy-source-if-none-match"] = input_["copy_source_if_none_match"]
    if "copy_source_if_unmodified_since" in input_:
        headers["x-amz-copy-source-if-unmodified-since"] = (
            capo_s3._protocol.serialize.fmt_http_date(
                input_["copy_source_if_unmodified_since"]
            )
        )
    if "expires" in input_:
        headers["Expires"] = input_["expires"]
    if "grant_full_control" in input_:
        headers["x-amz-grant-full-control"] = input_["grant_full_control"]
    if "grant_read" in input_:
        headers["x-amz-grant-read"] = input_["grant_read"]
    if "grant_read_acp" in input_:
        headers["x-amz-grant-read-acp"] = input_["grant_read_acp"]
    if "grant_write_acp" in input_:
        headers["x-amz-grant-write-acp"] = input_["grant_write_acp"]
    if "if_match" in input_:
        headers["If-Match"] = input_["if_match"]
    if "if_none_match" in input_:
        headers["If-None-Match"] = input_["if_none_match"]
    if "metadata_directive" in input_:
        headers["x-amz-metadata-directive"] = (
            capo_s3.types.metadata_directive.to_xml_text(input_["metadata_directive"])
        )
    if "tagging_directive" in input_:
        headers["x-amz-tagging-directive"] = (
            capo_s3.types.tagging_directive.to_xml_text(input_["tagging_directive"])
        )
    if "annotation_directive" in input_:
        headers["x-amz-object-annotation-directive"] = (
            capo_s3.types.annotation_directive.to_xml_text(
                input_["annotation_directive"]
            )
        )
    if "server_side_encryption" in input_:
        headers["x-amz-server-side-encryption"] = (
            capo_s3.types.server_side_encryption.to_xml_text(
                input_["server_side_encryption"]
            )
        )
    if "storage_class" in input_:
        headers["x-amz-storage-class"] = capo_s3.types.storage_class.to_xml_text(
            input_["storage_class"]
        )
    if "website_redirect_location" in input_:
        headers["x-amz-website-redirect-location"] = input_["website_redirect_location"]
    if "sse_customer_algorithm" in input_:
        headers["x-amz-server-side-encryption-customer-algorithm"] = input_[
            "sse_customer_algorithm"
        ]
    if "sse_customer_key" in input_:
        headers["x-amz-server-side-encryption-customer-key"] = input_[
            "sse_customer_key"
        ]
    if "sse_customer_key_md5" in input_:
        headers["x-amz-server-side-encryption-customer-key-MD5"] = input_[
            "sse_customer_key_md5"
        ]
    if "ssekms_key_id" in input_:
        headers["x-amz-server-side-encryption-aws-kms-key-id"] = input_["ssekms_key_id"]
    if "ssekms_encryption_context" in input_:
        headers["x-amz-server-side-encryption-context"] = input_[
            "ssekms_encryption_context"
        ]
    if "bucket_key_enabled" in input_:
        headers["x-amz-server-side-encryption-bucket-key-enabled"] = (
            "true" if input_["bucket_key_enabled"] else "false"
        )
    if "copy_source_sse_customer_algorithm" in input_:
        headers["x-amz-copy-source-server-side-encryption-customer-algorithm"] = input_[
            "copy_source_sse_customer_algorithm"
        ]
    if "copy_source_sse_customer_key" in input_:
        headers["x-amz-copy-source-server-side-encryption-customer-key"] = input_[
            "copy_source_sse_customer_key"
        ]
    if "copy_source_sse_customer_key_md5" in input_:
        headers["x-amz-copy-source-server-side-encryption-customer-key-MD5"] = input_[
            "copy_source_sse_customer_key_md5"
        ]
    if "request_payer" in input_:
        headers["x-amz-request-payer"] = capo_s3.types.request_payer.to_xml_text(
            input_["request_payer"]
        )
    if "tagging" in input_:
        headers["x-amz-tagging"] = input_["tagging"]
    if "object_lock_mode" in input_:
        headers["x-amz-object-lock-mode"] = capo_s3.types.object_lock_mode.to_xml_text(
            input_["object_lock_mode"]
        )
    if "object_lock_retain_until_date" in input_:
        headers["x-amz-object-lock-retain-until-date"] = (
            capo_s3._protocol.serialize.fmt_date_time(
                input_["object_lock_retain_until_date"]
            )
        )
    if "object_lock_legal_hold_status" in input_:
        headers["x-amz-object-lock-legal-hold"] = (
            capo_s3.types.object_lock_legal_hold_status.to_xml_text(
                input_["object_lock_legal_hold_status"]
            )
        )
    if "expected_bucket_owner" in input_:
        headers["x-amz-expected-bucket-owner"] = input_["expected_bucket_owner"]
    if "expected_source_bucket_owner" in input_:
        headers["x-amz-source-expected-bucket-owner"] = input_[
            "expected_source_bucket_owner"
        ]
    if "metadata" in input_:
        for k, v in input_["metadata"].items():
            headers["x-amz-meta-" + k] = v
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def copy_object(
    options: OperationOptions,
    input_: capo_s3.types.copy_object_request.CopyObjectRequest,
) -> tuple[capo_s3.types.copy_object_output.CopyObjectOutput, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        body = response.read()
        if response.status >= 300 or is_xml_error_body(body):
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_copy_object(
    options: AsyncOperationOptions,
    input_: capo_s3.types.copy_object_request.CopyObjectRequest,
) -> tuple[capo_s3.types.copy_object_output.CopyObjectOutput, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        body = await response.aread()
        if response.status >= 300 or is_xml_error_body(body):
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
