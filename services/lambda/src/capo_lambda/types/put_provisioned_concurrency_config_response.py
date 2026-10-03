"""Generated from Smithy shape ``com.amazonaws.lambda#PutProvisionedConcurrencyConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.non_negative_integer
    import capo_lambda.types.positive_integer
    import capo_lambda.types.provisioned_concurrency_status_enum
    import capo_lambda.types.string
    import capo_lambda.types.timestamp


class PutProvisionedConcurrencyConfigResponse(TypedDict, closed=True):
    requested_provisioned_concurrent_executions: NotRequired[
        "capo_lambda.types.positive_integer.PositiveInteger"
    ]
    """<p>The amount of provisioned concurrency requested.</p>"""
    allocated_provisioned_concurrent_executions: NotRequired[
        "capo_lambda.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>The amount of provisioned concurrency allocated. When a weighted alias is used during linear and canary deployments, this value fluctuates depending on the amount of concurrency that is provisioned for the function versions.</p>"""
    available_provisioned_concurrent_executions: NotRequired[
        "capo_lambda.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>The amount of provisioned concurrency available.</p>"""
    status: NotRequired[
        "capo_lambda.types.provisioned_concurrency_status_enum.ProvisionedConcurrencyStatusEnum"
    ]
    """<p>The status of the allocation process.</p>"""
    status_reason: NotRequired["capo_lambda.types.string.String"]
    """<p>For failed allocations, the reason that provisioned concurrency could not be allocated.</p>"""
    last_modified: NotRequired["capo_lambda.types.timestamp.Timestamp"]
    """<p>The date and time that a user last updated the configuration, in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601 format</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutProvisionedConcurrencyConfigResponse) -> dict:
    out: dict = {}
    if "requested_provisioned_concurrent_executions" in value:
        out["RequestedProvisionedConcurrentExecutions"] = value[
            "requested_provisioned_concurrent_executions"
        ]
    if "allocated_provisioned_concurrent_executions" in value:
        out["AllocatedProvisionedConcurrentExecutions"] = value[
            "allocated_provisioned_concurrent_executions"
        ]
    if "available_provisioned_concurrent_executions" in value:
        out["AvailableProvisionedConcurrentExecutions"] = value[
            "available_provisioned_concurrent_executions"
        ]
    if "status" in value:
        import capo_lambda.types.provisioned_concurrency_status_enum

        out["Status"] = (
            capo_lambda.types.provisioned_concurrency_status_enum.serialize_json(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "last_modified" in value:
        out["LastModified"] = value["last_modified"]
    return out


def deserialize_json(data: dict) -> PutProvisionedConcurrencyConfigResponse:
    out: PutProvisionedConcurrencyConfigResponse = {}  # type: ignore[typeddict-item]
    if data.get("RequestedProvisionedConcurrentExecutions") is not None:
        out["requested_provisioned_concurrent_executions"] = data[
            "RequestedProvisionedConcurrentExecutions"
        ]
    if data.get("AllocatedProvisionedConcurrentExecutions") is not None:
        out["allocated_provisioned_concurrent_executions"] = data[
            "AllocatedProvisionedConcurrentExecutions"
        ]
    if data.get("AvailableProvisionedConcurrentExecutions") is not None:
        out["available_provisioned_concurrent_executions"] = data[
            "AvailableProvisionedConcurrentExecutions"
        ]
    if data.get("Status") is not None:
        import capo_lambda.types.provisioned_concurrency_status_enum

        out["status"] = (
            capo_lambda.types.provisioned_concurrency_status_enum.deserialize_json(
                data["Status"]
            )
        )
    if data.get("StatusReason") is not None:
        out["status_reason"] = data["StatusReason"]
    if data.get("LastModified") is not None:
        out["last_modified"] = data["LastModified"]
    return out
