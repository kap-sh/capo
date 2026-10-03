"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateProvisionedModelThroughputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.commitment_duration
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.model_identifier
    import capo_bedrock.types.positive_integer
    import capo_bedrock.types.provisioned_model_name
    import capo_bedrock.types.tag_list


class CreateProvisionedModelThroughputRequest(TypedDict, closed=True):
    client_request_token: NotRequired[
        "capo_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the Amazon S3 User Guide.</p>"""
    model_units: "capo_bedrock.types.positive_integer.PositiveInteger"
    """<p>Number of model units to allocate. A model unit delivers a specific throughput level for the specified model. The throughput level of a model unit specifies the total number of input and output tokens that it can process and generate within a span of one minute. By default, your account has no model units for purchasing Provisioned Throughputs with commitment. You must first visit the <a href="https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase">Amazon Web Services support center</a> to request MUs.</p> <p>For model unit quotas, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html#prov-thru-quotas">Provisioned Throughput quotas</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p> <p>For more information about what an MU specifies, contact your Amazon Web Services account manager.</p>"""
    provisioned_model_name: (
        "capo_bedrock.types.provisioned_model_name.ProvisionedModelName"
    )
    """<p>The name for this Provisioned Throughput.</p>"""
    model_id: "capo_bedrock.types.model_identifier.ModelIdentifier"
    """<p>The Amazon Resource Name (ARN) or name of the model to associate with this Provisioned Throughput. For a list of models for which you can purchase Provisioned Throughput, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#prov-throughput-models">Amazon Bedrock model IDs for purchasing Provisioned Throughput</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>"""
    commitment_duration: NotRequired[
        "capo_bedrock.types.commitment_duration.CommitmentDuration"
    ]
    """<p>The commitment duration requested for the Provisioned Throughput. Billing occurs hourly and is discounted for longer commitment terms. To request a no-commit Provisioned Throughput, omit this field.</p> <p>Custom models support all levels of commitment. To see which base models support no commitment, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/pt-supported.html">Supported regions and models for Provisioned Throughput</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a> </p>"""
    tags: NotRequired["capo_bedrock.types.tag_list.TagList"]
    """<p>Tags to associate with this Provisioned Throughput.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProvisionedModelThroughputRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    out["modelUnits"] = value["model_units"]
    out["provisionedModelName"] = value["provisioned_model_name"]
    out["modelId"] = value["model_id"]
    if "commitment_duration" in value:
        import capo_bedrock.types.commitment_duration

        out["commitmentDuration"] = (
            capo_bedrock.types.commitment_duration.serialize_json(
                value["commitment_duration"]
            )
        )
    if "tags" in value:
        import capo_bedrock.types.tag_list

        out["tags"] = capo_bedrock.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateProvisionedModelThroughputRequest:
    out: CreateProvisionedModelThroughputRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("modelUnits") is not None:
        out["model_units"] = data["modelUnits"]
    else:
        raise DeserializationError(
            "CreateProvisionedModelThroughputRequest.model_units required"
        )
    if data.get("provisionedModelName") is not None:
        out["provisioned_model_name"] = data["provisionedModelName"]
    else:
        raise DeserializationError(
            "CreateProvisionedModelThroughputRequest.provisioned_model_name required"
        )
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError(
            "CreateProvisionedModelThroughputRequest.model_id required"
        )
    if data.get("commitmentDuration") is not None:
        import capo_bedrock.types.commitment_duration

        out["commitment_duration"] = (
            capo_bedrock.types.commitment_duration.deserialize_json(
                data["commitmentDuration"]
            )
        )
    if data.get("tags") is not None:
        import capo_bedrock.types.tag_list

        out["tags"] = capo_bedrock.types.tag_list.deserialize_json(data["tags"])
    return out
