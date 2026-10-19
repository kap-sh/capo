"""Generated from Smithy shape ``com.amazonaws.b2bi#ListCapabilitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.capability_list
    import capo_b2bi.types.page_token


class ListCapabilitiesResponse(TypedDict, closed=True):
    capabilities: "capo_b2bi.types.capability_list.CapabilityList"
    """<p>Returns one or more capabilities associated with this partnership.</p>"""
    next_token: NotRequired["capo_b2bi.types.page_token.PageToken"]
    """<p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListCapabilitiesResponse) -> dict:
    out: dict = {}
    import capo_b2bi.types.capability_list

    out["capabilities"] = capo_b2bi.types.capability_list.serialize_aws_json_1_0(
        value["capabilities"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListCapabilitiesResponse:
    out: ListCapabilitiesResponse = {}  # type: ignore[typeddict-item]
    if data.get("capabilities") is not None:
        import capo_b2bi.types.capability_list

        out["capabilities"] = capo_b2bi.types.capability_list.deserialize_aws_json_1_0(
            data["capabilities"]
        )
    else:
        out["capabilities"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
