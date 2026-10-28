"""Generated from Smithy shape ``com.amazonaws.cleanrooms#WorkerComputeConfigurationProperties``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.spark_properties


class WorkerComputeConfigurationPropertiesSparkMember(TypedDict, closed=True):
    spark: "capo_cleanrooms.types.spark_properties.SparkProperties"


WorkerComputeConfigurationProperties: TypeAlias = (
    WorkerComputeConfigurationPropertiesSparkMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: WorkerComputeConfigurationProperties) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"WorkerComputeConfigurationProperties: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "spark" in value:
        import capo_cleanrooms.types.spark_properties

        return {
            "spark": capo_cleanrooms.types.spark_properties.serialize_json(
                value["spark"]
            )
        }
    else:
        raise SerializationError(
            "WorkerComputeConfigurationProperties: no variant present"
        )


def deserialize_json(data: dict) -> WorkerComputeConfigurationProperties:
    if data.get("spark") is not None:
        import capo_cleanrooms.types.spark_properties

        return {
            "spark": capo_cleanrooms.types.spark_properties.deserialize_json(
                data["spark"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "WorkerComputeConfigurationProperties: no recognized variant key"
        )
