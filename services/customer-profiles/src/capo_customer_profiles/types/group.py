"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Group``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.dimension_list
    import capo_customer_profiles.types.include_options
    import capo_customer_profiles.types.source_segment_list


class Group(TypedDict, closed=True):
    dimensions: NotRequired["capo_customer_profiles.types.dimension_list.DimensionList"]
    """<p>Defines the attributes to segment on.</p>"""
    source_segments: NotRequired[
        "capo_customer_profiles.types.source_segment_list.SourceSegmentList"
    ]
    """<p>Defines the starting source of data.</p>"""
    source_type: "capo_customer_profiles.types.include_options.IncludeOptions"
    """<p>Defines how to interact with the source data.</p>"""
    type: "capo_customer_profiles.types.include_options.IncludeOptions"
    """<p>Defines how to interact with the profiles found in the current filtering.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Group) -> dict:
    out: dict = {}
    if "dimensions" in value:
        import capo_customer_profiles.types.dimension_list

        out["Dimensions"] = capo_customer_profiles.types.dimension_list.serialize_json(
            value["dimensions"]
        )
    if "source_segments" in value:
        import capo_customer_profiles.types.source_segment_list

        out["SourceSegments"] = (
            capo_customer_profiles.types.source_segment_list.serialize_json(
                value["source_segments"]
            )
        )
    import capo_customer_profiles.types.include_options

    out["SourceType"] = capo_customer_profiles.types.include_options.serialize_json(
        value.get("source_type", "ALL")
    )
    import capo_customer_profiles.types.include_options

    out["Type"] = capo_customer_profiles.types.include_options.serialize_json(
        value.get("type", "ALL")
    )
    return out


def deserialize_json(data: dict) -> Group:
    out: Group = {}  # type: ignore[typeddict-item]
    if data.get("Dimensions") is not None:
        import capo_customer_profiles.types.dimension_list

        out["dimensions"] = (
            capo_customer_profiles.types.dimension_list.deserialize_json(
                data["Dimensions"]
            )
        )
    if data.get("SourceSegments") is not None:
        import capo_customer_profiles.types.source_segment_list

        out["source_segments"] = (
            capo_customer_profiles.types.source_segment_list.deserialize_json(
                data["SourceSegments"]
            )
        )
    if data.get("SourceType") is not None:
        import capo_customer_profiles.types.include_options

        out["source_type"] = (
            capo_customer_profiles.types.include_options.deserialize_json(
                data["SourceType"]
            )
        )
    else:
        out["source_type"] = "ALL"
    if data.get("Type") is not None:
        import capo_customer_profiles.types.include_options

        out["type"] = capo_customer_profiles.types.include_options.deserialize_json(
            data["Type"]
        )
    else:
        out["type"] = "ALL"
    return out


def redact_sensitive(value: Group) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "dimensions" in value:
        import capo_customer_profiles.types.dimension_list

        out["dimensions"] = (
            capo_customer_profiles.types.dimension_list.redact_sensitive(
                value["dimensions"]
            )
        )
    return out
