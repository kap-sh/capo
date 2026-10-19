"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchGetProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.batch_get_profile_id_list
    import capo_customer_profiles.types.name


class BatchGetProfileRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    profile_ids: (
        "capo_customer_profiles.types.batch_get_profile_id_list.BatchGetProfileIdList"
    )
    """<p>List of unique identifiers for customer profiles to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetProfileRequest) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.batch_get_profile_id_list

    out["ProfileIds"] = (
        capo_customer_profiles.types.batch_get_profile_id_list.serialize_json(
            value["profile_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetProfileRequest:
    out: BatchGetProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProfileIds") is not None:
        import capo_customer_profiles.types.batch_get_profile_id_list

        out["profile_ids"] = (
            capo_customer_profiles.types.batch_get_profile_id_list.deserialize_json(
                data["ProfileIds"]
            )
        )
    else:
        out["profile_ids"] = []
    return out
