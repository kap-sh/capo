"""Generated from Smithy shape ``com.amazonaws.continuum#CollectorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.environment_source_role_arn


class CollectorDetails(TypedDict, closed=True):
    collector_data_access_role_arn: NotRequired[
        "capo_continuum.types.environment_source_role_arn.EnvironmentSourceRoleArn"
    ]
    """IAM role that Continuum assumes to authorize its access to associated Collector inventory. Required for nonempty Collector inventory resolution, in the same account or across accounts. This is independent from any S3 source role."""


# --- restJson1 ser/de ---
def serialize_json(value: CollectorDetails) -> dict:
    out: dict = {}
    if "collector_data_access_role_arn" in value:
        out["collectorDataAccessRoleArn"] = value["collector_data_access_role_arn"]
    return out


def deserialize_json(data: dict) -> CollectorDetails:
    out: CollectorDetails = {}  # type: ignore[typeddict-item]
    if data.get("collectorDataAccessRoleArn") is not None:
        out["collector_data_access_role_arn"] = data["collectorDataAccessRoleArn"]
    return out
