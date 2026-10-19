"""Generated from Smithy shape ``com.amazonaws.inspector2#EnableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id_set
    import capo_inspector2.types.client_token
    import capo_inspector2.types.enable_resource_type_list


class EnableRequest(TypedDict, closed=True):
    account_ids: NotRequired["capo_inspector2.types.account_id_set.AccountIdSet"]
    """<p>A list of account IDs you want to enable Amazon Inspector scans for.</p>"""
    resource_types: (
        "capo_inspector2.types.enable_resource_type_list.EnableResourceTypeList"
    )
    """<p>The resource scan types you want to enable.</p>"""
    client_token: NotRequired["capo_inspector2.types.client_token.ClientToken"]
    """<p>The idempotency token for the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_inspector2.types.account_id_set

        out["accountIds"] = capo_inspector2.types.account_id_set.serialize_json(
            value["account_ids"]
        )
    import capo_inspector2.types.enable_resource_type_list

    out["resourceTypes"] = (
        capo_inspector2.types.enable_resource_type_list.serialize_json(
            value["resource_types"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> EnableRequest:
    out: EnableRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountIds") is not None:
        import capo_inspector2.types.account_id_set

        out["account_ids"] = capo_inspector2.types.account_id_set.deserialize_json(
            data["accountIds"]
        )
    if data.get("resourceTypes") is not None:
        import capo_inspector2.types.enable_resource_type_list

        out["resource_types"] = (
            capo_inspector2.types.enable_resource_type_list.deserialize_json(
                data["resourceTypes"]
            )
        )
    else:
        out["resource_types"] = []
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
