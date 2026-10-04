"""Generated from Smithy shape ``com.amazonaws.health#ServiceLifecycle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.lifecycle_event_list
    import capo_health.types.service
    import capo_health.types.string


class ServiceLifecycle(TypedDict, closed=True):
    service: NotRequired["capo_health.types.service.service"]
    """<p>The name of the Amazon Web Services service.</p>"""
    version: NotRequired["capo_health.types.string.string"]
    """<p>The version of the service.</p>"""
    title: NotRequired["capo_health.types.string.string"]
    """<p>A human-readable title for the lifecycle entry.</p>"""
    recommended_version: NotRequired["capo_health.types.string.string"]
    """<p>The recommended version to upgrade to.</p>"""
    lifecycle_events: NotRequired[
        "capo_health.types.lifecycle_event_list.LifecycleEventList"
    ]
    """<p>The list of lifecycle events for this service version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceLifecycle) -> dict:
    out: dict = {}
    if "service" in value:
        out["service"] = value["service"]
    if "version" in value:
        out["version"] = value["version"]
    if "title" in value:
        out["title"] = value["title"]
    if "recommended_version" in value:
        out["recommendedVersion"] = value["recommended_version"]
    if "lifecycle_events" in value:
        import capo_health.types.lifecycle_event_list

        out["lifecycleEvents"] = (
            capo_health.types.lifecycle_event_list.serialize_aws_json_1_1(
                value["lifecycle_events"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceLifecycle:
    out: ServiceLifecycle = {}  # type: ignore[typeddict-item]
    if data.get("service") is not None:
        out["service"] = data["service"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("recommendedVersion") is not None:
        out["recommended_version"] = data["recommendedVersion"]
    if data.get("lifecycleEvents") is not None:
        import capo_health.types.lifecycle_event_list

        out["lifecycle_events"] = (
            capo_health.types.lifecycle_event_list.deserialize_aws_json_1_1(
                data["lifecycleEvents"]
            )
        )
    return out
