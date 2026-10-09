"""Generated from Smithy shape ``com.amazonaws.s3#ListObjectsV2``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import capo_s3._auth._signers
import capo_s3._auth._sigv4
import capo_s3._protocol.eventstream
import capo_s3.errors.no_such_bucket
import capo_s3.types.common_prefix_list
import capo_s3.types.encoding_type
import capo_s3.types.list_objects_v2_output
import capo_s3.types.list_objects_v2_request
import capo_s3.types.object_list
import capo_s3.types.optional_object_attributes_list
import capo_s3.types.request_charged
import capo_s3.types.request_payer
from capo_s3._protocol.errors import find_error_element, parse_error_metadata
from capo_s3._protocol.xml import Element, fromstring
from capo_s3._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_s3._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_s3.errors import UnknownServiceError

STATUS_CODE_TO_CODE = {404: "NoSuchBucket"}


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
        case "NoSuchBucket":
            raise capo_s3.errors.no_such_bucket.NoSuchBucket.from_xml(error_el, message)
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_s3.types.list_objects_v2_output.ListObjectsV2Output:
    out: capo_s3.types.list_objects_v2_output.ListObjectsV2Output = (
        capo_s3.types.list_objects_v2_output.deserialize_xml(
            fromstring(response.read())
        )
    )
    if "x-amz-request-charged" in response.headers:
        out["request_charged"] = capo_s3.types.request_charged.from_xml_text(
            response.headers["x-amz-request-charged"]
        )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_s3.types.list_objects_v2_output.ListObjectsV2Output:
    out: capo_s3.types.list_objects_v2_output.ListObjectsV2Output = (
        capo_s3.types.list_objects_v2_output.deserialize_xml(
            fromstring(await response.aread())
        )
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
    input_: capo_s3.types.list_objects_v2_request.ListObjectsV2Request,
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
            Prefix=input_.get("prefix"),
            CopySource=options.copy_source,
            DisableAccessPoints=options.disable_access_points,
            DisableMultiRegionAccessPoints=options.disable_multi_region_access_points,
            UseArnRegion=options.use_arn_region,
            UseS3ExpressControlEndpoint=options.use_s3_express_control_endpoint,
            DisableS3ExpressSessionAuth=options.disable_s3_express_session_auth,
        )
    )  # noqa: F841
    import capo_s3.types.encoding_type
    import capo_s3.types.optional_object_attributes
    import capo_s3.types.request_payer

    url = endpoint.url.rstrip("/") + "?list-type=2"
    params: list[tuple[str, str]] = []
    if "delimiter" in input_:
        params.append(("delimiter", input_["delimiter"]))
    if "encoding_type" in input_:
        params.append(
            (
                "encoding-type",
                capo_s3.types.encoding_type.to_xml_text(input_["encoding_type"]),
            )
        )
    if "max_keys" in input_:
        params.append(("max-keys", str(input_["max_keys"])))
    if "prefix" in input_:
        params.append(("prefix", input_["prefix"]))
    if "continuation_token" in input_:
        params.append(("continuation-token", input_["continuation_token"]))
    if "fetch_owner" in input_:
        params.append(("fetch-owner", "true" if input_["fetch_owner"] else "false"))
    if "start_after" in input_:
        params.append(("start-after", input_["start_after"]))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "request_payer" in input_:
        headers["x-amz-request-payer"] = capo_s3.types.request_payer.to_xml_text(
            input_["request_payer"]
        )
    if "expected_bucket_owner" in input_:
        headers["x-amz-expected-bucket-owner"] = input_["expected_bucket_owner"]
    if "optional_object_attributes" in input_:
        headers["x-amz-optional-object-attributes"] = ", ".join(
            capo_s3.types.optional_object_attributes.to_xml_text(item)
            for item in input_["optional_object_attributes"]
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
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_objects_v2(
    options: OperationOptions,
    input_: capo_s3.types.list_objects_v2_request.ListObjectsV2Request,
) -> tuple[capo_s3.types.list_objects_v2_output.ListObjectsV2Output, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            raise_error(response, handle_error)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_list_objects_v2(
    options: AsyncOperationOptions,
    input_: capo_s3.types.list_objects_v2_request.ListObjectsV2Request,
) -> tuple[capo_s3.types.list_objects_v2_output.ListObjectsV2Output, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 300:
            await response.aread()
            raise_error(response, handle_error)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
