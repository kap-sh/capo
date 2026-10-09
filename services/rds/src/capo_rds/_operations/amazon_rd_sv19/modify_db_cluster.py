"""Generated from Smithy shape ``com.amazonaws.rds#ModifyDBCluster``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import capo_rds._auth._signers
import capo_rds._auth._sigv4
import capo_rds._protocol.eventstream
import capo_rds.errors.db_cluster_already_exists_fault
import capo_rds.errors.db_cluster_not_found_fault
import capo_rds.errors.db_cluster_parameter_group_not_found_fault
import capo_rds.errors.db_instance_already_exists_fault
import capo_rds.errors.db_parameter_group_not_found_fault
import capo_rds.errors.db_subnet_group_not_found_fault
import capo_rds.errors.domain_not_found_fault
import capo_rds.errors.invalid_db_cluster_state_fault
import capo_rds.errors.invalid_db_instance_state_fault
import capo_rds.errors.invalid_db_security_group_state_fault
import capo_rds.errors.invalid_db_subnet_group_state_fault
import capo_rds.errors.invalid_global_cluster_state_fault
import capo_rds.errors.invalid_subnet
import capo_rds.errors.invalid_vpc_network_state_fault
import capo_rds.errors.kms_key_not_accessible_fault
import capo_rds.errors.network_type_not_supported
import capo_rds.errors.option_group_not_found_fault
import capo_rds.errors.storage_quota_exceeded_fault
import capo_rds.errors.storage_type_not_available_fault
import capo_rds.errors.storage_type_not_supported_fault
import capo_rds.errors.vpc_encryption_control_violation_exception
import capo_rds.types.cloudwatch_logs_export_configuration
import capo_rds.types.database_insights_mode
import capo_rds.types.db_cluster
import capo_rds.types.master_user_authentication_type
import capo_rds.types.modify_db_cluster_message
import capo_rds.types.modify_db_cluster_result
import capo_rds.types.scaling_configuration
import capo_rds.types.serverless_v2_scaling_configuration
import capo_rds.types.vpc_security_group_id_list
from capo_rds._protocol.errors import find_error_element, parse_error_metadata
from capo_rds._protocol.xml import fromstring
from capo_rds._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_rds._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_rds.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    error_el = find_error_element(root)
    match code:
        case "DBClusterAlreadyExistsFault":
            raise capo_rds.errors.db_cluster_already_exists_fault.DBClusterAlreadyExistsFault.from_query(
                error_el, message
            )
        case "DBClusterNotFoundFault":
            raise capo_rds.errors.db_cluster_not_found_fault.DBClusterNotFoundFault.from_query(
                error_el, message
            )
        case "DBClusterParameterGroupNotFound":
            raise capo_rds.errors.db_cluster_parameter_group_not_found_fault.DBClusterParameterGroupNotFoundFault.from_query(
                error_el, message
            )
        case "DBInstanceAlreadyExists":
            raise capo_rds.errors.db_instance_already_exists_fault.DBInstanceAlreadyExistsFault.from_query(
                error_el, message
            )
        case "DBParameterGroupNotFound":
            raise capo_rds.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault.from_query(
                error_el, message
            )
        case "DBSubnetGroupNotFoundFault":
            raise capo_rds.errors.db_subnet_group_not_found_fault.DBSubnetGroupNotFoundFault.from_query(
                error_el, message
            )
        case "DomainNotFoundFault":
            raise capo_rds.errors.domain_not_found_fault.DomainNotFoundFault.from_query(
                error_el, message
            )
        case "InvalidDBClusterStateFault":
            raise capo_rds.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault.from_query(
                error_el, message
            )
        case "InvalidDBInstanceState":
            raise capo_rds.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault.from_query(
                error_el, message
            )
        case "InvalidDBSecurityGroupState":
            raise capo_rds.errors.invalid_db_security_group_state_fault.InvalidDBSecurityGroupStateFault.from_query(
                error_el, message
            )
        case "InvalidDBSubnetGroupStateFault":
            raise capo_rds.errors.invalid_db_subnet_group_state_fault.InvalidDBSubnetGroupStateFault.from_query(
                error_el, message
            )
        case "InvalidGlobalClusterStateFault":
            raise capo_rds.errors.invalid_global_cluster_state_fault.InvalidGlobalClusterStateFault.from_query(
                error_el, message
            )
        case "InvalidSubnet":
            raise capo_rds.errors.invalid_subnet.InvalidSubnet.from_query(
                error_el, message
            )
        case "InvalidVPCNetworkStateFault":
            raise capo_rds.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault.from_query(
                error_el, message
            )
        case "KMSKeyNotAccessibleFault":
            raise capo_rds.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault.from_query(
                error_el, message
            )
        case "NetworkTypeNotSupported":
            raise capo_rds.errors.network_type_not_supported.NetworkTypeNotSupported.from_query(
                error_el, message
            )
        case "OptionGroupNotFoundFault":
            raise capo_rds.errors.option_group_not_found_fault.OptionGroupNotFoundFault.from_query(
                error_el, message
            )
        case "StorageQuotaExceeded":
            raise capo_rds.errors.storage_quota_exceeded_fault.StorageQuotaExceededFault.from_query(
                error_el, message
            )
        case "StorageTypeNotAvailableFault":
            raise capo_rds.errors.storage_type_not_available_fault.StorageTypeNotAvailableFault.from_query(
                error_el, message
            )
        case "StorageTypeNotSupported":
            raise capo_rds.errors.storage_type_not_supported_fault.StorageTypeNotSupportedFault.from_query(
                error_el, message
            )
        case "VpcEncryptionControlViolationException":
            raise capo_rds.errors.vpc_encryption_control_violation_exception.VpcEncryptionControlViolationException.from_query(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_rds.types.modify_db_cluster_result.ModifyDBClusterResult:
    root = fromstring(response.read())
    result = root.find("ModifyDBClusterResult")
    out: capo_rds.types.modify_db_cluster_result.ModifyDBClusterResult = (
        capo_rds.types.modify_db_cluster_result.deserialize_query(
            result if result is not None else root
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_rds.types.modify_db_cluster_result.ModifyDBClusterResult:
    root = fromstring(await response.aread())
    result = root.find("ModifyDBClusterResult")
    out: capo_rds.types.modify_db_cluster_result.ModifyDBClusterResult = (
        capo_rds.types.modify_db_cluster_result.deserialize_query(
            result if result is not None else root
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_rds._auth._signers.Signer | None:
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
            sigv4_config = capo_rds._auth._sigv4.build_sigv4_auth_scheme(
                "rds", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_rds._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_rds.types.modify_db_cluster_message.ModifyDBClusterMessage,
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
    pairs.append(("Action", "ModifyDBCluster"))
    pairs.append(("Version", "2014-10-31"))
    capo_rds.types.modify_db_cluster_message.serialize_query(input_, pairs, "")
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


def modify_db_cluster(
    options: OperationOptions,
    input_: capo_rds.types.modify_db_cluster_message.ModifyDBClusterMessage,
) -> tuple[
    capo_rds.types.modify_db_cluster_result.ModifyDBClusterResult, zapros.Response
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


async def async_modify_db_cluster(
    options: AsyncOperationOptions,
    input_: capo_rds.types.modify_db_cluster_message.ModifyDBClusterMessage,
) -> tuple[
    capo_rds.types.modify_db_cluster_result.ModifyDBClusterResult, zapros.Response
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
