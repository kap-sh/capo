"""Generated from Smithy shape ``com.amazonaws.s3#SelectObjectContent``."""

from __future__ import annotations

from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_s3._auth._signers
import capo_s3._auth._sigv4
import capo_s3._protocol.eventstream
import capo_s3.types.expression_type
import capo_s3.types.input_serialization
import capo_s3.types.output_serialization
import capo_s3.types.request_progress
import capo_s3.types.scan_range
import capo_s3.types.select_object_content_event_stream
import capo_s3.types.select_object_content_output
import capo_s3.types.select_object_content_request
from capo_s3._protocol.errors import parse_error_metadata
from capo_s3._protocol.eventstream import (
    MessageDecoder,
    async_raw_stream_to_events,
    raw_stream_to_events,
)
from capo_s3._protocol.xml import Element, SubElement, fromstring, tostring
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
) -> capo_s3.types.select_object_content_output.SelectObjectContentOutput:
    _message_decoder = MessageDecoder()
    _union_deser = (
        capo_s3.types.select_object_content_event_stream.deserialize_event_xml
    )
    _iter = cast(Any, response.iter_bytes())
    out: capo_s3.types.select_object_content_output.SelectObjectContentOutput = {
        "payload": cast(
            Any, raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_s3.types.select_object_content_output.SelectObjectContentOutput:
    _message_decoder = MessageDecoder()
    _union_deser = (
        capo_s3.types.select_object_content_event_stream.deserialize_event_xml
    )
    _iter = cast(Any, response.async_iter_bytes())
    out: capo_s3.types.select_object_content_output.SelectObjectContentOutput = {
        "payload": cast(
            Any, async_raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
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
    input_: capo_s3.types.select_object_content_request.SelectObjectContentRequest,
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
            Key=options.key,
            Prefix=options.prefix,
            CopySource=options.copy_source,
            DisableAccessPoints=options.disable_access_points,
            DisableMultiRegionAccessPoints=options.disable_multi_region_access_points,
            UseArnRegion=options.use_arn_region,
            UseS3ExpressControlEndpoint=options.use_s3_express_control_endpoint,
            DisableS3ExpressSessionAuth=options.disable_s3_express_session_auth,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/{Key+}?select&select-type=2"
    url = url.replace("{Key+}", quote(input_["key"], safe="/"))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
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
    if "expected_bucket_owner" in input_:
        headers["x-amz-expected-bucket-owner"] = input_["expected_bucket_owner"]
    import capo_s3.types.expression_type
    import capo_s3.types.input_serialization
    import capo_s3.types.output_serialization
    import capo_s3.types.request_progress
    import capo_s3.types.scan_range

    root = Element("SelectObjectContentRequest")
    if "expression" in input_:
        SubElement(root, "Expression").text = input_["expression"]
    if "expression_type" in input_:
        capo_s3.types.expression_type.serialize_xml(
            input_["expression_type"], root, "ExpressionType"
        )
    if "request_progress" in input_:
        capo_s3.types.request_progress.serialize_xml(
            input_["request_progress"], root, "RequestProgress"
        )
    if "input_serialization" in input_:
        capo_s3.types.input_serialization.serialize_xml(
            input_["input_serialization"], root, "InputSerialization"
        )
    if "output_serialization" in input_:
        capo_s3.types.output_serialization.serialize_xml(
            input_["output_serialization"], root, "OutputSerialization"
        )
    if "scan_range" in input_:
        capo_s3.types.scan_range.serialize_xml(input_["scan_range"], root, "ScanRange")
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


def select_object_content(
    options: OperationOptions,
    input_: capo_s3.types.select_object_content_request.SelectObjectContentRequest,
) -> tuple[
    capo_s3.types.select_object_content_output.SelectObjectContentOutput,
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


async def async_select_object_content(
    options: AsyncOperationOptions,
    input_: capo_s3.types.select_object_content_request.SelectObjectContentRequest,
) -> tuple[
    capo_s3.types.select_object_content_output.SelectObjectContentOutput,
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
