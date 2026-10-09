"""Generated from Smithy shape ``com.amazonaws.neptune#RestoreDBClusterFromSnapshot``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import capo_neptune._auth._signers
import capo_neptune._auth._sigv4
import capo_neptune._protocol.eventstream
import capo_neptune.errors.db_cluster_already_exists_fault
import capo_neptune.errors.db_cluster_parameter_group_not_found_fault
import capo_neptune.errors.db_cluster_quota_exceeded_fault
import capo_neptune.errors.db_cluster_snapshot_not_found_fault
import capo_neptune.errors.db_snapshot_not_found_fault
import capo_neptune.errors.db_subnet_group_not_found_fault
import capo_neptune.errors.insufficient_db_cluster_capacity_fault
import capo_neptune.errors.insufficient_storage_cluster_capacity_fault
import capo_neptune.errors.invalid_db_cluster_snapshot_state_fault
import capo_neptune.errors.invalid_db_snapshot_state_fault
import capo_neptune.errors.invalid_restore_fault
import capo_neptune.errors.invalid_subnet
import capo_neptune.errors.invalid_vpc_network_state_fault
import capo_neptune.errors.kms_key_not_accessible_fault
import capo_neptune.errors.network_type_not_supported_fault
import capo_neptune.errors.option_group_not_found_fault
import capo_neptune.errors.storage_quota_exceeded_fault
import capo_neptune.types.availability_zones
import capo_neptune.types.db_cluster
import capo_neptune.types.log_type_list
import capo_neptune.types.restore_db_cluster_from_snapshot_message
import capo_neptune.types.restore_db_cluster_from_snapshot_result
import capo_neptune.types.serverless_v2_scaling_configuration
import capo_neptune.types.tag_list
import capo_neptune.types.vpc_security_group_id_list
from capo_neptune._protocol.errors import find_error_element, parse_error_metadata
from capo_neptune._protocol.xml import fromstring
from capo_neptune._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_neptune._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_neptune.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    error_el = find_error_element(root)
    match code:
        case "DBClusterAlreadyExistsFault":
            raise capo_neptune.errors.db_cluster_already_exists_fault.DBClusterAlreadyExistsFault.from_query(
                error_el, message
            )
        case "DBClusterParameterGroupNotFound":
            raise capo_neptune.errors.db_cluster_parameter_group_not_found_fault.DBClusterParameterGroupNotFoundFault.from_query(
                error_el, message
            )
        case "DBClusterQuotaExceededFault":
            raise capo_neptune.errors.db_cluster_quota_exceeded_fault.DBClusterQuotaExceededFault.from_query(
                error_el, message
            )
        case "DBClusterSnapshotNotFoundFault":
            raise capo_neptune.errors.db_cluster_snapshot_not_found_fault.DBClusterSnapshotNotFoundFault.from_query(
                error_el, message
            )
        case "DBSnapshotNotFound":
            raise capo_neptune.errors.db_snapshot_not_found_fault.DBSnapshotNotFoundFault.from_query(
                error_el, message
            )
        case "DBSubnetGroupNotFoundFault":
            raise capo_neptune.errors.db_subnet_group_not_found_fault.DBSubnetGroupNotFoundFault.from_query(
                error_el, message
            )
        case "InsufficientDBClusterCapacityFault":
            raise capo_neptune.errors.insufficient_db_cluster_capacity_fault.InsufficientDBClusterCapacityFault.from_query(
                error_el, message
            )
        case "InsufficientStorageClusterCapacity":
            raise capo_neptune.errors.insufficient_storage_cluster_capacity_fault.InsufficientStorageClusterCapacityFault.from_query(
                error_el, message
            )
        case "InvalidDBClusterSnapshotStateFault":
            raise capo_neptune.errors.invalid_db_cluster_snapshot_state_fault.InvalidDBClusterSnapshotStateFault.from_query(
                error_el, message
            )
        case "InvalidDBSnapshotState":
            raise capo_neptune.errors.invalid_db_snapshot_state_fault.InvalidDBSnapshotStateFault.from_query(
                error_el, message
            )
        case "InvalidRestoreFault":
            raise capo_neptune.errors.invalid_restore_fault.InvalidRestoreFault.from_query(
                error_el, message
            )
        case "InvalidSubnet":
            raise capo_neptune.errors.invalid_subnet.InvalidSubnet.from_query(
                error_el, message
            )
        case "InvalidVPCNetworkStateFault":
            raise capo_neptune.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault.from_query(
                error_el, message
            )
        case "KMSKeyNotAccessibleFault":
            raise capo_neptune.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault.from_query(
                error_el, message
            )
        case "NetworkTypeNotSupported":
            raise capo_neptune.errors.network_type_not_supported_fault.NetworkTypeNotSupportedFault.from_query(
                error_el, message
            )
        case "OptionGroupNotFoundFault":
            raise capo_neptune.errors.option_group_not_found_fault.OptionGroupNotFoundFault.from_query(
                error_el, message
            )
        case "StorageQuotaExceeded":
            raise capo_neptune.errors.storage_quota_exceeded_fault.StorageQuotaExceededFault.from_query(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_neptune.types.restore_db_cluster_from_snapshot_result.RestoreDBClusterFromSnapshotResult:
    root = fromstring(response.read())
    result = root.find("RestoreDBClusterFromSnapshotResult")
    out: capo_neptune.types.restore_db_cluster_from_snapshot_result.RestoreDBClusterFromSnapshotResult = capo_neptune.types.restore_db_cluster_from_snapshot_result.deserialize_query(
        result if result is not None else root
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_neptune.types.restore_db_cluster_from_snapshot_result.RestoreDBClusterFromSnapshotResult:
    root = fromstring(await response.aread())
    result = root.find("RestoreDBClusterFromSnapshotResult")
    out: capo_neptune.types.restore_db_cluster_from_snapshot_result.RestoreDBClusterFromSnapshotResult = capo_neptune.types.restore_db_cluster_from_snapshot_result.deserialize_query(
        result if result is not None else root
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_neptune._auth._signers.Signer | None:
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
            sigv4_config = capo_neptune._auth._sigv4.build_sigv4_auth_scheme(
                "rds", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_neptune._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_neptune.types.restore_db_cluster_from_snapshot_message.RestoreDBClusterFromSnapshotMessage,
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
    pairs.append(("Action", "RestoreDBClusterFromSnapshot"))
    pairs.append(("Version", "2014-10-31"))
    capo_neptune.types.restore_db_cluster_from_snapshot_message.serialize_query(
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


def restore_db_cluster_from_snapshot(
    options: OperationOptions,
    input_: capo_neptune.types.restore_db_cluster_from_snapshot_message.RestoreDBClusterFromSnapshotMessage,
) -> tuple[
    capo_neptune.types.restore_db_cluster_from_snapshot_result.RestoreDBClusterFromSnapshotResult,
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


async def async_restore_db_cluster_from_snapshot(
    options: AsyncOperationOptions,
    input_: capo_neptune.types.restore_db_cluster_from_snapshot_message.RestoreDBClusterFromSnapshotMessage,
) -> tuple[
    capo_neptune.types.restore_db_cluster_from_snapshot_result.RestoreDBClusterFromSnapshotResult,
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
