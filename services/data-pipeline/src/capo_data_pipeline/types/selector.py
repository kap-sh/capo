"""Generated from Smithy shape ``com.amazonaws.datapipeline#Selector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.operator
    import capo_data_pipeline.types.string


class Selector(TypedDict, closed=True):
    field_name: NotRequired["capo_data_pipeline.types.string.string"]
    """<p>The name of the field that the operator will be applied to. The field name is the "key" portion of the field definition in the pipeline definition syntax that is used by the AWS Data Pipeline API. If the field is not set on the object, the condition fails.</p>"""
    operator: NotRequired["capo_data_pipeline.types.operator.Operator"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Selector) -> dict:
    out: dict = {}
    if "field_name" in value:
        out["fieldName"] = value["field_name"]
    if "operator" in value:
        import capo_data_pipeline.types.operator

        out["operator"] = capo_data_pipeline.types.operator.serialize_aws_json_1_1(
            value["operator"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Selector:
    out: Selector = {}  # type: ignore[typeddict-item]
    if data.get("fieldName") is not None:
        out["field_name"] = data["fieldName"]
    if data.get("operator") is not None:
        import capo_data_pipeline.types.operator

        out["operator"] = capo_data_pipeline.types.operator.deserialize_aws_json_1_1(
            data["operator"]
        )
    return out
