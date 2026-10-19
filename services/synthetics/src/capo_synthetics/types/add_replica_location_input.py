"""Generated from Smithy shape ``com.amazonaws.synthetics#AddReplicaLocationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.kms_key_arn
    import capo_synthetics.types.location
    import capo_synthetics.types.vpc_config_input


class AddReplicaLocationInput(TypedDict, closed=True):
    location: "capo_synthetics.types.location.Location"
    """<p>The Amazon Web Services Region where the canary replica should be created, for example <code>us-east-1</code>.</p>"""
    vpc_config: NotRequired["capo_synthetics.types.vpc_config_input.VpcConfigInput"]
    """<p>The VPC configuration to use for the canary replica in this location. If not specified, the replica runs without VPC connectivity.</p>"""
    kms_key_arn: NotRequired["capo_synthetics.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the customer-managed AWS Key Management Service (AWS KMS) key used to encrypt the canary replica's AWS Lambda function environment variables at rest. If you don't specify a value, the service uses an AWS-managed key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddReplicaLocationInput) -> dict:
    out: dict = {}
    out["Location"] = value["location"]
    if "vpc_config" in value:
        import capo_synthetics.types.vpc_config_input

        out["VpcConfig"] = capo_synthetics.types.vpc_config_input.serialize_json(
            value["vpc_config"]
        )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> AddReplicaLocationInput:
    out: AddReplicaLocationInput = {}  # type: ignore[typeddict-item]
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    else:
        out["location"] = ""
    if data.get("VpcConfig") is not None:
        import capo_synthetics.types.vpc_config_input

        out["vpc_config"] = capo_synthetics.types.vpc_config_input.deserialize_json(
            data["VpcConfig"]
        )
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out
