"""Generated from Smithy shape ``com.amazonaws.docdb#CreateDBCluster``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import capo_docdb._auth._signers
import capo_docdb._auth._sigv4
import capo_docdb._protocol.eventstream
import capo_docdb.errors.db_cluster_already_exists_fault
import capo_docdb.errors.db_cluster_not_found_fault
import capo_docdb.errors.db_cluster_parameter_group_not_found_fault
import capo_docdb.errors.db_cluster_quota_exceeded_fault
import capo_docdb.errors.db_instance_not_found_fault
import capo_docdb.errors.db_subnet_group_does_not_cover_enough_a_zs
import capo_docdb.errors.db_subnet_group_not_found_fault
import capo_docdb.errors.global_cluster_not_found_fault
import capo_docdb.errors.insufficient_storage_cluster_capacity_fault
import capo_docdb.errors.invalid_db_cluster_state_fault
import capo_docdb.errors.invalid_db_instance_state_fault
import capo_docdb.errors.invalid_db_subnet_group_state_fault
import capo_docdb.errors.invalid_global_cluster_state_fault
import capo_docdb.errors.invalid_subnet
import capo_docdb.errors.invalid_vpc_network_state_fault
import capo_docdb.errors.kms_key_not_accessible_fault
import capo_docdb.errors.network_type_not_supported
import capo_docdb.errors.storage_quota_exceeded_fault
import capo_docdb.types.availability_zones
import capo_docdb.types.create_db_cluster_message
import capo_docdb.types.create_db_cluster_result
import capo_docdb.types.db_cluster
import capo_docdb.types.log_type_list
import capo_docdb.types.serverless_v2_scaling_configuration
import capo_docdb.types.tag_list
import capo_docdb.types.vpc_security_group_id_list
from capo_docdb._protocol.errors import find_error_element, parse_error_metadata
from capo_docdb._protocol.xml import fromstring
from capo_docdb._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_docdb._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_docdb.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    error_el = find_error_element(root)
    match code:
        case "DBClusterAlreadyExistsFault":
            raise capo_docdb.errors.db_cluster_already_exists_fault.DBClusterAlreadyExistsFault.from_query(
                error_el, message
            )
        case "DBClusterNotFoundFault":
            raise capo_docdb.errors.db_cluster_not_found_fault.DBClusterNotFoundFault.from_query(
                error_el, message
            )
        case "DBClusterParameterGroupNotFound":
            raise capo_docdb.errors.db_cluster_parameter_group_not_found_fault.DBClusterParameterGroupNotFoundFault.from_query(
                error_el, message
            )
        case "DBClusterQuotaExceededFault":
            raise capo_docdb.errors.db_cluster_quota_exceeded_fault.DBClusterQuotaExceededFault.from_query(
                error_el, message
            )
        case "DBInstanceNotFound":
            raise capo_docdb.errors.db_instance_not_found_fault.DBInstanceNotFoundFault.from_query(
                error_el, message
            )
        case "DBSubnetGroupDoesNotCoverEnoughAZs":
            raise capo_docdb.errors.db_subnet_group_does_not_cover_enough_a_zs.DBSubnetGroupDoesNotCoverEnoughAZs.from_query(
                error_el, message
            )
        case "DBSubnetGroupNotFoundFault":
            raise capo_docdb.errors.db_subnet_group_not_found_fault.DBSubnetGroupNotFoundFault.from_query(
                error_el, message
            )
        case "GlobalClusterNotFoundFault":
            raise capo_docdb.errors.global_cluster_not_found_fault.GlobalClusterNotFoundFault.from_query(
                error_el, message
            )
        case "InsufficientStorageClusterCapacity":
            raise capo_docdb.errors.insufficient_storage_cluster_capacity_fault.InsufficientStorageClusterCapacityFault.from_query(
                error_el, message
            )
        case "InvalidDBClusterStateFault":
            raise capo_docdb.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault.from_query(
                error_el, message
            )
        case "InvalidDBInstanceState":
            raise capo_docdb.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault.from_query(
                error_el, message
            )
        case "InvalidDBSubnetGroupStateFault":
            raise capo_docdb.errors.invalid_db_subnet_group_state_fault.InvalidDBSubnetGroupStateFault.from_query(
                error_el, message
            )
        case "InvalidGlobalClusterStateFault":
            raise capo_docdb.errors.invalid_global_cluster_state_fault.InvalidGlobalClusterStateFault.from_query(
                error_el, message
            )
        case "InvalidSubnet":
            raise capo_docdb.errors.invalid_subnet.InvalidSubnet.from_query(
                error_el, message
            )
        case "InvalidVPCNetworkStateFault":
            raise capo_docdb.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault.from_query(
                error_el, message
            )
        case "KMSKeyNotAccessibleFault":
            raise capo_docdb.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault.from_query(
                error_el, message
            )
        case "NetworkTypeNotSupported":
            raise capo_docdb.errors.network_type_not_supported.NetworkTypeNotSupported.from_query(
                error_el, message
            )
        case "StorageQuotaExceeded":
            raise capo_docdb.errors.storage_quota_exceeded_fault.StorageQuotaExceededFault.from_query(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_docdb.types.create_db_cluster_result.CreateDBClusterResult:
    root = fromstring(response.read())
    result = root.find("CreateDBClusterResult")
    out: capo_docdb.types.create_db_cluster_result.CreateDBClusterResult = (
        capo_docdb.types.create_db_cluster_result.deserialize_query(
            result if result is not None else root
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_docdb.types.create_db_cluster_result.CreateDBClusterResult:
    root = fromstring(await response.aread())
    result = root.find("CreateDBClusterResult")
    out: capo_docdb.types.create_db_cluster_result.CreateDBClusterResult = (
        capo_docdb.types.create_db_cluster_result.deserialize_query(
            result if result is not None else root
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_docdb._auth._signers.Signer | None:
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
            sigv4_config = capo_docdb._auth._sigv4.build_sigv4_auth_scheme(
                "rds", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_docdb._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_docdb.types.create_db_cluster_message.CreateDBClusterMessage,
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
    pairs.append(("Action", "CreateDBCluster"))
    pairs.append(("Version", "2014-10-31"))
    capo_docdb.types.create_db_cluster_message.serialize_query(input_, pairs, "")
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


def create_db_cluster(
    options: OperationOptions,
    input_: capo_docdb.types.create_db_cluster_message.CreateDBClusterMessage,
) -> tuple[
    capo_docdb.types.create_db_cluster_result.CreateDBClusterResult, zapros.Response
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


async def async_create_db_cluster(
    options: AsyncOperationOptions,
    input_: capo_docdb.types.create_db_cluster_message.CreateDBClusterMessage,
) -> tuple[
    capo_docdb.types.create_db_cluster_result.CreateDBClusterResult, zapros.Response
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
