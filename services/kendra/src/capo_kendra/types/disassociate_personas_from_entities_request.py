"""Generated from Smithy shape ``com.amazonaws.kendra#DisassociatePersonasFromEntitiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.entity_ids_list
    import capo_kendra.types.experience_id
    import capo_kendra.types.index_id


class DisassociatePersonasFromEntitiesRequest(TypedDict, closed=True):
    id: "capo_kendra.types.experience_id.ExperienceId"
    """<p>The identifier of your Amazon Kendra experience.</p>"""
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for your Amazon Kendra experience.</p>"""
    entity_ids: "capo_kendra.types.entity_ids_list.EntityIdsList"
    """<p>The identifiers of users or groups in your IAM Identity Center identity source. For example, user IDs could be user emails.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociatePersonasFromEntitiesRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["IndexId"] = value["index_id"]
    import capo_kendra.types.entity_ids_list

    out["EntityIds"] = capo_kendra.types.entity_ids_list.serialize_aws_json_1_1(
        value["entity_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociatePersonasFromEntitiesRequest:
    out: DisassociatePersonasFromEntitiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        out["index_id"] = ""
    if data.get("EntityIds") is not None:
        import capo_kendra.types.entity_ids_list

        out["entity_ids"] = capo_kendra.types.entity_ids_list.deserialize_aws_json_1_1(
            data["EntityIds"]
        )
    else:
        out["entity_ids"] = []
    return out
