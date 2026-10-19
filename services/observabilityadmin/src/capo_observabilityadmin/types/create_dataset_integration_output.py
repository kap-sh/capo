"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CreateDatasetIntegrationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_observabilityadmin.types.resource_arn


class CreateDatasetIntegrationOutput(TypedDict, closed=True):
    arn: "capo_observabilityadmin.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the created dataset integration.</p>"""
    role_arn: "capo_observabilityadmin.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role associated with the dataset integration.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the dataset integration was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the dataset integration was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDatasetIntegrationOutput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["RoleArn"] = value["role_arn"]
    import capo_observabilityadmin.types._prelude.timestamp

    out["CreatedAt"] = capo_observabilityadmin.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_observabilityadmin.types._prelude.timestamp

    out["UpdatedAt"] = capo_observabilityadmin.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> CreateDatasetIntegrationOutput:
    out: CreateDatasetIntegrationOutput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    if data.get("CreatedAt") is not None:
        import capo_observabilityadmin.types._prelude.timestamp

        out["created_at"] = (
            capo_observabilityadmin.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("UpdatedAt") is not None:
        import capo_observabilityadmin.types._prelude.timestamp

        out["updated_at"] = (
            capo_observabilityadmin.types._prelude.timestamp.deserialize_json(
                data["UpdatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
