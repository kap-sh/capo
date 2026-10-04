"""Generated from Smithy shape ``com.amazonaws.health#ServiceLifecycleFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.service


class ServiceLifecycleFilter(TypedDict, closed=True):
    service: NotRequired["capo_health.types.service.service"]
    """<p>The Amazon Web Services service name to filter by.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceLifecycleFilter) -> dict:
    out: dict = {}
    if "service" in value:
        out["service"] = value["service"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceLifecycleFilter:
    out: ServiceLifecycleFilter = {}  # type: ignore[typeddict-item]
    if data.get("service") is not None:
        out["service"] = data["service"]
    return out
