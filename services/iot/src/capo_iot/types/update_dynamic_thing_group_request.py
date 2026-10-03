"""Generated from Smithy shape ``com.amazonaws.iot#UpdateDynamicThingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.index_name
    import capo_iot.types.optional_version
    import capo_iot.types.query_string
    import capo_iot.types.query_version
    import capo_iot.types.thing_group_name
    import capo_iot.types.thing_group_properties


class UpdateDynamicThingGroupRequest(TypedDict, closed=True):
    thing_group_name: "capo_iot.types.thing_group_name.ThingGroupName"
    """<p>The name of the dynamic thing group to update.</p>"""
    thing_group_properties: "capo_iot.types.thing_group_properties.ThingGroupProperties"
    """<p>The dynamic thing group properties to update.</p>"""
    expected_version: NotRequired["capo_iot.types.optional_version.OptionalVersion"]
    """<p>The expected version of the dynamic thing group to update.</p>"""
    index_name: NotRequired["capo_iot.types.index_name.IndexName"]
    """<p>The dynamic thing group index to update.</p> <note> <p>Currently one index is supported: <code>AWS_Things</code>.</p> </note>"""
    query_string: NotRequired["capo_iot.types.query_string.QueryString"]
    """<p>The dynamic thing group search query string to update.</p>"""
    query_version: NotRequired["capo_iot.types.query_version.QueryVersion"]
    """<p>The dynamic thing group query version to update.</p> <note> <p>Currently one query version is supported: "2017-09-30". If not specified, the query version defaults to this value.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDynamicThingGroupRequest) -> dict:
    out: dict = {}
    import capo_iot.types.thing_group_properties

    out["thingGroupProperties"] = capo_iot.types.thing_group_properties.serialize_json(
        value["thing_group_properties"]
    )
    if "expected_version" in value:
        out["expectedVersion"] = value["expected_version"]
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    if "query_string" in value:
        out["queryString"] = value["query_string"]
    if "query_version" in value:
        out["queryVersion"] = value["query_version"]
    return out


def deserialize_json(data: dict) -> UpdateDynamicThingGroupRequest:
    out: UpdateDynamicThingGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("thingGroupProperties") is not None:
        import capo_iot.types.thing_group_properties

        out["thing_group_properties"] = (
            capo_iot.types.thing_group_properties.deserialize_json(
                data["thingGroupProperties"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDynamicThingGroupRequest.thing_group_properties required"
        )
    if data.get("expectedVersion") is not None:
        out["expected_version"] = data["expectedVersion"]
    if data.get("indexName") is not None:
        out["index_name"] = data["indexName"]
    if data.get("queryString") is not None:
        out["query_string"] = data["queryString"]
    if data.get("queryVersion") is not None:
        out["query_version"] = data["queryVersion"]
    return out
