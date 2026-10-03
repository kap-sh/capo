"""Generated from Smithy shape ``com.amazonaws.iot#DescribeIndexResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.index_name
    import capo_iot.types.index_schema
    import capo_iot.types.index_status


class DescribeIndexResponse(TypedDict, closed=True):
    index_name: NotRequired["capo_iot.types.index_name.IndexName"]
    """<p>The index name.</p>"""
    index_status: NotRequired["capo_iot.types.index_status.IndexStatus"]
    """<p>The index status.</p>"""
    schema: NotRequired["capo_iot.types.index_schema.IndexSchema"]
    """<p>Contains a value that specifies the type of indexing performed. Valid values are:</p> <ul> <li> <p>REGISTRY – Your thing index contains only registry data.</p> </li> <li> <p>REGISTRY_AND_SHADOW - Your thing index contains registry data and shadow data.</p> </li> <li> <p>REGISTRY_AND_CONNECTIVITY_STATUS - Your thing index contains registry data and thing connectivity status data.</p> </li> <li> <p>REGISTRY_AND_SHADOW_AND_CONNECTIVITY_STATUS - Your thing index contains registry data, shadow data, and thing connectivity status data.</p> </li> <li> <p>MULTI_INDEXING_MODE - Your thing index contains multiple data sources. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/apireference/API_GetIndexingConfiguration.html">GetIndexingConfiguration</a>.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeIndexResponse) -> dict:
    out: dict = {}
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    if "index_status" in value:
        import capo_iot.types.index_status

        out["indexStatus"] = capo_iot.types.index_status.serialize_json(
            value["index_status"]
        )
    if "schema" in value:
        out["schema"] = value["schema"]
    return out


def deserialize_json(data: dict) -> DescribeIndexResponse:
    out: DescribeIndexResponse = {}  # type: ignore[typeddict-item]
    if data.get("indexName") is not None:
        out["index_name"] = data["indexName"]
    if data.get("indexStatus") is not None:
        import capo_iot.types.index_status

        out["index_status"] = capo_iot.types.index_status.deserialize_json(
            data["indexStatus"]
        )
    if data.get("schema") is not None:
        out["schema"] = data["schema"]
    return out
