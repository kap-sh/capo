"""Generated from Smithy shape ``com.amazonaws.securityhub#GetRemediationsV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.next_token
    import capo_securityhub.types.remediation_v2_item_list


class GetRemediationsV2Response(TypedDict, closed=True):
    items: NotRequired[
        "capo_securityhub.types.remediation_v2_item_list.RemediationV2ItemList"
    ]
    """<p>An array of remediation targets returned by the operation.</p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to use to request the next page of results. Otherwise, this parameter is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRemediationsV2Response) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_securityhub.types.remediation_v2_item_list

        out["Items"] = capo_securityhub.types.remediation_v2_item_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetRemediationsV2Response:
    out: GetRemediationsV2Response = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_securityhub.types.remediation_v2_item_list

        out["items"] = capo_securityhub.types.remediation_v2_item_list.deserialize_json(
            data["Items"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
