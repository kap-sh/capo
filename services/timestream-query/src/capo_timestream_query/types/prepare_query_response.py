"""Generated from Smithy shape ``com.amazonaws.timestreamquery#PrepareQueryResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import capo_timestream_query.types.parameter_mapping_list
    import capo_timestream_query.types.query_string
    import capo_timestream_query.types.select_column_list


class PrepareQueryResponse(TypedDict, closed=True):
    query_string: "capo_timestream_query.types.query_string.QueryString"
    """<p>The query string that you want prepare.</p>"""
    columns: "capo_timestream_query.types.select_column_list.SelectColumnList"
    """<p>A list of SELECT clause columns of the submitted query string. </p>"""
    parameters: (
        "capo_timestream_query.types.parameter_mapping_list.ParameterMappingList"
    )
    """<p>A list of parameters used in the submitted query string. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PrepareQueryResponse) -> dict:
    out: dict = {}
    out["QueryString"] = value["query_string"]
    import capo_timestream_query.types.select_column_list

    out["Columns"] = (
        capo_timestream_query.types.select_column_list.serialize_aws_json_1_0(
            value["columns"]
        )
    )
    import capo_timestream_query.types.parameter_mapping_list

    out["Parameters"] = (
        capo_timestream_query.types.parameter_mapping_list.serialize_aws_json_1_0(
            value["parameters"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PrepareQueryResponse:
    out: PrepareQueryResponse = {}  # type: ignore[typeddict-item]
    if data.get("QueryString") is not None:
        out["query_string"] = data["QueryString"]
    else:
        raise DeserializationError("PrepareQueryResponse.query_string required")
    if data.get("Columns") is not None:
        import capo_timestream_query.types.select_column_list

        out["columns"] = (
            capo_timestream_query.types.select_column_list.deserialize_aws_json_1_0(
                data["Columns"]
            )
        )
    else:
        raise DeserializationError("PrepareQueryResponse.columns required")
    if data.get("Parameters") is not None:
        import capo_timestream_query.types.parameter_mapping_list

        out["parameters"] = (
            capo_timestream_query.types.parameter_mapping_list.deserialize_aws_json_1_0(
                data["Parameters"]
            )
        )
    else:
        raise DeserializationError("PrepareQueryResponse.parameters required")
    return out


def redact_sensitive(value: PrepareQueryResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "query_string" in value:
        out["query_string"] = "*** Sensitive Data Redacted ***"
    return out
