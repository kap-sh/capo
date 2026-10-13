"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchGetCalculatedAttributeForProfileResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_error_list
    import capo_customer_profiles.types.calculated_attribute_value_list
    import capo_customer_profiles.types.condition_overrides


class BatchGetCalculatedAttributeForProfileResponse(TypedDict, closed=True):
    errors: NotRequired[
        "capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_error_list.BatchGetCalculatedAttributeForProfileErrorList"
    ]
    """<p>List of errors for calculated attribute values that could not be retrieved.</p>"""
    calculated_attribute_values: NotRequired[
        "capo_customer_profiles.types.calculated_attribute_value_list.CalculatedAttributeValueList"
    ]
    """<p>List of calculated attribute values retrieved.</p>"""
    condition_overrides: NotRequired[
        "capo_customer_profiles.types.condition_overrides.ConditionOverrides"
    ]
    """<p>Overrides the condition block within the original calculated attribute definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCalculatedAttributeForProfileResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_error_list

        out["Errors"] = (
            capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_error_list.serialize_json(
                value["errors"]
            )
        )
    if "calculated_attribute_values" in value:
        import capo_customer_profiles.types.calculated_attribute_value_list

        out["CalculatedAttributeValues"] = (
            capo_customer_profiles.types.calculated_attribute_value_list.serialize_json(
                value["calculated_attribute_values"]
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


def deserialize_json(data: dict) -> BatchGetCalculatedAttributeForProfileResponse:
    out: BatchGetCalculatedAttributeForProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("Errors") is not None:
        import capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_error_list

        out["errors"] = (
            capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_error_list.deserialize_json(
                data["Errors"]
            )
        )
    if data.get("CalculatedAttributeValues") is not None:
        import capo_customer_profiles.types.calculated_attribute_value_list

        out["calculated_attribute_values"] = (
            capo_customer_profiles.types.calculated_attribute_value_list.deserialize_json(
                data["CalculatedAttributeValues"]
            )
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
    value: BatchGetCalculatedAttributeForProfileResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "condition_overrides" in value:
        out["condition_overrides"] = "*** Sensitive Data Redacted ***"
    return out
