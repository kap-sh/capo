"""Generated from Smithy shape ``com.amazonaws.iot#CreateDynamicThingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.index_name
    import capo_iot.types.query_string
    import capo_iot.types.query_version
    import capo_iot.types.tag_list
    import capo_iot.types.thing_group_name
    import capo_iot.types.thing_group_properties


class CreateDynamicThingGroupRequest(TypedDict, closed=True):
    thing_group_name: "capo_iot.types.thing_group_name.ThingGroupName"
    """<p>The dynamic thing group name to create.</p>"""
    thing_group_properties: NotRequired[
        "capo_iot.types.thing_group_properties.ThingGroupProperties"
    ]
    """<p>The dynamic thing group properties.</p>"""
    index_name: NotRequired["capo_iot.types.index_name.IndexName"]
    """<p>The dynamic thing group index name.</p> <note> <p>Currently one index is supported: <code>AWS_Things</code>.</p> </note>"""
    query_string: "capo_iot.types.query_string.QueryString"
    """<p>The dynamic thing group search query string.</p> <p>See <a href="https://docs.aws.amazon.com/iot/latest/developerguide/query-syntax.html">Query Syntax</a> for information about query string syntax.</p>"""
    query_version: NotRequired["capo_iot.types.query_version.QueryVersion"]
    """<p>The dynamic thing group query version.</p> <note> <p>Currently one query version is supported: "2017-09-30". If not specified, the query version defaults to this value.</p> </note>"""
    tags: NotRequired["capo_iot.types.tag_list.TagList"]
    """<p>Metadata which can be used to manage the dynamic thing group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDynamicThingGroupRequest) -> dict:
    out: dict = {}
    if "thing_group_properties" in value:
        import capo_iot.types.thing_group_properties

        out["thingGroupProperties"] = (
            capo_iot.types.thing_group_properties.serialize_json(
                value["thing_group_properties"]
            )
        )
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    out["queryString"] = value["query_string"]
    if "query_version" in value:
        out["queryVersion"] = value["query_version"]
    if "tags" in value:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDynamicThingGroupRequest:
    out: CreateDynamicThingGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("thingGroupProperties") is not None:
        import capo_iot.types.thing_group_properties

        out["thing_group_properties"] = (
            capo_iot.types.thing_group_properties.deserialize_json(
                data["thingGroupProperties"]
            )
        )
    if data.get("indexName") is not None:
        out["index_name"] = data["indexName"]
    if data.get("queryString") is not None:
        out["query_string"] = data["queryString"]
    else:
        raise DeserializationError(
            "CreateDynamicThingGroupRequest.query_string required"
        )
    if data.get("queryVersion") is not None:
        out["query_version"] = data["queryVersion"]
    if data.get("tags") is not None:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.deserialize_json(data["tags"])
    return out
