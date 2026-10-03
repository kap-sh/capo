"""Generated from Smithy shape ``com.amazonaws.proton#ListServiceInstancesFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.list_service_instances_filter_by
    import capo_proton.types.list_service_instances_filter_value


class ListServiceInstancesFilter(TypedDict, closed=True):
    key: NotRequired[
        "capo_proton.types.list_service_instances_filter_by.ListServiceInstancesFilterBy"
    ]
    """<p>The name of a filtering criterion.</p>"""
    value: NotRequired[
        "capo_proton.types.list_service_instances_filter_value.ListServiceInstancesFilterValue"
    ]
    """<p>A value to filter by.</p> <p>With the date/time keys (<code>*At{Before,After}</code>), the value is a valid <a href="https://datatracker.ietf.org/doc/html/rfc3339.html">RFC 3339</a> string with no UTC offset and with an optional fractional precision (for example, <code>1985-04-12T23:20:50.52Z</code>).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListServiceInstancesFilter) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListServiceInstancesFilter:
    out: ListServiceInstancesFilter = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out
