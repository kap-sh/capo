"""Generated from Smithy shape ``com.amazonaws.glue#HudiTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.connection_name
    import capo_glue.types.nullable_integer
    import capo_glue.types.path_list


class HudiTarget(TypedDict, closed=True):
    paths: NotRequired["capo_glue.types.path_list.PathList"]
    """<p>An array of Amazon S3 location strings for Hudi, each indicating the root folder with which the metadata files for a Hudi table resides. The Hudi folder may be located in a child folder of the root folder.</p> <p>The crawler will scan all folders underneath a path for a Hudi folder.</p>"""
    connection_name: NotRequired["capo_glue.types.connection_name.ConnectionName"]
    """<p>The name of the connection to use to connect to the Hudi target. If your Hudi files are stored in buckets that require VPC authorization, you can set their connection properties here.</p>"""
    exclusions: NotRequired["capo_glue.types.path_list.PathList"]
    """<p>A list of glob patterns used to exclude from the crawl. For more information, see <a href="https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html">Catalog Tables with a Crawler</a>.</p>"""
    maximum_traversal_depth: NotRequired[
        "capo_glue.types.nullable_integer.NullableInteger"
    ]
    """<p>The maximum depth of Amazon S3 paths that the crawler can traverse to discover the Hudi metadata folder in your Amazon S3 path. Used to limit the crawler run time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HudiTarget) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> HudiTarget:
    out: HudiTarget = {}  # type: ignore[typeddict-item]
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
