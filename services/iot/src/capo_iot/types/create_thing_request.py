"""Generated from Smithy shape ``com.amazonaws.iot#CreateThingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.attribute_payload
    import capo_iot.types.billing_group_name
    import capo_iot.types.thing_name
    import capo_iot.types.thing_type_name


class CreateThingRequest(TypedDict, closed=True):
    thing_name: "capo_iot.types.thing_name.ThingName"
    """<p>The name of the thing to create.</p> <p>You can't change a thing's name after you create it. To change a thing's name, you must create a new thing, give it the new name, and then delete the old thing.</p>"""
    thing_type_name: NotRequired["capo_iot.types.thing_type_name.ThingTypeName"]
    """<p>The name of the thing type associated with the new thing.</p>"""
    attribute_payload: NotRequired["capo_iot.types.attribute_payload.AttributePayload"]
    r"""<p>The attribute payload, which consists of up to three name/value pairs in a JSON document. For example:</p> <p> <code>{\"attributes\":{\"string1\":\"string2\"}}</code> </p>"""
    billing_group_name: NotRequired[
        "capo_iot.types.billing_group_name.BillingGroupName"
    ]
    """<p>The name of the billing group the thing will be added to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateThingRequest) -> dict:
    out: dict = {}
    if "thing_type_name" in value:
        out["thingTypeName"] = value["thing_type_name"]
    if "attribute_payload" in value:
        import capo_iot.types.attribute_payload

        out["attributePayload"] = capo_iot.types.attribute_payload.serialize_json(
            value["attribute_payload"]
        )
    if "billing_group_name" in value:
        out["billingGroupName"] = value["billing_group_name"]
    return out


def deserialize_json(data: dict) -> CreateThingRequest:
    out: CreateThingRequest = {}  # type: ignore[typeddict-item]
    if data.get("thingTypeName") is not None:
        out["thing_type_name"] = data["thingTypeName"]
    if data.get("attributePayload") is not None:
        import capo_iot.types.attribute_payload

        out["attribute_payload"] = capo_iot.types.attribute_payload.deserialize_json(
            data["attributePayload"]
        )
    if data.get("billingGroupName") is not None:
        out["billing_group_name"] = data["billingGroupName"]
    return out
