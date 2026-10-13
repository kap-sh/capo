"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchGetCalculatedAttributeForProfileRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_id_list
    import capo_customer_profiles.types.condition_overrides
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.type_name


class BatchGetCalculatedAttributeForProfileRequest(TypedDict, closed=True):
    calculated_attribute_name: "capo_customer_profiles.types.type_name.typeName"
    """<p>The unique name of the calculated attribute.</p>"""
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    profile_ids: "capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_id_list.BatchGetCalculatedAttributeForProfileIdList"
    """<p>List of unique identifiers for customer profiles to retrieve.</p>"""
    condition_overrides: NotRequired[
        "capo_customer_profiles.types.condition_overrides.ConditionOverrides"
    ]
    """<p>Overrides the condition block within the original calculated attribute definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCalculatedAttributeForProfileRequest) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_id_list

    out["ProfileIds"] = (
        capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_id_list.serialize_json(
            value["profile_ids"]
        )
    )
    if "condition_overrides" in value:
        import capo_customer_profiles.types.condition_overrides

        out["ConditionOverrides"] = (
            capo_customer_profiles.types.condition_overrides.serialize_json(
                value["condition_overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetCalculatedAttributeForProfileRequest:
    out: BatchGetCalculatedAttributeForProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProfileIds") is not None:
        import capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_id_list

        out["profile_ids"] = (
            capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_id_list.deserialize_json(
                data["ProfileIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetCalculatedAttributeForProfileRequest.profile_ids required"
        )
    if data.get("ConditionOverrides") is not None:
        import capo_customer_profiles.types.condition_overrides

        out["condition_overrides"] = (
            capo_customer_profiles.types.condition_overrides.deserialize_json(
                data["ConditionOverrides"]
            )
        )
    return out


def redact_sensitive(
    value: BatchGetCalculatedAttributeForProfileRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "condition_overrides" in value:
        out["condition_overrides"] = "*** Sensitive Data Redacted ***"
    return out
