"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainingDatasetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.training_dataset_arn
    import capo_cleanroomsml.types.training_dataset_status


class TrainingDatasetSummary(TypedDict, closed=True):
    create_time: "datetime.datetime"
    """<p>The time at which the training dataset was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the training dataset was updated.</p>"""
    training_dataset_arn: (
        "capo_cleanroomsml.types.training_dataset_arn.TrainingDatasetArn"
    )
    """<p>The Amazon Resource Name (ARN) of the training dataset.</p>"""
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the training dataset.</p>"""
    status: "capo_cleanroomsml.types.training_dataset_status.TrainingDatasetStatus"
    """<p>The status of the training dataset.</p>"""
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the training dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrainingDatasetSummary) -> dict:
    out: dict = {}
    import capo_cleanroomsml._protocol.serialize

    out["createTime"] = capo_cleanroomsml._protocol.serialize.fmt_date_time(
        value["create_time"]
    )
    import capo_cleanroomsml._protocol.serialize

    out["updateTime"] = capo_cleanroomsml._protocol.serialize.fmt_date_time(
        value["update_time"]
    )
    out["trainingDatasetArn"] = value["training_dataset_arn"]
    out["name"] = value["name"]
    import capo_cleanroomsml.types.training_dataset_status

    out["status"] = capo_cleanroomsml.types.training_dataset_status.serialize_json(
        value["status"]
    )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> TrainingDatasetSummary:
    out: TrainingDatasetSummary = {}  # type: ignore[typeddict-item]
    if data.get("createTime") is not None:
        import datetime

        out["create_time"] = datetime.datetime.fromisoformat(
            data["createTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["create_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updateTime") is not None:
        import datetime

        out["update_time"] = datetime.datetime.fromisoformat(
            data["updateTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("trainingDatasetArn") is not None:
        out["training_dataset_arn"] = data["trainingDatasetArn"]
    else:
        out["training_dataset_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("status") is not None:
        import capo_cleanroomsml.types.training_dataset_status

        out["status"] = (
            capo_cleanroomsml.types.training_dataset_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_cleanroomsml.types.training_dataset_status.TrainingDatasetStatus", ""
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
