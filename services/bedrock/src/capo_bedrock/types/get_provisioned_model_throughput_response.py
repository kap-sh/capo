"""Generated from Smithy shape ``com.amazonaws.bedrock#GetProvisionedModelThroughputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.commitment_duration
    import capo_bedrock.types.error_message
    import capo_bedrock.types.foundation_model_arn
    import capo_bedrock.types.model_arn
    import capo_bedrock.types.positive_integer
    import capo_bedrock.types.provisioned_model_arn
    import capo_bedrock.types.provisioned_model_name
    import capo_bedrock.types.provisioned_model_status
    import capo_bedrock.types.timestamp


class GetProvisionedModelThroughputResponse(TypedDict, closed=True):
    model_units: "capo_bedrock.types.positive_integer.PositiveInteger"
    """<p>The number of model units allocated to this Provisioned Throughput.</p>"""
    desired_model_units: "capo_bedrock.types.positive_integer.PositiveInteger"
    """<p>The number of model units that was requested for this Provisioned Throughput.</p>"""
    provisioned_model_name: (
        "capo_bedrock.types.provisioned_model_name.ProvisionedModelName"
    )
    """<p>The name of the Provisioned Throughput.</p>"""
    provisioned_model_arn: (
        "capo_bedrock.types.provisioned_model_arn.ProvisionedModelArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Provisioned Throughput.</p>"""
    model_arn: "capo_bedrock.types.model_arn.ModelArn"
    """<p>The Amazon Resource Name (ARN) of the model associated with this Provisioned Throughput.</p>"""
    desired_model_arn: "capo_bedrock.types.model_arn.ModelArn"
    """<p>The Amazon Resource Name (ARN) of the model requested to be associated to this Provisioned Throughput. This value differs from the <code>modelArn</code> if updating hasn't completed.</p>"""
    foundation_model_arn: "capo_bedrock.types.foundation_model_arn.FoundationModelArn"
    """<p>The Amazon Resource Name (ARN) of the base model for which the Provisioned Throughput was created, or of the base model that the custom model for which the Provisioned Throughput was created was customized.</p>"""
    status: "capo_bedrock.types.provisioned_model_status.ProvisionedModelStatus"
    """<p>The status of the Provisioned Throughput. </p>"""
    creation_time: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp of the creation time for this Provisioned Throughput. </p>"""
    last_modified_time: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp of the last time that this Provisioned Throughput was modified. </p>"""
    failure_message: NotRequired["capo_bedrock.types.error_message.ErrorMessage"]
    """<p>A failure message for any issues that occurred during creation, updating, or deletion of the Provisioned Throughput.</p>"""
    commitment_duration: NotRequired[
        "capo_bedrock.types.commitment_duration.CommitmentDuration"
    ]
    """<p>Commitment duration of the Provisioned Throughput.</p>"""
    commitment_expiration_time: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>The timestamp for when the commitment term for the Provisioned Throughput expires.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProvisionedModelThroughputResponse) -> dict:
    out: dict = {}
    out["modelUnits"] = value["model_units"]
    out["desiredModelUnits"] = value["desired_model_units"]
    out["provisionedModelName"] = value["provisioned_model_name"]
    out["provisionedModelArn"] = value["provisioned_model_arn"]
    out["modelArn"] = value["model_arn"]
    out["desiredModelArn"] = value["desired_model_arn"]
    out["foundationModelArn"] = value["foundation_model_arn"]
    import capo_bedrock.types.provisioned_model_status

    out["status"] = capo_bedrock.types.provisioned_model_status.serialize_json(
        value["status"]
    )
    import capo_bedrock.types.timestamp

    out["creationTime"] = capo_bedrock.types.timestamp.serialize_json(
        value["creation_time"]
    )
    import capo_bedrock.types.timestamp

    out["lastModifiedTime"] = capo_bedrock.types.timestamp.serialize_json(
        value["last_modified_time"]
    )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    if "commitment_duration" in value:
        import capo_bedrock.types.commitment_duration

        out["commitmentDuration"] = (
            capo_bedrock.types.commitment_duration.serialize_json(
                value["commitment_duration"]
            )
        )
    if "commitment_expiration_time" in value:
        import capo_bedrock.types.timestamp

        out["commitmentExpirationTime"] = capo_bedrock.types.timestamp.serialize_json(
            value["commitment_expiration_time"]
        )
    return out


def deserialize_json(data: dict) -> GetProvisionedModelThroughputResponse:
    out: GetProvisionedModelThroughputResponse = {}  # type: ignore[typeddict-item]
    if data.get("modelUnits") is not None:
        out["model_units"] = data["modelUnits"]
    else:
        out["model_units"] = 0
    if data.get("desiredModelUnits") is not None:
        out["desired_model_units"] = data["desiredModelUnits"]
    else:
        out["desired_model_units"] = 0
    if data.get("provisionedModelName") is not None:
        out["provisioned_model_name"] = data["provisionedModelName"]
    else:
        out["provisioned_model_name"] = ""
    if data.get("provisionedModelArn") is not None:
        out["provisioned_model_arn"] = data["provisionedModelArn"]
    else:
        out["provisioned_model_arn"] = ""
    if data.get("modelArn") is not None:
        out["model_arn"] = data["modelArn"]
    else:
        out["model_arn"] = ""
    if data.get("desiredModelArn") is not None:
        out["desired_model_arn"] = data["desiredModelArn"]
    else:
        out["desired_model_arn"] = ""
    if data.get("foundationModelArn") is not None:
        out["foundation_model_arn"] = data["foundationModelArn"]
    else:
        out["foundation_model_arn"] = ""
    if data.get("status") is not None:
        import capo_bedrock.types.provisioned_model_status

        out["status"] = capo_bedrock.types.provisioned_model_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock.types.provisioned_model_status.ProvisionedModelStatus", ""
        )
    if data.get("creationTime") is not None:
        import capo_bedrock.types.timestamp

        out["creation_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastModifiedTime") is not None:
        import capo_bedrock.types.timestamp

        out["last_modified_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["lastModifiedTime"]
        )
    else:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("failureMessage") is not None:
        out["failure_message"] = data["failureMessage"]
    if data.get("commitmentDuration") is not None:
        import capo_bedrock.types.commitment_duration

        out["commitment_duration"] = (
            capo_bedrock.types.commitment_duration.deserialize_json(
                data["commitmentDuration"]
            )
        )
    if data.get("commitmentExpirationTime") is not None:
        import capo_bedrock.types.timestamp

        out["commitment_expiration_time"] = (
            capo_bedrock.types.timestamp.deserialize_json(
                data["commitmentExpirationTime"]
            )
        )
    return out
