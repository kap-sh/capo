"""Generated from Smithy shape ``com.amazonaws.datazone#AssetItemAdditionalAttributes``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.form_output_list
    import capo_datazone.types.match_rationale
    import capo_datazone.types.time_series_data_point_summary_form_output_list


class AssetItemAdditionalAttributes(TypedDict, closed=True):
    forms_output: NotRequired["capo_datazone.types.form_output_list.FormOutputList"]
    """<p>The forms included in the additional attributes of an inventory asset.</p>"""
    read_only_forms_output: NotRequired[
        "capo_datazone.types.form_output_list.FormOutputList"
    ]
    """<p>The read-only forms included in the additional attributes of an inventory asset.</p>"""
    latest_time_series_data_point_forms_output: NotRequired[
        "capo_datazone.types.time_series_data_point_summary_form_output_list.TimeSeriesDataPointSummaryFormOutputList"
    ]
    """<p>The latest time series data points forms included in the additional attributes of an asset.</p>"""
    match_rationale: NotRequired["capo_datazone.types.match_rationale.MatchRationale"]
    """<p>List of rationales indicating why this item was matched by search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetItemAdditionalAttributes) -> dict:
    out: dict = {}
    if "forms_output" in value:
        import capo_datazone.types.form_output_list

        out["formsOutput"] = capo_datazone.types.form_output_list.serialize_json(
            value["forms_output"]
        )
    if "read_only_forms_output" in value:
        import capo_datazone.types.form_output_list

        out["readOnlyFormsOutput"] = (
            capo_datazone.types.form_output_list.serialize_json(
                value["read_only_forms_output"]
            )
        )
    if "latest_time_series_data_point_forms_output" in value:
        import capo_datazone.types.time_series_data_point_summary_form_output_list

        out["latestTimeSeriesDataPointFormsOutput"] = (
            capo_datazone.types.time_series_data_point_summary_form_output_list.serialize_json(
                value["latest_time_series_data_point_forms_output"]
            )
        )
    if "match_rationale" in value:
        import capo_datazone.types.match_rationale

        out["matchRationale"] = capo_datazone.types.match_rationale.serialize_json(
            value["match_rationale"]
        )
    return out


def deserialize_json(data: dict) -> AssetItemAdditionalAttributes:
    out: AssetItemAdditionalAttributes = {}  # type: ignore[typeddict-item]
    if data.get("formsOutput") is not None:
        import capo_datazone.types.form_output_list

        out["forms_output"] = capo_datazone.types.form_output_list.deserialize_json(
            data["formsOutput"]
        )
    if data.get("readOnlyFormsOutput") is not None:
        import capo_datazone.types.form_output_list

        out["read_only_forms_output"] = (
            capo_datazone.types.form_output_list.deserialize_json(
                data["readOnlyFormsOutput"]
            )
        )
    if data.get("latestTimeSeriesDataPointFormsOutput") is not None:
        import capo_datazone.types.time_series_data_point_summary_form_output_list

        out["latest_time_series_data_point_forms_output"] = (
            capo_datazone.types.time_series_data_point_summary_form_output_list.deserialize_json(
                data["latestTimeSeriesDataPointFormsOutput"]
            )
        )
    if data.get("matchRationale") is not None:
        import capo_datazone.types.match_rationale

        out["match_rationale"] = capo_datazone.types.match_rationale.deserialize_json(
            data["matchRationale"]
        )
    return out


def redact_sensitive(value: AssetItemAdditionalAttributes) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "forms_output" in value:
        import capo_datazone.types.form_output_list

        out["forms_output"] = capo_datazone.types.form_output_list.redact_sensitive(
            value["forms_output"]
        )
    if "read_only_forms_output" in value:
        import capo_datazone.types.form_output_list

        out["read_only_forms_output"] = (
            capo_datazone.types.form_output_list.redact_sensitive(
                value["read_only_forms_output"]
            )
        )
    return out
