"""Generated from Smithy shape ``com.amazonaws.kendra#DisassociateEntitiesFromExperienceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.disassociate_entity_list
    import capo_kendra.types.experience_id
    import capo_kendra.types.index_id


class DisassociateEntitiesFromExperienceRequest(TypedDict, closed=True):
    id: "capo_kendra.types.experience_id.ExperienceId"
    """<p>The identifier of your Amazon Kendra experience.</p>"""
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for your Amazon Kendra experience.</p>"""
    entity_list: "capo_kendra.types.disassociate_entity_list.DisassociateEntityList"
    """<p>Lists users or groups in your IAM Identity Center identity source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateEntitiesFromExperienceRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["IndexId"] = value["index_id"]
    import capo_kendra.types.disassociate_entity_list

    out["EntityList"] = (
        capo_kendra.types.disassociate_entity_list.serialize_aws_json_1_1(
            value["entity_list"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateEntitiesFromExperienceRequest:
    out: DisassociateEntitiesFromExperienceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        out["index_id"] = ""
    if data.get("EntityList") is not None:
        import capo_kendra.types.disassociate_entity_list

        out["entity_list"] = (
            capo_kendra.types.disassociate_entity_list.deserialize_aws_json_1_1(
                data["EntityList"]
            )
        )
    else:
        out["entity_list"] = []
    return out
