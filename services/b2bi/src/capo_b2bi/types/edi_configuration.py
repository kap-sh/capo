"""Generated from Smithy shape ``com.amazonaws.b2bi#EdiConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import capo_b2bi.types.capability_direction
    import capo_b2bi.types.edi_type
    import capo_b2bi.types.s3_location
    import capo_b2bi.types.transformer_id


class EdiConfiguration(TypedDict, closed=True):
    capability_direction: NotRequired[
        "capo_b2bi.types.capability_direction.CapabilityDirection"
    ]
    """<p>Specifies whether this is capability is for inbound or outbound transformations.</p>"""
    type: "capo_b2bi.types.edi_type.EdiType"
    """<p>Returns the type of the capability. Currently, only <code>edi</code> is supported.</p>"""
    input_location: "capo_b2bi.types.s3_location.S3Location"
    """<p>Contains the Amazon S3 bucket and prefix for the location of the input file, which is contained in an <code>S3Location</code> object.</p>"""
    output_location: "capo_b2bi.types.s3_location.S3Location"
    """<p>Contains the Amazon S3 bucket and prefix for the location of the output file, which is contained in an <code>S3Location</code> object.</p>"""
    transformer_id: "capo_b2bi.types.transformer_id.TransformerId"
    """<p>Returns the system-assigned unique identifier for the transformer.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EdiConfiguration) -> dict:
    out: dict = {}
    if "capability_direction" in value:
        import capo_b2bi.types.capability_direction

        out["capabilityDirection"] = (
            capo_b2bi.types.capability_direction.serialize_aws_json_1_0(
                value["capability_direction"]
            )
        )
    import capo_b2bi.types.edi_type

    out["type"] = capo_b2bi.types.edi_type.serialize_aws_json_1_0(value["type"])
    import capo_b2bi.types.s3_location

    out["inputLocation"] = capo_b2bi.types.s3_location.serialize_aws_json_1_0(
        value["input_location"]
    )
    import capo_b2bi.types.s3_location

    out["outputLocation"] = capo_b2bi.types.s3_location.serialize_aws_json_1_0(
        value["output_location"]
    )
    out["transformerId"] = value["transformer_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EdiConfiguration:
    out: EdiConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("capabilityDirection") is not None:
        import capo_b2bi.types.capability_direction

        out["capability_direction"] = (
            capo_b2bi.types.capability_direction.deserialize_aws_json_1_0(
                data["capabilityDirection"]
            )
        )
    if data.get("type") is not None:
        import capo_b2bi.types.edi_type

        out["type"] = capo_b2bi.types.edi_type.deserialize_aws_json_1_0(data["type"])
    else:
        out["type"] = {"$unknown": {"name": ""}}
    if data.get("inputLocation") is not None:
        import capo_b2bi.types.s3_location

        out["input_location"] = capo_b2bi.types.s3_location.deserialize_aws_json_1_0(
            data["inputLocation"]
        )
    else:
        raise DeserializationError("EdiConfiguration.input_location required")
    if data.get("outputLocation") is not None:
        import capo_b2bi.types.s3_location

        out["output_location"] = capo_b2bi.types.s3_location.deserialize_aws_json_1_0(
            data["outputLocation"]
        )
    else:
        raise DeserializationError("EdiConfiguration.output_location required")
    if data.get("transformerId") is not None:
        out["transformer_id"] = data["transformerId"]
    else:
        out["transformer_id"] = ""
    return out
