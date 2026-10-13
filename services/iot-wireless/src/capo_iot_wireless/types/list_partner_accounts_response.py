"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListPartnerAccountsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.next_token
    import capo_iot_wireless.types.sidewalk_account_list


class ListPartnerAccountsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_iot_wireless.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""
    sidewalk: NotRequired[
        "capo_iot_wireless.types.sidewalk_account_list.SidewalkAccountList"
    ]
    """<p>The Sidewalk account credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPartnerAccountsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "sidewalk" in value:
        import capo_iot_wireless.types.sidewalk_account_list

        out["Sidewalk"] = capo_iot_wireless.types.sidewalk_account_list.serialize_json(
            value["sidewalk"]
        )
    return out


def deserialize_json(data: dict) -> ListPartnerAccountsResponse:
    out: ListPartnerAccountsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Sidewalk") is not None:
        import capo_iot_wireless.types.sidewalk_account_list

        out["sidewalk"] = (
            capo_iot_wireless.types.sidewalk_account_list.deserialize_json(
                data["Sidewalk"]
            )
        )
    return out


def redact_sensitive(value: ListPartnerAccountsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sidewalk" in value:
        import capo_iot_wireless.types.sidewalk_account_list

        out["sidewalk"] = (
            capo_iot_wireless.types.sidewalk_account_list.redact_sensitive(
                value["sidewalk"]
            )
        )
    return out
