"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationStringFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.remediation_string_field
    import capo_securityhub.types.remediation_string_filter_condition


class RemediationStringFilter(TypedDict, closed=True):
    field_name: NotRequired[
        "capo_securityhub.types.remediation_string_field.RemediationStringField"
    ]
    """<p>The name of the filter field. Valid values are <code>Resource.Type</code>, <code>Priority</code>, <code>Status</code>, <code>Resource.Id</code>, <code>Resource.ResourceOwnerAccountId</code>, and <code>Resource.CloudProvider</code>.</p>"""
    filter: NotRequired[
        "capo_securityhub.types.remediation_string_filter_condition.RemediationStringFilterCondition"
    ]
    """<p>The string filter definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemediationStringFilter) -> dict:
    out: dict = {}
    if "field_name" in value:
        import capo_securityhub.types.remediation_string_field

        out["FieldName"] = (
            capo_securityhub.types.remediation_string_field.serialize_json(
                value["field_name"]
            )
        )
    if "filter" in value:
        import capo_securityhub.types.remediation_string_filter_condition

        out["Filter"] = (
            capo_securityhub.types.remediation_string_filter_condition.serialize_json(
                value["filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> RemediationStringFilter:
    out: RemediationStringFilter = {}  # type: ignore[typeddict-item]
    if data.get("FieldName") is not None:
        import capo_securityhub.types.remediation_string_field

        out["field_name"] = (
            capo_securityhub.types.remediation_string_field.deserialize_json(
                data["FieldName"]
            )
        )
    if data.get("Filter") is not None:
        import capo_securityhub.types.remediation_string_filter_condition

        out["filter"] = (
            capo_securityhub.types.remediation_string_filter_condition.deserialize_json(
                data["Filter"]
            )
        )
    return out
