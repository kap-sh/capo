"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateAccountPoolInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.account_pool_id
    import capo_datazone.types.account_pool_name
    import capo_datazone.types.account_source
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.resolution_strategy


class UpdateAccountPoolInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The domain ID where the account pool that is to be updated lives.</p>"""
    identifier: "capo_datazone.types.account_pool_id.AccountPoolId"
    """<p>The ID of the account pool that is to be updated.</p>"""
    name: NotRequired["capo_datazone.types.account_pool_name.AccountPoolName"]
    """<p>The name of the account pool that is to be updated.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the account pool that is to be udpated.</p>"""
    resolution_strategy: NotRequired[
        "capo_datazone.types.resolution_strategy.ResolutionStrategy"
    ]
    """<p>The mechanism used to resolve the account selection from the account pool.</p>"""
    account_source: NotRequired["capo_datazone.types.account_source.AccountSource"]
    """<p>The source of accounts for the account pool. In the current release, it's either a static list of accounts provided by the customer or a custom Amazon Web Services Lambda handler. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountPoolInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "resolution_strategy" in value:
        import capo_datazone.types.resolution_strategy

        out["resolutionStrategy"] = (
            capo_datazone.types.resolution_strategy.serialize_json(
                value["resolution_strategy"]
            )
        )
    if "account_source" in value:
        import capo_datazone.types.account_source

        out["accountSource"] = capo_datazone.types.account_source.serialize_json(
            value["account_source"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAccountPoolInput:
    out: UpdateAccountPoolInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("resolutionStrategy") is not None:
        import capo_datazone.types.resolution_strategy

        out["resolution_strategy"] = (
            capo_datazone.types.resolution_strategy.deserialize_json(
                data["resolutionStrategy"]
            )
        )
    if data.get("accountSource") is not None:
        import capo_datazone.types.account_source

        out["account_source"] = capo_datazone.types.account_source.deserialize_json(
            data["accountSource"]
        )
    return out


def redact_sensitive(value: UpdateAccountPoolInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "account_source" in value:
        import capo_datazone.types.account_source

        out["account_source"] = capo_datazone.types.account_source.redact_sensitive(
            value["account_source"]
        )
    return out
