"""Generated from Smithy shape ``com.amazonaws.taxsettings#ListTaxRegistrationsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_taxsettings.types.account_details_list
    import capo_taxsettings.types.pagination_token_string


class ListTaxRegistrationsResponse(TypedDict, closed=True):
    account_details: "capo_taxsettings.types.account_details_list.AccountDetailsList"
    """<p>The list of account details. This contains account Ids and TRN Information for each of the linked accounts. </p>"""
    next_token: NotRequired[
        "capo_taxsettings.types.pagination_token_string.PaginationTokenString"
    ]
    """<p> The token to retrieve the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTaxRegistrationsResponse) -> dict:
    out: dict = {}
    import capo_taxsettings.types.account_details_list

    out["accountDetails"] = capo_taxsettings.types.account_details_list.serialize_json(
        value["account_details"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTaxRegistrationsResponse:
    out: ListTaxRegistrationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("accountDetails") is not None:
        import capo_taxsettings.types.account_details_list

        out["account_details"] = (
            capo_taxsettings.types.account_details_list.deserialize_json(
                data["accountDetails"]
            )
        )
    else:
        raise DeserializationError(
            "ListTaxRegistrationsResponse.account_details required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListTaxRegistrationsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "account_details" in value:
        import capo_taxsettings.types.account_details_list

        out["account_details"] = (
            capo_taxsettings.types.account_details_list.redact_sensitive(
                value["account_details"]
            )
        )
    return out
