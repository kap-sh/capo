"""Generated from Smithy shape ``com.amazonaws.datapipeline#Operator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.operator_type
    import capo_data_pipeline.types.string_list


class Operator(TypedDict, closed=True):
    type: NotRequired["capo_data_pipeline.types.operator_type.OperatorType"]
    """<p> The logical operation to be performed: equal (<code>EQ</code>), equal reference (<code>REF_EQ</code>), less than or equal (<code>LE</code>), greater than or equal (<code>GE</code>), or between (<code>BETWEEN</code>). Equal reference (<code>REF_EQ</code>) can be used only with reference fields. The other comparison types can be used only with String fields. The comparison types you can use apply only to certain object fields, as detailed below. </p> <p> The comparison operators EQ and REF_EQ act on the following fields: </p> <ul> <li>name</li> <li>@sphere</li> <li>parent</li> <li>@componentParent</li> <li>@instanceParent</li> <li>@status</li> <li>@scheduledStartTime</li> <li>@scheduledEndTime</li> <li>@actualStartTime</li> <li>@actualEndTime</li> </ul> <p> The comparison operators <code>GE</code>, <code>LE</code>, and <code>BETWEEN</code> act on the following fields: </p> <ul> <li>@scheduledStartTime</li> <li>@scheduledEndTime</li> <li>@actualStartTime</li> <li>@actualEndTime</li> </ul> <p>Note that fields beginning with the at sign (@) are read-only and set by the web service. When you name fields, you should choose names containing only alpha-numeric values, as symbols may be reserved by AWS Data Pipeline. User-defined fields that you add to a pipeline should prefix their name with the string "my".</p>"""
    values: NotRequired["capo_data_pipeline.types.string_list.stringList"]
    """<p>The value that the actual field value will be compared with.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Operator) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_data_pipeline.types.operator_type

        out["type"] = capo_data_pipeline.types.operator_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "values" in value:
        import capo_data_pipeline.types.string_list

        out["values"] = capo_data_pipeline.types.string_list.serialize_aws_json_1_1(
            value["values"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Operator:
    out: Operator = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_data_pipeline.types.operator_type

        out["type"] = capo_data_pipeline.types.operator_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if data.get("values") is not None:
        import capo_data_pipeline.types.string_list

        out["values"] = capo_data_pipeline.types.string_list.deserialize_aws_json_1_1(
            data["values"]
        )
    return out
