"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeEntitiesDetectionJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.entities_detection_job_properties


class DescribeEntitiesDetectionJobResponse(TypedDict, closed=True):
    entities_detection_job_properties: NotRequired[
        "capo_comprehend.types.entities_detection_job_properties.EntitiesDetectionJobProperties"
    ]
    """<p>An object that contains the properties associated with an entities detection job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEntitiesDetectionJobResponse) -> dict:
    out: dict = {}
    if "entities_detection_job_properties" in value:
        import capo_comprehend.types.entities_detection_job_properties

        out["EntitiesDetectionJobProperties"] = (
            capo_comprehend.types.entities_detection_job_properties.serialize_aws_json_1_1(
                value["entities_detection_job_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEntitiesDetectionJobResponse:
    out: DescribeEntitiesDetectionJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("EntitiesDetectionJobProperties") is not None:
        import capo_comprehend.types.entities_detection_job_properties

        out["entities_detection_job_properties"] = (
            capo_comprehend.types.entities_detection_job_properties.deserialize_aws_json_1_1(
                data["EntitiesDetectionJobProperties"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeEntitiesDetectionJobResponse) -> dict:
    out: dict = {}
    if "entities_detection_job_properties" in value:
        import capo_comprehend.types.entities_detection_job_properties

        out["EntitiesDetectionJobProperties"] = (
            capo_comprehend.types.entities_detection_job_properties.serialize_cbor(
                value["entities_detection_job_properties"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeEntitiesDetectionJobResponse:
    out: DescribeEntitiesDetectionJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("EntitiesDetectionJobProperties") is not None:
        import capo_comprehend.types.entities_detection_job_properties

        out["entities_detection_job_properties"] = (
            capo_comprehend.types.entities_detection_job_properties.deserialize_cbor(
                data["EntitiesDetectionJobProperties"]
            )
        )
    return out
