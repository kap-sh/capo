"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ListMarketplaceRevenueShares``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import capo_partnercentral_revenue_measurement._auth._signers
import capo_partnercentral_revenue_measurement._auth._sigv4
import capo_partnercentral_revenue_measurement._protocol.eventstream
import capo_partnercentral_revenue_measurement.errors.access_denied_exception
import capo_partnercentral_revenue_measurement.errors.internal_server_exception
import capo_partnercentral_revenue_measurement.errors.throttling_exception
import capo_partnercentral_revenue_measurement.errors.validation_exception
import capo_partnercentral_revenue_measurement.types.catalog_name
import capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_shares_input
import capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_shares_output
import capo_partnercentral_revenue_measurement.types.marketplace_product_id_list
import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_sort_by
import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_summary_list
import capo_partnercentral_revenue_measurement.types.product_code_list
import capo_partnercentral_revenue_measurement.types.sort_order
from capo_partnercentral_revenue_measurement._protocol import cbor
from capo_partnercentral_revenue_measurement._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_partnercentral_revenue_measurement._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_partnercentral_revenue_measurement.errors import (
    UnknownServiceError,
)


def handle_error(response: zapros.Response) -> Never:
    data, code, message = cbor.parse_error(response)
    match code:
        case "AccessDeniedException":
            raise capo_partnercentral_revenue_measurement.errors.access_denied_exception.AccessDeniedException.from_cbor(
                data, message
            )
        case "InternalServerException":
            raise capo_partnercentral_revenue_measurement.errors.internal_server_exception.InternalServerException.from_cbor(
                data, message
            )
        case "ThrottlingException":
            raise capo_partnercentral_revenue_measurement.errors.throttling_exception.ThrottlingException.from_cbor(
                data, message
            )
        case "ValidationException":
            raise capo_partnercentral_revenue_measurement.errors.validation_exception.ValidationException.from_cbor(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_shares_output.ListMarketplaceRevenueSharesOutput:
    out: capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_shares_output.ListMarketplaceRevenueSharesOutput = capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_shares_output.deserialize_cbor(
        cbor.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_shares_output.ListMarketplaceRevenueSharesOutput:
    out: capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_shares_output.ListMarketplaceRevenueSharesOutput = capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_shares_output.deserialize_cbor(
        cbor.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_partnercentral_revenue_measurement._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if (
        options.credentials_provider is not None
        and name_to_schema
        and not name_to_schema.keys() & {"sigv4a", "sigv4", "sigv4-s3express"}
    ):
        raise RuntimeError(
            "Endpoint requires an unsupported auth scheme: " + ", ".join(name_to_schema)
        )
    if options.credentials_provider is not None:
        sigv4_config = name_to_schema.get("sigv4a")
        if sigv4_config is not None:
            return capo_partnercentral_revenue_measurement._auth._signers.SigV4ASigner(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    if options.credentials_provider is not None:
        endpoint_scheme = name_to_schema.get("sigv4") or name_to_schema.get(
            "sigv4-s3express"
        )
        if endpoint_scheme is not None or not name_to_schema:
            sigv4_config = capo_partnercentral_revenue_measurement._auth._sigv4.build_sigv4_auth_scheme(
                "partnercentral", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return (
                    capo_partnercentral_revenue_measurement._auth._signers.SigV4Signer(
                        options.credentials_provider, auth_scheme=sigv4_config
                    )
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_shares_input.ListMarketplaceRevenueSharesInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/service/PartnerCentralRevenueMeasurement/operation/ListMarketplaceRevenueShares"
    )
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["smithy-protocol"] = "rpc-v2-cbor"
    headers["accept"] = "application/cbor"
    body: bytes | None = cbor.dumps(
        capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_shares_input.serialize_cbor(
            input_
        )
    )
    headers["content-type"] = "application/cbor"
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


def list_marketplace_revenue_shares(
    options: OperationOptions,
    input_: capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_shares_input.ListMarketplaceRevenueSharesInput,
) -> tuple[
    capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_shares_output.ListMarketplaceRevenueSharesOutput,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if (
            response.status != 200
            or response.headers.get("smithy-protocol") != "rpc-v2-cbor"
        ):
            response.read()
            raise_error(response, handle_error)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_list_marketplace_revenue_shares(
    options: AsyncOperationOptions,
    input_: capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_shares_input.ListMarketplaceRevenueSharesInput,
) -> tuple[
    capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_shares_output.ListMarketplaceRevenueSharesOutput,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if (
            response.status != 200
            or response.headers.get("smithy-protocol") != "rpc-v2-cbor"
        ):
            await response.aread()
            raise_error(response, handle_error)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
