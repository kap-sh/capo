"""Generated from Smithy shape ``com.amazonaws.continuum#IssuePatchDelivery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.issue_patch_delivery_count
    import capo_continuum.types.issue_patch_delivery_failure_reasons
    import capo_continuum.types.issue_patch_delivery_status


class IssuePatchDelivery(TypedDict, closed=True):
    status: "capo_continuum.types.issue_patch_delivery_status.IssuePatchDeliveryStatus"
    """The overall result, in priority order: FAILED when any patch's destination delivery failed or exhausted its retries; otherwise PENDING while any is still in progress; otherwise SUCCEEDED when at least one was delivered; otherwise SKIPPED."""
    patch_count: (
        "capo_continuum.types.issue_patch_delivery_count.IssuePatchDeliveryCount"
    )
    """Number of the issue's patches that have a destination delivery."""
    succeeded_count: (
        "capo_continuum.types.issue_patch_delivery_count.IssuePatchDeliveryCount"
    )
    """Number of those patches delivered to their destination."""
    failed_count: (
        "capo_continuum.types.issue_patch_delivery_count.IssuePatchDeliveryCount"
    )
    """Number of those patches whose delivery failed or exhausted its retries."""
    failure_reasons: NotRequired[
        "capo_continuum.types.issue_patch_delivery_failure_reasons.IssuePatchDeliveryFailureReasons"
    ]
    """Distinct reasons of the failed deliveries, in ascending order. Present only when failedCount is greater than zero."""


# --- restJson1 ser/de ---
def serialize_json(value: IssuePatchDelivery) -> dict:
    out: dict = {}
    import capo_continuum.types.issue_patch_delivery_status

    out["status"] = capo_continuum.types.issue_patch_delivery_status.serialize_json(
        value["status"]
    )
    out["patchCount"] = value["patch_count"]
    out["succeededCount"] = value["succeeded_count"]
    out["failedCount"] = value["failed_count"]
    if "failure_reasons" in value:
        import capo_continuum.types.issue_patch_delivery_failure_reasons

        out["failureReasons"] = (
            capo_continuum.types.issue_patch_delivery_failure_reasons.serialize_json(
                value["failure_reasons"]
            )
        )
    return out


def deserialize_json(data: dict) -> IssuePatchDelivery:
    out: IssuePatchDelivery = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_continuum.types.issue_patch_delivery_status

        out["status"] = (
            capo_continuum.types.issue_patch_delivery_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_continuum.types.issue_patch_delivery_status.IssuePatchDeliveryStatus",
            "",
        )
    if data.get("patchCount") is not None:
        out["patch_count"] = data["patchCount"]
    else:
        out["patch_count"] = 0
    if data.get("succeededCount") is not None:
        out["succeeded_count"] = data["succeededCount"]
    else:
        out["succeeded_count"] = 0
    if data.get("failedCount") is not None:
        out["failed_count"] = data["failedCount"]
    else:
        out["failed_count"] = 0
    if data.get("failureReasons") is not None:
        import capo_continuum.types.issue_patch_delivery_failure_reasons

        out["failure_reasons"] = (
            capo_continuum.types.issue_patch_delivery_failure_reasons.deserialize_json(
                data["failureReasons"]
            )
        )
    return out
