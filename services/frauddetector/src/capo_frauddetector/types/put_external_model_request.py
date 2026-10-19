"""Generated from Smithy shape ``com.amazonaws.frauddetector#PutExternalModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_frauddetector.types.model_endpoint_status
    import capo_frauddetector.types.model_input_configuration
    import capo_frauddetector.types.model_output_configuration
    import capo_frauddetector.types.model_source
    import capo_frauddetector.types.sage_maker_endpoint_identifier
    import capo_frauddetector.types.string
    import capo_frauddetector.types.tag_list


class PutExternalModelRequest(TypedDict, closed=True):
    model_endpoint: "capo_frauddetector.types.sage_maker_endpoint_identifier.sageMakerEndpointIdentifier"
    """<p>The model endpoints name.</p>"""
    model_source: "capo_frauddetector.types.model_source.ModelSource"
    """<p>The source of the model.</p>"""
    invoke_model_endpoint_role_arn: "capo_frauddetector.types.string.string"
    """<p>The IAM role used to invoke the model endpoint.</p>"""
    input_configuration: (
        "capo_frauddetector.types.model_input_configuration.ModelInputConfiguration"
    )
    """<p>The model endpoint input configuration.</p>"""
    output_configuration: (
        "capo_frauddetector.types.model_output_configuration.ModelOutputConfiguration"
    )
    """<p>The model endpoint output configuration.</p>"""
    model_endpoint_status: (
        "capo_frauddetector.types.model_endpoint_status.ModelEndpointStatus"
    )
    """<p>The model endpoint’s status in Amazon Fraud Detector.</p>"""
    tags: NotRequired["capo_frauddetector.types.tag_list.tagList"]
    """<p>A collection of key and value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutExternalModelRequest) -> dict:
    out: dict = {}
    out["modelEndpoint"] = value["model_endpoint"]
    import capo_frauddetector.types.model_source

    out["modelSource"] = capo_frauddetector.types.model_source.serialize_aws_json_1_1(
        value["model_source"]
    )
    out["invokeModelEndpointRoleArn"] = value["invoke_model_endpoint_role_arn"]
    import capo_frauddetector.types.model_input_configuration

    out["inputConfiguration"] = (
        capo_frauddetector.types.model_input_configuration.serialize_aws_json_1_1(
            value["input_configuration"]
        )
    )
    import capo_frauddetector.types.model_output_configuration

    out["outputConfiguration"] = (
        capo_frauddetector.types.model_output_configuration.serialize_aws_json_1_1(
            value["output_configuration"]
        )
    )
    import capo_frauddetector.types.model_endpoint_status

    out["modelEndpointStatus"] = (
        capo_frauddetector.types.model_endpoint_status.serialize_aws_json_1_1(
            value["model_endpoint_status"]
        )
    )
    if "tags" in value:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutExternalModelRequest:
    out: PutExternalModelRequest = {}  # type: ignore[typeddict-item]
    if data.get("modelEndpoint") is not None:
        out["model_endpoint"] = data["modelEndpoint"]
    else:
        out["model_endpoint"] = ""
    if data.get("modelSource") is not None:
        import capo_frauddetector.types.model_source

        out["model_source"] = (
            capo_frauddetector.types.model_source.deserialize_aws_json_1_1(
                data["modelSource"]
            )
        )
    else:
        import typing

        out["model_source"] = typing.cast(
            "capo_frauddetector.types.model_source.ModelSource", ""
        )
    if data.get("invokeModelEndpointRoleArn") is not None:
        out["invoke_model_endpoint_role_arn"] = data["invokeModelEndpointRoleArn"]
    else:
        out["invoke_model_endpoint_role_arn"] = ""
    if data.get("inputConfiguration") is not None:
        import capo_frauddetector.types.model_input_configuration

        out["input_configuration"] = (
            capo_frauddetector.types.model_input_configuration.deserialize_aws_json_1_1(
                data["inputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutExternalModelRequest.input_configuration required"
        )
    if data.get("outputConfiguration") is not None:
        import capo_frauddetector.types.model_output_configuration

        out["output_configuration"] = (
            capo_frauddetector.types.model_output_configuration.deserialize_aws_json_1_1(
                data["outputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutExternalModelRequest.output_configuration required"
        )
    if data.get("modelEndpointStatus") is not None:
        import capo_frauddetector.types.model_endpoint_status

        out["model_endpoint_status"] = (
            capo_frauddetector.types.model_endpoint_status.deserialize_aws_json_1_1(
                data["modelEndpointStatus"]
            )
        )
    else:
        import typing

        out["model_endpoint_status"] = typing.cast(
            "capo_frauddetector.types.model_endpoint_status.ModelEndpointStatus", ""
        )
    if data.get("tags") is not None:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
