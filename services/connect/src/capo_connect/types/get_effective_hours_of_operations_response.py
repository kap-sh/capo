"""Generated from Smithy shape ``com.amazonaws.connect#GetEffectiveHoursOfOperationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.effective_hours_of_operation_list
    import capo_connect.types.effective_override_hours_list
    import capo_connect.types.time_zone


class GetEffectiveHoursOfOperationsResponse(TypedDict, closed=True):
    effective_hours_of_operation_list: NotRequired[
        "capo_connect.types.effective_hours_of_operation_list.EffectiveHoursOfOperationList"
    ]
    """<p>Information about the effective hours of operations.</p>"""
    effective_override_hours_list: NotRequired[
        "capo_connect.types.effective_override_hours_list.EffectiveOverrideHoursList"
    ]
    """<p>Information about override configurations applied to the base hours of operation to calculate the effective hours.</p> <p>For more information about how override types are applied, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/hours-of-operation-overrides.html">Build your list of overrides</a> in the <i> Administrator Guide</i>.</p>"""
    time_zone: NotRequired["capo_connect.types.time_zone.TimeZone"]
    """<p>The time zone for the hours of operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEffectiveHoursOfOperationsResponse) -> dict:
    out: dict = {}
    if "effective_hours_of_operation_list" in value:
        import capo_connect.types.effective_hours_of_operation_list

        out["EffectiveHoursOfOperationList"] = (
            capo_connect.types.effective_hours_of_operation_list.serialize_json(
                value["effective_hours_of_operation_list"]
            )
        )
    if "effective_override_hours_list" in value:
        import capo_connect.types.effective_override_hours_list

        out["EffectiveOverrideHoursList"] = (
            capo_connect.types.effective_override_hours_list.serialize_json(
                value["effective_override_hours_list"]
            )
        )
    if "time_zone" in value:
        out["TimeZone"] = value["time_zone"]
    return out


def deserialize_json(data: dict) -> GetEffectiveHoursOfOperationsResponse:
    out: GetEffectiveHoursOfOperationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("EffectiveHoursOfOperationList") is not None:
        import capo_connect.types.effective_hours_of_operation_list

        out["effective_hours_of_operation_list"] = (
            capo_connect.types.effective_hours_of_operation_list.deserialize_json(
                data["EffectiveHoursOfOperationList"]
            )
        )
    if data.get("EffectiveOverrideHoursList") is not None:
        import capo_connect.types.effective_override_hours_list

        out["effective_override_hours_list"] = (
            capo_connect.types.effective_override_hours_list.deserialize_json(
                data["EffectiveOverrideHoursList"]
            )
        )
    if data.get("TimeZone") is not None:
        out["time_zone"] = data["TimeZone"]
    return out
