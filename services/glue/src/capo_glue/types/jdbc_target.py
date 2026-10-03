"""Generated from Smithy shape ``com.amazonaws.glue#JdbcTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.connection_name
    import capo_glue.types.enable_additional_metadata
    import capo_glue.types.path
    import capo_glue.types.path_list


class JdbcTarget(TypedDict, closed=True):
    connection_name: NotRequired["capo_glue.types.connection_name.ConnectionName"]
    """<p>The name of the connection to use to connect to the JDBC target.</p>"""
    path: NotRequired["capo_glue.types.path.Path"]
    """<p>The path of the JDBC target.</p>"""
    exclusions: NotRequired["capo_glue.types.path_list.PathList"]
    """<p>A list of glob patterns used to exclude from the crawl. For more information, see <a href="https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html">Catalog Tables with a Crawler</a>.</p>"""
    enable_additional_metadata: NotRequired[
        "capo_glue.types.enable_additional_metadata.EnableAdditionalMetadata"
    ]
    """<p>Specify a value of <code>RAWTYPES</code> or <code>COMMENTS</code> to enable additional metadata in table responses. <code>RAWTYPES</code> provides the native-level datatype. <code>COMMENTS</code> provides comments associated with a column or table in the database.</p> <p>If you do not need additional metadata, keep the field empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JdbcTarget) -> dict:
    out: dict = {}
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "path" in value:
        out["Path"] = value["path"]
    if "exclusions" in value:
        import capo_glue.types.path_list

        out["Exclusions"] = capo_glue.types.path_list.serialize_aws_json_1_1(
            value["exclusions"]
        )
    if "enable_additional_metadata" in value:
        import capo_glue.types.enable_additional_metadata

        out["EnableAdditionalMetadata"] = (
            capo_glue.types.enable_additional_metadata.serialize_aws_json_1_1(
                value["enable_additional_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> JdbcTarget:
    out: JdbcTarget = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionName") is not None:
        out["connection_name"] = data["ConnectionName"]
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    if data.get("Exclusions") is not None:
        import capo_glue.types.path_list

        out["exclusions"] = capo_glue.types.path_list.deserialize_aws_json_1_1(
            data["Exclusions"]
        )
    if data.get("EnableAdditionalMetadata") is not None:
        import capo_glue.types.enable_additional_metadata

        out["enable_additional_metadata"] = (
            capo_glue.types.enable_additional_metadata.deserialize_aws_json_1_1(
                data["EnableAdditionalMetadata"]
            )
        )
    return out
