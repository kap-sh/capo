"""Generated from Smithy shape ``com.amazonaws.b2bi#ListPartnershipsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.page_token
    import capo_b2bi.types.partnership_list


class ListPartnershipsResponse(TypedDict, closed=True):
    partnerships: "capo_b2bi.types.partnership_list.PartnershipList"
    """<p>Specifies a list of your partnerships.</p>"""
    next_token: NotRequired["capo_b2bi.types.page_token.PageToken"]
    """<p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListPartnershipsResponse) -> dict:
    out: dict = {}
    import capo_b2bi.types.partnership_list

    out["partnerships"] = capo_b2bi.types.partnership_list.serialize_aws_json_1_0(
        value["partnerships"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListPartnershipsResponse:
    out: ListPartnershipsResponse = {}  # type: ignore[typeddict-item]
    if data.get("partnerships") is not None:
        import capo_b2bi.types.partnership_list

        out["partnerships"] = capo_b2bi.types.partnership_list.deserialize_aws_json_1_0(
            data["partnerships"]
        )
    else:
        out["partnerships"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
