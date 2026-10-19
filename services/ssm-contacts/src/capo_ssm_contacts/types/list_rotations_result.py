"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ListRotationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.pagination_token
    import capo_ssm_contacts.types.rotations


class ListRotationsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ssm_contacts.types.pagination_token.PaginationToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""
    rotations: "capo_ssm_contacts.types.rotations.Rotations"
    """<p>Information about rotations that meet the filter criteria.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRotationsResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_ssm_contacts.types.rotations

    out["Rotations"] = capo_ssm_contacts.types.rotations.serialize_aws_json_1_1(
        value["rotations"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRotationsResult:
    out: ListRotationsResult = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Rotations") is not None:
        import capo_ssm_contacts.types.rotations

        out["rotations"] = capo_ssm_contacts.types.rotations.deserialize_aws_json_1_1(
            data["Rotations"]
        )
    else:
        out["rotations"] = []
    return out
