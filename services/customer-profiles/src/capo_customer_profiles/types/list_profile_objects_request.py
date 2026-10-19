"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListProfileObjectsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.max_size100
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.object_filter
    import capo_customer_profiles.types.token
    import capo_customer_profiles.types.type_name
    import capo_customer_profiles.types.uuid


class ListProfileObjectsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous call to ListProfileObjects.</p>"""
    max_results: NotRequired["capo_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of objects returned per page.</p>"""
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    object_type_name: "capo_customer_profiles.types.type_name.typeName"
    """<p>The name of the profile object type.</p>"""
    profile_id: "capo_customer_profiles.types.uuid.uuid"
    """<p>The unique identifier of a customer profile.</p>"""
    object_filter: NotRequired[
        "capo_customer_profiles.types.object_filter.ObjectFilter"
    ]
    """<p>Applies a filter to the response to include profile objects with the specified index values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfileObjectsRequest) -> dict:
    out: dict = {}
    out["ObjectTypeName"] = value["object_type_name"]
    out["ProfileId"] = value["profile_id"]
    if "object_filter" in value:
        import capo_customer_profiles.types.object_filter

        out["ObjectFilter"] = capo_customer_profiles.types.object_filter.serialize_json(
            value["object_filter"]
        )
    return out


def deserialize_json(data: dict) -> ListProfileObjectsRequest:
    out: ListProfileObjectsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ObjectTypeName") is not None:
        out["object_type_name"] = data["ObjectTypeName"]
    else:
        out["object_type_name"] = ""
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        out["profile_id"] = ""
    if data.get("ObjectFilter") is not None:
        import capo_customer_profiles.types.object_filter

        out["object_filter"] = (
            capo_customer_profiles.types.object_filter.deserialize_json(
                data["ObjectFilter"]
            )
        )
    return out
