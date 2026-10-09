"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#UpdateApplicationVersion``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import capo_elastic_beanstalk._auth._signers
import capo_elastic_beanstalk._auth._sigv4
import capo_elastic_beanstalk._protocol.eventstream
import capo_elastic_beanstalk.types.application_version_description
import capo_elastic_beanstalk.types.application_version_description_message
import capo_elastic_beanstalk.types.update_application_version_message
from capo_elastic_beanstalk._protocol.errors import parse_error_metadata
from capo_elastic_beanstalk._protocol.xml import (
    fromstring,
)
from capo_elastic_beanstalk._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_elastic_beanstalk._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_elastic_beanstalk.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_elastic_beanstalk.types.application_version_description_message.ApplicationVersionDescriptionMessage:
    root = fromstring(response.read())
    result = root.find("UpdateApplicationVersionResult")
    out: capo_elastic_beanstalk.types.application_version_description_message.ApplicationVersionDescriptionMessage = capo_elastic_beanstalk.types.application_version_description_message.deserialize_query(
        result if result is not None else root
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_elastic_beanstalk.types.application_version_description_message.ApplicationVersionDescriptionMessage:
    root = fromstring(await response.aread())
    result = root.find("UpdateApplicationVersionResult")
    out: capo_elastic_beanstalk.types.application_version_description_message.ApplicationVersionDescriptionMessage = capo_elastic_beanstalk.types.application_version_description_message.deserialize_query(
        result if result is not None else root
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_elastic_beanstalk._auth._signers.Signer | None:
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
            sigv4_config = capo_elastic_beanstalk._auth._sigv4.build_sigv4_auth_scheme(
                "elasticbeanstalk", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_elastic_beanstalk._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_elastic_beanstalk.types.update_application_version_message.UpdateApplicationVersionMessage,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    pairs: list[tuple[str, str]] = []
    pairs.append(("Action", "UpdateApplicationVersion"))
    pairs.append(("Version", "2010-12-01"))
    capo_elastic_beanstalk.types.update_application_version_message.serialize_query(
        input_, pairs, ""
    )
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
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


def update_application_version(
    options: OperationOptions,
    input_: capo_elastic_beanstalk.types.update_application_version_message.UpdateApplicationVersionMessage,
) -> tuple[
    capo_elastic_beanstalk.types.application_version_description_message.ApplicationVersionDescriptionMessage,
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


async def async_update_application_version(
    options: AsyncOperationOptions,
    input_: capo_elastic_beanstalk.types.update_application_version_message.UpdateApplicationVersionMessage,
) -> tuple[
    capo_elastic_beanstalk.types.application_version_description_message.ApplicationVersionDescriptionMessage,
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
