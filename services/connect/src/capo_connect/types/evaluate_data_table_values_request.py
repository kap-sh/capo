"""Generated from Smithy shape ``com.amazonaws.connect#EvaluateDataTableValuesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.data_table_id
    import capo_connect.types.data_table_value_evaluation_set_list
    import capo_connect.types.instance_id
    import capo_connect.types.max_result100
    import capo_connect.types.next_token
    import capo_connect.types.time_zone


class EvaluateDataTableValuesRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The unique identifier for the Amazon Connect instance.</p>"""
    data_table_id: "capo_connect.types.data_table_id.DataTableId"
    """<p>The unique identifier for the data table. Must also accept the table ARN with or without a version alias.</p>"""
    values: "capo_connect.types.data_table_value_evaluation_set_list.DataTableValueEvaluationSetList"
    """<p>A list of value evaluation sets specifying which primary values and attributes to evaluate.</p>"""
    time_zone: NotRequired["capo_connect.types.time_zone.TimeZone"]
    """<p>Optional IANA timezone identifier to use when resolving time based dynamic values. Defaults to the data table time zone if not provided.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    max_results: NotRequired["capo_connect.types.max_result100.MaxResult100"]
    """<p>The maximum number of data table values to return in one page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluateDataTableValuesRequest) -> dict:
    out: dict = {}
    import capo_connect.types.data_table_value_evaluation_set_list

    out["Values"] = (
        capo_connect.types.data_table_value_evaluation_set_list.serialize_json(
            value["values"]
        )
    )
    if "time_zone" in value:
        out["TimeZone"] = value["time_zone"]
    return out


def deserialize_json(data: dict) -> EvaluateDataTableValuesRequest:
    out: EvaluateDataTableValuesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Values") is not None:
        import capo_connect.types.data_table_value_evaluation_set_list

        out["values"] = (
            capo_connect.types.data_table_value_evaluation_set_list.deserialize_json(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    if data.get("TimeZone") is not None:
        out["time_zone"] = data["TimeZone"]
    return out
