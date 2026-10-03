"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSourceSearchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.data_source_filter_attribute
    import capo_quicksight.types.filter_operator
    import capo_quicksight.types.string


class DataSourceSearchFilter(TypedDict, closed=True):
    operator: "capo_quicksight.types.filter_operator.FilterOperator"
    """<p>The comparison operator that you want to use as a filter, for example <code>"Operator": "StringEquals"</code>. Valid values are <code>"StringEquals"</code> and <code>"StringLike"</code>.</p> <p>If you set the operator value to <code>"StringEquals"</code>, you need to provide an ownership related filter in the <code>"NAME"</code> field and the arn of the user or group whose data sources you want to search in the <code>"Value"</code> field. For example, <code>"Name":"DIRECT_QUICKSIGHT_OWNER", "Operator": "StringEquals", "Value": "arn:aws:quicksight:us-east-1:1:user/default/UserName1"</code>.</p> <p>If you set the value to <code>"StringLike"</code>, you need to provide the name of the data sources you are searching for. For example, <code>"Name":"DATASOURCE_NAME", "Operator": "StringLike", "Value": "Test"</code>. The <code>"StringLike"</code> operator only supports the <code>NAME</code> value <code>DATASOURCE_NAME</code>.</p>"""
    name: "capo_quicksight.types.data_source_filter_attribute.DataSourceFilterAttribute"
    """<p>The name of the value that you want to use as a filter, for example, <code>"Name": "DIRECT_QUICKSIGHT_OWNER"</code>.</p> <p>Valid values are defined as follows:</p> <ul> <li> <p> <code>DIRECT_QUICKSIGHT_VIEWER_OR_OWNER</code>: Provide an ARN of a user or group, and any data sources with that ARN listed as one of the owners or viewers of the data sources are returned. Implicit permissions from folders or groups are not considered.</p> </li> <li> <p> <code>DIRECT_QUICKSIGHT_OWNER</code>: Provide an ARN of a user or group, and any data sources with that ARN listed as one of the owners if the data source are returned. Implicit permissions from folders or groups are not considered.</p> </li> <li> <p> <code>DIRECT_QUICKSIGHT_SOLE_OWNER</code>: Provide an ARN of a user or group, and any data sources with that ARN listed as the only owner of the data source are returned. Implicit permissions from folders or groups are not considered.</p> </li> <li> <p> <code>DATASOURCE_NAME</code>: Any data sources whose names have a substring match to the provided value are returned.</p> </li> </ul>"""
    value: "capo_quicksight.types.string.String"
    """<p>The value of the named item, for example <code>DIRECT_QUICKSIGHT_OWNER</code>, that you want to use as a filter, for example, <code>"Value": "arn:aws:quicksight:us-east-1:1:user/default/UserName1"</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceSearchFilter) -> dict:
    out: dict = {}
    import capo_quicksight.types.filter_operator

    out["Operator"] = capo_quicksight.types.filter_operator.serialize_json(
        value["operator"]
    )
    import capo_quicksight.types.data_source_filter_attribute

    out["Name"] = capo_quicksight.types.data_source_filter_attribute.serialize_json(
        value["name"]
    )
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> DataSourceSearchFilter:
    out: DataSourceSearchFilter = {}  # type: ignore[typeddict-item]
    if data.get("Operator") is not None:
        import capo_quicksight.types.filter_operator

        out["operator"] = capo_quicksight.types.filter_operator.deserialize_json(
            data["Operator"]
        )
    else:
        raise DeserializationError("DataSourceSearchFilter.operator required")
    if data.get("Name") is not None:
        import capo_quicksight.types.data_source_filter_attribute

        out["name"] = (
            capo_quicksight.types.data_source_filter_attribute.deserialize_json(
                data["Name"]
            )
        )
    else:
        raise DeserializationError("DataSourceSearchFilter.name required")
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("DataSourceSearchFilter.value required")
    return out
