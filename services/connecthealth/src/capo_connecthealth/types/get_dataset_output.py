"""Generated from Smithy shape ``com.amazonaws.connecthealth#GetDatasetOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_connecthealth.types.bounded_safe_string
    import capo_connecthealth.types.dataset_arn
    import capo_connecthealth.types.dataset_artifacts
    import capo_connecthealth.types.dataset_config
    import capo_connecthealth.types.dataset_id
    import capo_connecthealth.types.dataset_status
    import capo_connecthealth.types.dataset_type


class GetDatasetOutput(TypedDict, closed=True):
    arn: "capo_connecthealth.types.dataset_arn.DatasetArn"
    """<p>The Amazon Resource Name (ARN) of the dataset.</p>"""
    dataset_id: "capo_connecthealth.types.dataset_id.DatasetId"
    """<p>The unique identifier of the dataset.</p>"""
    name: "capo_connecthealth.types.bounded_safe_string.BoundedSafeString"
    """<p>The name of the dataset.</p>"""
    type: "capo_connecthealth.types.dataset_type.DatasetType"
    """<p>The type of the dataset.</p>"""
    config: "capo_connecthealth.types.dataset_config.DatasetConfig"
    """<p>The configuration that you provided when you created the dataset.</p>"""
    status: "capo_connecthealth.types.dataset_status.DatasetStatus"
    """<p>The status of the dataset.</p>"""
    status_details: NotRequired[
        "capo_connecthealth.types.bounded_safe_string.BoundedSafeString"
    ]
    """<p>Details about the status of the dataset, such as the reason that it failed to build or delete.</p>"""
    artifacts: NotRequired[
        "capo_connecthealth.types.dataset_artifacts.DatasetArtifacts"
    ]
    """<p>The results of building the dataset, such as medical coding evaluation scores. Available after Amazon Connect Health builds the dataset.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time that the dataset was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The date and time that the dataset was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDatasetOutput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["datasetId"] = value["dataset_id"]
    out["name"] = value["name"]
    import capo_connecthealth.types.dataset_type

    out["type"] = capo_connecthealth.types.dataset_type.serialize_json(value["type"])
    import capo_connecthealth.types.dataset_config

    out["config"] = capo_connecthealth.types.dataset_config.serialize_json(
        value["config"]
    )
    import capo_connecthealth.types.dataset_status

    out["status"] = capo_connecthealth.types.dataset_status.serialize_json(
        value["status"]
    )
    if "status_details" in value:
        out["statusDetails"] = value["status_details"]
    if "artifacts" in value:
        import capo_connecthealth.types.dataset_artifacts

        out["artifacts"] = capo_connecthealth.types.dataset_artifacts.serialize_json(
            value["artifacts"]
        )
    import capo_connecthealth.types._prelude.timestamp

    out["createdAt"] = capo_connecthealth.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_connecthealth.types._prelude.timestamp

    out["updatedAt"] = capo_connecthealth.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> GetDatasetOutput:
    out: GetDatasetOutput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    else:
        out["dataset_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        import capo_connecthealth.types.dataset_type

        out["type"] = capo_connecthealth.types.dataset_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_connecthealth.types.dataset_type.DatasetType", ""
        )
    if data.get("config") is not None:
        import capo_connecthealth.types.dataset_config

        out["config"] = capo_connecthealth.types.dataset_config.deserialize_json(
            data["config"]
        )
    else:
        out["config"] = {"$unknown": {"name": ""}}
    if data.get("status") is not None:
        import capo_connecthealth.types.dataset_status

        out["status"] = capo_connecthealth.types.dataset_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_connecthealth.types.dataset_status.DatasetStatus", ""
        )
    if data.get("statusDetails") is not None:
        out["status_details"] = data["statusDetails"]
    if data.get("artifacts") is not None:
        import capo_connecthealth.types.dataset_artifacts

        out["artifacts"] = capo_connecthealth.types.dataset_artifacts.deserialize_json(
            data["artifacts"]
        )
    if data.get("createdAt") is not None:
        import capo_connecthealth.types._prelude.timestamp

        out["created_at"] = (
            capo_connecthealth.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_connecthealth.types._prelude.timestamp

        out["updated_at"] = (
            capo_connecthealth.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
