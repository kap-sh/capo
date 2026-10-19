"""Generated from Smithy shape ``com.amazonaws.sagemaker#MetricSpecification``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker.errors import DeserializationError, SerializationError
from capo_sagemaker.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemaker.types.customized_metric_specification
    import capo_sagemaker.types.predefined_metric_specification


class _MetricSpecification_Predefined(TypedDict, closed=True):
    Predefined: "capo_sagemaker.types.predefined_metric_specification.PredefinedMetricSpecification"


class _MetricSpecification_Customized(TypedDict, closed=True):
    Customized: "capo_sagemaker.types.customized_metric_specification.CustomizedMetricSpecification"


MetricSpecification: TypeAlias = (
    _MetricSpecification_Predefined
    | _MetricSpecification_Customized
    | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricSpecification) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"MetricSpecification: cannot serialize unknown variant {value.name!r}"
        )
    elif "Predefined" in value:
        import capo_sagemaker.types.predefined_metric_specification

        return {
            "Predefined": capo_sagemaker.types.predefined_metric_specification.serialize_aws_json_1_1(
                value["Predefined"]
            )
        }
    elif "Customized" in value:
        import capo_sagemaker.types.customized_metric_specification

        return {
            "Customized": capo_sagemaker.types.customized_metric_specification.serialize_aws_json_1_1(
                value["Customized"]
            )
        }
    else:
        raise SerializationError("MetricSpecification: no variant present")


def deserialize_aws_json_1_1(data: dict) -> MetricSpecification:
    if data.get("Predefined") is not None:
        import capo_sagemaker.types.predefined_metric_specification

        return {
            "Predefined": capo_sagemaker.types.predefined_metric_specification.deserialize_aws_json_1_1(
                data["Predefined"]
            )
        }
    elif data.get("Customized") is not None:
        import capo_sagemaker.types.customized_metric_specification

        return {
            "Customized": capo_sagemaker.types.customized_metric_specification.deserialize_aws_json_1_1(
                data["Customized"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("MetricSpecification: no recognized variant key")
