"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ShiftDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.ssm_contacts_arn_list


class ShiftDetails(TypedDict, closed=True):
    overridden_contact_ids: (
        "capo_ssm_contacts.types.ssm_contacts_arn_list.SsmContactsArnList"
    )
    """<p>The Amazon Resources Names (ARNs) of the contacts who were replaced in a shift when an override was created. If the override is deleted, these contacts are restored to the shift.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShiftDetails) -> dict:
    out: dict = {}
    import capo_ssm_contacts.types.ssm_contacts_arn_list

    out["OverriddenContactIds"] = (
        capo_ssm_contacts.types.ssm_contacts_arn_list.serialize_aws_json_1_1(
            value["overridden_contact_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ShiftDetails:
    out: ShiftDetails = {}  # type: ignore[typeddict-item]
    if data.get("OverriddenContactIds") is not None:
        import capo_ssm_contacts.types.ssm_contacts_arn_list

        out["overridden_contact_ids"] = (
            capo_ssm_contacts.types.ssm_contacts_arn_list.deserialize_aws_json_1_1(
                data["OverriddenContactIds"]
            )
        )
    else:
        out["overridden_contact_ids"] = []
    return out
