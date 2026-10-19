"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteProfileKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.request_value_list
    import capo_customer_profiles.types.uuid


class DeleteProfileKeyRequest(TypedDict, closed=True):
    profile_id: "capo_customer_profiles.types.uuid.uuid"
    """<p>The unique identifier of a customer profile.</p>"""
    key_name: "capo_customer_profiles.types.name.name"
    """<p>A searchable identifier of a customer profile.</p>"""
    values: "capo_customer_profiles.types.request_value_list.requestValueList"
    """<p>A list of key values.</p>"""
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProfileKeyRequest) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    out["KeyName"] = value["key_name"]
    import capo_customer_profiles.types.request_value_list

    out["Values"] = capo_customer_profiles.types.request_value_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> DeleteProfileKeyRequest:
    out: DeleteProfileKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        out["profile_id"] = ""
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
