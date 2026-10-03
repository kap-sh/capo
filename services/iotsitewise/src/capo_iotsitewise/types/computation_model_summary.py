"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputationModelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.computation_model_status
    import capo_iotsitewise.types.computation_model_type
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.restricted_description
    import capo_iotsitewise.types.restricted_name
    import capo_iotsitewise.types.timestamp
    import capo_iotsitewise.types.version


class ComputationModelSummary(TypedDict, closed=True):
    id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the computation model.</p>"""
    arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the computation model, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:computation-model/${ComputationModelId}</code> </p>"""
    name: "capo_iotsitewise.types.restricted_name.RestrictedName"
    """<p>The name of the computation model.</p>"""
    description: NotRequired[
        "capo_iotsitewise.types.restricted_description.RestrictedDescription"
    ]
    """<p>The description of the computation model.</p>"""
    type: "capo_iotsitewise.types.computation_model_type.ComputationModelType"
    """<p>The type of the computation model.</p>"""
    creation_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The model creation date, in Unix epoch time.</p>"""
    last_update_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The time the model was last updated, in Unix epoch time.</p>"""
    status: "capo_iotsitewise.types.computation_model_status.ComputationModelStatus"
    """<p>The current status of the computation model.</p>"""
    version: "capo_iotsitewise.types.version.Version"
    """<p>The version of the computation model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComputationModelSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_iotsitewise.types.computation_model_type

    out["type"] = capo_iotsitewise.types.computation_model_type.serialize_json(
        value["type"]
    )
    import capo_iotsitewise.types.timestamp

    out["creationDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["creation_date"]
    )
    import capo_iotsitewise.types.timestamp

    out["lastUpdateDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["last_update_date"]
    )
    import capo_iotsitewise.types.computation_model_status

    out["status"] = capo_iotsitewise.types.computation_model_status.serialize_json(
        value["status"]
    )
    out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> ComputationModelSummary:
    out: ComputationModelSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ComputationModelSummary.id required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ComputationModelSummary.arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ComputationModelSummary.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("type") is not None:
        import capo_iotsitewise.types.computation_model_type

        out["type"] = capo_iotsitewise.types.computation_model_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("ComputationModelSummary.type required")
    if data.get("creationDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["creation_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    else:
        raise DeserializationError("ComputationModelSummary.creation_date required")
    if data.get("lastUpdateDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["last_update_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["lastUpdateDate"]
        )
    else:
        raise DeserializationError("ComputationModelSummary.last_update_date required")
    if data.get("status") is not None:
        import capo_iotsitewise.types.computation_model_status

        out["status"] = (
            capo_iotsitewise.types.computation_model_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("ComputationModelSummary.status required")
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("ComputationModelSummary.version required")
    return out
