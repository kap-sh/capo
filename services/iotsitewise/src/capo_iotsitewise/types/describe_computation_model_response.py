"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeComputationModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.action_definitions
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.computation_model_configuration
    import capo_iotsitewise.types.computation_model_data_binding
    import capo_iotsitewise.types.computation_model_status
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.restricted_description
    import capo_iotsitewise.types.restricted_name
    import capo_iotsitewise.types.timestamp
    import capo_iotsitewise.types.version


class DescribeComputationModelResponse(TypedDict, closed=True):
    computation_model_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the computation model.</p>"""
    computation_model_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the computation model, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:computation-model/${ComputationModelId}</code> </p>"""
    computation_model_name: "capo_iotsitewise.types.restricted_name.RestrictedName"
    """<p>The name of the computation model.</p>"""
    computation_model_description: NotRequired[
        "capo_iotsitewise.types.restricted_description.RestrictedDescription"
    ]
    """<p>The description of the computation model.</p>"""
    computation_model_configuration: "capo_iotsitewise.types.computation_model_configuration.ComputationModelConfiguration"
    """<p>The configuration for the computation model.</p>"""
    computation_model_data_binding: "capo_iotsitewise.types.computation_model_data_binding.ComputationModelDataBinding"
    """<p>The data binding for the computation model. Key is a variable name defined in configuration. Value is a <code>ComputationModelDataBindingValue</code> referenced by the variable.</p>"""
    computation_model_creation_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The model creation date, in Unix epoch time.</p>"""
    computation_model_last_update_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the model was last updated, in Unix epoch time.</p>"""
    computation_model_status: (
        "capo_iotsitewise.types.computation_model_status.ComputationModelStatus"
    )
    """<p>The current status of the asset model, which contains a state and an error message if any.</p>"""
    computation_model_version: "capo_iotsitewise.types.version.Version"
    """<p>The version of the computation model.</p>"""
    action_definitions: "capo_iotsitewise.types.action_definitions.ActionDefinitions"
    """<p>The available actions for this computation model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeComputationModelResponse) -> dict:
    out: dict = {}
    out["computationModelId"] = value["computation_model_id"]
    out["computationModelArn"] = value["computation_model_arn"]
    out["computationModelName"] = value["computation_model_name"]
    if "computation_model_description" in value:
        out["computationModelDescription"] = value["computation_model_description"]
    import capo_iotsitewise.types.computation_model_configuration

    out["computationModelConfiguration"] = (
        capo_iotsitewise.types.computation_model_configuration.serialize_json(
            value["computation_model_configuration"]
        )
    )
    import capo_iotsitewise.types.computation_model_data_binding

    out["computationModelDataBinding"] = (
        capo_iotsitewise.types.computation_model_data_binding.serialize_json(
            value["computation_model_data_binding"]
        )
    )
    import capo_iotsitewise.types.timestamp

    out["computationModelCreationDate"] = (
        capo_iotsitewise.types.timestamp.serialize_json(
            value["computation_model_creation_date"]
        )
    )
    import capo_iotsitewise.types.timestamp

    out["computationModelLastUpdateDate"] = (
        capo_iotsitewise.types.timestamp.serialize_json(
            value["computation_model_last_update_date"]
        )
    )
    import capo_iotsitewise.types.computation_model_status

    out["computationModelStatus"] = (
        capo_iotsitewise.types.computation_model_status.serialize_json(
            value["computation_model_status"]
        )
    )
    out["computationModelVersion"] = value["computation_model_version"]
    import capo_iotsitewise.types.action_definitions

    out["actionDefinitions"] = capo_iotsitewise.types.action_definitions.serialize_json(
        value["action_definitions"]
    )
    return out


def deserialize_json(data: dict) -> DescribeComputationModelResponse:
    out: DescribeComputationModelResponse = {}  # type: ignore[typeddict-item]
    if data.get("computationModelId") is not None:
        out["computation_model_id"] = data["computationModelId"]
    else:
        raise DeserializationError(
            "DescribeComputationModelResponse.computation_model_id required"
        )
    if data.get("computationModelArn") is not None:
        out["computation_model_arn"] = data["computationModelArn"]
    else:
        raise DeserializationError(
            "DescribeComputationModelResponse.computation_model_arn required"
        )
    if data.get("computationModelName") is not None:
        out["computation_model_name"] = data["computationModelName"]
    else:
        raise DeserializationError(
            "DescribeComputationModelResponse.computation_model_name required"
        )
    if data.get("computationModelDescription") is not None:
        out["computation_model_description"] = data["computationModelDescription"]
    if data.get("computationModelConfiguration") is not None:
        import capo_iotsitewise.types.computation_model_configuration

        out["computation_model_configuration"] = (
            capo_iotsitewise.types.computation_model_configuration.deserialize_json(
                data["computationModelConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeComputationModelResponse.computation_model_configuration required"
        )
    if data.get("computationModelDataBinding") is not None:
        import capo_iotsitewise.types.computation_model_data_binding

        out["computation_model_data_binding"] = (
            capo_iotsitewise.types.computation_model_data_binding.deserialize_json(
                data["computationModelDataBinding"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeComputationModelResponse.computation_model_data_binding required"
        )
    if data.get("computationModelCreationDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["computation_model_creation_date"] = (
            capo_iotsitewise.types.timestamp.deserialize_json(
                data["computationModelCreationDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeComputationModelResponse.computation_model_creation_date required"
        )
    if data.get("computationModelLastUpdateDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["computation_model_last_update_date"] = (
            capo_iotsitewise.types.timestamp.deserialize_json(
                data["computationModelLastUpdateDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeComputationModelResponse.computation_model_last_update_date required"
        )
    if data.get("computationModelStatus") is not None:
        import capo_iotsitewise.types.computation_model_status

        out["computation_model_status"] = (
            capo_iotsitewise.types.computation_model_status.deserialize_json(
                data["computationModelStatus"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeComputationModelResponse.computation_model_status required"
        )
    if data.get("computationModelVersion") is not None:
        out["computation_model_version"] = data["computationModelVersion"]
    else:
        raise DeserializationError(
            "DescribeComputationModelResponse.computation_model_version required"
        )
    if data.get("actionDefinitions") is not None:
        import capo_iotsitewise.types.action_definitions

        out["action_definitions"] = (
            capo_iotsitewise.types.action_definitions.deserialize_json(
                data["actionDefinitions"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeComputationModelResponse.action_definitions required"
        )
    return out
