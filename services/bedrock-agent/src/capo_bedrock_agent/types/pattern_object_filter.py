"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PatternObjectFilter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.filter_list
    import capo_bedrock_agent.types.filtered_object_type


class PatternObjectFilter(TypedDict, closed=True):
    object_type: "capo_bedrock_agent.types.filtered_object_type.FilteredObjectType"
    """<p>The supported object type or content type of the data source.</p>"""
    inclusion_filters: NotRequired["capo_bedrock_agent.types.filter_list.FilterList"]
    """<p>A list of one or more inclusion regular expression patterns to include certain object types that adhere to the pattern. If you specify an inclusion and exclusion filter/pattern and both match a document, the exclusion filter takes precedence and the document isn’t crawled.</p>"""
    exclusion_filters: NotRequired["capo_bedrock_agent.types.filter_list.FilterList"]
    """<p>A list of one or more exclusion regular expression patterns to exclude certain object types that adhere to the pattern. If you specify an inclusion and exclusion filter/pattern and both match a document, the exclusion filter takes precedence and the document isn’t crawled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PatternObjectFilter) -> dict:
    out: dict = {}
    out["objectType"] = value["object_type"]
    if "inclusion_filters" in value:
        import capo_bedrock_agent.types.filter_list

        out["inclusionFilters"] = capo_bedrock_agent.types.filter_list.serialize_json(
            value["inclusion_filters"]
        )
    if "exclusion_filters" in value:
        import capo_bedrock_agent.types.filter_list

        out["exclusionFilters"] = capo_bedrock_agent.types.filter_list.serialize_json(
            value["exclusion_filters"]
        )
    return out


def deserialize_json(data: dict) -> PatternObjectFilter:
    out: PatternObjectFilter = {}  # type: ignore[typeddict-item]
    if data.get("objectType") is not None:
        out["object_type"] = data["objectType"]
    else:
        out["object_type"] = ""
    if data.get("inclusionFilters") is not None:
        import capo_bedrock_agent.types.filter_list

        out["inclusion_filters"] = (
            capo_bedrock_agent.types.filter_list.deserialize_json(
                data["inclusionFilters"]
            )
        )
    if data.get("exclusionFilters") is not None:
        import capo_bedrock_agent.types.filter_list

        out["exclusion_filters"] = (
            capo_bedrock_agent.types.filter_list.deserialize_json(
                data["exclusionFilters"]
            )
        )
    return out


def redact_sensitive(value: PatternObjectFilter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "object_type" in value:
        out["object_type"] = "*** Sensitive Data Redacted ***"
    if "inclusion_filters" in value:
        out["inclusion_filters"] = "*** Sensitive Data Redacted ***"
    if "exclusion_filters" in value:
        out["exclusion_filters"] = "*** Sensitive Data Redacted ***"
    return out
