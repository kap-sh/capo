"""Generated from Smithy shape ``com.amazonaws.docdb#ServerlessV2PlatformVersionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.serverless_v2_platform_version_list
    import capo_docdb.types.string


class ServerlessV2PlatformVersionsMessage(TypedDict, closed=True):
    marker: NotRequired["capo_docdb.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    serverless_v2_platform_versions: NotRequired[
        "capo_docdb.types.serverless_v2_platform_version_list.ServerlessV2PlatformVersionList"
    ]
    """<p>A list of <code>ServerlessV2PlatformVersionInfo</code> elements.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ServerlessV2PlatformVersionsMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "serverless_v2_platform_versions" in value:
        import capo_docdb.types.serverless_v2_platform_version_list

        capo_docdb.types.serverless_v2_platform_version_list.serialize_query(
            value["serverless_v2_platform_versions"],
            pairs,
            f"{key_prefix}ServerlessV2PlatformVersions",
        )


def deserialize_query(el: Element) -> ServerlessV2PlatformVersionsMessage:
    out: ServerlessV2PlatformVersionsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_serverless_v2_platform_versions = el.find("ServerlessV2PlatformVersions")
    if child_serverless_v2_platform_versions is not None:
        import capo_docdb.types.serverless_v2_platform_version_list

        out["serverless_v2_platform_versions"] = (
            capo_docdb.types.serverless_v2_platform_version_list.deserialize_query(
                child_serverless_v2_platform_versions
            )
        )
    return out
