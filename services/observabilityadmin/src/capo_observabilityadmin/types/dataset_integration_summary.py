"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#DatasetIntegrationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_observabilityadmin.types.resource_arn


class DatasetIntegrationSummary(TypedDict, closed=True):
    arn: "capo_observabilityadmin.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the dataset integration.</p>"""
    role_arn: NotRequired["capo_observabilityadmin.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role associated with the dataset integration.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the dataset integration was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the dataset integration was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetIntegrationSummary) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "created_at" in value:
        import capo_observabilityadmin.types._prelude.timestamp

        out["CreatedAt"] = (
            capo_observabilityadmin.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import capo_observabilityadmin.types._prelude.timestamp

        out["UpdatedAt"] = (
            capo_observabilityadmin.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> DatasetIntegrationSummary:
    out: DatasetIntegrationSummary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("CreatedAt") is not None:
        import capo_observabilityadmin.types._prelude.timestamp

        out["created_at"] = (
            capo_observabilityadmin.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if data.get("UpdatedAt") is not None:
        import capo_observabilityadmin.types._prelude.timestamp

        out["updated_at"] = (
            capo_observabilityadmin.types._prelude.timestamp.deserialize_json(
                data["UpdatedAt"]
            )
        )
    return out
