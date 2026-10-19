"""Generated from Smithy shape ``com.amazonaws.ssm#StartAssociationsOnceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.association_id_list


class StartAssociationsOnceRequest(TypedDict, closed=True):
    association_ids: "capo_ssm.types.association_id_list.AssociationIdList"
    """<p>The association IDs that you want to run immediately and only one time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartAssociationsOnceRequest) -> dict:
    out: dict = {}
    import capo_ssm.types.association_id_list

    out["AssociationIds"] = capo_ssm.types.association_id_list.serialize_aws_json_1_1(
        value["association_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartAssociationsOnceRequest:
    out: StartAssociationsOnceRequest = {}  # type: ignore[typeddict-item]
    if data.get("AssociationIds") is not None:
        import capo_ssm.types.association_id_list

        out["association_ids"] = (
            capo_ssm.types.association_id_list.deserialize_aws_json_1_1(
                data["AssociationIds"]
            )
        )
    else:
        out["association_ids"] = []
    return out
