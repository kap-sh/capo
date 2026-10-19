"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ObjectFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.request_value_list


class ObjectFilter(TypedDict, closed=True):
    key_name: "capo_customer_profiles.types.name.name"
    """<p>A searchable identifier of a profile object. The predefined keys you can use to search for <code>_asset</code> include: <code>_assetId</code>, <code>_assetName</code>, and <code>_serialNumber</code>. The predefined keys you can use to search for <code>_case</code> include: <code>_caseId</code>. The predefined keys you can use to search for <code>_order</code> include: <code>_orderId</code>.</p>"""
    values: "capo_customer_profiles.types.request_value_list.requestValueList"
    """<p>A list of key values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ObjectFilter) -> dict:
    out: dict = {}
    out["KeyName"] = value["key_name"]
    import capo_customer_profiles.types.request_value_list

    out["Values"] = capo_customer_profiles.types.request_value_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> ObjectFilter:
    out: ObjectFilter = {}  # type: ignore[typeddict-item]
    if data.get("KeyName") is not None:
        out["key_name"] = data["KeyName"]
    else:
        out["key_name"] = ""
    if data.get("Values") is not None:
        import capo_customer_profiles.types.request_value_list

        out["values"] = (
            capo_customer_profiles.types.request_value_list.deserialize_json(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    return out
