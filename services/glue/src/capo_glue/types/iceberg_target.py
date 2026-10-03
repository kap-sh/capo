"""Generated from Smithy shape ``com.amazonaws.glue#IcebergTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.connection_name
    import capo_glue.types.nullable_integer
    import capo_glue.types.path_list


class IcebergTarget(TypedDict, closed=True):
    paths: NotRequired["capo_glue.types.path_list.PathList"]
    """<p>One or more Amazon S3 paths that contains Iceberg metadata folders as <code>s3://bucket/prefix</code>.</p>"""
    connection_name: NotRequired["capo_glue.types.connection_name.ConnectionName"]
    """<p>The name of the connection to use to connect to the Iceberg target.</p>"""
    exclusions: NotRequired["capo_glue.types.path_list.PathList"]
    """<p>A list of glob patterns used to exclude from the crawl. For more information, see <a href="https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html">Catalog Tables with a Crawler</a>.</p>"""
    maximum_traversal_depth: NotRequired[
        "capo_glue.types.nullable_integer.NullableInteger"
    ]
    """<p>The maximum depth of Amazon S3 paths that the crawler can traverse to discover the Iceberg metadata folder in your Amazon S3 path. Used to limit the crawler run time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergTarget) -> dict:
    out: dict = {}
    if "paths" in value:
        import capo_glue.types.path_list

        out["Paths"] = capo_glue.types.path_list.serialize_aws_json_1_1(value["paths"])
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "exclusions" in value:
        import capo_glue.types.path_list

        out["Exclusions"] = capo_glue.types.path_list.serialize_aws_json_1_1(
            value["exclusions"]
        )
    if "maximum_traversal_depth" in value:
        out["MaximumTraversalDepth"] = value["maximum_traversal_depth"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergTarget:
    out: IcebergTarget = {}  # type: ignore[typeddict-item]
    if data.get("Paths") is not None:
        import capo_glue.types.path_list

        out["paths"] = capo_glue.types.path_list.deserialize_aws_json_1_1(data["Paths"])
    if data.get("ConnectionName") is not None:
        out["connection_name"] = data["ConnectionName"]
    if data.get("Exclusions") is not None:
        import capo_glue.types.path_list

        out["exclusions"] = capo_glue.types.path_list.deserialize_aws_json_1_1(
            data["Exclusions"]
        )
    if data.get("MaximumTraversalDepth") is not None:
        out["maximum_traversal_depth"] = data["MaximumTraversalDepth"]
    return out
