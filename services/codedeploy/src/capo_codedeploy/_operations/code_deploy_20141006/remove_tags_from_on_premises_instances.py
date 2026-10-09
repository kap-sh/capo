"""Generated from Smithy shape ``com.amazonaws.codedeploy#RemoveTagsFromOnPremisesInstances``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_codedeploy._auth._signers
import capo_codedeploy._auth._sigv4
import capo_codedeploy._protocol.eventstream
import capo_codedeploy.errors.instance_limit_exceeded_exception
import capo_codedeploy.errors.instance_name_required_exception
import capo_codedeploy.errors.instance_not_registered_exception
import capo_codedeploy.errors.invalid_instance_name_exception
import capo_codedeploy.errors.invalid_tag_exception
import capo_codedeploy.errors.tag_limit_exceeded_exception
import capo_codedeploy.errors.tag_required_exception
import capo_codedeploy.types.instance_name_list
import capo_codedeploy.types.remove_tags_from_on_premises_instances_input
import capo_codedeploy.types.tag_list
from capo_codedeploy._protocol.errors import parse_error_metadata_json
from capo_codedeploy._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_codedeploy._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_codedeploy.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InstanceLimitExceededException":
            raise capo_codedeploy.errors.instance_limit_exceeded_exception.InstanceLimitExceededException.from_aws_json_1_1(
                data, message
            )
        case "InstanceNameRequiredException":
            raise capo_codedeploy.errors.instance_name_required_exception.InstanceNameRequiredException.from_aws_json_1_1(
                data, message
            )
        case "InstanceNotRegisteredException":
            raise capo_codedeploy.errors.instance_not_registered_exception.InstanceNotRegisteredException.from_aws_json_1_1(
                data, message
            )
        case "InvalidInstanceNameException":
            raise capo_codedeploy.errors.invalid_instance_name_exception.InvalidInstanceNameException.from_aws_json_1_1(
                data, message
            )
        case "InvalidTagException":
            raise capo_codedeploy.errors.invalid_tag_exception.InvalidTagException.from_aws_json_1_1(
                data, message
            )
        case "TagLimitExceededException":
            raise capo_codedeploy.errors.tag_limit_exceeded_exception.TagLimitExceededException.from_aws_json_1_1(
                data, message
            )
        case "TagRequiredException":
            raise capo_codedeploy.errors.tag_required_exception.TagRequiredException.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_codedeploy._auth._signers.Signer | None:
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
            sigv4_config = capo_codedeploy._auth._sigv4.build_sigv4_auth_scheme(
                "codedeploy", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_codedeploy._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_codedeploy.types.remove_tags_from_on_premises_instances_input.RemoveTagsFromOnPremisesInstancesInput,
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
    headers["X-Amz-Target"] = "CodeDeploy_20141006.RemoveTagsFromOnPremisesInstances"
    body: bytes | None = json.dumps(
        capo_codedeploy.types.remove_tags_from_on_premises_instances_input.serialize_aws_json_1_1(
            input_
        ),
        allow_nan=False,
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
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


def remove_tags_from_on_premises_instances(
    options: OperationOptions,
    input_: capo_codedeploy.types.remove_tags_from_on_premises_instances_input.RemoveTagsFromOnPremisesInstancesInput,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            raise_error(response, handle_error)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_remove_tags_from_on_premises_instances(
    options: AsyncOperationOptions,
    input_: capo_codedeploy.types.remove_tags_from_on_premises_instances_input.RemoveTagsFromOnPremisesInstancesInput,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 300:
            await response.aread()
            raise_error(response, handle_error)
        return None, response
    except BaseException:
        await response.aclose()
        raise
