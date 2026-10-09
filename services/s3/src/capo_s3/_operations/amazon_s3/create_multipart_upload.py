"""Generated from Smithy shape ``com.amazonaws.s3#CreateMultipartUpload``."""

from __future__ import annotations

from email.utils import parsedate_to_datetime as _parse_http_date
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_s3._auth._signers
import capo_s3._auth._sigv4
import capo_s3._protocol.eventstream
import capo_s3.types.abort_date
import capo_s3.types.checksum_algorithm
import capo_s3.types.checksum_type
import capo_s3.types.create_multipart_upload_output
import capo_s3.types.create_multipart_upload_request
import capo_s3.types.metadata
import capo_s3.types.object_canned_acl
import capo_s3.types.object_lock_event_hold
import capo_s3.types.object_lock_legal_hold_status
import capo_s3.types.object_lock_mode
import capo_s3.types.object_lock_retain_until_date
import capo_s3.types.request_charged
import capo_s3.types.request_payer
import capo_s3.types.server_side_encryption
import capo_s3.types.storage_class
from capo_s3._protocol.errors import parse_error_metadata
from capo_s3._protocol.xml import fromstring
from capo_s3._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_s3._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_s3.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    body = response.read()
    if not body:
        raise UnknownServiceError(code=None, message=None, response=response)
    root = fromstring(body)
    code, message = parse_error_metadata(root)
    match code:
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_s3.types.create_multipart_upload_output.CreateMultipartUploadOutput:
    out: capo_s3.types.create_multipart_upload_output.CreateMultipartUploadOutput = (
        capo_s3.types.create_multipart_upload_output.deserialize_xml(
            fromstring(response.read())
        )
    )
    if "x-amz-abort-date" in response.headers:
        out["abort_date"] = _parse_http_date(response.headers["x-amz-abort-date"])
    if "x-amz-abort-rule-id" in response.headers:
        out["abort_rule_id"] = response.headers["x-amz-abort-rule-id"]
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
    if "x-amz-checksum-algorithm" in response.headers:
        out["checksum_algorithm"] = capo_s3.types.checksum_algorithm.from_xml_text(
            response.headers["x-amz-checksum-algorithm"]
        )
    if "x-amz-checksum-type" in response.headers:
        out["checksum_type"] = capo_s3.types.checksum_type.from_xml_text(
            response.headers["x-amz-checksum-type"]
        )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_s3.types.create_multipart_upload_output.CreateMultipartUploadOutput:
    out: capo_s3.types.create_multipart_upload_output.CreateMultipartUploadOutput = (
        capo_s3.types.create_multipart_upload_output.deserialize_xml(
            fromstring(await response.aread())
        )
    )
    if "x-amz-abort-date" in response.headers:
        out["abort_date"] = _parse_http_date(response.headers["x-amz-abort-date"])
    if "x-amz-abort-rule-id" in response.headers:
        out["abort_rule_id"] = response.headers["x-amz-abort-rule-id"]
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
    if "x-amz-checksum-algorithm" in response.headers:
        out["checksum_algorithm"] = capo_s3.types.checksum_algorithm.from_xml_text(
            response.headers["x-amz-checksum-algorithm"]
        )
    if "x-amz-checksum-type" in response.headers:
        out["checksum_type"] = capo_s3.types.checksum_type.from_xml_text(
            response.headers["x-amz-checksum-type"]
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
    input_: capo_s3.types.create_multipart_upload_request.CreateMultipartUploadRequest,
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
            CopySource=options.copy_source,
            DisableAccessPoints=options.disable_access_points,
            DisableMultiRegionAccessPoints=options.disable_multi_region_access_points,
            UseArnRegion=options.use_arn_region,
            UseS3ExpressControlEndpoint=options.use_s3_express_control_endpoint,
            DisableS3ExpressSessionAuth=options.disable_s3_express_session_auth,
        )
    )  # noqa: F841
    import capo_s3._protocol.serialize
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.checksum_type
    import capo_s3.types.object_canned_acl
    import capo_s3.types.object_lock_event_hold
    import capo_s3.types.object_lock_legal_hold_status
    import capo_s3.types.object_lock_mode
    import capo_s3.types.request_payer
    import capo_s3.types.server_side_encryption
    import capo_s3.types.storage_class

    url = endpoint.url.rstrip("/") + "/{Key+}?uploads"
    url = url.replace("{Key+}", quote(input_["key"], safe="/"))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "acl" in input_:
        headers["x-amz-acl"] = capo_s3.types.object_canned_acl.to_xml_text(
            input_["acl"]
        )
    if "cache_control" in input_:
        headers["Cache-Control"] = input_["cache_control"]
    if "content_disposition" in input_:
        headers["Content-Disposition"] = input_["content_disposition"]
    if "content_encoding" in input_:
        headers["Content-Encoding"] = input_["content_encoding"]
    if "content_language" in input_:
        headers["Content-Language"] = input_["content_language"]
    if "content_type" in input_:
        headers["Content-Type"] = input_["content_type"]
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
    if "object_lock_event_hold" in input_:
        headers["x-amz-object-lock-event-hold"] = (
            capo_s3.types.object_lock_event_hold.to_xml_text(
                input_["object_lock_event_hold"]
            )
        )
    if "object_lock_event_hold_duration_days" in input_:
        headers["x-amz-object-lock-event-hold-duration-days"] = str(
            input_["object_lock_event_hold_duration_days"]
        )
    if "object_lock_event_hold_duration_years" in input_:
        headers["x-amz-object-lock-event-hold-duration-years"] = str(
            input_["object_lock_event_hold_duration_years"]
        )
    if "expected_bucket_owner" in input_:
        headers["x-amz-expected-bucket-owner"] = input_["expected_bucket_owner"]
    if "checksum_algorithm" in input_:
        headers["x-amz-checksum-algorithm"] = (
            capo_s3.types.checksum_algorithm.to_xml_text(input_["checksum_algorithm"])
        )
    if "checksum_type" in input_:
        headers["x-amz-checksum-type"] = capo_s3.types.checksum_type.to_xml_text(
            input_["checksum_type"]
        )
    if "metadata" in input_:
        for k, v in input_["metadata"].items():
            headers["x-amz-meta-" + k] = v
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
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_multipart_upload(
    options: OperationOptions,
    input_: capo_s3.types.create_multipart_upload_request.CreateMultipartUploadRequest,
) -> tuple[
    capo_s3.types.create_multipart_upload_output.CreateMultipartUploadOutput,
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


async def async_create_multipart_upload(
    options: AsyncOperationOptions,
    input_: capo_s3.types.create_multipart_upload_request.CreateMultipartUploadRequest,
) -> tuple[
    capo_s3.types.create_multipart_upload_output.CreateMultipartUploadOutput,
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
