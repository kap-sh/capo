"""Generated from Smithy shape ``com.amazonaws.ssm#CreateAssociationBatchRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.association_dispatch_assume_role_arn
    import capo_ssm.types.create_association_batch_request_entries


class CreateAssociationBatchRequest(TypedDict, closed=True):
    entries: "capo_ssm.types.create_association_batch_request_entries.CreateAssociationBatchRequestEntries"
    """<p>One or more associations.</p>"""
    association_dispatch_assume_role: NotRequired[
        "capo_ssm.types.association_dispatch_assume_role_arn.AssociationDispatchAssumeRoleArn"
    ]
    """<p>A role used by association to take actions on your behalf. State Manager will assume this role and call required APIs when dispatching configurations to nodes. If not specified, <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/using-service-linked-roles.html"> service-linked role for Systems Manager</a> will be used by default. </p> <note> <p>It is recommended that you define a custom IAM role so that you have full control of the permissions that State Manager has when taking actions on your behalf.</p> <p>Service-linked role support in State Manager is being phased out. Associations relying on service-linked role may require updates in the future to continue functioning properly.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAssociationBatchRequest) -> dict:
    out: dict = {}
    import capo_ssm.types.create_association_batch_request_entries

    out["Entries"] = (
        capo_ssm.types.create_association_batch_request_entries.serialize_aws_json_1_1(
            value["entries"]
        )
    )
    if "association_dispatch_assume_role" in value:
        out["AssociationDispatchAssumeRole"] = value["association_dispatch_assume_role"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAssociationBatchRequest:
    out: CreateAssociationBatchRequest = {}  # type: ignore[typeddict-item]
    if data.get("Entries") is not None:
        import capo_ssm.types.create_association_batch_request_entries

        out["entries"] = (
            capo_ssm.types.create_association_batch_request_entries.deserialize_aws_json_1_1(
                data["Entries"]
            )
        )
    else:
        raise DeserializationError("CreateAssociationBatchRequest.entries required")
    if data.get("AssociationDispatchAssumeRole") is not None:
        out["association_dispatch_assume_role"] = data["AssociationDispatchAssumeRole"]
    return out
