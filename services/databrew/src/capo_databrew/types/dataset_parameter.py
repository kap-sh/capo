"""Generated from Smithy shape ``com.amazonaws.databrew#DatasetParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.create_column
    import capo_databrew.types.datetime_options
    import capo_databrew.types.filter_expression
    import capo_databrew.types.parameter_type
    import capo_databrew.types.path_parameter_name


class DatasetParameter(TypedDict, closed=True):
    name: "capo_databrew.types.path_parameter_name.PathParameterName"
    """<p>The name of the parameter that is used in the dataset's Amazon S3 path.</p>"""
    type: "capo_databrew.types.parameter_type.ParameterType"
    """<p>The type of the dataset parameter, can be one of a 'String', 'Number' or 'Datetime'.</p>"""
    datetime_options: NotRequired[
        "capo_databrew.types.datetime_options.DatetimeOptions"
    ]
    """<p>Additional parameter options such as a format and a timezone. Required for datetime parameters.</p>"""
    create_column: "capo_databrew.types.create_column.CreateColumn"
    """<p>Optional boolean value that defines whether the captured value of this parameter should be used to create a new column in a dataset.</p>"""
    filter: NotRequired["capo_databrew.types.filter_expression.FilterExpression"]
    """<p>The optional filter expression structure to apply additional matching criteria to the parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetParameter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_databrew.types.parameter_type

    out["Type"] = capo_databrew.types.parameter_type.serialize_json(value["type"])
    if "datetime_options" in value:
        import capo_databrew.types.datetime_options

        out["DatetimeOptions"] = capo_databrew.types.datetime_options.serialize_json(
            value["datetime_options"]
        )
    out["CreateColumn"] = value.get("create_column", False)
    if "filter" in value:
        import capo_databrew.types.filter_expression

        out["Filter"] = capo_databrew.types.filter_expression.serialize_json(
            value["filter"]
        )
    return out


def deserialize_json(data: dict) -> DatasetParameter:
    out: DatasetParameter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Type") is not None:
        import capo_databrew.types.parameter_type

        out["type"] = capo_databrew.types.parameter_type.deserialize_json(data["Type"])
    else:
        import typing

        out["type"] = typing.cast(
            "capo_databrew.types.parameter_type.ParameterType", ""
        )
    if data.get("DatetimeOptions") is not None:
        import capo_databrew.types.datetime_options

        out["datetime_options"] = capo_databrew.types.datetime_options.deserialize_json(
            data["DatetimeOptions"]
        )
    if data.get("CreateColumn") is not None:
        out["create_column"] = data["CreateColumn"]
    else:
        out["create_column"] = False
    if data.get("Filter") is not None:
        import capo_databrew.types.filter_expression

        out["filter"] = capo_databrew.types.filter_expression.deserialize_json(
            data["Filter"]
        )
    return out
