"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdateProvisioningPreferences``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.stack_set_accounts
    import capo_service_catalog.types.stack_set_failure_tolerance_count
    import capo_service_catalog.types.stack_set_failure_tolerance_percentage
    import capo_service_catalog.types.stack_set_max_concurrency_count
    import capo_service_catalog.types.stack_set_max_concurrency_percentage
    import capo_service_catalog.types.stack_set_operation_type
    import capo_service_catalog.types.stack_set_regions


class UpdateProvisioningPreferences(TypedDict, closed=True):
    stack_set_accounts: NotRequired[
        "capo_service_catalog.types.stack_set_accounts.StackSetAccounts"
    ]
    """<p>One or more Amazon Web Services accounts that will have access to the provisioned product.</p> <p>Applicable only to a <code>CFN_STACKSET</code> provisioned product type.</p> <p>The Amazon Web Services accounts specified should be within the list of accounts in the <code>STACKSET</code> constraint. To get the list of accounts in the <code>STACKSET</code> constraint, use the <code>DescribeProvisioningParameters</code> operation.</p> <p>If no values are specified, the default value is all accounts from the <code>STACKSET</code> constraint.</p>"""
    stack_set_regions: NotRequired[
        "capo_service_catalog.types.stack_set_regions.StackSetRegions"
    ]
    """<p>One or more Amazon Web Services Regions where the provisioned product will be available.</p> <p>Applicable only to a <code>CFN_STACKSET</code> provisioned product type.</p> <p>The specified Regions should be within the list of Regions from the <code>STACKSET</code> constraint. To get the list of Regions in the <code>STACKSET</code> constraint, use the <code>DescribeProvisioningParameters</code> operation.</p> <p>If no values are specified, the default value is all Regions from the <code>STACKSET</code> constraint.</p>"""
    stack_set_failure_tolerance_count: NotRequired[
        "capo_service_catalog.types.stack_set_failure_tolerance_count.StackSetFailureToleranceCount"
    ]
    """<p>The number of accounts, per Region, for which this operation can fail before Service Catalog stops the operation in that Region. If the operation is stopped in a Region, Service Catalog doesn't attempt the operation in any subsequent Regions.</p> <p>Applicable only to a <code>CFN_STACKSET</code> provisioned product type.</p> <p>Conditional: You must specify either <code>StackSetFailureToleranceCount</code> or <code>StackSetFailureTolerancePercentage</code>, but not both.</p> <p>The default value is <code>0</code> if no value is specified.</p>"""
    stack_set_failure_tolerance_percentage: NotRequired[
        "capo_service_catalog.types.stack_set_failure_tolerance_percentage.StackSetFailureTolerancePercentage"
    ]
    """<p>The percentage of accounts, per Region, for which this stack operation can fail before Service Catalog stops the operation in that Region. If the operation is stopped in a Region, Service Catalog doesn't attempt the operation in any subsequent Regions.</p> <p>When calculating the number of accounts based on the specified percentage, Service Catalog rounds down to the next whole number.</p> <p>Applicable only to a <code>CFN_STACKSET</code> provisioned product type.</p> <p>Conditional: You must specify either <code>StackSetFailureToleranceCount</code> or <code>StackSetFailureTolerancePercentage</code>, but not both.</p>"""
    stack_set_max_concurrency_count: NotRequired[
        "capo_service_catalog.types.stack_set_max_concurrency_count.StackSetMaxConcurrencyCount"
    ]
    """<p>The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of <code>StackSetFailureToleranceCount</code>. <code>StackSetMaxConcurrentCount</code> is at most one more than the <code>StackSetFailureToleranceCount</code>.</p> <p>Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.</p> <p>Applicable only to a <code>CFN_STACKSET</code> provisioned product type.</p> <p>Conditional: You must specify either <code>StackSetMaxConcurrentCount</code> or <code>StackSetMaxConcurrentPercentage</code>, but not both.</p>"""
    stack_set_max_concurrency_percentage: NotRequired[
        "capo_service_catalog.types.stack_set_max_concurrency_percentage.StackSetMaxConcurrencyPercentage"
    ]
    """<p>The maximum percentage of accounts in which to perform this operation at one time.</p> <p>When calculating the number of accounts based on the specified percentage, Service Catalog rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, Service Catalog sets the number as <code>1</code> instead.</p> <p>Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.</p> <p>Applicable only to a <code>CFN_STACKSET</code> provisioned product type.</p> <p>Conditional: You must specify either <code>StackSetMaxConcurrentCount</code> or <code>StackSetMaxConcurrentPercentage</code>, but not both.</p>"""
    stack_set_operation_type: NotRequired[
        "capo_service_catalog.types.stack_set_operation_type.StackSetOperationType"
    ]
    """<p>Determines what action Service Catalog performs to a stack set or a stack instance represented by the provisioned product. The default value is <code>UPDATE</code> if nothing is specified.</p> <p>Applicable only to a <code>CFN_STACKSET</code> provisioned product type.</p> <dl> <dt>CREATE</dt> <dd> <p>Creates a new stack instance in the stack set represented by the provisioned product. In this case, only new stack instances are created based on accounts and Regions; if new ProductId or ProvisioningArtifactID are passed, they will be ignored.</p> </dd> <dt>UPDATE</dt> <dd> <p>Updates the stack set represented by the provisioned product and also its stack instances.</p> </dd> <dt>DELETE</dt> <dd> <p>Deletes a stack instance in the stack set represented by the provisioned product.</p> </dd> </dl>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProvisioningPreferences) -> dict:
    out: dict = {}
    if "stack_set_accounts" in value:
        import capo_service_catalog.types.stack_set_accounts

        out["StackSetAccounts"] = (
            capo_service_catalog.types.stack_set_accounts.serialize_aws_json_1_1(
                value["stack_set_accounts"]
            )
        )
    if "stack_set_regions" in value:
        import capo_service_catalog.types.stack_set_regions

        out["StackSetRegions"] = (
            capo_service_catalog.types.stack_set_regions.serialize_aws_json_1_1(
                value["stack_set_regions"]
            )
        )
    if "stack_set_failure_tolerance_count" in value:
        out["StackSetFailureToleranceCount"] = value[
            "stack_set_failure_tolerance_count"
        ]
    if "stack_set_failure_tolerance_percentage" in value:
        out["StackSetFailureTolerancePercentage"] = value[
            "stack_set_failure_tolerance_percentage"
        ]
    if "stack_set_max_concurrency_count" in value:
        out["StackSetMaxConcurrencyCount"] = value["stack_set_max_concurrency_count"]
    if "stack_set_max_concurrency_percentage" in value:
        out["StackSetMaxConcurrencyPercentage"] = value[
            "stack_set_max_concurrency_percentage"
        ]
    if "stack_set_operation_type" in value:
        import capo_service_catalog.types.stack_set_operation_type

        out["StackSetOperationType"] = (
            capo_service_catalog.types.stack_set_operation_type.serialize_aws_json_1_1(
                value["stack_set_operation_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProvisioningPreferences:
    out: UpdateProvisioningPreferences = {}  # type: ignore[typeddict-item]
    if data.get("StackSetAccounts") is not None:
        import capo_service_catalog.types.stack_set_accounts

        out["stack_set_accounts"] = (
            capo_service_catalog.types.stack_set_accounts.deserialize_aws_json_1_1(
                data["StackSetAccounts"]
            )
        )
    if data.get("StackSetRegions") is not None:
        import capo_service_catalog.types.stack_set_regions

        out["stack_set_regions"] = (
            capo_service_catalog.types.stack_set_regions.deserialize_aws_json_1_1(
                data["StackSetRegions"]
            )
        )
    if data.get("StackSetFailureToleranceCount") is not None:
        out["stack_set_failure_tolerance_count"] = data["StackSetFailureToleranceCount"]
    if data.get("StackSetFailureTolerancePercentage") is not None:
        out["stack_set_failure_tolerance_percentage"] = data[
            "StackSetFailureTolerancePercentage"
        ]
    if data.get("StackSetMaxConcurrencyCount") is not None:
        out["stack_set_max_concurrency_count"] = data["StackSetMaxConcurrencyCount"]
    if data.get("StackSetMaxConcurrencyPercentage") is not None:
        out["stack_set_max_concurrency_percentage"] = data[
            "StackSetMaxConcurrencyPercentage"
        ]
    if data.get("StackSetOperationType") is not None:
        import capo_service_catalog.types.stack_set_operation_type

        out["stack_set_operation_type"] = (
            capo_service_catalog.types.stack_set_operation_type.deserialize_aws_json_1_1(
                data["StackSetOperationType"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateProvisioningPreferences) -> dict:
    out: dict = {}
    if "stack_set_accounts" in value:
        import capo_service_catalog.types.stack_set_accounts

        out["StackSetAccounts"] = (
            capo_service_catalog.types.stack_set_accounts.serialize_cbor(
                value["stack_set_accounts"]
            )
        )
    if "stack_set_regions" in value:
        import capo_service_catalog.types.stack_set_regions

        out["StackSetRegions"] = (
            capo_service_catalog.types.stack_set_regions.serialize_cbor(
                value["stack_set_regions"]
            )
        )
    if "stack_set_failure_tolerance_count" in value:
        out["StackSetFailureToleranceCount"] = value[
            "stack_set_failure_tolerance_count"
        ]
    if "stack_set_failure_tolerance_percentage" in value:
        out["StackSetFailureTolerancePercentage"] = value[
            "stack_set_failure_tolerance_percentage"
        ]
    if "stack_set_max_concurrency_count" in value:
        out["StackSetMaxConcurrencyCount"] = value["stack_set_max_concurrency_count"]
    if "stack_set_max_concurrency_percentage" in value:
        out["StackSetMaxConcurrencyPercentage"] = value[
            "stack_set_max_concurrency_percentage"
        ]
    if "stack_set_operation_type" in value:
        import capo_service_catalog.types.stack_set_operation_type

        out["StackSetOperationType"] = (
            capo_service_catalog.types.stack_set_operation_type.serialize_cbor(
                value["stack_set_operation_type"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UpdateProvisioningPreferences:
    out: UpdateProvisioningPreferences = {}  # type: ignore[typeddict-item]
    if data.get("StackSetAccounts") is not None:
        import capo_service_catalog.types.stack_set_accounts

        out["stack_set_accounts"] = (
            capo_service_catalog.types.stack_set_accounts.deserialize_cbor(
                data["StackSetAccounts"]
            )
        )
    if data.get("StackSetRegions") is not None:
        import capo_service_catalog.types.stack_set_regions

        out["stack_set_regions"] = (
            capo_service_catalog.types.stack_set_regions.deserialize_cbor(
                data["StackSetRegions"]
            )
        )
    if data.get("StackSetFailureToleranceCount") is not None:
        out["stack_set_failure_tolerance_count"] = data["StackSetFailureToleranceCount"]
    if data.get("StackSetFailureTolerancePercentage") is not None:
        out["stack_set_failure_tolerance_percentage"] = data[
            "StackSetFailureTolerancePercentage"
        ]
    if data.get("StackSetMaxConcurrencyCount") is not None:
        out["stack_set_max_concurrency_count"] = data["StackSetMaxConcurrencyCount"]
    if data.get("StackSetMaxConcurrencyPercentage") is not None:
        out["stack_set_max_concurrency_percentage"] = data[
            "StackSetMaxConcurrencyPercentage"
        ]
    if data.get("StackSetOperationType") is not None:
        import capo_service_catalog.types.stack_set_operation_type

        out["stack_set_operation_type"] = (
            capo_service_catalog.types.stack_set_operation_type.deserialize_cbor(
                data["StackSetOperationType"]
            )
        )
    return out
