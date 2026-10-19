"""Generated from Smithy shape ``com.amazonaws.datazone#PostTimeSeriesDataPointsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.client_token
    import capo_datazone.types.domain_id
    import capo_datazone.types.entity_identifier
    import capo_datazone.types.time_series_data_point_form_input_list
    import capo_datazone.types.time_series_entity_type


class PostTimeSeriesDataPointsInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which you want to post time series data points.</p>"""
    entity_identifier: "capo_datazone.types.entity_identifier.EntityIdentifier"
    """<p>The ID of the asset for which you want to post time series data points.</p>"""
    entity_type: "capo_datazone.types.time_series_entity_type.TimeSeriesEntityType"
    """<p>The type of the asset for which you want to post data points.</p>"""
    forms: "capo_datazone.types.time_series_data_point_form_input_list.TimeSeriesDataPointFormInputList"
    """<p>The forms that contain the data points that you want to post.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostTimeSeriesDataPointsInput) -> dict:
    out: dict = {}
    import capo_datazone.types.time_series_data_point_form_input_list

    out["forms"] = (
        capo_datazone.types.time_series_data_point_form_input_list.serialize_json(
            value["forms"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> PostTimeSeriesDataPointsInput:
    out: PostTimeSeriesDataPointsInput = {}  # type: ignore[typeddict-item]
    if data.get("forms") is not None:
        import capo_datazone.types.time_series_data_point_form_input_list

        out["forms"] = (
            capo_datazone.types.time_series_data_point_form_input_list.deserialize_json(
                data["forms"]
            )
        )
    else:
        out["forms"] = []
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
