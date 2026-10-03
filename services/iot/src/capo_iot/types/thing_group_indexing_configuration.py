"""Generated from Smithy shape ``com.amazonaws.iot#ThingGroupIndexingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.fields
    import capo_iot.types.thing_group_indexing_mode


class ThingGroupIndexingConfiguration(TypedDict, closed=True):
    thing_group_indexing_mode: (
        "capo_iot.types.thing_group_indexing_mode.ThingGroupIndexingMode"
    )
    """<p>Thing group indexing mode.</p>"""
    managed_fields: NotRequired["capo_iot.types.fields.Fields"]
    """<p>Contains fields that are indexed and whose types are already known by the Fleet Indexing service. This is an optional field. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/managing-fleet-index.html#managed-field">Managed fields</a> in the <i>Amazon Web Services IoT Core Developer Guide</i>.</p> <note> <p>You can't modify managed fields by updating fleet indexing configuration.</p> </note>"""
    custom_fields: NotRequired["capo_iot.types.fields.Fields"]
    """<p>A list of thing group fields to index. This list cannot contain any managed fields. Use the GetIndexingConfiguration API to get a list of managed fields.</p> <p>Contains custom field names and their data type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThingGroupIndexingConfiguration) -> dict:
    out: dict = {}
    import capo_iot.types.thing_group_indexing_mode

    out["thingGroupIndexingMode"] = (
        capo_iot.types.thing_group_indexing_mode.serialize_json(
            value["thing_group_indexing_mode"]
        )
    )
    if "managed_fields" in value:
        import capo_iot.types.fields

        out["managedFields"] = capo_iot.types.fields.serialize_json(
            value["managed_fields"]
        )
    if "custom_fields" in value:
        import capo_iot.types.fields

        out["customFields"] = capo_iot.types.fields.serialize_json(
            value["custom_fields"]
        )
    return out


def deserialize_json(data: dict) -> ThingGroupIndexingConfiguration:
    out: ThingGroupIndexingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("thingGroupIndexingMode") is not None:
        import capo_iot.types.thing_group_indexing_mode

        out["thing_group_indexing_mode"] = (
            capo_iot.types.thing_group_indexing_mode.deserialize_json(
                data["thingGroupIndexingMode"]
            )
        )
    else:
        raise DeserializationError(
            "ThingGroupIndexingConfiguration.thing_group_indexing_mode required"
        )
    if data.get("managedFields") is not None:
        import capo_iot.types.fields

        out["managed_fields"] = capo_iot.types.fields.deserialize_json(
            data["managedFields"]
        )
    if data.get("customFields") is not None:
        import capo_iot.types.fields

        out["custom_fields"] = capo_iot.types.fields.deserialize_json(
            data["customFields"]
        )
    return out
