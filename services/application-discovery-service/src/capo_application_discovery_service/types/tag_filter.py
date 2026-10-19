"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#TagFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.filter_name
    import capo_application_discovery_service.types.filter_values


class TagFilter(TypedDict, closed=True):
    name: "capo_application_discovery_service.types.filter_name.FilterName"
    """<p>A name of the tag filter.</p>"""
    values: "capo_application_discovery_service.types.filter_values.FilterValues"
    """<p>Values for the tag filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagFilter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_application_discovery_service.types.filter_values

    out["values"] = (
        capo_application_discovery_service.types.filter_values.serialize_aws_json_1_1(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagFilter:
    out: TagFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("values") is not None:
        import capo_application_discovery_service.types.filter_values

        out["values"] = (
            capo_application_discovery_service.types.filter_values.deserialize_aws_json_1_1(
                data["values"]
            )
        )
    else:
        out["values"] = []
    return out
