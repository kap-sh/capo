"""Generated from Smithy shape ``com.amazonaws.s3#HeadObject``."""

from __future__ import annotations

import datetime
from email.utils import parsedate_to_datetime as _parse_http_date
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_s3._auth._signers
import capo_s3._auth._sigv4
import capo_s3._protocol.eventstream
import capo_s3.errors.not_found
import capo_s3.types.archive_status
import capo_s3.types.checksum_mode
import capo_s3.types.checksum_type
import capo_s3.types.head_object_output
import capo_s3.types.head_object_request
import capo_s3.types.if_modified_since
import capo_s3.types.if_unmodified_since
import capo_s3.types.last_modified
import capo_s3.types.metadata
import capo_s3.types.object_lock_event_hold
import capo_s3.types.object_lock_legal_hold_status
import capo_s3.types.object_lock_mode
import capo_s3.types.object_lock_retain_until_date
import capo_s3.types.replication_status
import capo_s3.types.request_charged
import capo_s3.types.request_payer
import capo_s3.types.response_expires
import capo_s3.types.server_side_encryption
import capo_s3.types.storage_class
from capo_s3._protocol.errors import find_error_element, parse_error_metadata
from capo_s3._protocol.xml import Element, fromstring
from capo_s3._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_s3._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_s3.errors import UnknownServiceError

