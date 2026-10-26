"""Generated from Smithy shape ``com.amazonaws.glue#SearchMapFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.search_attribute
    import capo_glue.types.search_map_filter_value
    import capo_glue.types.search_map_key


class SearchMapFilter(TypedDict, closed=True):
    attribute: "capo_glue.types.search_attribute.SearchAttribute"
    """<p>The map attribute name to filter on.</p>"""
    key: "capo_glue.types.search_map_key.SearchMapKey"
    """<p>The key within the map attribute to filter on.</p>"""
    value: "capo_glue.types.search_map_filter_value.SearchMapFilterValue"
    """<p>The value to compare against.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchMapFilter) -> dict:
    out: dict = {}
    out["Attribute"] = value["attribute"]
    out["Key"] = value["key"]
    import capo_glue.types.search_map_filter_value

    out["Value"] = capo_glue.types.search_map_filter_value.serialize_aws_json_1_1(
        value["value"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchMapFilter:
    out: SearchMapFilter = {}  # type: ignore[typeddict-item]
    if data.get("Attribute") is not None:
        out["attribute"] = data["Attribute"]
    else:
        out["attribute"] = ""
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Value") is not None:
        import capo_glue.types.search_map_filter_value

        out["value"] = capo_glue.types.search_map_filter_value.deserialize_aws_json_1_1(
            data["Value"]
        )
    else:
        out["value"] = {"$unknown": {"name": ""}}
    return out
