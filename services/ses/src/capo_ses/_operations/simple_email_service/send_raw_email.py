"""Generated from Smithy shape ``com.amazonaws.ses#SendRawEmail``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import capo_ses._auth._signers
import capo_ses._auth._sigv4
import capo_ses._protocol.eventstream
import capo_ses.errors.account_sending_paused_exception
import capo_ses.errors.configuration_set_does_not_exist_exception
import capo_ses.errors.configuration_set_sending_paused_exception
import capo_ses.errors.mail_from_domain_not_verified_exception
import capo_ses.errors.message_rejected
import capo_ses.types.address_list
import capo_ses.types.message_tag_list
import capo_ses.types.raw_message
import capo_ses.types.send_raw_email_request
import capo_ses.types.send_raw_email_response
from capo_ses._protocol.errors import find_error_element, parse_error_metadata
from capo_ses._protocol.xml import fromstring
from capo_ses._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_ses._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_ses.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    error_el = find_error_element(root)
    match code:
        case "AccountSendingPausedException":
            raise capo_ses.errors.account_sending_paused_exception.AccountSendingPausedException.from_query(
                error_el, message
            )
        case "ConfigurationSetDoesNotExist":
            raise capo_ses.errors.configuration_set_does_not_exist_exception.ConfigurationSetDoesNotExistException.from_query(
                error_el, message
            )
        case "ConfigurationSetSendingPausedException":
            raise capo_ses.errors.configuration_set_sending_paused_exception.ConfigurationSetSendingPausedException.from_query(
                error_el, message
            )
        case "MailFromDomainNotVerifiedException":
            raise capo_ses.errors.mail_from_domain_not_verified_exception.MailFromDomainNotVerifiedException.from_query(
                error_el, message
            )
        case "MessageRejected":
            raise capo_ses.errors.message_rejected.MessageRejected.from_query(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_ses.types.send_raw_email_response.SendRawEmailResponse:
    root = fromstring(response.read())
    result = root.find("SendRawEmailResult")
    out: capo_ses.types.send_raw_email_response.SendRawEmailResponse = (
        capo_ses.types.send_raw_email_response.deserialize_query(
            result if result is not None else root
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_ses.types.send_raw_email_response.SendRawEmailResponse:
    root = fromstring(await response.aread())
    result = root.find("SendRawEmailResult")
    out: capo_ses.types.send_raw_email_response.SendRawEmailResponse = (
        capo_ses.types.send_raw_email_response.deserialize_query(
            result if result is not None else root
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_ses._auth._signers.Signer | None:
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
            sigv4_config = capo_ses._auth._sigv4.build_sigv4_auth_scheme(
                "ses", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_ses._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_ses.types.send_raw_email_request.SendRawEmailRequest,
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
    pairs.append(("Action", "SendRawEmail"))
    pairs.append(("Version", "2010-12-01"))
    capo_ses.types.send_raw_email_request.serialize_query(input_, pairs, "")
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


def send_raw_email(
    options: OperationOptions,
    input_: capo_ses.types.send_raw_email_request.SendRawEmailRequest,
) -> tuple[
    capo_ses.types.send_raw_email_response.SendRawEmailResponse, zapros.Response
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


async def async_send_raw_email(
    options: AsyncOperationOptions,
    input_: capo_ses.types.send_raw_email_request.SendRawEmailRequest,
) -> tuple[
    capo_ses.types.send_raw_email_response.SendRawEmailResponse, zapros.Response
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
