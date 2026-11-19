"""Generated from Smithy shape ``com.amazonaws.docdb#DescribeServerlessV2PlatformVersionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.boolean_optional
    import capo_docdb.types.filter_list
    import capo_docdb.types.integer_optional
    import capo_docdb.types.string


class DescribeServerlessV2PlatformVersionsMessage(TypedDict, closed=True):
    serverless_v2_platform_version: NotRequired["capo_docdb.types.string.String"]
    """<p>A specific platform version to return details for.</p> <p>Example: <code>3</code> </p>"""
    engine: NotRequired["capo_docdb.types.string.String"]
    """<p>The database engine to return platform version details for.</p>"""
    filters: NotRequired["capo_docdb.types.filter_list.FilterList"]
    """<p>This parameter isn't currently supported.</p>"""
    default_only: NotRequired["capo_docdb.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to return only the default platform versions for each engine. The default platform version is the version used for new DB clusters.</p>"""
    include_all: NotRequired["capo_docdb.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to also include platform versions that are no longer in use. If you don't specify a value, the response includes only active platform versions.</p>"""
    max_records: NotRequired["capo_docdb.types.integer_optional.IntegerOptional"]
    """<p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""
    marker: NotRequired["capo_docdb.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeServerlessV2PlatformVersionsMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "serverless_v2_platform_version" in value:
        pairs.append(
            (
                f"{key_prefix}ServerlessV2PlatformVersion",
                str(value["serverless_v2_platform_version"]),
            )
        )
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "filters" in value:
        import capo_docdb.types.filter_list

        capo_docdb.types.filter_list.serialize_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )
    if "default_only" in value:
        pairs.append(
            (f"{key_prefix}DefaultOnly", "true" if value["default_only"] else "false")
        )
    if "include_all" in value:
        pairs.append(
            (f"{key_prefix}IncludeAll", "true" if value["include_all"] else "false")
        )
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeServerlessV2PlatformVersionsMessage:
    out: DescribeServerlessV2PlatformVersionsMessage = {}  # type: ignore[typeddict-item]
    child_serverless_v2_platform_version = el.find("ServerlessV2PlatformVersion")
    if child_serverless_v2_platform_version is not None:
        out["serverless_v2_platform_version"] = str(
            child_serverless_v2_platform_version.text or ""
        )
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_docdb.types.filter_list

        out["filters"] = capo_docdb.types.filter_list.deserialize_query(child_filters)
    child_default_only = el.find("DefaultOnly")
    if child_default_only is not None:
        out["default_only"] = (child_default_only.text or "").lower() == "true"
    child_include_all = el.find("IncludeAll")
    if child_include_all is not None:
        out["include_all"] = (child_include_all.text or "").lower() == "true"
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
