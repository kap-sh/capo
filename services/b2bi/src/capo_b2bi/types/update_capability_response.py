"""Generated from Smithy shape ``com.amazonaws.b2bi#UpdateCapabilityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.capability_configuration
    import capo_b2bi.types.capability_id
    import capo_b2bi.types.capability_name
    import capo_b2bi.types.capability_type
    import capo_b2bi.types.created_date
    import capo_b2bi.types.instructions_documents
    import capo_b2bi.types.modified_date
    import capo_b2bi.types.resource_arn


class UpdateCapabilityResponse(TypedDict, closed=True):
    capability_id: "capo_b2bi.types.capability_id.CapabilityId"
    """<p>Returns a system-assigned unique identifier for the capability.</p>"""
    capability_arn: "capo_b2bi.types.resource_arn.ResourceArn"
    """<p>Returns an Amazon Resource Name (ARN) for a specific Amazon Web Services resource, such as a capability, partnership, profile, or transformer.</p>"""
    name: "capo_b2bi.types.capability_name.CapabilityName"
    """<p>Returns the name of the capability, used to identify it.</p>"""
    type: "capo_b2bi.types.capability_type.CapabilityType"
    """<p>Returns the type of the capability. Currently, only <code>edi</code> is supported.</p>"""
    configuration: "capo_b2bi.types.capability_configuration.CapabilityConfiguration"
    """<p>Returns a structure that contains the details for a capability.</p>"""
    instructions_documents: NotRequired[
        "capo_b2bi.types.instructions_documents.InstructionsDocuments"
    ]
    """<p>Returns one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability. Each item contains the name of the bucket and the key, to identify the document's location.</p>"""
    created_at: "capo_b2bi.types.created_date.CreatedDate"
    """<p>Returns a timestamp for creation date and time of the capability.</p>"""
    modified_at: NotRequired["capo_b2bi.types.modified_date.ModifiedDate"]
    """<p>Returns a timestamp for last time the capability was modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateCapabilityResponse) -> dict:
    out: dict = {}
    out["capabilityId"] = value["capability_id"]
    out["capabilityArn"] = value["capability_arn"]
    out["name"] = value["name"]
    import capo_b2bi.types.capability_type

    out["type"] = capo_b2bi.types.capability_type.serialize_aws_json_1_0(value["type"])
    import capo_b2bi.types.capability_configuration

    out["configuration"] = (
        capo_b2bi.types.capability_configuration.serialize_aws_json_1_0(
            value["configuration"]
        )
    )
    if "instructions_documents" in value:
        import capo_b2bi.types.instructions_documents

        out["instructionsDocuments"] = (
            capo_b2bi.types.instructions_documents.serialize_aws_json_1_0(
                value["instructions_documents"]
            )
        )
    import capo_b2bi.types.created_date

    out["createdAt"] = capo_b2bi.types.created_date.serialize_aws_json_1_0(
        value["created_at"]
    )
    if "modified_at" in value:
        import capo_b2bi.types.modified_date

        out["modifiedAt"] = capo_b2bi.types.modified_date.serialize_aws_json_1_0(
            value["modified_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateCapabilityResponse:
    out: UpdateCapabilityResponse = {}  # type: ignore[typeddict-item]
    if data.get("capabilityId") is not None:
        out["capability_id"] = data["capabilityId"]
    else:
        out["capability_id"] = ""
    if data.get("capabilityArn") is not None:
        out["capability_arn"] = data["capabilityArn"]
    else:
        out["capability_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        import capo_b2bi.types.capability_type

        out["type"] = capo_b2bi.types.capability_type.deserialize_aws_json_1_0(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast("capo_b2bi.types.capability_type.CapabilityType", "")
    if data.get("configuration") is not None:
        import capo_b2bi.types.capability_configuration

        out["configuration"] = (
            capo_b2bi.types.capability_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    else:
        import capo_b2bi.types._unknown

        out["configuration"] = capo_b2bi.types._unknown.UnknownUnionMember("")
    if data.get("instructionsDocuments") is not None:
        import capo_b2bi.types.instructions_documents

        out["instructions_documents"] = (
            capo_b2bi.types.instructions_documents.deserialize_aws_json_1_0(
                data["instructionsDocuments"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_b2bi.types.created_date

        out["created_at"] = capo_b2bi.types.created_date.deserialize_aws_json_1_0(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("modifiedAt") is not None:
        import capo_b2bi.types.modified_date

        out["modified_at"] = capo_b2bi.types.modified_date.deserialize_aws_json_1_0(
            data["modifiedAt"]
        )
    return out