STATUS_CODE_TO_CODE = {404: "NotFound"}


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
        case "NotFound":
            raise capo_s3.errors.not_found.NotFound.from_xml(error_el, message)
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_s3.types.head_object_output.HeadObjectOutput:
    out: capo_s3.types.head_object_output.HeadObjectOutput = {}  # type: ignore[typeddict-item]
    if "x-amz-delete-marker" in response.headers:
        out["delete_marker"] = response.headers["x-amz-delete-marker"].lower() == "true"
    if "accept-ranges" in response.headers:
        out["accept_ranges"] = response.headers["accept-ranges"]
    if "x-amz-expiration" in response.headers:
        out["expiration"] = response.headers["x-amz-expiration"]
    if "x-amz-restore" in response.headers:
        out["restore"] = response.headers["x-amz-restore"]
    if "x-amz-archive-status" in response.headers:
        out["archive_status"] = capo_s3.types.archive_status.from_xml_text(
            response.headers["x-amz-archive-status"]
        )
    if "Last-Modified" in response.headers:
        out["last_modified"] = _parse_http_date(response.headers["Last-Modified"])
    if "Content-Length" in response.headers:
        out["content_length"] = int(response.headers["Content-Length"])
    if "x-amz-checksum-crc32" in response.headers:
        out["checksum_crc32"] = response.headers["x-amz-checksum-crc32"]
    if "x-amz-checksum-crc32c" in response.headers:
        out["checksum_crc32_c"] = response.headers["x-amz-checksum-crc32c"]
    if "x-amz-checksum-crc64nvme" in response.headers:
        out["checksum_crc64_nvme"] = response.headers["x-amz-checksum-crc64nvme"]
    if "x-amz-checksum-sha1" in response.headers:
        out["checksum_sha1"] = response.headers["x-amz-checksum-sha1"]
    if "x-amz-checksum-sha256" in response.headers:
        out["checksum_sha256"] = response.headers["x-amz-checksum-sha256"]
    if "x-amz-checksum-sha512" in response.headers:
        out["checksum_sha512"] = response.headers["x-amz-checksum-sha512"]
    if "x-amz-checksum-md5" in response.headers:
        out["checksum_md5"] = response.headers["x-amz-checksum-md5"]
    if "x-amz-checksum-xxhash64" in response.headers:
        out["checksum_xxhash64"] = response.headers["x-amz-checksum-xxhash64"]
    if "x-amz-checksum-xxhash3" in response.headers:
        out["checksum_xxhash3"] = response.headers["x-amz-checksum-xxhash3"]
    if "x-amz-checksum-xxhash128" in response.headers:
        out["checksum_xxhash128"] = response.headers["x-amz-checksum-xxhash128"]
    if "x-amz-checksum-type" in response.headers:
        out["checksum_type"] = capo_s3.types.checksum_type.from_xml_text(
            response.headers["x-amz-checksum-type"]
        )
    if "ETag" in response.headers:
        out["e_tag"] = response.headers["ETag"]
    if "x-amz-missing-meta" in response.headers:
        out["missing_meta"] = int(response.headers["x-amz-missing-meta"])
    if "x-amz-version-id" in response.headers:
        out["version_id"] = response.headers["x-amz-version-id"]
    if "Cache-Control" in response.headers:
        out["cache_control"] = response.headers["Cache-Control"]
    if "Content-Disposition" in response.headers:
        out["content_disposition"] = response.headers["Content-Disposition"]
    if "Content-Encoding" in response.headers:
        out["content_encoding"] = response.headers["Content-Encoding"]
    if "Content-Language" in response.headers:
        out["content_language"] = response.headers["Content-Language"]
    if "Content-Type" in response.headers:
        out["content_type"] = response.headers["Content-Type"]
    if "Content-Range" in response.headers:
        out["content_range"] = response.headers["Content-Range"]
    if "Expires" in response.headers:
        out["expires"] = response.headers["Expires"]
    if "x-amz-website-redirect-location" in response.headers:
        out["website_redirect_location"] = response.headers[
            "x-amz-website-redirect-location"
        ]
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
    if "x-amz-server-side-encryption-bucket-key-enabled" in response.headers:
        out["bucket_key_enabled"] = (
            response.headers["x-amz-server-side-encryption-bucket-key-enabled"].lower()
            == "true"
        )
    if "x-amz-storage-class" in response.headers:
        out["storage_class"] = capo_s3.types.storage_class.from_xml_text(
            response.headers["x-amz-storage-class"]
        )
    if "x-amz-request-charged" in response.headers:
        out["request_charged"] = capo_s3.types.request_charged.from_xml_text(
            response.headers["x-amz-request-charged"]
        )
    if "x-amz-replication-status" in response.headers:
        out["replication_status"] = capo_s3.types.replication_status.from_xml_text(
            response.headers["x-amz-replication-status"]
        )
    if "x-amz-mp-parts-count" in response.headers:
        out["parts_count"] = int(response.headers["x-amz-mp-parts-count"])
    if "x-amz-tagging-count" in response.headers:
        out["tag_count"] = int(response.headers["x-amz-tagging-count"])
    if "x-amz-object-lock-mode" in response.headers:
        out["object_lock_mode"] = capo_s3.types.object_lock_mode.from_xml_text(
            response.headers["x-amz-object-lock-mode"]
        )
    if "x-amz-object-lock-retain-until-date" in response.headers:
        out["object_lock_retain_until_date"] = datetime.datetime.fromisoformat(
            response.headers["x-amz-object-lock-retain-until-date"].replace(
                "Z", "+00:00"
            )
        )
    if "x-amz-object-lock-legal-hold" in response.headers:
        out["object_lock_legal_hold_status"] = (
            capo_s3.types.object_lock_legal_hold_status.from_xml_text(
                response.headers["x-amz-object-lock-legal-hold"]
            )
        )
    if "x-amz-object-lock-event-hold" in response.headers:
        out["object_lock_event_hold"] = (
            capo_s3.types.object_lock_event_hold.from_xml_text(
                response.headers["x-amz-object-lock-event-hold"]
            )
        )
    if "x-amz-object-lock-event-hold-duration-days" in response.headers:
        out["object_lock_event_hold_duration_days"] = int(
            response.headers["x-amz-object-lock-event-hold-duration-days"]
        )
    if "x-amz-object-lock-event-hold-duration-years" in response.headers:
        out["object_lock_event_hold_duration_years"] = int(
            response.headers["x-amz-object-lock-event-hold-duration-years"]
        )
    out["metadata"] = {
        k[11:]: v
        for k, v in response.headers.items()
        if k.lower().startswith("x-amz-meta-")
    }
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_s3.types.head_object_output.HeadObjectOutput:
    out: capo_s3.types.head_object_output.HeadObjectOutput = {}  # type: ignore[typeddict-item]
    if "x-amz-delete-marker" in response.headers:
        out["delete_marker"] = response.headers["x-amz-delete-marker"].lower() == "true"
    if "accept-ranges" in response.headers:
        out["accept_ranges"] = response.headers["accept-ranges"]
    if "x-amz-expiration" in response.headers:
        out["expiration"] = response.headers["x-amz-expiration"]
    if "x-amz-restore" in response.headers:
        out["restore"] = response.headers["x-amz-restore"]
    if "x-amz-archive-status" in response.headers:
        out["archive_status"] = capo_s3.types.archive_status.from_xml_text(
            response.headers["x-amz-archive-status"]
        )
    if "Last-Modified" in response.headers:
        out["last_modified"] = _parse_http_date(response.headers["Last-Modified"])
    if "Content-Length" in response.headers:
        out["content_length"] = int(response.headers["Content-Length"])
    if "x-amz-checksum-crc32" in response.headers:
        out["checksum_crc32"] = response.headers["x-amz-checksum-crc32"]
    if "x-amz-checksum-crc32c" in response.headers:
        out["checksum_crc32_c"] = response.headers["x-amz-checksum-crc32c"]
    if "x-amz-checksum-crc64nvme" in response.headers:
        out["checksum_crc64_nvme"] = response.headers["x-amz-checksum-crc64nvme"]
    if "x-amz-checksum-sha1" in response.headers:
        out["checksum_sha1"] = response.headers["x-amz-checksum-sha1"]
    if "x-amz-checksum-sha256" in response.headers:
        out["checksum_sha256"] = response.headers["x-amz-checksum-sha256"]
    if "x-amz-checksum-sha512" in response.headers:
        out["checksum_sha512"] = response.headers["x-amz-checksum-sha512"]
    if "x-amz-checksum-md5" in response.headers:
        out["checksum_md5"] = response.headers["x-amz-checksum-md5"]
    if "x-amz-checksum-xxhash64" in response.headers:
        out["checksum_xxhash64"] = response.headers["x-amz-checksum-xxhash64"]
    if "x-amz-checksum-xxhash3" in response.headers:
        out["checksum_xxhash3"] = response.headers["x-amz-checksum-xxhash3"]
    if "x-amz-checksum-xxhash128" in response.headers:
        out["checksum_xxhash128"] = response.headers["x-amz-checksum-xxhash128"]
    if "x-amz-checksum-type" in response.headers:
        out["checksum_type"] = capo_s3.types.checksum_type.from_xml_text(
            response.headers["x-amz-checksum-type"]
        )
    if "ETag" in response.headers:
        out["e_tag"] = response.headers["ETag"]
    if "x-amz-missing-meta" in response.headers:
        out["missing_meta"] = int(response.headers["x-amz-missing-meta"])
    if "x-amz-version-id" in response.headers:
        out["version_id"] = response.headers["x-amz-version-id"]
    if "Cache-Control" in response.headers:
        out["cache_control"] = response.headers["Cache-Control"]
    if "Content-Disposition" in response.headers:
        out["content_disposition"] = response.headers["Content-Disposition"]
    if "Content-Encoding" in response.headers:
        out["content_encoding"] = response.headers["Content-Encoding"]
    if "Content-Language" in response.headers:
        out["content_language"] = response.headers["Content-Language"]
    if "Content-Type" in response.headers:
        out["content_type"] = response.headers["Content-Type"]
    if "Content-Range" in response.headers:
        out["content_range"] = response.headers["Content-Range"]
    if "Expires" in response.headers:
        out["expires"] = response.headers["Expires"]
    if "x-amz-website-redirect-location" in response.headers:
        out["website_redirect_location"] = response.headers[
            "x-amz-website-redirect-location"
        ]
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
    if "x-amz-server-side-encryption-bucket-key-enabled" in response.headers:
        out["bucket_key_enabled"] = (
            response.headers["x-amz-server-side-encryption-bucket-key-enabled"].lower()
            == "true"
        )
    if "x-amz-storage-class" in response.headers:
        out["storage_class"] = capo_s3.types.storage_class.from_xml_text(
            response.headers["x-amz-storage-class"]
        )
    if "x-amz-request-charged" in response.headers:
        out["request_charged"] = capo_s3.types.request_charged.from_xml_text(
            response.headers["x-amz-request-charged"]
        )
    if "x-amz-replication-status" in response.headers:
        out["replication_status"] = capo_s3.types.replication_status.from_xml_text(
            response.headers["x-amz-replication-status"]
        )
    if "x-amz-mp-parts-count" in response.headers:
        out["parts_count"] = int(response.headers["x-amz-mp-parts-count"])
    if "x-amz-tagging-count" in response.headers:
        out["tag_count"] = int(response.headers["x-amz-tagging-count"])
    if "x-amz-object-lock-mode" in response.headers:
        out["object_lock_mode"] = capo_s3.types.object_lock_mode.from_xml_text(
            response.headers["x-amz-object-lock-mode"]
        )
    if "x-amz-object-lock-retain-until-date" in response.headers:
        out["object_lock_retain_until_date"] = datetime.datetime.fromisoformat(
            response.headers["x-amz-object-lock-retain-until-date"].replace(
                "Z", "+00:00"
            )
        )
    if "x-amz-object-lock-legal-hold" in response.headers:
        out["object_lock_legal_hold_status"] = (
            capo_s3.types.object_lock_legal_hold_status.from_xml_text(
                response.headers["x-amz-object-lock-legal-hold"]
            )
        )
    if "x-amz-object-lock-event-hold" in response.headers:
        out["object_lock_event_hold"] = (
            capo_s3.types.object_lock_event_hold.from_xml_text(
                response.headers["x-amz-object-lock-event-hold"]
            )
        )
    if "x-amz-object-lock-event-hold-duration-days" in response.headers:
        out["object_lock_event_hold_duration_days"] = int(
            response.headers["x-amz-object-lock-event-hold-duration-days"]
        )
    if "x-amz-object-lock-event-hold-duration-years" in response.headers:
        out["object_lock_event_hold_duration_years"] = int(
            response.headers["x-amz-object-lock-event-hold-duration-years"]
        )
    out["metadata"] = {
        k[11:]: v
        for k, v in response.headers.items()
        if k.lower().startswith("x-amz-meta-")
    }
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
    input_: capo_s3.types.head_object_request.HeadObjectRequest,
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
    import capo_s3.types.checksum_mode
    import capo_s3.types.request_payer

    url = endpoint.url.rstrip("/") + "/{Key+}"
    url = url.replace("{Key+}", quote(input_["key"], safe="/"))
    params: list[tuple[str, str]] = []
    if "response_cache_control" in input_:
        params.append(("response-cache-control", input_["response_cache_control"]))
    if "response_content_disposition" in input_:
        params.append(
            ("response-content-disposition", input_["response_content_disposition"])
        )
    if "response_content_encoding" in input_:
        params.append(
            ("response-content-encoding", input_["response_content_encoding"])
        )
    if "response_content_language" in input_:
        params.append(
            ("response-content-language", input_["response_content_language"])
        )
    if "response_content_type" in input_:
        params.append(("response-content-type", input_["response_content_type"]))
    if "response_expires" in input_:
        params.append(
            (
                "response-expires",
                capo_s3._protocol.serialize.fmt_http_date(input_["response_expires"]),
            )
        )
    if "version_id" in input_:
        params.append(("versionId", input_["version_id"]))
    if "part_number" in input_:
        params.append(("partNumber", str(input_["part_number"])))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "if_match" in input_:
        headers["If-Match"] = input_["if_match"]
    if "if_modified_since" in input_:
        headers["If-Modified-Since"] = capo_s3._protocol.serialize.fmt_http_date(
            input_["if_modified_since"]
        )
    if "if_none_match" in input_:
        headers["If-None-Match"] = input_["if_none_match"]
    if "if_unmodified_since" in input_:
        headers["If-Unmodified-Since"] = capo_s3._protocol.serialize.fmt_http_date(
            input_["if_unmodified_since"]
        )
    if "range" in input_:
        headers["Range"] = input_["range"]
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
    if "request_payer" in input_:
        headers["x-amz-request-payer"] = capo_s3.types.request_payer.to_xml_text(
            input_["request_payer"]
        )
    if "expected_bucket_owner" in input_:
        headers["x-amz-expected-bucket-owner"] = input_["expected_bucket_owner"]
    if "checksum_mode" in input_:
        headers["x-amz-checksum-mode"] = capo_s3.types.checksum_mode.to_xml_text(
            input_["checksum_mode"]
        )
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
        normalized_url, "HEAD", headers=headers, body=body, context={"signer": signer}
    )


def head_object(
    options: OperationOptions,
    input_: capo_s3.types.head_object_request.HeadObjectRequest,
) -> tuple[capo_s3.types.head_object_output.HeadObjectOutput, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            raise_error(response, handle_error)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_head_object(
    options: AsyncOperationOptions,
    input_: capo_s3.types.head_object_request.HeadObjectRequest,
) -> tuple[capo_s3.types.head_object_output.HeadObjectOutput, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 300:
            await response.aread()
            raise_error(response, handle_error)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
