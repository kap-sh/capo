"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchPutProfileObjectRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.batch_put_profile_object_request_item_list
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.type_name


class BatchPutProfileObjectRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    object_type_name: "capo_customer_profiles.types.type_name.typeName"
    """<p>The name of the profile object type.</p>"""
    items: "capo_customer_profiles.types.batch_put_profile_object_request_item_list.BatchPutProfileObjectRequestItemList"
    """<p>A list of items to add to the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutProfileObjectRequest) -> dict:
    out: dict = {}
    out["ObjectTypeName"] = value["object_type_name"]
    import capo_customer_profiles.types.batch_put_profile_object_request_item_list

    out["Items"] = (
        capo_customer_profiles.types.batch_put_profile_object_request_item_list.serialize_json(
            value["items"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchPutProfileObjectRequest:
    out: BatchPutProfileObjectRequest = {}  # type: ignore[typeddict-item]
    if data.get("ObjectTypeName") is not None:
        out["object_type_name"] = data["ObjectTypeName"]
    else:
        out["object_type_name"] = ""
    if data.get("Items") is not None:
        import capo_customer_profiles.types.batch_put_profile_object_request_item_list

        out["items"] = (
            capo_customer_profiles.types.batch_put_profile_object_request_item_list.deserialize_json(
                data["Items"]
            )
        )
    else:
        out["items"] = []
    return out


def redact_sensitive(value: BatchPutProfileObjectRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_customer_profiles.types.batch_put_profile_object_request_item_list

        out["items"] = (
            capo_customer_profiles.types.batch_put_profile_object_request_item_list.redact_sensitive(
                value["items"]
            )
        )
    return out
