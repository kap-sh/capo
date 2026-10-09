"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#Search``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_cloudsearch_domain._auth._signers
import capo_cloudsearch_domain._auth._sigv4
import capo_cloudsearch_domain._protocol.eventstream
import capo_cloudsearch_domain.errors.search_exception
import capo_cloudsearch_domain.types.facets
import capo_cloudsearch_domain.types.hits
import capo_cloudsearch_domain.types.query_parser
import capo_cloudsearch_domain.types.search_request
import capo_cloudsearch_domain.types.search_response
import capo_cloudsearch_domain.types.search_status
import capo_cloudsearch_domain.types.stats
from capo_cloudsearch_domain._protocol.errors import parse_error_metadata_json
from capo_cloudsearch_domain._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_cloudsearch_domain._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_cloudsearch_domain.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "SearchException":
            raise capo_cloudsearch_domain.errors.search_exception.SearchException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cloudsearch_domain.types.search_response.SearchResponse:
    out: capo_cloudsearch_domain.types.search_response.SearchResponse = (
        capo_cloudsearch_domain.types.search_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_cloudsearch_domain.types.search_response.SearchResponse:
    out: capo_cloudsearch_domain.types.search_response.SearchResponse = (
        capo_cloudsearch_domain.types.search_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_cloudsearch_domain._auth._signers.Signer | None:
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
            sigv4_config = capo_cloudsearch_domain._auth._sigv4.build_sigv4_auth_scheme(
                "cloudsearch", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_cloudsearch_domain._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_cloudsearch_domain.types.search_request.SearchRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_cloudsearch_domain.types.query_parser

    url = endpoint.url.rstrip("/") + "/2013-01-01/search?format=sdk&pretty=true"
    params: list[tuple[str, str]] = []
    if "cursor" in input_:
        params.append(("cursor", input_["cursor"]))
    if "expr" in input_:
        params.append(("expr", input_["expr"]))
    if "facet" in input_:
        params.append(("facet", input_["facet"]))
    if "filter_query" in input_:
        params.append(("fq", input_["filter_query"]))
    if "highlight" in input_:
        params.append(("highlight", input_["highlight"]))
    params.append(("partial", "true" if input_.get("partial", False) else "false"))
    if "query" in input_:
        params.append(("q", input_["query"]))
    if "query_options" in input_:
        params.append(("q.options", input_["query_options"]))
    if "query_parser" in input_:
        params.append(
            (
                "q.parser",
                capo_cloudsearch_domain.types.query_parser.serialize_json(
                    input_["query_parser"]
                ),
            )
        )
    if "return" in input_:
        params.append(("return", input_["return"]))
    params.append(("size", str(input_.get("size", 0))))
    if "sort" in input_:
        params.append(("sort", input_["sort"]))
    params.append(("start", str(input_.get("start", 0))))
    if "stats" in input_:
        params.append(("stats", input_["stats"]))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
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


def search(
    options: OperationOptions,
    input_: capo_cloudsearch_domain.types.search_request.SearchRequest,
) -> tuple[
    capo_cloudsearch_domain.types.search_response.SearchResponse, zapros.Response
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


async def async_search(
    options: AsyncOperationOptions,
    input_: capo_cloudsearch_domain.types.search_request.SearchRequest,
) -> tuple[
    capo_cloudsearch_domain.types.search_response.SearchResponse, zapros.Response
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
