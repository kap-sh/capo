"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DependencyDiscoveryConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.dependency_discovery_status


class DependencyDiscoveryConfig(TypedDict, closed=True):
    status: "capo_resiliencehubv2.types.dependency_discovery_status.DependencyDiscoveryStatus"
    """<p>The current status of dependency discovery.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when dependency discovery was last updated.</p>"""
    eligible_resource_count: NotRequired["int"]
    """<p>The count of resources eligible for dependency attribution.</p>"""
    message: NotRequired["str"]
    """<p>A status message for dependency discovery, displayed during the initialization state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DependencyDiscoveryConfig) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.dependency_discovery_status

    out["status"] = (
        capo_resiliencehubv2.types.dependency_discovery_status.serialize_json(
            value["status"]
        )
    )
    if "updated_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updatedAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "eligible_resource_count" in value:
        out["eligibleResourceCount"] = value["eligible_resource_count"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DependencyDiscoveryConfig:
    out: DependencyDiscoveryConfig = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_resiliencehubv2.types.dependency_discovery_status

        out["status"] = (
            capo_resiliencehubv2.types.dependency_discovery_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_resiliencehubv2.types.dependency_discovery_status.DependencyDiscoveryStatus",
            "",
        )
    if data.get("updatedAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updated_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    if data.get("eligibleResourceCount") is not None:
        out["eligible_resource_count"] = data["eligibleResourceCount"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
